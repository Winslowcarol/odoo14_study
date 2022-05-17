# -*- coding: utf-8 -*-
import logging
from odoo import models, fields, api
from odoo.exceptions import UserError #向用戶報出錯誤
from odoo.tools.translate import _ #向用戶報出錯誤

logger = logging.getLogger(__name__)
_logger = logging.getLogger(__name__) #使用read_group()從組中獲取數據

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char('Title', required=True)
    isbn = fields.Char('ISBN') #自定義記錄的搜索方式
    date_release = fields.Date('Release Date')
    cost_price = fields.Float('Book Cost') #使用read_group()從組中獲取數據
    author_ids = fields.Many2many('res.partner', string='Authors')
    category_id = fields.Many2one('library.book.category', string='Category')
    old_edition = fields.Many2one('library.book', string='Old Edition') #自定義記錄的搜索方式
    state = fields.Selection([
        ('draft', 'Unavailable'),
        ('available', 'Available'),
        ('borrowed', 'Borrowed'),
        ('lost', 'Lost')],
        'State', default="draft")
    manager_remarks = fields.Text('Manager Remarks') #繼承write()和create()

    def name_get(self):#繼承write()和create()
        result = []
        for book in self:
            authors = book.author_ids.mapped('name')
            name = '%s (%s)' % (book.name, ', '.join(authors))
            result.append((book.id, name))
        return result

    def grouped_data(self):#使用read_group()從組中獲取數據
        data = self._get_average_cost()
        _logger.info("Groupped Data %s" % data)

    @api.model
    def _get_average_cost(self):#使用read_group()從組中獲取數據
        grouped_result = self.read_group(
            [('cost_price', "!=", False)], # Domain
            ['category_id', 'cost_price:avg'], # Fields to access
            ['category_id'] # group_by
            )
        return grouped_result

    @api.model #自定義記錄的搜索方式
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
        args = [] if args is None else args.copy()
        if not (name == '' and operator == 'ilike'):
            args += ['|', '|', '|',
                     ('name', operator, name),
                     ('isbn', operator, name),
                     ('author_ids.name', operator, name)
                     ]
        return super(LibraryBook, self)._name_search(
            name=name, args=args, operator=operator,
            limit=limit, name_get_uid=name_get_uid)

    @api.model #繼承write()和create()
    def create(self, values):
        if not self.user_has_groups('my_library.group_librarian'):
            if 'manager_remarks' in values:
                raise UserError(
                    'You are not allowed to modify '
                    'manager_remarks'
                )
        return super(LibraryBook, self).create(values)

    def write(self, values):
        if not self.user_has_groups('my_library.group_librarian'):
            if 'manager_remarks' in values:
                raise UserError(
                    'You are not allowed to modify '
                    'manager_remarks'
                )
        return super(LibraryBook, self).write(values)

    #定義模型方法及使用API裝飾器
    @api.model
    def is_allowed_transition(self, old_state, new_state):
        allowed = [('draft', 'available'),
                   ('available', 'borrowed'),
                   ('borrowed', 'available'),
                   ('available', 'lost'),
                   ('borrowed', 'lost'),
                   ('lost', 'available')]
        return (old_state, new_state) in allowed

    def change_state(self, new_state):
        for book in self:
            if book.is_allowed_transition(book.state, new_state):
                book.state = new_state
            else:
                #continue  #原本的，以下報錯使用的
                message = _('Moving from %s to %s is not allowd') % (book.state, new_state)
                raise UserError(message)

    def make_available(self):
        self.change_state('available')

    def make_borrowed(self):
        self.change_state('borrowed')

    def make_lost(self):
        self.change_state('lost')

    def log_all_library_members(self): #獲取其它模型的空記錄集
        library_member_model = self.env['library.member']  # This is an empty recordset of model library.member
        all_members = library_member_model.search([])
        print("ALL MEMBERS:", all_members)
        return True

    def change_release_date(self): #更新記錄集中記錄值
        self.ensure_one()
        self.date_release = fields.Date.today()

    def find_book(self): #搜索記錄 search on model
        domain = [
            '|',
            '&', ('name', 'ilike', 'Book Name'),
            ('category_id.name', '=', 'Category Name'),
            '&', ('name', 'ilike', 'Book Name 2'),
            ('category_id.name', '=', 'Category Name 2')
        ]
        books = self.search(domain)
        logger.info('Books found: %s', books)
        return True

    # Filter recordset
    def filter_books(self):
        all_books = self.search([])
        filtered_books = self.books_with_multiple_authors(all_books)
        logger.info('Filtered Books: %s', filtered_books)

    @api.model
    def books_with_multiple_authors(self, all_books):
        def predicate(book):
            if len(book.author_ids) > 1:
                return True
        return all_books.filtered(predicate)

    # Traversing recordset
    def mapped_books(self):
        all_books = self.search([])
        books_authors = self.get_author_names(all_books)
        logger.info('Books Authors: %s', books_authors)

    @api.model
    def get_author_names(self, all_books):
        return all_books.mapped('author_ids.name')

    # Sorting recordset
    def sort_books(self):
        all_books = self.search([])
        books_sorted = self.sort_books_by_date(all_books)
        logger.info('Books before sorting: %s', all_books)
        logger.info('Books after sorting: %s', books_sorted)

    @api.model
    def sort_books_by_date(self, all_books):
        return all_books.sorted(key='date_release')



class LibraryMember(models.Model):

    _name = 'library.member'
    _inherits = {'res.partner': 'partner_id'}
    _description = "Library member"

    partner_id = fields.Many2one('res.partner', required=True, ondelete='cascade')
    date_start = fields.Date('Member Since')
    date_end = fields.Date('Termination Date')
    member_number = fields.Char()
    date_of_birth = fields.Date('Date of birth')

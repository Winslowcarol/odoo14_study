# -*- coding: utf-8 -*-
from datetime import timedelta
from odoo import models, fields, api
from odoo.exceptions import ValidationError

#使用抽象模型實現可復用模型功能
class BaseArchive(models.AbstractModel):
    _name = 'base.archive'
    _description = 'Abstract Archive'

    active = fields.Boolean(default=True)

    def do_archive(self):
        for record in self:
            record.active = not record.active

class LibraryBook(models.Model):
    # 定義模型表現及排序
    _name = 'library.book'
    _inherit = ['base.archive'] # 使用抽象模型實現可復用模型功能
    _description = 'Library Book'
    _rec_name = 'short_name'
    _order = 'date_release desc, name'
    # 向模型添加數據字段以下
    name = fields.Char('Title', required=True)
    short_name = fields.Char('Short Title', required=True)
    notes = fields.Text('Internal Notes')
    date_release = fields.Date('Release Date')
    date_updated = fields.Datetime('Last Updated')

    author_ids = fields.Many2many('res.partner', string='Authors') # 添加關聯字段
    state = fields.Selection(
        [('draft', 'Not Available'),
         ('available', 'Available'),
         ('lost', 'Lost')],
        'State')
    description = fields.Html('Description')
    cover = fields.Binary('Book Cover')
    out_of_print = fields.Boolean('Out of Print?')
    pages = fields.Integer('Number of Pages')
    reader_rating = fields.Float(
        'Reader Average Rating',
        digits=(14, 4),  # Optional precision (total, decimals),
    )
    cost_price = fields.Float('Book Cost', digits='Book Price') #使用可配置精度的浮點字段
    currency_id = fields.Many2one(
        'res.currency', string='Currency')
    # 向模型添加貨幣字段
    retail_price = fields.Monetary(
        'Retail Price',
        # optional: currency_field='currency_id',
    )
    # 添加關聯字段
    publisher_id = fields.Many2one('res.partner', string='Publisher',
        # optional:
        ondelete='set null',
        context={},
        domain=[],)
    #暴露存儲在其它模型中的關聯字段 fields.Char('XXOO', related='publisher_id.city'...
    publisher_city = fields.Char(
        'Publisher City',
        related='publisher_id.city',
        readonly=True)
    category_id = fields.Many2one('library.book.category')
    age_days = fields.Float(
        string='Days Since Release',
        compute='_compute_age', inverse='_inverse_age', search='_search_age',
        store=False,
        compute_sudo=True,
    )
    #使用引用字段添加動態關聯-fields.Reference
    ref_doc_id = fields.Reference(selection='_referencable_models', string='Reference Document')

    @api.model
    def _referencable_models(self):
        models = self.env['ir.model'].search([('field_id.name', '=', 'message_ids')])
        return [(x.model, x.name) for x in models]

    @api.depends('date_release')
    def _compute_age(self):
        today = fields.Date.today()
        for book in self:
            if book.date_release:
                delta = today - book.date_release
                book.age_days = delta.days
            else:
                book.age_days = 0

    # This reverse method of _compute_age. Used to make age_days field editable
    # It is optional if you don't want to make compute field editable then you can remove this
    def _inverse_age(self):
        today = fields.Date.today()
        for book in self.filtered('date_release'):
            d = today - timedelta(days=book.age_days)
            book.date_release = d

    # This used to enable search on compute fields
    # It is optional if you don't want to make enable search then you can remove this
    def _search_age(self, operator, value):
        today = fields.Date.today()
        value_days = timedelta(days=value)
        value_date = today - value_days
        # convert the operator:
        # book with age > value have a date < value_date
        operator_map = {
            '>': '<', '>=': '<=',
            '<': '>', '<=': '>=',
        }
        new_op = operator_map.get(operator, operator)
        return [('date_release', new_op, value_date)]

    def name_get(self):
        """ This method used to customize display name of the record """
        result = []
        for record in self:
            rec_name = "%s (%s)" % (record.name, record.date_release)
            result.append((record.id, rec_name))
        return result
    #向模型添加約束驗證-SQL法
    _sql_constraints = [
        ('name_uniq', 'UNIQUE(name)', 'Book title must be unique.'),
        ('positive_page', 'CHECK(pages>0)', 'No. of pages must be positive')
    ]

    # 向模型添加約束驗證-API法
    @api.constrains('date_release')
    def _check_release_date(self):
        for record in self:
            if record.date_release and record.date_release > fields.Date.today():
                raise models.ValidationError('Release date must be in the past')

#向模型添加關聯字段
class ResPartner(models.Model):
    _inherit = 'res.partner'
    published_book_ids = fields.One2many('library.book', 'publisher_id',
            string='Published Books')
    authored_book_ids = fields.Many2many('library.book',string='Authored Books',
                                         # relation='library_book_res_partner_rel' # optional
        )
    count_books = fields.Integer('Number of Authored Books',
                                 compute='_compute_count_books') #向模型添加計算字段
    #使用繼承向模型添加功能
    @api.depends('authored_book_ids')
    def _compute_count_books(self):
        for r in self:
            r.count_books = len(r.authored_book_ids)

#使用代理繼承將功能拷貝至另一個模型
class LibraryMember(models.Model):
    _name = 'library.member'
    _inherits = {'res.partner': 'partner_id'}
    _description = 'Library Member'
#new definition for members
    partner_id = fields.Many2one('res.partner', required=True, ondelete='cascade')
    date_start = fields.Date('Member Since')
    date_end = fields.Date('Termination Date')
    member_number = fields.Char()
    date_of_birth = fields.Date('Date of birth')
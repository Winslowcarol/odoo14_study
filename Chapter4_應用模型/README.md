這個章節，是一些基本較簡單的功能入門，分別有以下：

#### 1.Defining the model representation and order
#### 2.Adding data fields to a model
#### 3.Using a float field with configurable precision
#### 4.Adding a monetary field to a model
#### 5.Adding relational fields to a model
#### 6.Adding a hierarchy to a model
#### 7.Adding constraint validations to a model
#### 8.Adding computed fields to a model
#### 9.Exposing related fields stored in other models
#### 10.Adding dynamic relations using reference fields
#### 11.Adding features to a model using inheritance
#### 12.Using abstract models for reusable model features
#### 13.Using delegation inheritance to copy features to another model


# 1.定義模型表現及排序 model attribution

## 前言
○ _rec_name:展示、紀錄標題。沒有欄位name宣告(name_get)的時候，我們會使用`_rec_name`代表每一筆紀錄。
    
○ _order：順序，資料排序的準則，輸入多筆記錄，要依照哪個欄位排列？
    
○ 基礎類型：Char, Text, Boolean, Integer, Float, Date, Datetime, Binary
* 日後搜尋：Text效能差，Char效能好
* 計算時：Float（記得宣告digit）會比起 Integer精準
* 日期與日期時間應用不同，使用前自行判斷定義	
* Binary: 物件型態，store binary files, such as images or documents.
      
○ 複雜類型：Function, Selection
    
○ 關係類型：Many2one, One2many, Many2many

## 步驟

## 補充		
**field中參數：**
* 1. `string="欄位名稱"`
* 2. `required=True`  是否必填項目
* 3. `fields.Selection([('1', '必修'), ('2', '選修')], string="課程型態", required=True)`  選項以tuple()裝在list[]中。
* 4. `default='填預設值'` 預設值，像是選項代號、呼叫今日時間給予時間選項。
* 5. `fields.Date` 日期欄位，另有Datetime可以選擇
* 6. `_rec_name` 沒有欄位name宣告(name_get)的時候，我們會使用`_rec_name`代表每一筆紀錄。 (record representation)
* 7. `Binary` 可以放圖片、檔案。
  
# 3.使用可配置精度的浮點字段 decimal precision 
## 前言
Float
## 步驟
## 補充

# 4.向模型添加貨幣字段 monetary field
## 前言
## 步驟
## 補充
# 5.向模型添加關聯字段 relational_fields(one2many, many2one, many2many)
## 前言
## 步驟
## 補充	
 ![image](https://user-images.githubusercontent.com/77597518/173006812-36ee5f95-16bd-4d4c-9d7d-5d1ba227e75e.png)

	
![image](https://user-images.githubusercontent.com/77597518/173006572-5582b69e-5101-4c16-aec0-d1a07dc80383.png)


# 6.向模型添加等級 hierarchy_model
## 前言
## 步驟
## 補充
# 7.向模型添加約束驗證 constraints
## 前言
## 步驟
## 補充
# 8.向模型添加計算字段 compute_fields
## 前言
## 步驟
## 補充
# 9.暴露存儲在其它模型中的關聯字段 related_fields
## 前言
## 步驟
## 補充
# 10.使用引用字段添加動態關聯 reference_fields
## 前言
## 步驟
## 補充
# 11.使用繼承向模型添加功能 Adding features to a model using inheritance
## 前言
odoo中提供了三種繼承：
### 1.Class inheritance (extension):在原生模型之上擴增功能。所以是使用原生模型的DB，多加上欄位資料。 這一章節要使用的。
### 2.Prototype inheritance:拷貝原本的模型所有功能，並寫把資料寫到新的DB，不使用原生模型的DB。通常取名.copy。
### 3.Delegation inheritance:使用`_inherits`，不想要使用那麼多新的DB空間放重複的資料，但又想要再增添欄位的時候，用另一個schema紀錄新欄位，畫面呈現的時候把原本的schema跟新的schema一起抓出來呈現。就會使用這個繼承。

這個章節使用Class inheritance，這邊範例使用添加功能1.關聯many2one，功能2.compute 
## 步驟
### Step1:py檔中加上model，使用`_inherit`，不用將模型命名，class抄原生的，加入兩個要添加的功能欄位。
```
class ResPartner(models.Model):
    _inherit = 'res.partner'
    _order = 'name'
    authored_book_ids = fields.Many2many(
        'library.book', string='Authored Books')
    count_books = fields.Integer( 'Number of Authored Books',
                  compute='_compute_count_books' )
```
### Step2:py檔中使用了compute記得在同個class下寫函式。
```
@api.depends('authored_book_ids')
def _compute_count_books(self):
   for r in self:
      r.count_books = len(r.authored_book_ids)
```
### Step3:View 也可以繼承，沒有view繼承會去抓原生的view，但因為擴增欄位了，所以我們就繼承來擴增。記得要放在__menifest__.py檔中的data。
```
<field name="inherit_id" ref="res.partner"/>

<field name="arch" type="xml">        
              <!-- position: after|before|replace|attributes|inside -->
      <xpath expr="//field[@name='']" position="">
          <field name="authored_book_ids">
	  <field name="count_books">
      </xpath>
              
</field>
```
## 補充
擴增的位置position可以選擇參數：after|before|replace|attributes|inside           
	
# 12.使用繼承拷貝模型定義 Copy model definition using inheritance (Prototype inheritance)
## 前言
拷貝原本的模型所有功能，並寫把資料重複寫到新的DB(新的一張table)，不使用原生模型的DB。通常取名.copy。
## 步驟
### Step1:創一個library_book_copy.py
```
from odoo import models, fields, api

class LibraryBookCopy(models.Model):
    _name = "library.book.copy"
    _inherit = "library.book"
    _description = "Library Book's Copy"
```
### Step2:同上面11，記得去__init__.py 新增model，然後要view也要改。模板範例如下：
```
<record id="view_inherit__form" model="ir.ui.view">
	<field name="name">view.inherit..form</field>
        <field name="model"></field>
        <field name="inherit_id" ref="res.partner"/>
        <field name="arch" type="xml">
              
              <!-- position: after|before|replace|attributes|inside -->
           <xpath expr="//field[@name='']" position="">
                  <!-- Add your fields or attributes here -->
           </xpath>
              
        </field>
</record>
```
## 補充
可以打開pgadmin，看是否有無新的DB寫上一樣的功能。
# 13.使用代理繼承將功能複製至另一個模型 Using delegation inheritance to copy features to another model (Delegation inheritance)
## 前言
這邊比較像是節外生枝。在原生的功能及table上，創建另一個table架在原生的table上使用。這邊範例是從'res.partner'模型下取'partner_id'來用。再創一個新的table。
## 步驟
### Step1:py檔寫入。
```
class LibraryMember(models.Model):
    _name = 'library.member'
    _inherits = {'res.partner': 'partner_id'}
    partner_id = fields.Many2one(
        'res.partner',
        ondelete='cascade')
```
### Step2:這邊增加四個欄位，產生新的table。
```
date_start = fields.Date('Member Since')
date_end = fields.Date('Termination Date')
member_number = fields.Char()
date_of_birth = fields.Date('Date of birth')
```
## 補充
ondelete='cascade'
# 14.使用摘要模型實現可復用模型功能 abstract_models
## 前言
## 步驟
## 補充
常用在報表，如果我們每天都要看一次當月銷售量，這樣我們都要調出銷售紀錄，重新篩選一次資料。這時候可以寫一個 Abstract model，設定好調取公式。
只要選項勾一勾就可以出現報表了。而且這個model不會把你調取的資料存到DB，輸出完摘要後馬上消失。只有動作寫起來，一個外掛程式的概念。



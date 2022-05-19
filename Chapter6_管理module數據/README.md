開始本章節之前，請先卸載及刪除上一章節的my_library，並使用chapter4-06_hierarchy_model的script開始。
本章中，從XML出發的odoo～～，透過修改XML中程式碼學習如何添加、刪改數據到module。分成以下單元：

**1.使用外部ID和命名空間 external identifier**

**2.使用XML文件加載數據 load data from xml**

**3.使用noupdate和forcecreate標記 noupdate andforcecreate**

**4.使用CSV文件加載數據 load from CSV file**

**5.插件更新和數據遷移 data migrations**

**6.從XML文件中刪除記錄 delete from xml**

**7.在XML文件中調用函數 invoke method from xml**


# 1.使用外部ID和命名空間 external_identifier
  ## 前言
   在這兒我們不從models寫函式修改命名資料，我們使用外部ID搭配XML來修改命名資料。在這兒我們先學習怎麼查詢ID。
   
   ► 查找XML ID: `設定修改開發者模式>小蟲子>查看元數據(metadata)`
		就可以找到以XML ID：	my_library.book_cookbook
    
   記住這ID是你要寫在XML當中的。
  ## 開始
  ### Step1: 更新__manifest__.py當中的聲明
  ```
  'data': [
  'data/data.xml',
  ],
  ```
  用取消註解的方式打開以上聲明。這邊就是聲明有一個data.xml檔案放在data資料夾下，讓主機抓到此檔案。
  ### Step2: 新增一個data.xml，放在data資料夾中，然後測試內容如下：
  ```
  <record id="book_cookbook" model="library.book">
    <field name="name">Odoo 14 Development Cookbook</field>
  </record>
  <record id="base.main_company" model="res.company">
    <field name="name">Packt Publishing</field>
  </record>
  ```
  你可以猜測到，我們創了一本書籍資料。然後我們修改了公司名稱。這邊的id就仰賴上方教導你的。可以比對一下。
  ### Step3: 在odoo網頁更新升級模組後，去網頁看是不是真的做了紀錄！！
  
# 2.使用XML文件加載數據 load_data_from_xml
  ## 前言
  ## 開始
  ### Step1:
  ### Step2:
  ### Step3:
# 3.使用noupdate和forcecreate標記 noupdate_and_forcecreate
  ## 前言
  遇到模組更新時，我們會疑惑Step1中用XML寫入的紀錄是否隨著模組更新後消失？刪除？複寫？這邊提供了兩個方案：
  
  **1)noupdate**：遇到模組更新時，會把更新前舊有的紀錄再寫到更新後模組裡(沒有要被刪掉的意思）。設定在xml檔中的`<odoo noupdate="1">`
  
  **2)forcecreate**：舊有的紀錄沒有要寫進去更新後的模組(就是要更新覆蓋的意思）。所以在模型後加入此指令：`forcecreate="False"`
  ## 開始
  ### Step1:noupdate，在data.xml裡頭修改：
  ```
  <odoo noupdate="1">
    <record id="res_partner_packt" model="res.partner">
      <field name="name">Packt publishing</field>
      <field name="city">Birmingham</field>
      <field name="country_id" ref="base.uk"/>
    </record>
  </odoo>
  ```
  ### Step2:forcecreate，在data.xml裡頭修改：
  ```
  <odoo noupdate="1">
    <record id="book_category_all" model="library.book.category" forcecreate="false">
      <field name="name">All books</field>
    </record>
  </odoo>
  ```
  ### Step3:在odoo網頁更新升級模組後....沒有嘗試刪改模組更新模組，我也未知。
# 4.使用CSV文件加載數據 
  ## 前言
  這章節沒有要跑跟要示範的script，這邊以security/ir.model.access.csv為例，說明CSV文件如何管控權限。
  所以先看懂CSV檔案，然後欄位分別代表什麼意思，以及0或1有如開關。這個應該在最初剛架完第一個addon就了解。

# 5.module更新和數據遷移 data_migrations
  ## 前言
  module更新時，有些model會存在版本更新前後是否相容問題，這時候採用這個遷移功能讓model的功能也更新。Odoo在更新時將聲明文件中的版本號寫入到ir_module_module表中。這邊以欄位`date_release`為例，進行遷移。
  ## 開始
  ### Step1:創建資料夾與資料夾放置。
  在my_library下創一個`migrations`資料夾，然後再創一個版本夾`14.0.1`，裡面多兩個py檔。
  
  <img width="202" alt="截圖 2022-05-19 上午8 47 48" src="https://user-images.githubusercontent.com/77597518/169178928-69246e94-ee3b-4539-8cfa-adb93fec7f28.png">
  
  ### Step2:寫一個函式，讓數據遷移。寫在`pre-migrate.py`裡頭
  ```
  def migrate(cr, version):
    cr.execute("""
        ALTER TABLE library_book
        RENAME COLUMN date_release TO date_release_char""")
  ```
  你會發現這邊出現了SQL語法，也就是讓底層SQL叫出數據來遷移。
  
  ### Step3:寫一個函式，讓數據遷移後做更新(變更)。寫在`post-migrate.py`裡頭
  ```
  from odoo import fields
  from datetime import date

  def migrate(cr, version):
    cr.execute('SELECT id, date_release_char FROM library_book')
    for record_id, old_date in cr.fetchall():
        # check if the field happens to be set in Odoo's internal
        # format
        new_date = None
        try:
            new_date = fields.Date.to_date(old_date)
        except ValueError:
            if len(old_date) == 4 and old_date.isdigit():
                # probably a year
                new_date = date(int(old_date), 1, 1)
            else:
                # try some separators, play with day/month/year
                # order ...
                pass
        if new_date:
            cr.execute('UPDATE library_book SET date_release=%s',
                       (new_date,))
  ```
  ### Step4: 提升__manifest__.py文件中的版本
  `'version': '14.0.1',`
  然後就在odoo網頁更新模組，主機就會自動抓取你現在的版本，判別是否進行數據遷移跟更新。
# 6.從XML文件中刪除記錄 delete_from_xml
  ## 前言
  這邊要識別的標籤屬性是model名稱，然後自己創一個把資料刪除的標籤ID。刪除方法有兩種：
  
	1) 刪除之前在XML文件創出的紀錄
	新建標籤：ID，寫在XML中
	`<delete model="library.book.category" id="book_category_to_delete"/>`
	
	2) 不是在XML文件創出的紀錄（是odoo系統寫入的）
	使用search domain當成標籤
        `<delete model="library.book.category" search="[('name', 'ilike', 'Test')]"/>`
  ## 開始
  ### Step1:在`data.xml`模擬創兩筆資料，等等拿來刪掉：
  ```
  <record id="book_category_to_delete" model="library.book.category">
  	<field name="name">Test Category</field>
  </record> 
  <record id="book_category_not_delete" model="library.book.category">
  	<field name="name">Test Category 2</field>
  </record>
  ```
  ### Step2:在`data.xml`設定要刪除的資料
  ```
  <delete model="library.book.category" id="book_category_to_delete"/>
  ```
  這邊你只下了刪除一筆的指令。而且是刪除之前在XML文件創出的紀錄。
  ### Step3:在odoo網頁升級模組後，查看category
   ![image](https://user-images.githubusercontent.com/77597518/169181044-eaefb105-9c40-4f85-b507-417d6257795a.png)
	
   一個Test Category有刪掉，一個Test Category 2（沒執行功能）沒刪掉。
  
# 7.在XML文件中調用函數 invoke_method_from_xml
  ## 前言
  ## 開始
  ### Step1:
  ### Step2:
  ### Step3:

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
  ## 開始
  ### Step1:
  ### Step2:
  ### Step3:
# 5.插件更新和數據遷移 data_migrations
  ## 前言
  ## 開始
  ### Step1:
  ### Step2:
  ### Step3:
# 6.從XML文件中刪除記錄 delete_from_xml
  ## 前言
  ## 開始
  ### Step1:
  ### Step2:
  ### Step3:
# 7.在XML文件中調用函數 invoke_method_from_xml
  ## 前言
  ## 開始
  ### Step1:
  ### Step2:
  ### Step3:

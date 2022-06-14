這個章節，是一些基本較簡單的功能入門，分別有以下：
#### 1.定義模型表現及排序 model attribution
○ _rec_name:展示、紀錄標題
    
○ _order：順序
    
○ _description：給用戶看的模型標題
    
#### 2.向模型添加數據字段 data field
		
***以下第3~5節，說明資料型態，這邊統整分三類：***
    
○ 基礎類型：Char, Text, Boolean, Integer, Float, Date, Datetime, Binary
* 日後搜尋：Text效能差，Char效能好
* 計算時：Float（記得宣告digit）會比起 Integer精準
* 日期與日期時間應用不同，使用前自行判斷定義	
* Binary: 物件型態，store binary files, such as images or documents.
      
○ 複雜類型：Function, Selection
    
○ 關係類型：Many2one, One2many, Many2many

***field中參數：***
* 1. `string="欄位名稱"`
* 2. `required=True`  是否必填項目
* 3. `fields.Selection([('1', '必修'), ('2', '選修')], string="課程型態", required=True)`  選項以tuple()裝在list[]中。
* 4. `default='填預設值'` 預設值，像是選項代號、呼叫今日時間給予時間選項。
* 5. 
  
#### 3.使用可配置精度的浮點字段 decimal precision 
    Float
#### 4.向模型添加貨幣字段 monetary field
#### 5.向模型添加關聯字段 relational_fields(one2many, many2one, many2many)
	
 ![image](https://user-images.githubusercontent.com/77597518/173006812-36ee5f95-16bd-4d4c-9d7d-5d1ba227e75e.png)

	
![image](https://user-images.githubusercontent.com/77597518/173006572-5582b69e-5101-4c16-aec0-d1a07dc80383.png)


#### 6.向模型添加等級 hierarchy_model
#### 7.向模型添加約束驗證 constraints
#### 8.向模型添加計算字段 compute_fields
#### 9.暴露存儲在其它模型中的關聯字段 related_fields
#### 10.使用引用字段添加動態關聯 reference_fields
#### 11.使用繼承向模型添加功能 model_inheritance
#### 12.使用繼承拷貝模型定義 copy_model
#### 13.使用代理繼承將功能拷貝至另一個模型 inheritance_delegation
#### 14.使用摘要模型實現可復用模型功能 abstract_models
常用在報表，如果我們每天都要看一次當月銷售量，這樣我們都要調出銷售紀錄，重新篩選一次資料。這時候可以寫一個 Abstract model，設定好調取公式。
只要選項勾一勾就可以出現報表了。而且這個model不會把你調取的資料存到DB，輸出完摘要後馬上消失。只有動作寫起來，一個外掛程式的概念。



這個章節，是一些基本較簡單的功能入門，分別有以下：
#### 1.定義模型表現及排序 model attribution
○ _rec_name:展示、紀錄標題
    
○ _order：順序
    
○ _description：給用戶看的模型標題
    
#### 2.向模型添加數據字段 data field
		
以下第3~5節，說明資料型態，這邊統整分三類：
    
○ 基礎類型：Char, Text, Boolean, Integer, Float, Date, Datetime, Binary
		§ 日後搜尋：Text效能差，Char效能好
		§ 計算時：Float（記得宣告digit）會比起 Integer精準
		§ 日期與日期時間應用不同，使用前自行判斷定義	
		§ Binary: 物件型態，store binary files, such as images or documents.
      
○ 複雜類型：Function, Selection
    
○ 關係類型：Many2one, One2many, Many2many
  
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
#### 14.使用抽象模型實現可復用模型功能 abstract_models

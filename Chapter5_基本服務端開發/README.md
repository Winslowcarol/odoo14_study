這個章節，關注在「服務端」，也就是terminal提供了哪些數據、哪些功能、哪些服務。
分成幾個單元如下：
#### 1. 定義模型方法及使用API裝飾器
#### 2. 向用戶報出錯誤
#### 3.獲取其它模型的空記錄集
#### 4.新建記錄
#### 5.更新記錄集中記錄值 *Updating values of recordset records*
#### 6.搜索記錄 *Searching for records*
#### 7.合併記錄集
#### 8.過濾記錄集
#### 9.遍歷記錄集關聯
#### 10.記錄集排序
#### 11.繼承模型中定義的業務邏輯
#### 12.繼承write()和create()
#### 13.自定義記錄的搜索方式
#### 14.使用read_group()從組中獲取數據

開始前，先到網頁**卸載**chapter4使用的my_library，再至自己的my-addon中刪掉my_library。
使用版本為chapter3完成的版本開始。

# 1. 定義模型方法及使用API裝飾器
# 2. 向用戶報出錯誤
# 3.獲取其它模型的空記錄集
# 4.新建記錄
# 5.更新記錄集中記錄值 Updating values of recordset records
## 前言
## 步驟
## 說明
	(0,_,{‘field’:value}) 	新建一條記錄並將其與之關聯
	(1,id,{‘field’:value})	更新已關聯記錄的值
	(2,id,_)	移除關聯並刪除id關聯的記錄
	(3,id,_)	移除關聯但不刪除id關聯的記錄,通常使用來刪除many2many欄位關聯值
	(4,id,_)	關聯已存在記錄,僅適用  many-to-many 欄位
	(5,_,_)	刪除所有關聯,但不刪除關聯記錄
	(6,_,[ids])	替換已關聯記錄清單為此處清單

	上述底線_ 字元代表非關聯值,通常填入0 或 False。添加(4) 和 替換(6) 是最常使用的命令
# 6.搜索記錄 Searching for records
## 前言
    這兒透過使用宣告domain，使用名稱(name)跟分類(cate)來找到書本(book)。
## 步驟
### (1) def find_book(self):
	function
### (2) domain =
	設定搜索域
	補充：https://odootricks.tips/about/building-blocks/domain-in-odoo/
### (3) books = self.search(domain)
	search()方法也可以用search_count(domain)
## 說明

# 7.合併記錄集
## 前言
## 步驟
## 說明
# 8.過濾記錄集
# 9.遍歷記錄集關聯
# 10.記錄集排序
# 11.繼承模型中定義的業務邏輯
# 12.繼承write()和create()
# 13.自定義記錄的搜索方式
# 14.使用read_group()從組中獲取數據

這個章節，關注在「服務端」，也就是terminal提供了哪些數據、哪些功能、哪些服務。
分成幾個單元如下：
#### 1. 定義模型方法及使用API裝飾器
#### 2. 向用戶報出錯誤
#### 3.獲取其它模型的空記錄集
#### 4.新建記錄
#### 5.更新記錄集中記錄值
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
# 5.更新記錄集中記錄值
# 6.搜索記錄 Searching for records
### 前言
    這兒透過使用宣告domain，使用名稱(name)跟分類(cate)來找到書本(book)。
### 步驟
#### (1) def find_book(self):
	function
#### (2) domain =
	設定搜索域
	補充：https://odootricks.tips/about/building-blocks/domain-in-odoo/
#### (3) books = self.search(domain)
	search()方法也可以用search_count(domain)
### 說明

# 7.合併記錄集
### 前言
### 步驟
### 說明
# 8.過濾記錄集
# 9.遍歷記錄集關聯
# 10.記錄集排序
# 11.繼承模型中定義的業務邏輯
# 12.繼承write()和create()
# 13.自定義記錄的搜索方式
# 14.使用read_group()從組中獲取數據

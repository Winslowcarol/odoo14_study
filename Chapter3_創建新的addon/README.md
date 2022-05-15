# 使用Pycharm創建新的addon

在這個章節中，開始一個addon的基本架構。我們可以說addon是一個模組(module)，或是一個模塊。
而如果我們都單純的使用終端機terminal來寫code會非常的需要腦中有個清晰架構，所以最簡易輕便的方式就是找個IDE輔助自己。
這邊我都是使用Pycharm讓自己可視整個架構。先讓我們看一個odoo中的addon骨架長怎樣。

 ![image](https://user-images.githubusercontent.com/77597518/168454050-007c4a72-21ca-48c6-903f-50a7959923bf.png)

知道骨架之後，每個細節都是非常微小但都具有功能，時間允許之下，可以瀏覽官網odoo doc-[Building a Module](https://www.odoo.com/documentation/14.0/developer/howtos/backend.html#security)，
這兒我們不依照每一個細節寫code，我們用一個odoo快速的功能-scaffold快速幫我們建立一個骨架。

## 使用odoo scaffold 的功能複製一個addon基本的骨架。

oodo提供了[scaffold自動創建骨架](https://www.odoo.com/documentation/14.0/developer/misc/other/cmdline.html#scaffolding)的套件，可以去官網Command-line interface (CLI)查詢。

我們依照下面步驟進行：
### Step1:打開IDE-Pycharm

到你的應用程式，打開pycharm，點開你上次設定好的project。畫面左上資料夾結構那兒，按下右鍵會有非常多的功能。
### Step2:Set up new file(package)並命名，下語法scaffold

在左上資料夾結構那兒，在my-addon夾子按下右鍵創建新的資料。

<img width="663" alt="截圖 2022-05-15 下午9 56 02" src="https://user-images.githubusercontent.com/77597518/168476561-b1aff63e-abba-43d9-b0bf-62a693d90e87.png">

這時候你也同時看到你上一次設定好的odoo資料夾，在odoo資料夾中點下odoo-bin，就執行這個環境了。

<img width="414" alt="截圖 2022-05-15 下午9 59 35" src="https://user-images.githubusercontent.com/77597518/168476681-8af3c5b6-01e4-4d29-b17e-862057744a6a.png">

接下來你會看到下方有terminal出現，這兒就是我們要下指令的地方。

`python odoo-bin scaffold myfirstaddon ../my-addons/`

整個骨架複製完成！！
### Step3:回到localhost html畫面，確認有無新建模組成功。

骨架複製完成後，在網頁回到localhost(之前你的IP網址)，按下 ![image](https://user-images.githubusercontent.com/77597518/168476815-3c2c5dbe-16c8-4e3d-b81f-ffe179edf596.png)

再到模組搜尋myfirstaddon，就可以出現在你的畫面上了！但現在還沒解鎖很多基本功能跟網頁可視化功能。

### Step4:修改基本要件，開始我們的odoo-MVC之旅！！

當我們了解骨架之後，我們先去`__Mainfest__.py`打開security(python的取消註解)。<img width="314" alt="截圖 2022-05-15 下午10 18 15" src="https://user-images.githubusercontent.com/77597518/168477454-57e1fcbd-1828-41c7-94cb-80d434fe661c.png">

然後確認MVC(model, views, controllers)是否開啟功能。

#### (1)model
`models/models.py`檔案中，把最基本的功能打開(python的取消註解)。裡面已經自動寫入你當初創addon的名稱。這兒是之後我們要建立所有功能(function)的地方，就是後端的意思。
#### (2)views
`views/views.xml`檔案中，把最基本的功能打開(python的取消註解)。這兒是網頁可視化的部分，我們要開始學習html語法，跟理解可視化效果。
#### (3)controllers
`controllers/controllers.py`檔案中，把最基本的功能打開(python的取消註解)。這兒比較像是中央控制器，會幫你的model設定途徑的開關。
#### (4)升級，創建成功！
打開網頁localhost，在myfirstaddon的模組按下升級update，升級成功就會跳到你的ERP第一個模組畫面了！！升級失敗，網頁會報錯，然後就是debug之路了！
			
			

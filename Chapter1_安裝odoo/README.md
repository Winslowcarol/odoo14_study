
**我使用電腦的是Macbook pro 14，按照Macbook的安裝方式。**
# Install odoo14 on Macbook

## Step 1:打開終端機確認以下軟體是否事先安裝
### (1)python
`$ python3 --version`
### (2)pip or pip3
`$ pip3 --version`
     
### (3)資料庫 PostgreSQL
安裝參考[Installing Postgres Database using Homebrew](https://www.sqlshack.com/setting-up-a-postgresql-database-on-mac/)

安裝結束後記得創建一個給odoo登入的帳密，Mac的主設帳號是自己，要用以下方式才可以以postgres登入

`psql -U postgres`

輸入密碼

設定Postgres使用者：	
```
Create user odoo superuser;
alter user odoo with password 'odoo'
```

## Step 2:架設環境
[Mac版本-參考連結有影片唷！](https://googlyengineer.blogspot.com/2021/08/how-to-setup-odoo-on-macbook-pro.html)
```
xcode-select -p
xcode-select --install
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
nano ~/.bash_profile
export PATH="/usr/local/bin:$PATH"
source ~/.bash_profile
brew install git
brew search python
python3.7 -m venv ~/odoo14env
source ~/odoo14env/bin/activate
git clone https://github.com/odoo/odoo.git -b 14.0 --single-branch --depth 1
cd odoo
python3.7 -m pip install -r requirements.txt
python odoo-bin
```
通常在最後幾步驟會一直出錯，可能是path不對，也可能是密碼不對，這時候在odoo資料下增設odoo.conf檔案，讓系統自動去抓密碼或path。

如果在步驟
`python3.7 -m pip install -r requirements.txt`
有安裝成功，可以先裝完IDE再來處理odoo.conf，可視化會輕鬆很多。

## Step 3:Create database (可以在IDE完成後再執行)
這一步是使用odoo建立一個PostgreSQL資料庫，存在你的local端。

terminal執行`python odoo-bin`

打開瀏覽器，輸入http://127.0.0.1:8069/ （127.0.0.1因電腦不同而異）

設定資料，創建database。Master code習慣設定odoo或同一組密碼，資料庫命名習慣標上odoo版本。

在這兒安裝[pgadmin](https://www.pgadmin.org/download/pgadmin-4-macos/)方便日後檢查PostgreSQL資料庫。


## Step 4:安裝IDE-pycharm
因為前輩都用pycharm，我就安裝pycharm了。

### (1)按照[PyCharm](https://www.jetbrains.com/pycharm/)官網安裝即可。
### (2)打開PyCharm, 會請你先建立project（my-addon)，
到Preference設定環境，我們要開發odoo的是python3.7(odoo14env)，前幾個步驟架設好的環境。
<img width="443" alt="截圖 2022-05-13 下午5 23 20" src="https://user-images.githubusercontent.com/77597518/168253811-1715ebeb-697e-490d-8ecd-4161458d39ee.png">
到Preference設定目錄

### (3) 

Set up new file (package)


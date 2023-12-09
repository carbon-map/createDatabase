from getFuel import getInform
import pymysql
import os
from dotenv import load_dotenv

# 載入 .env 
load_dotenv()

# 資料庫設定
db_settings = {
    "host": os.getenv('host'),
    "port": int(os.getenv('port')),
    "user": os.getenv('user'),
    "password": os.getenv('password'),
    "db": os.getenv('db'),
    "charset": "utf8"
}


try:
    # 建立Connection物件
    conn = pymysql.connect(**db_settings)
    # 建立Cursor物件
    with conn.cursor() as cursor:
      data = getInform()
      for i in data:
        command = f"INSERT INTO fuel (year, month, city, gasoline, diesel_fuel) VALUES ({i['year']}, {i['month']}, '{i['city']}', {i['gasoline']}, {i['diesel_fuel']});"
        print(command)
        cursor.execute(command)
        conn.commit()
        
except Exception as ex:
    print(ex)
import pandas as pd
import openpyxl
import os
import re
from tqdm import tqdm


def getInform():
  data = []
  path = './file/'
  extensionName = '.xlsx'

  fileList=os.listdir(path)

  for i in tqdm(fileList):
    df = pd.read_excel(path + i, sheet_name='銷售統計表', usecols="A, C, D")
    
    # 其他地方沒有資料
    df = df[3:25] 
    
    # 獲得年份月份
    matches = re.findall(r'\d+', i)
    
    # 將所有縣市的資料變成一個 list
    # 用此方法去遍歷儲存格的每個 row 
    for index, row in df.iterrows():
      infromation = {
        'year' : int(matches[0]),
        'month': int(matches[1]),
        'city': row[0],
        'gasoline': int(row[1]),
        'diesel_fuel': int(row[2])
      }
      data.append(infromation)
  
  return data
  

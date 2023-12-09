import os
import re

path = "./file/"

fileList=os.listdir(path)


for i in fileList:
  matches = re.findall(r'\d+', i)
  newname = str(int(matches[0]) - 1911) + '-' + matches[1] + '.xlsx'
  os.rename(path + i, path + newname)
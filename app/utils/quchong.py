#quchong
#单元格去重与统计

import pandas as pd

#从excel表格中读取单元格，去掉重复单元格内容
def rmduplicate(xlsfile):
    data = pd.read_excel(xlsfile)

    newdata = []
    for i in data:
        for j in data[i]:
            if not isinstance(j, str):
                continue
            j = j.replace(' ', '').strip()
            if j not in newdata:
                newdata.append(j)
    return newdata

#从excel表格中读取单元格，统计单元格内容频次
def countcells(xlsfile):
    data = pd.read_excel(xlsfile, header=None, index_col=None)
    newdata = {}
    for i in data:
        for j in data[i]:
            if not isinstance(j,str) or j == 'nan':
                continue
            j = str.strip(j).replace(' ', '')
            if j not in newdata:
                newdata[j] = 1
            else:
                newdata[j] += 1
    return newdata




#encoding:utf-8
#从两个excel表格文件中匹配出有共同元素的两列

def excelmapping(file1,file2,field,path,mod='left'):
    import pandas as pd

    fields = field.replace(" ","").split('|')
    '''
    print(fields)
    cvts={}
    for k in fields:
        cvts[k]=str
    
    df1 = pd.read_excel(file1,converters=cvts)
    df2 = pd.read_excel(file2,converters=cvts)
    '''
    # 为避免身份证、学号等信息变成浮点类型，强制将所有列转换成str具有更大通用性
    df1 = pd.read_excel(file1,dtype=str)
    df2 = pd.read_excel(file2,dtype=str)

    df3 = pd.merge(df1,df2,on=fields,how=mod)
    mapfile = path + r'匹配结果.xlsx'
    '''
    with open(mapfile,'w') as file:
        df3.to_excel(file,'匹配结果')

    '''   
    writer = pd.ExcelWriter(mapfile)
    df3.to_excel(writer,'匹配结果')
    writer.save()
    writer.close()

    return mapfile
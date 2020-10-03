import pandas as pd

# 综合素质教育评价
# 教学班匹配课程模块和任课老师
# df1格式:[学年|学期|年级|学段|科目代码|模块代码|模块名称|学科(与级部课表里的课程名一致)|01（1班任课老师姓名）|	……]
# filename:任课安排.xlsx
def toTechCourse(filename,savepath,classNo,className,classNums):

    df1 = pd.read_excel(filename,converters={'学期': str, '科目代码': str, '模块代码': str})
    df2 = pd.DataFrame()  # 存储结果
    # df2.columns=['学年','学期','年级','学段','科目代码','模块代码','教学班班号','教学班名称','任课老师姓名','教学班级']
    # 教学班班号=jxb+入学年份+学年+学期+模块代码+班级编号(01,02,...,16)
    # 教学班号前缀=jxb+入学年份(两位)+学年(起止学年后两位)+学期
    # preClassNo = 'jxb17'#2019-2020第一学期前缀,该前缀过于简单,社会公益2模块在多个年级反复开设,导致教学班重名,故采用补充学期作前缀
    # preClassNo = 'jxb1719201'#17年入学,当前学年2019-2020,上学期1,下学期2
    preClassNo = classNo
    # 教学班名称前缀=入学年份(两位)-学年(起止学年后两位)-学期(1-上学期，2-下学期)
    # preClassName = '17-1920-1'
    preClassName = className

    for index, row in df1.iterrows():

        # a,b 为单列
        a = row[0:7]
        b = row['01':classNums]  # 01-16 班任课老师

        i = 1  # 记录班号
        for t in b:
            if t == None or pd.isnull(t):
                # 去掉选课空值,跳过,班级号加1
                i += 1
                continue

            if i < 10:
                k = '0' + str(i)
            else:
                k = str(i)

            # 教学班班号,教学班名称长度不超过30个字符,超过要用缩写,
            c = a.copy()
            c['教学班班号'] = preClassNo + c['模块代码'] + k

            # #如果之前选修过,后又需补选休的课程,教学班名称会重复导致导入失败，用前缀preClassName进行唯一命名
            # c['教学班名称'] = c['学年'] + '-' + c['学期'] + c['模块名称']+ '教学' + k +'班'
            c['教学班名称'] = preClassName + c['模块名称'] + '教学' + k + '班'  # 命名唯一
            c['任课老师姓名'] = str(t).strip().replace(' ', '')
            c['教学班级'] = i

            # c只有1列，将c从series转换为dataframe
            d = pd.DataFrame(c)
            # print(type(d),d.T)

            # d进行转置后再拼接
            df2 = pd.concat([df2, d.T], axis=0, sort=False)
            i += 1

    writer = pd.ExcelWriter(savepath + '/教学班-任课老师.xlsx')
    df2.to_excel(writer, '以教学班选课导入')
    writer.save()
    writer.close()
    return savepath+'教学班-任课老师.xlsx'


# 综合素质评价
# 教学班匹配课程代码-任课老师-学生
# df4必含列[‘学籍’，‘姓名’，‘教学班级’，‘行政班级’]
# filename1:教学班-任课老师.xlsx
# filename2:学生信息.xlsx
# 学籍列必须字符串类型,教学班级列必须是正数型,个位数班级前不补零
def toStCourse(filename1,filename2,savepath):

    df3 = pd.read_excel(filename1,converters={'学期': str, '科目代码': str, '模块代码': str})
    df4 = pd.read_excel(filename2,converters={'学籍': str, '教学班级': int})
    group3 = df3.sort_values(by='教学班级').groupby('教学班级')
    group4 = df4.sort_values(by='教学班级').groupby('教学班级')

    result = []
    for id4, row4 in group4:
        # id4:groupby的分组号，由于是按照教学班级分组，因此id4的值对应教学班级号
        # id4值为整数
        row3 = group3.get_group(id4)

        for k3, v3 in row3.iterrows():
            for k4, v4 in row4.iterrows():
                result.append(v3.tolist() + v4.tolist())

    df = pd.DataFrame(result)
    df.columns = df3.columns.tolist() + df4.columns.tolist()

    writer = pd.ExcelWriter(savepath + '/教学班-任课老师-学生选课数据.xlsx')
    df3.to_excel(writer, '以教学班选课导入')
    df.to_excel(writer, '选课结果')
    writer.save()
    writer.close()
    return savepath+'教学班-任课老师-学生选课数据.xlsx'


# 生成课程表
# df5 包含['模块代码','模块名称','教学班班号','教学班名称','任课老师姓名','教学班级']
# df6 包含['模块代码','学科'] 学科名称要与df7课表中的学科名称一致
# df7格式=['类型','星期','节次','1班'...'16班']
# filename1:教学班-任课老师-学生选课数据.xlsx==df5
# filename2:任课安排.xlsx==df6
# filename3:课表.xlsx==df7
# 所有字段名称无左右空格

def toClassTimeDate(filename1,filename2,filename3,savepath):

    df5 = pd.read_excel(filename1,
                        converters={'模块代码': str, '教学班级': int})[['模块代码', '模块名称', '教学班班号', '教学班名称', '任课老师姓名', '教学班级']]
    df6 = pd.read_excel(filename2, converters={'模块代码': str})[['模块代码', '学科']]
    df7 = pd.read_excel(filename3,converters={'星期': str, '节次': str})

    # 转换为字典{学科简称:模块名}
    tmp = df6.to_dict(orient='records')
    subject = {}
    for line in tmp:
        subject[line['学科'].strip().replace(' ', '')] = line['模块代码']

    # 将二维课程表转换为['模块代码','班级','星期','节次','地点']的一维列表
    kechengSet = []  # 转换后的一维列表
    dclass = df7[0:1]  # 班级列表
    dlocation = df7[1:2]  # 上课地点列表

    # 开始逐行转换,每行内按班级逐次转换,每个班级的每个科目转换后保存到单独一个列表(kecheng[])
    for row in df7[2:].iterrows():
        classNum = 16  # 班级数
        for i in range(classNum):
            kecheng = []  # 保存当前行转换结果,[模块代码,班级,星期,节次,地点]
            classNub = str(i + 1) + '班'

            # k=学科名称,row[0]为索引,row[1]为数据内容
            k = row[1][classNub]

            # 不排课的单元格跳过,excel中空单元格默认为8个空格,不是None,将空格替换为空字符串后再判断
            if type(k) == float:
                k = str(k)
            k = k.strip().replace(' ', '')
            if k == '' or k == None or k == 'nan' or k == 's':  # s为空格占位符
                continue

            kecheng.append(subject[k])  # 模块代码
            kecheng.append(
                int(dclass[classNub].to_string(index=False)))  # 教学班级,dataframe先转换为字符串并去掉索引,df5中教学班级为int类型,这里也转换为int
            kecheng.append(str(row[1]['星期']))  # 星期
            kecheng.append(str(row[1]['节次']))  # 节次
            kecheng.append(dlocation[classNub].to_string(index=False))  # 上课地点,dataframe先转换为字符串并去掉索引

            # 存入总列表中
            kechengSet.append(kecheng)

    # 将转换后的课程表列表再转换为DataFrame格式
    df8 = pd.DataFrame(kechengSet)
    df8.columns = ['模块代码', '教学班级', '星期', '节次', '地点']

    # 与df5合并
    df9 = pd.merge(df5, df8, how='outer', on=['模块代码', '教学班级'])

    # 写入excel
    writer = pd.ExcelWriter(savepath + '/排课表.xlsx')
    df9.to_excel(writer, '排课表')
    writer.save()
    writer.close()
    return savepath+'排课表.xlsx'
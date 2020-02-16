#将自明排课表输出的带制表符的txt格式课程表转换为逗号分割的csv格式文件
#课程名称要与df6中学科一列的名称保持一致
import os.path
import tempfile

def zmto_csv(file):
    name,ext = os.path.splitext(file.name)
    if ext not in 'txt':
        return "文件类型错误,不是txt文件"

    remap = {
        ord('┌'):None, #删除
        ord('┬'):None,
        ord('─'):None,
        ord('├'):None,
        ord('┼'):None,
        ord('┤'):None,
        ord('┴'):None,
        ord('┘'):None,
        ord('└'):None,
        ord('┐'):None,
        ord('│'):',',
        ord(' '):''#空格替换为空串
    }

    #创建临时文件
    csvtemp = tempfile.NamedTemporaryFile('w+b',prefix='ziming')

    # NamedTemporaryFile 在windows下无效,需要将临时文件先关闭再打开才行
    import platform
    if platform.system() == 'Windows':
        csvtemp.close()

    with open(csvtemp.name,'w+b') as csvf:
        with open(file.name) as f:
            for line in f:
                s = line.translate(remap)
                csvf.write(s)
        csvf.seek(0)
        return csvtemp
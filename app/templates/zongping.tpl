%include('header')
<h3>高中综合素质评价数据生成系统</h3>
<p>山东省高中综合素质评价平台需要导入三个模板，课程计划导入模板.xls（<a href='./zongping/download/1-upsubject.xls' target='_blank'>点击下载</a>），教学班-选课结果.xls（<a href='./zongping/download/2-upcourse.xls' target='_blank'>点击下载</a>），课程表导入模板.xls（<a href='./zongping/download/3-upschedule.xls' target='_blank'>点击下载</a>）。
    后两个模板填充数据量较大，通过下面的程序生成所需数据，再填入上述模板中。</p>
<p><b>一、生成教学班-选课结果模板所需数据</b></p>
<p>先手工填充中间模板1-任课安排.xlsx（<a href='./zongping/download/1-teachers.xlsx' target='_blank'>点击下载</a>）和中间模板2-学生信息.xlsx(<a href='./zongping/download/2-students.xlsx' target='_blank'>点击下载</a>），将自动生成教学班-选课结果.xls 所需数据</p>
<p>学生信息以学籍平台数据为准，<a href='/excelmap' target='_blank'>学籍信息匹配工具</a></p>
<p></p>
<p>教学班号前缀=jxb+入学年份(两位)+学年(起止学年后两位)+学期。例jxb1719201 ：17年入学,当前学年2019-2020,上学期1,下学期2'</p>
<p>教学班名称前缀=入学年份(两位)-学年(起止学年后两位)-学期(1-上学期，2-下学期)。例17-1920-1：17年入学，2019-2020学年，上学期</p>

<form action='/zongping/upload0' name='form0' id='form0' method='post' enctype='multipart/form-data'>
    上传任课安排.xlsx<input type='file' name='course'><br />
    上传学生信息.xlsx<input type='file' name='student'><br />
    教学班号前缀<input type='text' name='preno' ><br />
    教学班名称前缀<input type='text' name='prename'><br />
    教学班级数量<input type='text' name='classnum'><br />
    <input type='submit' name='submit' value='生成教学班-选课结果.xls所需数据'><br />
</form>

<p><b>二、生成课程表导入模板</b></p>
<p>填充中间模板1-任课安排.xlsx，上一步生成的教学班-任课老师-学生信息.xlsx，中间模板3-课表.xlsx（<a href='./zongping/download/3-schedule.xlsx' target='_blank'>点击下载</a>)，将自动生成课程表导入模板.xls所需数据。</p>
<p>可以将自明排课表生产的txt课表转换成excel格式再上传。<a href='/ziming' target='_blank'>自明排课表转换工具</a></p>
<form action='/zongping/upload1' name='form1' id='form1' method='post' enctype='multipart/form-data'>
    上传任课安排.xlsx<input type='file' name='teacher'><br />
    上传教学班-任课老师-学生选课数据.xlsx<input type='file' name='course1'><br />
    上传课表.xlsx<input type='file' name='schedule' ><br />
    <input type='submit' name='submit1' value='生成课程表导入模板.xls所需数据'><br />
</form>

<p><b>三、填充综合素质评价平台正式模板</b></p>

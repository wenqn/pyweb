
<h2>excel 字段比较</h2>
<h3>输入:xls或者xlsx，匹配字段名称必须在两个表格中一致</h3>
<p>表格A、表格B,</p><p>匹配字段:姓名</p>
<table>
    <tr><td>
        <table>
        <th>姓名</th><th>学号</th>
        <tr><td>张三</td><td>1001</td></tr>
        <tr><td>李四</td><td>1002</td></tr>
        <tr><td>王五</td><td>1003</td></tr>
            <tr><td>　　</td><td>　　</td></tr>
        </table>
    </td>
    <td>
        <table>
        <th>姓名</th><th>身份证</th>
        <tr><td>张三</td><td>370303.......1001</td></tr>
        <tr><td>王五</td><td>370303.......1002</td></tr>
        <tr><td>赵六</td><td>370303.......1003</td></tr>
        <tr><td>李四</td><td>370303.......1004</td></tr>
        </table>
    </td></tr>
</table>
<h3>输出：xlsx</h3>
 <table>
        <th>姓名</th><th>学号</th><th>身份证</th>
        <tr><td>张三</td><td>1001</td><td>370303.......1001</td></tr>
        <tr><td>李四</td><td>1002</td><td>370303.......1004</td></tr>
        <tr><td>王五</td><td>1003</td><td>370303.......1002</td></tr>
        <tr><td>赵六</td><td>    </td><td>370303.......1003</td></tr>
 </table>
<p></p><p></p>

%include('uploads.tpl',subapp='excelmap',num=2,title='excel字段比较',line='<p>匹配字段：<input type="text" name="field" size="30">多个字段用|分割<p><p>匹配模式：<select name="mod"><option value="left">left</option><option value="right">right</option><option value="inner">inner</option><option value="outer">outer</option></select></p>')
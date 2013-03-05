#!/usr/bin/python

# Import the CGI, string, sys modules
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
# Define function to generate HTML form.
def login_form():
    html="""



<body>

<form>
<input type="radio" name="album" value="
upload
" /> 
upload
<br />
        <INPUT TYPE="hidden" NAME="action" VALUE="file_choose">
        <INPUT TYPE=submit VALUE="Enter">
        </FORM>
    

            </body>
            </html>

"""
    print(html)



def upload_file_data(form):
    #Check session is correct


    #Get file info
    fileInfo = form['file']

    if fileInfo.filename:
        # Remove directory path to extract name only
        fileName = os.path.basename(fileInfo.filename)
        open(fileName, 'wb').write(fileInfo.file.read())
        print('<H2>The file ' + fileName + ' was uploaded successfully</H2>')
        print(' <FORM ACTION="cetus_load.cgi" METHOD="POST" enctype="multipart/form-data">')
        print('    <input type="hidden" name="file_name" value=" ')
        print(fileName)
        print( '">')
        print('<br>')
        print('<input type="submit" value="RUN">')
        print('<INPUT TYPE="hidden" NAME="action" VALUE="run_app"> </from>')    
    #print('<image src='+'"users/'+user+"/albums/"+album+'/' + fileName + '" width=400 height=300>')
    else:
        message = 'No file was uploaded'
   

def file_choose(form):


    
    html="""
        <HTML>

        <FORM ACTION="cetus_load.cgi" METHOD="POST" enctype="multipart/form-data">
            <input type="hidden" name="action" value="upload_file_data">
            <BR><I>Browse Files:</I> <INPUT TYPE="FILE" NAME="file">
            <br>
            <input type="submit" value="Press"> to upload the file!
            </form>
        </HTML>
    """
    print(html)

def run_app(form):

    file_name=form["file_name"].value[3:-2]
    #cmd = ['java','-jar','cetusgui.jar',file_name]
    cmd = ('java -jar cetusgui.jar '+file_name)
    print('runing command <br>')
    print(cmd)
    print('<br>')
    output = commands.getoutput('java -version')
    print('current dic:' + output+ '<br>') 
    html="""
      
        <h3>terminal output</h3>
        <FORM ACTION="cetus_load.cgi" METHOD="POST" enctype="multipart/form-data">
            <input type="hidden" name="action" value="download_file">
            <input type="hidden" name="file_name" value=\""""+file_name+"""\">
            <br>
            <input type="submit" value="download the file"> 
            </form>
        
    """
    
    print html
    #output = subprocess.Popen( cmd, stdout=subprocess.PIPE ).communicate()[0]
    output = commands.getoutput(cmd)
    print output.replace('\n','<br>')
    print('</html>')


def download_file(form):
    file_name=form["file_name"].value
    print('a link to the file '+file_name)
    print('</br>')
    print('<li><a href="cetus_output/'+file_name+'" >'+file_name+'</a></li>')
    
# Define main function.
def main():
    #try:
    form = cgi.FieldStorage()
    if "action" in form:
        action=form["action"].value

        if action == "upload_file":
                upload_file(form)
                  
        elif action == "upload_file_data":

                upload_file_data(form)
           
        elif action == "file_choose":

                file_choose(form)
            
        elif action == "run_app":

                run_app(form)
        elif action=="download_file":
                download_file(form)
        else:
            login_form()
    else:
        login_form()
    #except:
    #    login_form()
    #    print("Unexpected error:", sys.exc_info()[0])

# Call main function.
main()

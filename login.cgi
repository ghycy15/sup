#!/usr/bin/python

# Import the CGI, string, sys modules
import cgi, string, sys, os, re, random

import cgitb; cgitb.enable()  # for troubleshooting

import glob
import shutil

# Required header that tells the browser how to render the HTML.
print("Content-Type: text/html\n\n")
print """

<html xmlns="http://www.w3.org/1999/xhtml">
<head>

<title>CS390 Picture Sharing Web Application</title>
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
"""

# Define function to generate HTML form.
def login_form():
    html="""


<body>

<div class="container">
	<div class="header">
  		<h1 align="center">CS390 Picture Sharing User Administration</h1>
  	</div>
  <div class="sidebar1">
    <ul class="nav">
      <li><a href="app.cgi" target="_blank">Home</a></li>
      <li><a href="create.cgi" target="_blank">Create Account</a></li>
    </ul>
  <!-- end .sidebar1 --></div>
  <div class="content"><h2>Type User and Password:</h2>
	<TABLE BORDER = 0>
	<FORM METHOD=post ACTION="login.cgi">
	<TR><TH>Username:</TH><TD><INPUT TYPE=text NAME="username"></TD><TR>
	<TR><TH>Password:</TH><TD><INPUT TYPE=password NAME="password"></TD></TR>
	</TABLE>

	<INPUT TYPE=hidden NAME="action" VALUE="login">
	<INPUT TYPE=submit VALUE="Enter">
	</FORM>

  <!-- end .content --></div>
  <div class="footer"><p align="right">CS390-PYTHON WEB APP</p>
    <!-- end .footer --></div>
<!-- end .container --></div>
</body>
</html>
"""
    print(html)

# Define function to test the password.
def check_password(user, passwd):

    if re.search("\.\.", user) or re.search("/", user):
        print("failed with ..")
        return "failed"

    try:
        passwd_file = open("users/"+user+"/password.txt", 'r')
    except:
        #No user"
        return "failed"

    stored_password = passwd_file.readline().strip()
    passwd_file.close()
    #print( "stored_password=\""+stored_password+"\"")
    if (stored_password==passwd): 
        return "passed"
    else:
        return "failed"


def display_admin_options(user, session):
    if (check_session(user,session) != "passed"):
        login_form()
        print("Wrong session:", sys.exc_info()[0])
        return "failed"
    html="""
		<body>
		<div class="container">
			<div class="header">
				<h1 align="center">CS390 Picture Sharing Admin Options</h1>
			</div>
		<div class="sidebar1">
			<ul class="nav">
			<li><a href="app.cgi" target="_blank">Home</a></li>
            <li> <a href="login.cgi?action=view_pictures&user={user}&session={session}">View own Pictures</a>
            <li> <a href="login.cgi?action=view_others&user={user}&session={session}">View Pictures of others</a>
            <li> <a href="login.cgi?action=new-album&user={user}&session={session}">Create new album</a>
            <li> <a href="login.cgi?action=upload-pic&user={user}&session={session}">Upload Picture</a>
            <li> <a href="login.cgi?action=delete-album&user={user}&session={session}">Delete album</a>
            <li> <a href="login.cgi?action=delete-pic&user={user}&session={session}">Delete Picture</a>
            <li> <a href="login.cgi?action=make-public&user={user}&session={session}">Make a album public</a>
            <li> <a href="login.cgi?action=change-pw&user={user}&session={session}">Change Password</a>
            <li> <a href="login.cgi?action=delete-user&user={user}&session={session}">Delete User</a>
			</ul>
		<!-- end .sidebar1 --></div>
		<div class="content">

        

    """
        #Also set a session number in a hidden field so the
        #cgi can check that the user has been authenticated
    print(html.format(user=user,session=session))
    
def print_pics(user,session):
    print("<h2>All the Pictures User has</h2>")
    dir_a="users/"+user+"/albums/*"
    albums=glob.glob(dir_a)
    for album in albums:
        print """
        <table border="0">
        """
            #Read all pictures
        dir_a=album+"/*"
        pics=glob.glob(dir_a)

            #Read all pictures
        tmp = album.rpartition('/')

        print '<h3>'
        print tmp[2]+"</a></h3>"
        html="""
            

        <FORM>
            <input type="hidden" name="action" value="view_album">
            <input type="hidden" name="session" value={session}>
            <input type="hidden" name="album" value={album}>
            <input type="hidden" name="user" value={user}>
            <input type="submit" value="View Ablum"> 
            </form>
            
        """
        print(html.format(album=album,session=session,user=user))
            # Print pictures in a table
        pics_in_row=0
        for pic in pics:
            name = pic.rpartition('/')
            if name[2] == "password.txt":
                continue
            print "<td>"
            print '<a href="%s">' % pic
            print '<img src="%s" width="100" height="100"><p>' % pic
            print '</a>'
            print "</td>"
            pics_in_row = pics_in_row + 1
            if pics_in_row == 5:
                print "</tr></table>"
                print"<table>"
                pics_in_row=0
        print "</table>"       
    
def print_more():

    print"""
            <!-- end .content --></div>
            <div class="footer"><p align="right">CS390-PYTHON WEB APP</p>
            <!-- end .footer --></div>
            <!-- end .container --></div>
            </body>
            </html>

    """

def read_session_string(user):
    session_file = open("users/"+user+"/session.txt", 'r')
    session = session_file.readline().strip()
    session_file.close()
    return session

def create_session(user):
    n=20
    char_set = string.ascii_uppercase + string.digits
    session = ''.join(random.sample(char_set,n)) 

    #store random string as session number
    session_file = open("users/"+user+"/session.txt", 'w')
    session_file.write(session)
    session_file.close()
    return session

def check_session(username,session):
   # print("Checking session")
   # if "user" in form and "session" in form:
    #    print("User here")
       # username=form["user"].value
       # session=form["session"].value
     #   print("user=",username," session=",session)
    session_stored=read_session_string(username)
     #   print(" session_stored="+session_stored)
    if session_stored==session:
        return "passed"
    
    return "failed"
    
def upload_album(form):


    
    html="""
        <HTML>

        <FORM ACTION="login.cgi" METHOD="POST" enctype="multipart/form-data">
            <input type="hidden" name="user" value="{user}">
            <input type="hidden" name="session" value="{session}">
            <input type="hidden" name="action" value="upload_pic_data">
            <input type="hidden" name="album" value={album}>
            <BR><I>Browse Picture:</I> <INPUT TYPE="FILE" NAME="file">
            <br>
            <input type="submit" value="Press"> to upload the picture!
            </form>
        </HTML>
    """
    album=form["album"].value
    user=form["user"].value
    session=form["session"].value
    print(html.format(user=user,session=session,album=album))
    print(album)

def upload_pic(form):
    
    user=form["user"].value
    session=form["session"].value
    print("<h3>User's current albums</h3>")
    #print("<FORM METHOD=post ACTION="login2.cgi" enctype="multipart/form-data">")
    
    dir="users/"+user+"/albums/*"
    albums=glob.glob(dir)
    print "<form>"
    for album in albums:
        print "<input type=\"radio\" name=\"album\" value=\""
        tmp = album.rpartition('/')
        print tmp[2]
        print "\" /> "
        print tmp[2]
        print "<br />"

		
    html = """
        <input type="hidden" name="user" value="{user}">
        <input type="hidden" name="session" value="{session}">
        <INPUT TYPE="hidden" NAME="action" VALUE="upload_album">
        <INPUT TYPE=submit VALUE="Enter">
        </FORM>
    """
    session=form["session"].value
    print(html.format(user=user,session=session))

def upload_pic_data(form):
    #Check session is correct


    #Get file info
    fileInfo = form['file']
    
    #Get user
    user=form["user"].value
    album=form["album"].value
    # Check if the file was uploaded
    if fileInfo.filename:
        # Remove directory path to extract name only
        fileName = os.path.basename(fileInfo.filename)
        open("users/"+user+"/albums/"+album+'/'+ fileName, 'wb').write(fileInfo.file.read())
        print('<H2>The picture ' + fileName + ' was uploaded successfully</H2>')
        print('<image src='+'"users/'+user+"/albums/"+album+'/' + fileName + '" width=400 height=300>')
    else:
        message = 'No file was uploaded'
   
def new_album(form):


 
    html="""

            <TABLE BORDER = 0>
            <FORM METHOD=post ACTION="login.cgi">
            <TR><TH>Album Name:</TH><TD><INPUT TYPE=text NAME="album"></TD><TR>
            </TABLE>
            <input type="hidden" name="user" value="{user}">
            <input type="hidden" name="session" value="{session}">
            <INPUT TYPE=hidden NAME="action" VALUE="new-album-response">
            <INPUT TYPE=submit VALUE="Enter">
            </FORM>

    """
    user=form["user"].value
    session=form["session"].value
    print(html.format(user=user,session=session))
    

def create_album(form):

    #print("new album created!")
    album=form["album"].value
    album=album.strip()
    session=form["session"].value
    user=form["user"].value
    html = """
        
        <TABLE BORDER = 0>
        <FORM METHOD=post ACTION="login.cgi" enctype="multipart/form-data">
        </TABLE>
        <H3>Do you want to make it public or private:</H3>
        <input type="radio" name="pp" value="private">Private</br>
        <input type="radio" name="pp" value="public">Public</br>
        <input type="hidden" name="user" value="{user}">
        <input type="hidden" name="session" value="{session}">
        <INPUT TYPE=hidden NAME="action" VALUE="album_setting">
        <input type="hidden" name="album" value="{album}">
        <INPUT TYPE=submit VALUE="Enter">
        </FORM>
    """

    dir="users/"+user+"/albums/"+album
    if not os.path.exists(dir):
        os.makedirs(dir)
        
    
    print(html.format(user=user,session=session,album=album))
    
def album_setting(form):
    pp=form["pp"].value
    if pp=="private":
        html = """
            <H1>Album setting</H1>
            <FORM>
            <TR><TH>Enter Password for the album:</TH><TD><INPUT TYPE=password NAME="pw"></TD><TR>
            <input type="hidden" name="user" value="{user}">
            <input type="hidden" name="session" value="{session}">
            <input type="hidden" name="album" value="{album}">
            <input type="hidden" name="action" value="make_private_response">
            <INPUT TYPE=submit VALUE="Enter">
            
            </FORM>
        """
        session=form["session"].value
        user=form["user"].value
        album=form["album"].value
        dir="users/"+user+"/albums/"+album
        print(html.format(user=user,session=session,album=album))
    else:
        user=form["user"].value
        album=form["album"].value
	#album=album.strip()
        dir="users/"+user+"/albums/"+album
        pw='NO PASSWORD'
        passwd_file = open(dir+"/password.txt", 'w').write(pw)
        print("The album is public")
        
        
def delete_album(form):
    print("<h2>delete album</h2>")

    user=form["user"].value
    session=form["session"].value
    print("<h3>User's current albums</h3>")
    #print("<FORM METHOD=post ACTION="login2.cgi" enctype="multipart/form-data">")
    
    dir="users/"+user+"/albums/*"
    albums=glob.glob(dir)
    print "<form>"
    for album in albums:
        print "<input type=\"checkbox\" name=\"albumname\" value=\""
        tmp = album.rpartition('/')
        print tmp[2]
        print "\" /> "
        print tmp[2]
        print "<br />"

		
    html = """
        <input type="hidden" name="user" value="{user}">
        <input type="hidden" name="session" value="{session}">
        <INPUT TYPE=hidden NAME="action" VALUE="delete-album-response">
        <INPUT TYPE=submit VALUE="Enter">
        </FORM>
    """
    session=form["session"].value
    print(html.format(user=user,session=session))

def delete_album_response(form):
    print("<h2>delete response</h2>")
    #if form.method == 'POST':
    album=form.getlist('albumname')
    #print(album[1])
    user=form["user"].value
    session=form["session"].value
    #dalbum=form["d-album"].value
    #albums=glob.glob(dir)
    #for album in albums:
    #    tmp = album.rpartition('/')
    #    print tmp[2]
    #    tmp2=tmp[2]
    #    clicked=form[tmp2].value
    #    print clicked
    for al in album:
        alb=al.strip()
        dir = "users/"+user+"/albums/"+alb
        print "</br>"+alb+" deleted"
        
        shutil.rmtree(dir)

def make_public(form):
    print("select album")

    user=form["user"].value
    session=form["session"].value
    print("<h3>User's current albums</h3>")
    #print("<FORM METHOD=post ACTION="login2.cgi" enctype="multipart/form-data">")
    
    dir="users/"+user+"/albums/*"
    albums=glob.glob(dir)
    print "<form>"
    for album in albums:
        print "<input type=\"radio\" name=\"album\" value=\""
        tmp = album.rpartition('/')
        print tmp[2]
        print "\" /> "
        print tmp[2]
        print "<br />"

		
    html = """
        <input type="hidden" name="user" value="{user}">
        <input type="hidden" name="session" value="{session}">
        <INPUT TYPE="hidden" NAME="action" VALUE="new-album-response">
        <INPUT TYPE=submit VALUE="Enter">
        </FORM>
    """
    session=form["session"].value
    print(html.format(user=user,session=session))

def change_pw(form):
    #print("chang pw")
    html = """
        <H1>Change Password</H1>
        <TABLE BORDER = 0>
        <FORM METHOD=post ACTION="login.cgi" enctype="multipart/form-data">
        <TR><TH>The password you want to change to:</TH><TD><INPUT TYPE=password NAME="new_pw"></TD><TR>
        </TABLE>
        <input type="hidden" name="user" value="{user}">
        <input type="hidden" name="session" value="{session}">
        <INPUT TYPE=hidden NAME="action" VALUE="change_pw_response">
        <INPUT TYPE=submit VALUE="Enter">
        </FORM>
    """
    user=form["user"].value
    session=form["session"].value
    print(html.format(user=user,session=session))
	
def change_pw_response(form):
    user=form["user"].value
    new_pw=form["new_pw"].value
    #print new_pw
    if new_pw == '':
        print("</br>please enter an value password")
    else:
        passwd_file = open("users/"+user+"/password.txt", 'w')
        
        passwd_file.write(new_pw)
        passwd_file.close()
        print("password changed")


def make_private_response(form):
    user=form["user"].value
    album=form["album"].value
    dir="users/"+user+"/albums/"+album
    pw=form["pw"].value
    open(dir+"/password.txt", 'w').write(pw)
    print("The album is private now")
    
def view_album(form):
    print "<h3>View Album</h3>"
    album=form["album"].value
    album=album.strip()
    dir_a=album+"/*"
    pics=glob.glob(dir_a)
    print("<table>")
    pics_in_row=0
    for pic in pics:
        name = pic.rpartition('/')
        if name[2] == "password.txt":
            continue
        print "<td>"
        print '<a href="%s">' % pic
        print '<img src="%s" width="100" height="100"><p>' % pic
        print '</a>'
        print "</td>"
        pics_in_row = pics_in_row + 1
        if pics_in_row == 5:
            print "</tr>"
            pics_in_row=0
                
    
    print "</table>"
    
def delete_user(form):
    user=form["user"].value
    dir="users/"+user
    shutil.rmtree(dir)
    print '<h3>User deleted</h3>'
    print '<li><a href="app.cgi" target="_blank">Go back to home</a></li>'

def delete_pics(form):
    print("<h2>select album</h2>")
    user=form["user"].value
    session=form["session"].value
    print("<h3>User's current albums</h3>")
    #print("<FORM METHOD=post ACTION="login2.cgi" enctype="multipart/form-data">")
    
    dir="users/"+user+"/albums/*"
    albums=glob.glob(dir)
    print "<form>"
    for album in albums:
        print "<input type=\"radio\" name=\"album\" value=\""
        tmp = album.rpartition('/')
        print tmp[2]
        print "\" /> "
        print tmp[2]
        print "<br />"

		
    html = """
        <input type="hidden" name="user" value="{user}">
        <input type="hidden" name="session" value="{session}">
        <INPUT TYPE="hidden" NAME="action" VALUE="delete_pics_from">
        <INPUT TYPE=submit VALUE="Enter">
        </FORM>
    """
    session=form["session"].value
    print(html.format(user=user,session=session))

def delete_pics_from(form):
    print("Select picture to delete")
    album=form["album"].value
    user=form["user"].value
    session=form["session"].value
    album=album.strip()
    dir='users/'+user+"/albums/"+album+'/*'
    pics=glob.glob(dir)
    print("<table>")
    pics_in_row=0
    print("<form>")
    for pic in pics:
        name = pic.rpartition('/')
        if name[2] == "password.txt":
            continue
        print "<td>"
        print '<img src="%s" width="100" height="100"><p>' % pic
        print '<input type = checkbox name = d_pics value = "%s">' %pic
        print "</td>"
        pics_in_row = pics_in_row + 1
        if pics_in_row == 5:
            print "</tr>"
            print "</table>"
            print "<table>"
            pics_in_row=0
                
    print "</table>"
    html = """
        <INPUT TYPE=hidden NAME="action" VALUE="delete_selected">
        <input type="hidden" name="user" value="{user}">
        <input type="hidden" name="session" value="{session}">
        <input type="hidden" name="album" value="{album}">
        <INPUT TYPE=submit VALUE="Enter">
        </form>
    """
    print(html.format(user=user,session=session,album=album))
    
def delete_selected(form):
    pics=form.getlist('d_pics')
    user=form["user"].value
    session=form["session"].value
    album=form["album"].value
    for pic in pics:
        dir=pic.strip()
        pi=dir.rpartition('/')
        print "</br>"
        print pi[2]
        print "deleted"
        os.remove(dir)
    
def view_others(form):
    print '<div class="content"><h1>Albums Preview</h1>'
    dir="users/*"
    users=glob.glob(dir)
    for user in users:
        print "<h2>"
        
        #print '<a href="%s">' % user

        print "User Name:"+user[6:]
        #print '</a>'
        print "</h2>"
        
        #####################################################	
        # Get album
        dir_a=user+"/albums/*"
        albums=glob.glob(dir_a)
        
        
        for album in albums:
            print """
            <table border="0">
            """
            #Read all pictures
            dir_a=album+"/*"
            pics=glob.glob(dir_a)
            passwd_file = open(album+"/password.txt", 'r')
            stored_password = passwd_file.readline().strip()
            #Read all pictures
            tmp = album.rpartition('/')
            if stored_password != "NO PASSWORD" :
               print "<h3>"+tmp[2]+"</h3></br>"
               print "private</br>"
               continue
            print '<h3>'
            print tmp[2]+"</h3>"
            html="""
            

            <FORM>
                <input type="hidden" name="action" value="view_album">
                <input type="hidden" name="album" value={album}>
                <input type="hidden" name="user" value="{user}">
                <input type="hidden" name="session" value="{session}">
                <input type="submit" value="View Ablum"> 
                </form>
            
            """
            user=form["user"].value
            session=form["session"].value
            print(html.format(album=album,user=user,session=session))
            # Print pictures in a table
            pics_in_row=0
            for pic in pics:
                name = pic.rpartition('/')
                if name[2] == "password.txt":
                    continue
                print "<td>"
                print '<a href="%s">' % pic
                print '<img src="%s" width="100" height="100"><p>' % pic
                print '</a>'
                print "</td>"
                pics_in_row = pics_in_row + 1
                if pics_in_row == 5:
                    print "</tr></table>"
                    break
            
            #if pics_in_row == 5:
            #    break
            print "</table>"

def view_album(form):
    print "<h3>View Album</h3>"
    album=form["album"].value
    album=album.strip()
    dir_a=album+"/*"
    pics=glob.glob(dir_a)
    print("<table>")
    pics_in_row=0
    for pic in pics:
        name = pic.rpartition('/')
        if name[2] == "password.txt":
            continue
        print "<td>"
        print '<a href="%s">' % pic
        print '<img src="%s" width="100" height="100"><p>' % pic
        print '</a>'
        print "</td>"
        pics_in_row = pics_in_row + 1
        if pics_in_row == 5:
            print "</tr>"
            pics_in_row=0
                
    
    print "</table>"
    
# Define main function.
def main():
    #try:
        form = cgi.FieldStorage()
        if "action" in form:
            action=form["action"].value
            #print("action=",action)
            if action == "login":
                if "username" in form and "password" in form:
                    #Test password
                    username=form["username"].value
                    password=form["password"].value
                    #print("You typed " + username + " and \"" + password +"\"<p>")
                    if check_password(username, password)=="passed":
                        session=create_session(username)
                        display_admin_options(username, session)
                        print_pics(username,session)
                        print_more()
                    else:
                        login_form()
                        print("<H3><font color=\"red\">Incorrect user/password</font></H3>")
            elif action == "new-album":
                user=form["user"].value
                session=form["session"].value
                if display_admin_options(user, session)!="failed":
                    new_album(form)
                    print_more()
            elif action == "upload-pic":
                user=form["user"].value
                session=form["session"].value
                if display_admin_options(user, session)!="failed":
                    upload_pic(form)
                    print_more()
            elif action == "upload_pic_data":
                user=form["user"].value
                session=form["session"].value
                if display_admin_options(user, session)!="failed":
                    upload_pic_data(form)
                    print_more()
            elif action == "new-album-response":
                user=form["user"].value
                session=form["session"].value
                if display_admin_options(user, session)!="failed":
                    create_album(form)
                    print_more()
            elif action == "delete-album":
                user=form["user"].value
                session=form["session"].value
                if display_admin_options(user, session)!="failed":
                    delete_album(form)
                    print_more()
            elif action == "change-pw":
                user=form["user"].value
                session=form["session"].value
                if display_admin_options(user, session)!="failed":
                    change_pw(form)
                    print_more()
            elif action == "make-public":
                user=form["user"].value
                session=form["session"].value
                if display_admin_options(user, session)!="failed":
                    make_public(form)
                    print_more()
            elif action=="make_private":
                user=form["user"].value
                session=form["session"].value
                if display_admin_options(user, session)!="failed":
                    make_private(form)
                    print_more()
            elif action=="make_private_response":
                user=form["user"].value
                session=form["session"].value
                if display_admin_options(user, session)!="failed":
                    make_private_response(form)
                    print_more()
            elif action == "delete-album-response":
                user=form["user"].value
                session=form["session"].value
                if display_admin_options(user, session)!="failed":
                    delete_album_response(form)
                    print_more()
            elif action == "change_pw_response":
                user=form["user"].value
                session=form["session"].value
                if display_admin_options(user, session)!="failed":
                    change_pw_response(form)
                    print_more()
            elif action == "upload_album":
                user=form["user"].value
                session=form["session"].value
                if display_admin_options(user, session)!="failed":
                    upload_album(form)
                    print_more()
            elif action=="album_setting":
                user=form["user"].value
                session=form["session"].value
                if display_admin_options(user, session)!="failed":
                    album_setting(form)
                    print_more()
            elif action == "view_album":
                user=form["user"].value
                session=form["session"].value
                if display_admin_options(user, session)!="failed":
                    view_album(form)
                    print_more()
            elif action == "delete-user":
                delete_user(form)
            elif action == "delete-pic":
                user=form["user"].value
                session=form["session"].value
                if display_admin_options(user, session)!="failed":
                    delete_pics(form)
                    print_more()
            elif action == "delete_pics_from":
                user=form["user"].value
                session=form["session"].value
                if display_admin_options(user, session)!="failed":
                    delete_pics_from(form)
                    print_more()
            elif action == "delete_selected":
                user=form["user"].value
                session=form["session"].value
                if display_admin_options(user, session)!="failed":
                    delete_selected(form)
                    print_more()
            elif action == "view_pictures":
                user=form["user"].value
                session=form["session"].value
                if display_admin_options(user, session)!="failed":
                    print_pics(user,session)
                    print_more()
            elif action == "view_others":
                user=form["user"].value
                session=form["session"].value
                if display_admin_options(user, session)!="failed":
                    view_others(form)
                    print_more()
            elif action == "view_album":
                user=form["user"].value
                session=form["session"].value
                if display_admin_options(user, session)!="failed":
                    view_album(form)
                    print_more()
        else:
            login_form()
    #except:
    #    login_form()
    #    print("Unexpected error:", sys.exc_info()[0])

# Call main function.
main()

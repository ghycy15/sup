#!/usr/bin/python

# Import the CGI module
import cgi
import os
import smtplib

# Required header that tells the browser how to render the HTML.
print "Content-Type: text/html\n\n"

# Define function to generate HTML form.
def generate_form():
    str = """
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
-->
</style></head>

<body>

<div class="container">
	<div class="header">
  		<h1 align="center">CS390 Picture Sharing Create Account</h1>
  	</div>
  <div class="sidebar1">
    <ul class="nav">
      <li><a href="app.cgi" target="_blank">Home</a></li>
      <li><a href="login.cgi" target="_blank">Log In</a></li>
    </ul>
  <!-- end .sidebar1 --></div>
  <div class="content"><h2>Please enter your user name(E-mail address) and password:</h2>
	<TABLE BORDER = 0>
	<FORM METHOD=post ACTION="create.cgi">
	<TR><TH>Username:</TH><TD><INPUT TYPE=text NAME="username"></TD><TR>
	<TR><TH>Password:</TH><TD><INPUT TYPE=password NAME="password"></TD></TR>
	</TABLE>

	<INPUT TYPE=hidden NAME="action" VALUE="display">
	<INPUT TYPE=submit VALUE="Enter">
	</FORM>

  <!-- end .content --></div>
  <div class="footer"><p align="right">CS390-PYTHON WEB APP</p>
    <!-- end .footer --></div>
<!-- end .container --></div>
</body>
</html>
"""
    print(str)

# Define function display data.
def display_data(username, password):
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
-->
</style></head>
    """

    str="""
<body>
<div class="container">
	<div class="header">
  		<h1 align="center">CS390 Picture Sharing Create Account</h1>
  	</div>
  <div class="sidebar1">
    <ul class="nav">
      <li><a href="app.cgi" target="_blank">Home</a></li>
      <li><a href="login.cgi" target="_blank">Log In</a></li>
    </ul>
  <!-- end .sidebar1 --></div>
  <div class="content"><h2>Congratulations! You have created an account successfully.</h2>
	<h3>Your user name is: %s</h3>
	<h3>Your user password is: %s</h3>
    </br>
    <h3>An email has sent to you.</h3>
    <h3>Please click the link in the email to active the account</h3>
  <!-- end .content --></div>
  <div class="footer"><p align="right">CS390-PYTHON WEB APP</p>
    <!-- end .footer --></div>
<!-- end .container --></div>
</body>
</html>
    """
    print(str % (username, password))

    
def create_user(form):

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
    -->
    </style></head>
    <body>
    <div class="container">
        <div class="header">
            <h1 align="center">CS390 Picture Sharing Create Account</h1>
        </div>
      <div class="sidebar1">
        <ul class="nav">
          <li><a href="app.cgi" target="_blank">Home</a></li>
          <li><a href="login.cgi" target="_blank">Log In</a></li>
        </ul>
      <!-- end .sidebar1 --></div>
      <div class="content"><h2>Congratulations! You have created an account successfully.</h2>
        
        </br>
      <!-- end .content --></div>
      <div class="footer"><p align="right">CS390-PYTHON WEB APP</p>
        <!-- end .footer --></div>
    <!-- end .container --></div>
    </body>
    </html>
        """
    dir="users/"+form["username"].value
    albums=dir+"/albums"
    if not os.path.exists(dir):
        os.makedirs(dir)
        os.makedirs(albums)
        passwd_file = open(dir+"/password.txt", 'w')
        passwd_file.write(form["password"].value)
        passwd_file.close()
    else:
        print("user already here!!!")
# Define main function.
def main():
    form = cgi.FieldStorage()
    if (form.has_key("action") and form.has_key("username") and form.has_key("password")):
        if (form["action"].value == "display"):
            dir="users/"+form["username"].value
            albums=dir+"/albums"
            if not os.path.exists(dir):
                #os.makedirs(dir)
                #os.makedirs(albums)
                #passwd_file = open(dir+"/password.txt", 'w')
                #passwd_file.write(form["password"].value)
                #passwd_file.close()
                
                #e-mail
                sender = 'mo.glo.gu@gmail.com'
                receivers = [form["username"].value]

                message = """Subject: Picture Share active link

                Welcome to CS390 Picture Share Application.
                Click the following link to active the account
                
                """
                message=message+"http://sslab01.cs.purdue.edu:8075/PictureShare/create.cgi?action=create_user&username="+form["username"].value+"&password="+form["password"].value
                
                try:
                    server = smtplib.SMTP('smtp.gmail.com:587')  
                    server.starttls()  
                    server.login('mo.glo.gu@gmail.com','9104266375')  
                    server.sendmail(sender, receivers, message)  
                    server.quit()        
                except SMTPException:
                    print "Error: unable to send email"
                                
                display_data(form["username"].value, form["password"].value)
        if (form["action"].value=="create_user"):
            create_user(form);
            
    else:
        generate_form()

# Call main function.
main()


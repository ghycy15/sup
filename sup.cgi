#!/usr/bin/python

#2011-2013 LCF
#SUP?
#3 Feb 2013
#Author @ Huyue Gu
#
# Import the CGI, string, sys modules
import cgi, string, sys, os, re, random, subprocess, commands
import cgitb; cgitb.enable()  # for troubleshooting
import glob
import shutil

from StringIO import StringIO
from os import getenv 




#font arial 
#Required header that tells the browser how to render the HTML.
print("Content-Type: text/html\n\n")

# Define function to generate HTML form.

    

def play(what,dist,cat):
    ip = getenv("REMOTE_ADDR")
    cmd = ('java '+'-jar '+'sup.jar '+' '+ip+' '+cat+' '+dist)
    output = commands.getoutput(cmd)
    #print output.find('Dataset')
    #print output
    loclist = output.split('Dataset')
    #print output.replace('\n','<br>')
    count = 0
    for value in loclist:
        count= count +1
    from random import randrange
    randomN = randrange(2,count-1)

    print """


<!doctype html>
<html>
<head>
<meta charset="UTF-8">
<title>Play</title>
<link href="play.css" rel="stylesheet" type="text/css"><!--[if lt IE 9]>
<script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script>
<![endif]-->

</head>

<body>
	
	<ul id="sdt_menu" class="sdt_menu">
				<li>
					<img id="menu" src="C-long(1).png" alt=""/>
					 <ul id="navigation">
   					 	 <li id="one"> <a>Walk</a><li>
   						 <li id="two"> <a >Bike</a></li>
   						 <li id="three"> <a >Drive</a></li>
					</ul>
				</li>
				<li>
					<img id="menu" src="C-long-menu2.png" alt=""/>
					 <ul id="navigation2">
   					 	 <li id="one"> <a>Walk</a><li>
   						 <li id="two"> <a >Bike</a></li>
   						 <li id="three"> <a >Drive</a></li>
					</ul>
				</li>
			</ul>
			
<div class="container"><a href = "index.html">
<img src="Logo2(1).png" width="200" height="200" style="float:left"/></a>
<div id="tabs">
  <ul style="float:left; margin-top:65px;">
    <li><a href="sup.cgi?action=eat&dist=5000"><img src="quote1.png" width="100" height="100" /></a></li>
    <li><a href="sup.cgi?action=play&dist=5000"><img src="quote2.png" width="100" height="100"/></a></li>
    <li><a href="sup.cgi?action=stay"><img src="quote3.png" width="100" height="100"/></a></li>
  </ul>
  
  
  <div id="tabs-2">
  
 	<div class="board2">
  	<div style="height:50px;"></div>
	<div class="sidebar1">
    <ul>
    <img src="logo4-7.png" width="120" height="120" style="margin:0px;float:left;" />
    <li><a href="#r1"><img src="logo4-1.png" width="120" height="120" style="margin:0px;float:right;" /></a></li>
    <li><a href="#r2"><img src="logo4-3.png" width="120" height="120" style="margin:0px;float:left;""/></a></li>
    <img src="logo4-8.png" width="120" height="120" style="margin:0px;float:right;" />
    <li><a href="#r3"><img src="logo4-4.png" width="120" height="120" style="margin:0px;float:right;" /></a></li>
    <img src="logo4-9.png" width="120" height="120" style="margin:0px;float:left;" />
    <img src="logo4-10.png" width="120" height="120" style="margin:0px;float:right;"/>
    <li><a href="#r4"><img src="logo4-5.png" width="120" height="120" style="margin:0px;float:left;"/></a></li>
    </ul>
    </div>
    <div class="content">
    <div id="r1">"""
    print '<br><br>'
    bizinfo = loclist[randomN].split('data')
        #print bizinfo
    print '<h2><a href ="',bizinfo[3],'"> ','<p><span style="font-family:arial,helvetica,sans-serif;"><strong><span style="font-size: 24px;"><span style="color: rgb(190, 30, 45);"><span>',bizinfo[0],'</span></span></span></strong></span></p></a>'
    catelist = bizinfo[5].split(',')
    print '<p><span style="font-family:arial,helvetica,sans-serif;"><strong><span style="font-size: 18px;"><span style="color: rgb(190, 30, 45);"><span>Category:</span></span></span></strong></span>'
    a = 0
    b = 0
    for cate in catelist:
        b=b+1
    print '<span style="font-family:arial,helvetica,sans-serif;"><span style="font-size: 20px;"><span style="color: rgb(190, 30, 45);"><span>'
    c = catelist[0].find('[')
    print catelist[0][c+1:]
    
    for a in range (1,(b-1)/2):
        c = catelist[a*2].find('[')
        print ' ,',catelist[a*2][c+1:]
    print '</span></span></span></span></p>'
    dissss = bizinfo[4].find('.')
    print '<p><span style="font-family:arial,helvetica,sans-serif;"><strong><span style="font-size: 18px;"><span style="color: rgb(190, 30, 45);"><span>Distance from you: </span></span></span></strong></span>'
    print '<span style="font-family:arial,helvetica,sans-serif;"><span style="font-size: 20px;"><span style="color: rgb(190, 30, 45);"><span>'
    print bizinfo[4][:dissss],'meters'
    print '</span></span></span></span></p>'
    print '<p><span style="font-family:arial,helvetica,sans-serif;"><strong><span style="font-size: 18px;"><span style="color: rgb(190, 30, 45);"><span>Address: </span></span></span></strong></span>'
    print '<span style="font-family:arial,helvetica,sans-serif;"><span style="font-size: 20px;"><span style="color: rgb(190, 30, 45);"><span>'
    print bizinfo[1],'<br>','</span></span></span></span></p>'
    print '<span style="font-family:arial,helvetica,margin-left:5px,sans-serif;"><span style="font-size: 20px;"><span style="color: rgb(190, 30, 45);"><span>'
    print bizinfo[2] 
    print '</span></span></span></span></p>'
    print '</div> <div id="r2">'
    print '<br><br>'
    if loclist[3] in loclist: 
        temp = loclist[randomN]
        loclist[randomN] = loclist[2]
        loclist[2]=temp
        randomN = randrange(3,count-1)
        bizinfo = loclist[randomN].split('data')
        print '<h2><a href ="',bizinfo[3],'"> ','<p><span style="font-family:arial,helvetica,sans-serif;"><strong><span style="font-size: 24px;"><span style="color: rgb(190, 30, 45);"><span>',bizinfo[0],'</span></span></span></strong></span></p></a>'
        catelist = bizinfo[5].split(',')
        print '<p><span style="font-family:arial,helvetica,sans-serif;"><strong><span style="font-size: 18px;"><span style="color: rgb(190, 30, 45);"><span>Category:</span></span></span></strong></span>'
        a = 0
        b = 0
        for cate in catelist:
            b=b+1
        print '<span style="font-family:arial,helvetica,sans-serif;"><span style="font-size: 20px;"><span style="color: rgb(190, 30, 45);"><span>'
        c = catelist[0].find('[')
        print catelist[0][c+1:]
    
        for a in range (1,(b-1)/2):
            c = catelist[a*2].find('[')
            print ' ,',catelist[a*2][c+1:]
        print '</span></span></span></span></p>'
        dissss = bizinfo[4].find('.')
        print '<p><span style="font-family:arial,helvetica,sans-serif;"><strong><span style="font-size: 18px;"><span style="color: rgb(190, 30, 45);"><span>Distance from you: </span></span></span></strong></span>'
        print '<span style="font-family:arial,helvetica,sans-serif;"><span style="font-size: 20px;"><span style="color: rgb(190, 30, 45);"><span>'
        print bizinfo[4][:dissss],'meters'
        print '</span></span></span></span></p>'
        print '<p><span style="font-family:arial,helvetica,sans-serif;"><strong><span style="font-size: 18px;"><span style="color: rgb(190, 30, 45);"><span>Address: </span></span></span></strong></span>'
        print '<span style="font-family:arial,helvetica,sans-serif;"><span style="font-size: 20px;"><span style="color: rgb(190, 30, 45);"><span>'
        print bizinfo[1],'<br>','</span></span></span></span></p>'
        print '<span style="font-family:arial,helvetica,margin-left:5px,sans-serif;"><span style="font-size: 20px;"><span style="color: rgb(190, 30, 45);"><span>'
        print bizinfo[2] 
        print '</span></span></span></span></p>'
    else:
        print 'No More results!'
    print' </div> <div id="r3">'
    print '<br><br>'
    if loclist[4] in loclist: 
        temp = loclist[randomN]
        loclist[randomN] = loclist[3]
        loclist[3]=temp
        randomN = randrange(4,count-1)
        bizinfo = loclist[randomN].split('data')
        print '<h2><a href ="',bizinfo[3],'"> ','<p><span style="font-family:arial,helvetica,sans-serif;"><strong><span style="font-size: 24px;"><span style="color: rgb(190, 30, 45);"><span>',bizinfo[0],'</span></span></span></strong></span></p></a>'
        catelist = bizinfo[5].split(',')
        print '<p><span style="font-family:arial,helvetica,sans-serif;"><strong><span style="font-size: 18px;"><span style="color: rgb(190, 30, 45);"><span>Category:</span></span></span></strong></span>'
        a = 0
        b = 0
        for cate in catelist:
            b=b+1
        print '<span style="font-family:arial,helvetica,sans-serif;"><span style="font-size: 20px;"><span style="color: rgb(190, 30, 45);"><span>'
        c = catelist[0].find('[')
        print catelist[0][c+1:]
    
        for a in range (1,(b-1)/2):
            c = catelist[a*2].find('[')
            print ' ,',catelist[a*2][c+1:]
        print '</span></span></span></span></p>'
        dissss = bizinfo[4].find('.')
        print '<p><span style="font-family:arial,helvetica,sans-serif;"><strong><span style="font-size: 18px;"><span style="color: rgb(190, 30, 45);"><span>Distance from you: </span></span></span></strong></span>'
        print '<span style="font-family:arial,helvetica,sans-serif;"><span style="font-size: 20px;"><span style="color: rgb(190, 30, 45);"><span>'
        print bizinfo[4][:dissss],'meters'
        print '</span></span></span></span></p>'
        print '<p><span style="font-family:arial,helvetica,sans-serif;"><strong><span style="font-size: 18px;"><span style="color: rgb(190, 30, 45);"><span>Address: </span></span></span></strong></span>'
        print '<span style="font-family:arial,helvetica,sans-serif;"><span style="font-size: 20px;"><span style="color: rgb(190, 30, 45);"><span>'
        print bizinfo[1],'<br>','</span></span></span></span></p>'
        print '<span style="font-family:arial,helvetica,margin-left:5px,sans-serif;"><span style="font-size: 20px;"><span style="color: rgb(190, 30, 45);"><span>'
        print bizinfo[2] 
        print '</span></span></span></span></p>'
    else:
        print 'No More results!'
    print'</div> <div id="r4">'
    print '<br><br>'
    if loclist[5] in loclist:
        temp = loclist[randomN]
        loclist[randomN] = loclist[3]
        loclist[3]=temp
        randomN = randrange(5,count-1)
        bizinfo = loclist[randomN].split('data')
        print '<h2><a href ="',bizinfo[3],'"> ','<p><span style="font-family:arial,helvetica,sans-serif;"><strong><span style="font-size: 24px;"><span style="color: rgb(190, 30, 45);"><span>',bizinfo[0],'</span></span></span></strong></span></p></a>'
        catelist = bizinfo[5].split(',')
        print '<p><span style="font-family:arial,helvetica,sans-serif;"><strong><span style="font-size: 18px;"><span style="color: rgb(190, 30, 45);"><span>Category:</span></span></span></strong></span>'
        a = 0
        b = 0
        for cate in catelist:
            b=b+1
        print '<span style="font-family:arial,helvetica,sans-serif;"><span style="font-size: 20px;"><span style="color: rgb(190, 30, 45);"><span>'
        c = catelist[0].find('[')
        print catelist[0][c+1:]
    
        for a in range (1,(b-1)/2):
            c = catelist[a*2].find('[')
            print ' ,',catelist[a*2][c+1:]
        print '</span></span></span></span></p>'
        dissss = bizinfo[4].find('.')
        print '<p><span style="font-family:arial,helvetica,sans-serif;"><strong><span style="font-size: 18px;"><span style="color: rgb(190, 30, 45);"><span>Distance from you: </span></span></span></strong></span>'
        print '<span style="font-family:arial,helvetica,sans-serif;"><span style="font-size: 20px;"><span style="color: rgb(190, 30, 45);"><span>'
        print bizinfo[4][:dissss],'meters'
        print '</span></span></span></span></p>'
        print '<p><span style="font-family:arial,helvetica,sans-serif;"><strong><span style="font-size: 18px;"><span style="color: rgb(190, 30, 45);"><span>Address: </span></span></span></strong></span>'
        print '<span style="font-family:arial,helvetica,sans-serif;"><span style="font-size: 20px;"><span style="color: rgb(190, 30, 45);"><span>'
        print bizinfo[1],'<br>','</span></span></span></span></p>'
        print '<span style="font-family:arial,helvetica,margin-left:5px,sans-serif;"><span style="font-size: 20px;"><span style="color: rgb(190, 30, 45);"><span>'
        print bizinfo[2] 
        print '</span></span></span></span></p>'
    else:
        print 'No More results!'
    print """
   </div><a href = "sup.cgi?action=play&dist=5000">
    <img src="test.png" width="500" height="156" style="margin-top:15px;"/>
    </div>
	</div>
	
  </div>
 <div class="footer">
    <p align="right"><img src = "http://s3-media3.ak.yelpcdn.com/assets/2/www/img/65526d1a519b/developers/Powered_By_Yelp_Red.png"></p>
    <!-- end .footer --></div>
<!-- end .container --></div>
 
<!-- The JavaScript -->
  <script src="http://code.jquery.com/jquery-1.8.3.js"></script>
  <script src="http://code.jquery.com/ui/1.10.0/jquery-ui.js"></script>
  <script type= "text/javascript" src="jquery.flip.js"></script>
  
  <script>
  
  /*
  
    $(function() {
    
    $("#imga").mouseenter(function(){
    	$("#imga").flip({
    	direction:'tb',
    	color: "#F7931D",
    	onAnimation: function(){
    		 window.location.href='#r2';
    	}
     })
	 
   });
   
   $("#imgb").mouseenter(function(){
    	$("#imgb").flip({
    	direction:'tb',
    	color: "#F7931D",
    	onAnimation: function(){
    		 window.location.href='#r2';
    	}
     })
   });
   
   $("#imgc").mouseenter(function(){
    	$("#imgc").flip({
    	direction:'lr',
    	content:'hi',
    	color: "#F7931D",
    	onEnd: function(){
    		window.location.href='#r3';
    	}
     })
   });
   
   $("#imgd").mouseenter(function(){
    	$("#imgd").flip({
    	direction:'bt',
    	content:'hi',
    	color: "#F7931D",
    	onEnd: function(){
    		window.location.href='#r4';
    	}
     })
   });
    
  });
  
  */
  $(function() {
    $( "#one" ).click(function(){
		
		window.location.href='sup.cgi?action=play&dist=10000';
		
	});
	 $( "#two" ).click(function(){
		
		window.location.href='sup.cgi?action=play&dist=2500';
		
	});
	
	 $( "#three" ).click(function(){
		
		window.location.href='sup.cgi?action=play&dist=1000';
		
	});
	
  });
  
 
   $(function() {
    $( "ul #navigation2 #one" ).click(function(){
		
		window.location.href='sup.cgi?action=cat&todo=play&cats=shopping&dist=5000';
		
	});
	 $( "ul #navigation2 #two" ).click(function(){
		
		window.location.href='sup.cgi?action=cat&todo=play&cats=nightlife&dist=5000';
		
	});
	
	 $( "ul #navigation2 #three" ).click(function(){
		
		window.location.href='sup.cgi?action=cat&todo=play&cats=arts,active&dist=5000';
		
	});
	
  });
 
  $(function() {
    $( ".board2" ).tabs();
  });
   $(function() {
 $('#sdt_menu > li').mouseenter(
 
  function () {
   $('#two',$(this)).stop().animate({'marginLeft':'60px'},400,"easeOutBack");
 $('#one',$(this)).stop().animate({'marginLeft':'255px'},400,"easeOutBack");
 $('#three',$(this)).stop().animate({'marginLeft':'60px'},400,"easeOutBack");
 
 
 
  }
 );
});


$(function() {
 $('#sdt_menu > li').mouseleave(
 
  function () {
  $('#two',$(this)).stop().animate({'marginLeft':'-105px'},400,"easeOutBack");
 $('#one',$(this)).stop().animate({'marginLeft':'-155px'},400,"easeOutBack");
 $('#three',$(this)).stop().animate({'marginLeft':'-120px'},400,"easeOutBack");
  
  }
 );
});
        
        
        
        
            $(function() {
				/**
				* for each menu element, on mouseenter, 
				* we enlarge the image, and show both sdt_active span and 
				* sdt_wrap span. If the element has a sub menu (sdt_box),
				* then we slide it - if the element is the last one in the menu
				* we slide it to the left, otherwise to the right
				*/
                $('#sdt_menu > li').bind('mouseenter',function(){
					var $elem = $(this);
					$elem.find('img')
						 .stop(true)
						 .animate({
							'margin-left':'0px'
						 },400,'easeOutBack')
					
				}).bind('mouseleave',function(){
					var $elem = $(this);
					$elem.find('img')
						 .stop(true)
						 .animate({
							'margin-left':'-440px'},400)
					
				});
            });
  
  </script>
</body>
</html>
"""
   # print '<h3>Other Results</h3>'
   # for n in range(2,count-1):
   #     bizinfo = loclist[n].split('data')
   #     #print bizinfo
   #     print '<a href ="',bizinfo[3],'">',bizinfo[0],'</a><br>'
   #     print 'distance from you:',bizinfo[4]
   #     print '<br>Address:',bizinfo[1],'<br>',bizinfo[2]
   #     print '<br><br>'

def eat(what,dist,cat):
    ip = getenv("REMOTE_ADDR")
    cmd = ('java '+'-jar '+'sup.jar'+' '+ip+' '+cat+' '+dist)
    output = commands.getoutput(cmd)
    #print output.find('Dataset')
    loclist = output.split('Dataset')
    #print output.replace('\n','<br>')
    count = 0
    for value in loclist:
        count= count +1
    from random import randrange
    randomN = randrange(2,count-1)

    print """
<!doctype html>
<html>
<head>
<meta charset="UTF-8">
<title>Sup</title>
<link href="eat.css" rel="stylesheet" type="text/css"><!--[if lt IE 9]>
<script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script>
<![endif]-->

</head>

<body>
	
	<ul id="sdt_menu" class="sdt_menu">
				<li>
					<img id="menu" src="C-long(1).png" alt=""/>
					 <ul id="navigation">
   					 	 <li id="one"> <a>Walk</a><li>
   						 <li id="two"> <a >Bike</a></li>
   						 <li id="three"> <a >Drive</a></li>
					</ul>
				</li>
				<li>
					<img id="menu" src="C-long-menu.png" alt=""/>
					 <ul id="navigation2">
   					 	 <li id="one"> <a>Walk</a><li>
   						 <li id="two"> <a >Bike</a></li>
   						 <li id="three"> <a >Drive</a></li>
					</ul>
				</li>
			</ul>
			

<div class="container"><a href = "index.html">
<img src="Logo2(1).png" width="200" height="200" style="float:left"/></a>
<div id="tabs">
  <ul style="float:left; margin-top:65px;">
    <li><a href="sup.cgi?action=eat&dist=5000"><img src="quote1.png" width="100" height="100" /></a></li>
    <li><a href="sup.cgi?action=play&dist=5000"><img src="quote2.png" width="100" height="100"/></a></li>
    <li><a href="sup.cgi?action=stay"><img src="quote3.png" width="100" height="100"/></a></li>
  </ul>
  <div id="tabs-1">
  
  <div class="board">
  	<div style="height:50px;"></div>
	<div class="sidebar1">
    <ul>
    <img src="logo4-7.png" width="120" height="120" style="margin:0px;float:left;" />
    <li><a href="#r1"><img id="imga" src="logo4-1.png" width="120" height="120" style="margin:0px;float:right;" /></a></li>
    <li><a href="#r2"><img id="imgb" src="logo4-3.png" width="120" height="120" style="margin:0px;float:left;""/></a></li>
    <img src="logo4-8.png" width="120" height="120" style="margin:0px;float:right;" />
    <li><a href="#r3"><img id="imgc" src="logo4-4.png" width="120" height="120" style="margin:0px;float:right;" /></a></li>
    <img src="logo4-9.png" width="120" height="120" style="margin:0px;float:left;" />
    <img src="logo4-10.png" width="120" height="120" style="margin:0px;float:right;"/>
    <li><a href="#r4"><img id="imgd" src="logo4-5.png" width="120" height="120" style="margin:0px;float:left;"/></a></li>
    </ul>
    </div>
    <div class="content">
    <div id="r1">"""
    #print '<p style="font-size:20pt;color:orange;line-height:25pt;">Our Choice!</p>'
    #print '<h2>',loclist[randomN].replace('\n','<br>'),'</h2>'
    #print '<br>'+loclist[0]
    print '<br><br>'
    bizinfo = loclist[randomN].split('data')
        #print bizinfo
    print '<h2><a href ="',bizinfo[3],'"> ','<p><span style="font-family:arial,helvetica,sans-serif;"><strong><span style="font-size: 24px;"><span style="color: rgb(190, 30, 45);"><span>',bizinfo[0],'</span></span></span></strong></span></p></a>'
    catelist = bizinfo[5].split(',')
    print '<p><span style="font-family:arial,helvetica,sans-serif;"><strong><span style="font-size: 18px;"><span style="color: rgb(190, 30, 45);"><span>Category:</span></span></span></strong></span>'
    a = 0
    b = 0
    for cate in catelist:
        b=b+1
    print '<span style="font-family:arial,helvetica,sans-serif;"><span style="font-size: 20px;"><span style="color: rgb(190, 30, 45);"><span>'
    c = catelist[0].find('[')
    print catelist[0][c+1:]
    
    for a in range (1,(b-1)/2):
        c = catelist[a*2].find('[')
        print ' ,',catelist[a*2][c+1:]
    print '</span></span></span></span></p>'
    dissss = bizinfo[4].find('.')
    print '<p><span style="font-family:arial,helvetica,sans-serif;"><strong><span style="font-size: 18px;"><span style="color: rgb(190, 30, 45);"><span>Distance from you: </span></span></span></strong></span>'
    print '<span style="font-family:arial,helvetica,sans-serif;"><span style="font-size: 20px;"><span style="color: rgb(190, 30, 45);"><span>'
    print bizinfo[4][:dissss],'meters'
    print '</span></span></span></span></p>'
    print '<p><span style="font-family:arial,helvetica,sans-serif;"><strong><span style="font-size: 18px;"><span style="color: rgb(190, 30, 45);"><span>Address: </span></span></span></strong></span>'
    print '<span style="font-family:arial,helvetica,sans-serif;"><span style="font-size: 20px;"><span style="color: rgb(190, 30, 45);"><span>'
    print bizinfo[1],'<br>','</span></span></span></span></p>'
    print '<span style="font-family:arial,helvetica,margin-left:5px,sans-serif;"><span style="font-size: 20px;"><span style="color: rgb(190, 30, 45);"><span>'
    print bizinfo[2] 
    print '</span></span></span></span></p>'
    print '</div> <div id="r2">'
    print '<br><br>'
    if loclist[3] in loclist: 
        temp = loclist[randomN]
        loclist[randomN] = loclist[2]
        loclist[2]=temp
        randomN = randrange(3,count-1)
        bizinfo = loclist[randomN].split('data')
        print '<h2><a href ="',bizinfo[3],'"> ','<p><span style="font-family:arial,helvetica,sans-serif;"><strong><span style="font-size: 24px;"><span style="color: rgb(190, 30, 45);"><span>',bizinfo[0],'</span></span></span></strong></span></p></a>'
        catelist = bizinfo[5].split(',')
        print '<p><span style="font-family:arial,helvetica,sans-serif;"><strong><span style="font-size: 18px;"><span style="color: rgb(190, 30, 45);"><span>Category:</span></span></span></strong></span>'
        a = 0
        b = 0
        for cate in catelist:
            b=b+1
        print '<span style="font-family:arial,helvetica,sans-serif;"><span style="font-size: 20px;"><span style="color: rgb(190, 30, 45);"><span>'
        c = catelist[0].find('[')
        print catelist[0][c+1:]
    
        for a in range (1,(b-1)/2):
            c = catelist[a*2].find('[')
            print ' ,',catelist[a*2][c+1:]
        print '</span></span></span></span></p>'
        dissss = bizinfo[4].find('.')
        print '<p><span style="font-family:arial,helvetica,sans-serif;"><strong><span style="font-size: 18px;"><span style="color: rgb(190, 30, 45);"><span>Distance from you: </span></span></span></strong></span>'
        print '<span style="font-family:arial,helvetica,sans-serif;"><span style="font-size: 20px;"><span style="color: rgb(190, 30, 45);"><span>'
        print bizinfo[4][:dissss],'meters'
        print '</span></span></span></span></p>'
        print '<p><span style="font-family:arial,helvetica,sans-serif;"><strong><span style="font-size: 18px;"><span style="color: rgb(190, 30, 45);"><span>Address: </span></span></span></strong></span>'
        print '<span style="font-family:arial,helvetica,sans-serif;"><span style="font-size: 20px;"><span style="color: rgb(190, 30, 45);"><span>'
        print bizinfo[1],'<br>','</span></span></span></span></p>'
        print '<span style="font-family:arial,helvetica,margin-left:5px,sans-serif;"><span style="font-size: 20px;"><span style="color: rgb(190, 30, 45);"><span>'
        print bizinfo[2] 
        print '</span></span></span></span></p>'
    else:
        print 'No More results!'
    print' </div> <div id="r3">'
    print '<br><br>'
    if loclist[4] in loclist: 
        temp = loclist[randomN]
        loclist[randomN] = loclist[3]
        loclist[3]=temp
        randomN = randrange(4,count-1)
        bizinfo = loclist[randomN].split('data')
        print '<h2><a href ="',bizinfo[3],'"> ','<p><span style="font-family:arial,helvetica,sans-serif;"><strong><span style="font-size: 24px;"><span style="color: rgb(190, 30, 45);"><span>',bizinfo[0],'</span></span></span></strong></span></p></a>'
        catelist = bizinfo[5].split(',')
        print '<p><span style="font-family:arial,helvetica,sans-serif;"><strong><span style="font-size: 18px;"><span style="color: rgb(190, 30, 45);"><span>Category:</span></span></span></strong></span>'
        a = 0
        b = 0
        for cate in catelist:
            b=b+1
        print '<span style="font-family:arial,helvetica,sans-serif;"><span style="font-size: 20px;"><span style="color: rgb(190, 30, 45);"><span>'
        c = catelist[0].find('[')
        print catelist[0][c+1:]
    
        for a in range (1,(b-1)/2):
            c = catelist[a*2].find('[')
            print ' ,',catelist[a*2][c+1:]
        print '</span></span></span></span></p>'
        dissss = bizinfo[4].find('.')
        print '<p><span style="font-family:arial,helvetica,sans-serif;"><strong><span style="font-size: 18px;"><span style="color: rgb(190, 30, 45);"><span>Distance from you: </span></span></span></strong></span>'
        print '<span style="font-family:arial,helvetica,sans-serif;"><span style="font-size: 20px;"><span style="color: rgb(190, 30, 45);"><span>'
        print bizinfo[4][:dissss],'meters'
        print '</span></span></span></span></p>'
        print '<p><span style="font-family:arial,helvetica,sans-serif;"><strong><span style="font-size: 18px;"><span style="color: rgb(190, 30, 45);"><span>Address: </span></span></span></strong></span>'
        print '<span style="font-family:arial,helvetica,sans-serif;"><span style="font-size: 20px;"><span style="color: rgb(190, 30, 45);"><span>'
        print bizinfo[1],'<br>','</span></span></span></span></p>'
        print '<span style="font-family:arial,helvetica,margin-left:5px,sans-serif;"><span style="font-size: 20px;"><span style="color: rgb(190, 30, 45);"><span>'
        print bizinfo[2] 
        print '</span></span></span></span></p>'
    else:
        print 'No More results!'
    print'</div> <div id="r4">'
    print '<br><br>'
    if loclist[5] in loclist:
        temp = loclist[randomN]
        loclist[randomN] = loclist[3]
        loclist[3]=temp
        randomN = randrange(5,count-1)
        bizinfo = loclist[randomN].split('data')
        print '<h2><a href ="',bizinfo[3],'"> ','<p><span style="font-family:arial,helvetica,sans-serif;"><strong><span style="font-size: 24px;"><span style="color: rgb(190, 30, 45);"><span>',bizinfo[0],'</span></span></span></strong></span></p></a>'
        catelist = bizinfo[5].split(',')
        print '<p><span style="font-family:arial,helvetica,sans-serif;"><strong><span style="font-size: 18px;"><span style="color: rgb(190, 30, 45);"><span>Category:</span></span></span></strong></span>'
        a = 0
        b = 0
        for cate in catelist:
            b=b+1
        print '<span style="font-family:arial,helvetica,sans-serif;"><span style="font-size: 20px;"><span style="color: rgb(190, 30, 45);"><span>'
        c = catelist[0].find('[')
        print catelist[0][c+1:]
    
        for a in range (1,(b-1)/2):
            c = catelist[a*2].find('[')
            print ' ,',catelist[a*2][c+1:]
        print '</span></span></span></span></p>'
        dissss = bizinfo[4].find('.')
        print '<p><span style="font-family:arial,helvetica,sans-serif;"><strong><span style="font-size: 18px;"><span style="color: rgb(190, 30, 45);"><span>Distance from you: </span></span></span></strong></span>'
        print '<span style="font-family:arial,helvetica,sans-serif;"><span style="font-size: 20px;"><span style="color: rgb(190, 30, 45);"><span>'
        print bizinfo[4][:dissss],'meters'
        print '</span></span></span></span></p>'
        print '<p><span style="font-family:arial,helvetica,sans-serif;"><strong><span style="font-size: 18px;"><span style="color: rgb(190, 30, 45);"><span>Address: </span></span></span></strong></span>'
        print '<span style="font-family:arial,helvetica,sans-serif;"><span style="font-size: 20px;"><span style="color: rgb(190, 30, 45);"><span>'
        print bizinfo[1],'<br>','</span></span></span></span></p>'
        print '<span style="font-family:arial,helvetica,margin-left:5px,sans-serif;"><span style="font-size: 20px;"><span style="color: rgb(190, 30, 45);"><span>'
        print bizinfo[2] 
        print '</span></span></span></span></p>'
    else:
        print 'No More results!'
    print """
 </div>
 <a href = "sup.cgi?action=eat&dist=5000">
    <img src="test.png" width="500" height="156" style="margin-top:15px;"/></a>
    </div>
	
  </div>

  </div>
   <div class="footer">
    <p align="right"><img src = "http://s3-media3.ak.yelpcdn.com/assets/2/www/img/65526d1a519b/developers/Powered_By_Yelp_Red.png"></p>
    <!-- end .footer --></div>
<!-- end .container --></div>
 
<!-- The JavaScript -->
  <script src="http://code.jquery.com/jquery-1.8.3.js"></script>
  <script src="http://code.jquery.com/ui/1.10.0/jquery-ui.js"></script>
  <script type= "text/javascript" src="jquery.flip.js"></script>
  
  <script>
  
  
  /*
    $(function() {
    
    $("#imga").mouseenter(function(){
    	$("#imga").flip({
    	direction:'tb',
    	color: "#F7931D",
    	onAnimation: function(){
    		 
    	}
     })
	 
   });
   
   $("#imgb").mouseenter(function(){
    	
   });
   
   $("#imgc").mouseenter(function(){
    	$("#imgc").flip({
    	direction:'lr',
    	content:'hi',
    	color: "#F7931D",
    	onEnd: function(){
    		
    	}
     })
   });
   
   $("#imgd").mouseenter(function(){
    	$("#imgd").flip({
    	direction:'bt',
    	content:'hi',
    	color: "#F7931D",
    	onEnd: function(){
    		
    	}
     })
   });
    
  });
  
  */
  $(function() {
    $( "#one" ).click(function(){
		
		window.location.href='sup.cgi?action=eat&dist=10000';
		
	});
	 $( "#two" ).click(function(){
		
		window.location.href='sup.cgi?action=eat&dist=2500';
		
	});
	
	 $( "#three" ).click(function(){
		
		window.location.href='sup.cgi?action=eat&dist=1000';
		
	});
	
  });

  
    $(function() {
    $( "ul #navigation2 #one" ).click(function(){
		
		window.location.href='sup.cgi?action=cat&dist=5000&todo=eat&cats=mexican';
		
	});
	 $( "ul #navigation2 #two" ).click(function(){
		
		window.location.href='sup.cgi?action=cat&dist=5000&todo=eat&cats=chinese,japanese,korean';
		
	});
	
	 $( "ul #navigation2 #three" ).click(function(){
		
		window.location.href='sup.cgi?action=cat&dist=5000&todo=eat&cats=newamerican,tradamerican,burgers,sandwiches,pizza';
		
	});
	
  });
  
 
  $(function() {
    $( ".board" ).tabs();
  });
  
   $(function() {
 $('#sdt_menu > li').mouseenter(
 
  function () {
   $('#two',$(this)).stop().animate({'marginLeft':'60px'},400,"easeOutBack");
 $('#one',$(this)).stop().animate({'marginLeft':'255px'},400,"easeOutBack");
 $('#three',$(this)).stop().animate({'marginLeft':'60px'},400,"easeOutBack");
 
 
 
  }
 );
});


$(function() {
 $('#sdt_menu > li').mouseleave(
 
  function () {
  $('#two',$(this)).stop().animate({'marginLeft':'-105px'},400,"easeOutBack");
 $('#one',$(this)).stop().animate({'marginLeft':'-155px'},400,"easeOutBack");
 $('#three',$(this)).stop().animate({'marginLeft':'-120px'},400,"easeOutBack");
  
  }
 );
});
        
        
        
        
            $(function() {
				/**
				* for each menu element, on mouseenter, 
				* we enlarge the image, and show both sdt_active span and 
				* sdt_wrap span. If the element has a sub menu (sdt_box),
				* then we slide it - if the element is the last one in the menu
				* we slide it to the left, otherwise to the right
				*/
                $('#sdt_menu > li').bind('mouseenter',function(){
					var $elem = $(this);
					$elem.find('img')
						 .stop(true)
						 .animate({
							'margin-left':'0px'
						 },400,'easeOutBack')
					
				}).bind('mouseleave',function(){
					var $elem = $(this);
					$elem.find('img')
						 .stop(true)
						 .animate({
							'margin-left':'-440px'},400)
					
				});
            });
  
  </script>
</body>
</html>
  


"""
   # print '<h3>Other Results</h3>'
   # for n in range(2,count-1):
   #     bizinfo = loclist[n].split('data')
   #     #print bizinfo
   #     print '<a href ="',bizinfo[3],'">',bizinfo[0],'</a><br>'
   #     print 'distance from you:',bizinfo[4]
   #     print '<br>Address:',bizinfo[1],'<br>',bizinfo[2]
   #     print '<br><br>'

def stay():

    fo = open("data.sup","r+")
    data = fo.read()
    fo.close()
    #print 'stay'
    to_do_list = data.split(';')
    count = len(to_do_list)
    from random import randrange
    
    print """
<!doctype html>
<html>
<head>
<meta charset="UTF-8">
<title>AtHome</title>
<link href="stay.css" rel="stylesheet" type="text/css"><!--[if lt IE 9]>
<script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script>
<![endif]-->

</head>

<body>
	
	
<div class="container">
<a href = "index.html">
<img src="Logo2(1).png" width="200" height="200" style="float:left"/></a>
<div id="tabs">
  <ul style="float:left; margin-top:65px;">
    <li><a href="sup.cgi?action=eat&dist=5000"><img src="quote1.png" width="100" height="100" /></a></li>
    <li><a href="sup.cgi?action=play&dist=5000"><img src="quote2.png" width="100" height="100"/></a></li>
    <li><a href= "sup.cgi?action=stay"><img src="quote3.png" width="100" height="100"/></a></li>
  </ul>
  
  
  <div id="tabs-2">
  
 	<div class="board3">
  	<div style="height:50px;"></div>
	<div class="sidebar1">
    <ul>
    <img src="logo4-7.png" width="120" height="120" style="margin:0px;float:left;" />
    <li><a href="#r1"><img src="logo4-1.png" width="120" height="120" style="margin:0px;float:right;" /></a></li>
    <li><a href="#r2"><img src="logo4-3.png" width="120" height="120" style="margin:0px;float:left;""/></a></li>
    <img src="logo4-8.png" width="120" height="120" style="margin:0px;float:right;" />
    <li><a href="#r3"><img src="logo4-4.png" width="120" height="120" style="margin:0px;float:right;" /></a></li>
    <img src="logo4-9.png" width="120" height="120" style="margin:0px;float:left;" />
    <img src="logo4-10.png" width="120" height="120" style="margin:0px;float:right;"/>
    <li><a href="#r4"><img src="logo4-5.png" width="120" height="120" style="margin:0px;float:left;"/></a></li>
    </ul>
    </div>
    <div class="content">
    <div id="r1">"""
    randomN = randrange(0,count-1)
    twoO = to_do_list[randomN].split(':')
    
    print '<br><br><p><span style="font-family:arial,helvetica,sans-serif;"><strong><span style="font-size: 40px;"><span style="color: rgb(190, 30, 45);"><span>',twoO[0],'</span></span></span></strong></span></br></p>'
    print '<br><br><p><span style="font-family:arial,helvetica,sans-serif;"><strong><span style="font-size: 18px;"><span style="color: rgb(190, 30, 45);"><span>Add more fun things!!!<br></span></span></span></strong></span>'
    print """
            <FORM ACTION="sup.cgi" METHOD="POST" enctype="multipart/form-data">
          
      <input type="text" name="to_do" />
      <button type="submit" value="Submit" />
      <input type="hidden" name="action" value="add_DB">
        </form>
 
                   </div>
    <div id="r2">

    """
    if to_do_list[1] in to_do_list:
        temp = to_do_list[randomN]
        to_do_list[randomN] = to_do_list[0]
        to_do_list[0]=temp
        randomN = randrange(1,count-1)
        twoO = to_do_list[randomN].split(':')
    
        print '<br><br><p><span style="font-family:arial,helvetica,sans-serif;"><strong><span style="font-size: 40px;"><span style="color: rgb(190, 30, 45);"><span>',twoO[0],'</span></span></span></strong></span></br></p>'
        print '<br><br><p><span style="font-family:arial,helvetica,sans-serif;"><strong><span style="font-size: 18px;"><span style="color: rgb(190, 30, 45);"><span>Add more fun things!!!<br></span></span></span></strong></span>'
        print """
            <FORM ACTION="sup.cgi" METHOD="POST" enctype="multipart/form-data">
          
      <input type="text" name="to_do" />
      <button type="submit" value="Submit" />
      <input type="hidden" name="action" value="add_DB">
        </form>
 
 
        </div>
    <div id="r3">
        """
    
    if to_do_list[2] in to_do_list:
        temp = to_do_list[randomN]
        to_do_list[randomN] = to_do_list[1]
        to_do_list[1]=temp
        randomN = randrange(2,count-1)
        twoO = to_do_list[randomN].split(':')
    
        print '<br><br><p><span style="font-family:arial,helvetica,sans-serif;"><strong><span style="font-size: 40px;"><span style="color: rgb(190, 30, 45);"><span>',twoO[0],'</span></span></span></strong></span></br></p>'
        print '<br><br><p><span style="font-family:arial,helvetica,sans-serif;"><strong><span style="font-size: 18px;"><span style="color: rgb(190, 30, 45);"><span>Add more fun things!!!<br></span></span></span></strong></span>'
        print """
            <FORM ACTION="sup.cgi" METHOD="POST" enctype="multipart/form-data">
          
      <input type="text" name="to_do" />
      <button type="submit" value="Submit" />
      <input type="hidden" name="action" value="add_DB">
        </form>
 
        </div>
    <div id="r4">
        """
        
 
    if to_do_list[3] in to_do_list:
        temp = to_do_list[randomN]
        to_do_list[randomN] = to_do_list[2]
        to_do_list[2]=temp
        randomN = randrange(3,count-1)
        twoO = to_do_list[randomN].split(':')
    
        print '<br><br><p><span style="font-family:arial,helvetica,sans-serif;"><strong><span style="font-size: 40px;"><span style="color: rgb(190, 30, 45);"><span>',twoO[0],'</span></span></span></strong></span></br></p>'
        print '<br><br><p><span style="font-family:arial,helvetica,sans-serif;"><strong><span style="font-size: 18px;"><span style="color: rgb(190, 30, 45);"><span>Add more fun things!!!<br></span></span></span></strong></span>'
        print """
            <FORM ACTION="sup.cgi" METHOD="POST" enctype="multipart/form-data">
          
      <input type="text" name="to_do" />
      <button type="submit" value="Submit" />
      <input type="hidden" name="action" value="add_DB">
        </form>
 
        """

    print """
    </div><a href = "sup.cgi?action=stay">
    <img src="test.png" width="500" height="156" style="margin-top:15px;"/></a>
    </div>
	</div>

	 <div class="footer">
    <p align="right"></p>
    <!-- end .footer --></div>
  </div>
 
<!-- end .container --></div>
 
<!-- The JavaScript -->
  <script src="http://code.jquery.com/jquery-1.8.3.js"></script>
  <script src="http://code.jquery.com/ui/1.10.0/jquery-ui.js"></script>
  <script type= "text/javascript" src="jquery.flip.js"></script>
  
  <script>
  
  /*
  
    $(function() {
    
    $("#imga").mouseenter(function(){
    	$("#imga").flip({
    	direction:'tb',
    	color: "#F7931D",
    	onAnimation: function(){
    		 window.location.href='#r2';
    	}
     })
	 
   });
   
   $("#imgb").mouseenter(function(){
    	$("#imgb").flip({
    	direction:'tb',
    	color: "#F7931D",
    	onAnimation: function(){
    		 window.location.href='#r2';
    	}
     })
   });
   
   $("#imgc").mouseenter(function(){
    	$("#imgc").flip({
    	direction:'lr',
    	content:'hi',
    	color: "#F7931D",
    	onEnd: function(){
    		window.location.href='#r3';
    	}
     })
   });
   
   $("#imgd").mouseenter(function(){
    	$("#imgd").flip({
    	direction:'bt',
    	content:'hi',
    	color: "#F7931D",
    	onEnd: function(){
    		window.location.href='#r4';
    	}
     })
   });
    
  });
  
  */
 
 
  $(function() {
    $( ".board3" ).tabs();
  });

  
  </script>
</body>
</html>
"""

    
def db_op(to_do):
    #print to_do
    fo = open("data.sup","r+")
    data = fo.read()
    fo.close()
    to_do_list = data.split(';')
    i=0
    exist = 0
    for value in to_do_list:
        #print value
        if to_do in value:
            exist = 1
            twoO = value.split(':')
            to_do_list[i] = twoO[0]+':'+str(int(twoO[1])+1)+';'
        i=i+1
    if exist==1:
        fo = open("data.sup","w")
        output = ''
        for value in to_do_list:
            output = output+value
        fo.write(output)
        fo.close()
    else:
        fo = open("data.sup","a")
        fo.write(to_do+":0;")
        fo.close()
    print """
<!doctype html>
<html>
<head>
<meta charset="UTF-8">
<title>AtHome</title>
<link href="stay.css" rel="stylesheet" type="text/css"><!--[if lt IE 9]>
<script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script>
<![endif]-->

</head>

<body>
	
	
<div class="container"><a href = "index.html">
<img src="Logo2(1).png" width="200" height="200" style="float:left"/></a>
<div id="tabs">
  <ul style="float:left; margin-top:65px;">
    <li><a href="sup.cgi?action=eat&dist=5000"><img src="quote1.png" width="100" height="100" /></a></li>
    <li><a href="sup.cgi?action=play&dist=5000"><img src="quote2.png" width="100" height="100"/></a></li>
    <li><a href="sup.cgi?action=stay"><img src="quote3.png" width="100" height="100"/></a></li>
  </ul>
  
  
  <div id="tabs-2">
  
 	<div class="board3">
  	<div style="height:50px;"></div>
	<div class="sidebar1">
    <ul>
    <img src="logo4-7.png" width="120" height="120" style="margin:0px;float:left;" />
    <li><a href="#r1"><img src="logo4-1.png" width="120" height="120" style="margin:0px;float:right;" /></a></li>
    <li><a href="#r2"><img src="logo4-3.png" width="120" height="120" style="margin:0px;float:left;""/></a></li>
    <img src="logo4-8.png" width="120" height="120" style="margin:0px;float:right;" />
    <li><a href="#r3"><img src="logo4-4.png" width="120" height="120" style="margin:0px;float:right;" /></a></li>
    <img src="logo4-9.png" width="120" height="120" style="margin:0px;float:left;" />
    <img src="logo4-10.png" width="120" height="120" style="margin:0px;float:right;"/>
    <li><a href="#r4"><img src="logo4-5.png" width="120" height="120" style="margin:0px;float:left;"/></a></li>
    </ul>
    </div>
    <div class="content">
    <div id="r1">"""
    print '<br><br><p><span style="font-family:arial,helvetica,sans-serif;"><strong><span style="font-size: 40px;"><span style="color: rgb(190, 30, 45);"><span>Successfully Added!</span></span></span></strong></span></br></p>'
    print"""
    </div>
    <div id="r2">
    Nothing here!
    </div>
    <div id="r3">
    Nothing here!
    </div>
    <div id="r4">
    Nothing here!
    """
    print """
    </div>
    <img src="test.png" width="500" height="156" style="margin-top:15px;"/>
    </div>
	</div>
  </div>
 
<!-- end .container --></div>
 
<!-- The JavaScript -->
  <script src="http://code.jquery.com/jquery-1.8.3.js"></script>
  <script src="http://code.jquery.com/ui/1.10.0/jquery-ui.js"></script>
  <script type= "text/javascript" src="jquery.flip.js"></script>
  
  <script>
  
  /*
  
    $(function() {
    
    $("#imga").mouseenter(function(){
    	$("#imga").flip({
    	direction:'tb',
    	color: "#F7931D",
    	onAnimation: function(){
    		 window.location.href='#r2';
    	}
     })
	 
   });
   
   $("#imgb").mouseenter(function(){
    	$("#imgb").flip({
    	direction:'tb',
    	color: "#F7931D",
    	onAnimation: function(){
    		 window.location.href='#r2';
    	}
     })
   });
   
   $("#imgc").mouseenter(function(){
    	$("#imgc").flip({
    	direction:'lr',
    	content:'hi',
    	color: "#F7931D",
    	onEnd: function(){
    		window.location.href='#r3';
    	}
     })
   });
   
   $("#imgd").mouseenter(function(){
    	$("#imgd").flip({
    	direction:'bt',
    	content:'hi',
    	color: "#F7931D",
    	onEnd: function(){
    		window.location.href='#r4';
    	}
     })
   });
    
  });
  
  */
 
 
  $(function() {
    $( ".board3" ).tabs();
  });

  
  </script>
</body>
</html>
"""
    
# Define main function.
def main():
    #try:
    form = cgi.FieldStorage()
    #db_op('play game')
    
    #print ip
    
    if "action" in form:
        action=form["action"].value

        if action == "cat":
            cat = form["cats"].value
            if form["todo"].value=='eat':
                if not form["dist"].value:
                    eat('eat','5000',cat)
                else:
                    eat('eat',form["dist"].value,cat)
            else:
                if not form["dist"].value:
                    play('eat','5000',cat)
                else:
                    play('eat',form["dist"].value,cat)
        elif action == "eat":
            
            #if not form["dist"].value:
            #    eat('eat','5000','restaurants')
            #else:
            eat('eat',form["dist"].value,'restaurants')
            #ip = getenv("REMOTE_ADDR")
            #cmd = ('java '+'-jar'+' sup.jar'+' '+ip+' '+'restaurants'+' '+'5000')
            #output = commands.getoutput(cmd)
            #print output
        elif action == "play":
            if not form["dist"].value:
                play('play','5000','active,arts,beautysvc,nightlife,shopping')
            else:
                play('play',form["dist"].value,'active,arts,beautysvc,nightlife,shopping')
        elif action == "stay":
            stay()
        elif action == "add_DB":
            db_op(form["to_do"].value)
    #print_more()
    #else:
    #    login_form()
    #except:
    #    login_form()
    #    print("Unexpected error:", sys.exc_info()[0])

# Call main function.
main()

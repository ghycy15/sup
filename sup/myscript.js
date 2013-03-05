 $(function() {
$( "#eat2, #play, #shop, #stay" ).draggable();
});



$(document).ready(function(){
	$( " #shop" ).hide();
	
	$("#logo").mouseenter(function(){
		
		$(this).animate(
			{"width":"+=40px",
			"height":"+=40px",
			
		},100);
		
		$(this).animate(
			{"width":"-=20px",
			"height":"-=20px",
			
		},100);
		
		$(this).animate(
			{"width":"+=10px",
			"height":"+=10px",
			
		},100);
		
		
		$("#eat2").animate({
        width: 150,
        height: 150,
        top: -350,
		left: -280,
    }, {
        duration: 1000,
        easing: "easeOutElastic"
    });
    
    	$("#play").delay(100).animate({
        width: 200,
        height: 200,
        top: -600,
        left: 300,
    }, {
        duration: 1000,
        easing: "easeOutElastic"
    });
		
		$("#stay").delay(200).animate({
        width: 100,
        height: 100,
        top: -370,
        left: -130,
    }, {
        duration: 1000,
        easing: "easeOutElastic"
    });
		
		
	});
	
	$("#eat2").click(function(){
		
		window.location.href="eat.html";
		
	});

	
	
	$("#logo").mouseout(function(){
		
		$(this).animate(
			{"width":"-=40px",
			"height":"-=40px",
			
		},100);
		
		$(this).animate(
			{"width":"+=20px",
			"height":"+=20px",
			
		},100);
		
		$(this).animate(
			{"width":"-=10px",
			"height":"-=10px",
			
		},100);
		
		$("#eat2").delay(1000).animate({
        width: 0,
        height: 0,
        top: -220,
    	left: -220,
        
    }, {
        duration: 1000,
        easing: "easeOutElastic"
    });
    
    $("#play").delay(1100).animate({
        width: 0,
        height: 0,
        top: -250,
        left: 150,
        
    }, {
        duration: 1000,
        easing: "easeOutElastic"
    });
    
    
     $("#stay").delay(1200).animate({
        width: 0,
        height: 0,
        top: -400,
        left: -80,
        
    }, {
        duration: 1000,
        easing: "easeOutElastic"
    });
	});
});
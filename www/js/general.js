$(document).ready(function(){
	
	
	
	$(".grow").hide();
	$(".grow").slideDown("slow");
	
	$(".fade-in").hide();
	$(".fade-in-slow").fadeIn(2000);
	$(".fade-in-med").fadeIn(1500);
	$(".fade-in-fast").fadeIn(1000);
	
	
	$(".more").hide();
	$(".showmore").click(function(){
			$(".more").slideToggle("slow");
			$(".showmore .choices").toggle();
	});
	
	
	// gallery - lightbox plugin
	$(function() {
		$('a.enlarge').lightBox();
	});
	
	$('#navigacija').localScroll();
	$.localScroll.hash()

});

/* Contact Form Validation */
function validate(form)
{
	if( form.cfName.value == "" || form.cfEmail.value == "" || form.cfComments.value == "" ) 
   { 
	  document.getElementById('message').innerHTML = 'Ве молам внесете го името, е-поштата и пораката.';
	  document.getElementById('message').style.display = 'block';
	  return false; 
   }
}
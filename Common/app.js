var main = function () {

	jQuery("document").ready(function($){
		for (i=0;i < 4;i++){
			$('#outerdiv').append('<div id="innerdiv" class="header">Hi there!</div>');
			$('#innerdiv').attr('id','X'+i);

		};

		var today = new Date().toISOString().split('T')[0];
		document.getElementsByName("start")[0].setAttribute('min', today);
		document.getElementsByName("end")[0].setAttribute('min', today);
	});

};
$(document).ready(main);
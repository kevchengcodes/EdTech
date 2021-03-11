var main = function () {

  jQuery("document").ready(function($){
    for (i=0;i < 4;i++){
      $('#outerdiv').append('<div id="innerdiv" class="header">Hi there!</div>');
      $('#innerdiv').attr('id','X'+i);

    };

  });

};
$(document).ready(main);
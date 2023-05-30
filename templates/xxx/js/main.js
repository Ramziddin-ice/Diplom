
$(document).ready(function () {
  var dax=[];
  $("#bos").click(function () { 
    $.ajax({
      url: "http://jsonplaceholder.typicode.com/todos",
      type: "GET",     
      success: function (data) {
        dax=data;
      },
      error:function(ex){
        console.log(ex);
      },
      beforeSend:function(){
        $("#bos").attr("disabled","disabled");
        $("#bos .spinner-border").toggleClass("d-none");
      },
      complete:function(){
        $("#bos").removeAttr("disabled");
        $("#bos .spinner-border").toggleClass("d-none");
      },
      async:false,


    });
    
    let haj=dax.length;
    $("#jam").text(haj+" ta");
    for( var i of dax){
      let b=i.completed,x="";
      if(b){
        x="checked";
      }
      let z="<div class='w-100 border my-2 p-2'>"+
          "<div class='form-check '><input type='checkbox' "+x+" class='form-check-input' id='"+i.id+"'>"+
          "<label class='form-check-label font-weight-bold' for='"+i.id+"'>"+i.title+"</label></div>";
        $(".offset-3").append(z);


    }

    
  });


});
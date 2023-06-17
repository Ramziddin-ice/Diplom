var counter = 0
$(document).ready(function () {
    $("#xbutton").click(
      function () {
        var datax=[];
          var trx=false;
        $.ajax({
          url: "http://shdiplom.uz/xresult/",
          //url: "http://127.0.0.1:8000/xresult/",
          type: "POST",
          data: $('#maxform').serialize(),
          success: function (data) {
              if (data.error){
                  trx=false;
                  if(data.first_text){
                  alert(data.first_text)}
                  if(data.second_text){
                  alert(data.second_text)}
                  if(data.number){
                  alert(data.number)}
              }
              else {
                  counter++
                  trx=true;
              datax=data}
            },
          error:function(ex){
            console.log(ex);
            },
          async:false
        });
      //  bosilganda iwlaw jaryoinda chiz jadvalga
          if (trx){
            var col="<tr class=\"table-primary\">"+"<th scope=\"row\">"+counter+"</th>"+"<td>"+datax.natija +"</td>"+"</tr>"
            $('#tabx').append(col)}
      })


})


$(document).ready(function () {
    $("#xbutton1").click(
      function () {
        var datax=[]

          counter++
        $.ajax({
            //url: "http://shdiplom.uz/detailsave/",
          url: "http://shdiplom.uz/detailsave/",
          type: "POST",
          data: $('#maxform').serialize(),
          success: function (data) {
              if (data.succes){
                  alert("Berilgan matin malumotlar obboriga qoshildi!")
              }
              else if (data.error){
                  alert("Bazda mavjud!")
              }
              else {
                  alert("Xato!")
              }

            },
          error:function(ex){
             alert("Xato!")
            },
          async:false
        });
      //  bosilganda iwlaw jaryoinda chiz jadvalga
      })
})
$(document).ready(function () {
    $("#xbutton2").click(
      function () {
        var datax=[]
           var trx=false;
          counter++
        $.ajax({
            url: "http://shdiplom.uz/detailchacks/",
          //url: "http://127.0.0.1:8000/detailchacks/",
          type: "POST",
          data: $('#maxform').serialize(),
          success: function (data) {
              if (data.error){
                  if(data.first_text){
                      trx=false;
                  alert(data.first_text)}
                  trx=false;
                  if(data.number){
                  alert(data.number)}
              } else {
              trx=true;
              datax=data}
            },
          error:function(ex){
             alert("Xato!")
            },
          async:false
        });
      //  bosilganda iwlaw jaryoinda chiz jadvalga
          if (trx){
           var col="<tr class=\"table-primary\">"+"<td>"+datax.natija +"</td>"+"</tr>"
            $('#tabx').append(col)}
      })
})

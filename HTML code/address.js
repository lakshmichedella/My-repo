$("#state2").hide();

function states(file){
        $.ajax({
                url: file,
                dataType: 'json',
                success: function(data) {
                   var items = [];
         
                   $.each(data, function(key, val) {
         
                     items.push('<option id="' + val["abbreviation"] + '">'+val["name"] + '</option>');
                
                   });
                   $("#state").html(items.join(''));
         
                },
               statusCode: {
                  404: function() {
                    alert('There was a problem with the server.  Try again soon!');
                  }
                }
             });
}

states("provinces.json");

$("#country").change( function() {

$country = $("#country").find(":selected").val();
//$("#count").text($country);
if($country =="other"){
        //$("#count").text("hello");
        $("#state").hide();
        $("#state2").show();
//$("#state").html("<input" + "type = " + "text "+ "name="+ "state " + "id=" + "state " + "class=" + "form-select" + "></select>")
} else if($country =="Canada") {
        $("#state").show();
        $("#state2").hide();
        states("provinces.json");
        //$("#count").text("hello");
} else if($country =="USA"){
        $("#state").show();
        $("#state2").hide();
        states("states.json");
}})
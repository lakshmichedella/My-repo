let bars = document.querySelector("#icon");

bars.addEventListener("click", myFunction);


function myFunction() {
    
    let x = document.querySelector("#menubar_holder");
    if (x.className === "m") {
      x.className += " responsive";
      
    } else {
      x.className = "m";
    }
  }

$(document).ready(function(){
$(".member-grid .like").click(
    function(){
      if ($(this).attr("class") !== "like selected"){
      $likes = $(this).siblings("p").children("span");
      $likes.text(parseFloat($likes.text())+1);
      $(this).siblings(".dislike").removeClass("selected");
      $(this).addClass("selected");
      //$likes.text($(this).attr("class")+ $(this).siblings(".dislike").attr("class"))
    }
      
    })

  $(".member-grid .dislike").click(
    function(){
      if ($(this).attr("class") !== "dislike selected"){
      $likes = $(this).siblings("p").children("span");
      $likes.text(parseFloat($likes.text()) > 0 ? parseFloat($likes.text())-1: 0);
      $(this).siblings(".like").removeClass("selected");
      $(this).addClass("selected");}})

   $("#rating").click(
        function(){
        $liek = 0;
        $disliek = 0;
        $but = $(this).siblings("#members");
        $but = $but.find(".member-grid").find(".selected");
        $($but).each(function() {
                $new = $(this).attr("class");
        if ($new === "like selected"){
                $liek ++;
        }
        if ($new === "dislike selected") {
                $disliek ++;
        }})
        $(this).siblings("p").text("Liek = "+ $liek + " Dislikes = " + $disliek);
        }
      )

})

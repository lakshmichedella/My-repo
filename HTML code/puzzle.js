$in = false;
$right = 0;
$wrong = 0;
//$snapped = false;
$("#points").text("Right: " + $right + "  Wrong: "+ $wrong);
$("#puzzle_container").on({
        mouseenter: function(){
        $(this).css("background-color", "blue");
},

        mouseleave: function(){
                $(this).css("background-color", "red");
                $hovering = false;
        },        
                
        mousedown: function(){
                $hovering = true;
                $box = 0;
                $(this).css("z-index", 4);
                $(".puzzle-piece").each(
                        function() {
                                $piecez = parseInt($(this).css("z-index"));
                                $(this).css("z-index", $piecez-1 > 0 ? $piecez-1:0)
                        }
                );
        },
        mouseup: function(){
                
                $hovering = false;
                if($in){
                        $(this).offset({left: $left - ($left%100)+126, top: $top - ($top%100)+388});
                        $(this).css("border-color", "black");
                        //$in=false;
                        //$snapped = true;
                        $box.addClass("snapped");
                        
                        //$("#win").text($box.attr("class"));
                                               
                                if($box.attr("id")==$(this).attr("id")){
                                        $right++;
                                        if($right==4){
                                                $("#win").text("You won!!!!");
                                        } 
                                }
                                else{
                                        $wrong++;
                                }
                } 
                $("#points").text("Right: " + $right + "  Wrong: "+ $wrong);
                
                
        },
        mousemove: function(e){
                
                if($hovering){
                        
                        $(this).offset({left: e.pageX-50, top: e.pageY-50});
                        $top = $(this).offset().top-388; //388
                        $left = $(this).offset().left-126; //126
                        //$("#coor").text($(window).scrollTop());
                        if(($top-0)%100<50 && ($left-0)%100<50){
                                $elems = document.elementsFromPoint($left+126 + $(window).scrollLeft(), $top+388-$(window).scrollTop());
                                
                                $elems.forEach(elmt => {
                                        
                                        if($(elmt).attr("class") == "puzzle-piece-box"){
                                                //$("#points").text($(elmt).offset().left + "    "+ $(elmt).offset().top);
                                               // $("#coor").text($(elmt).attr("class"));
                                                
                                                $(elmt).css("background-color", "grey");
                                                
                                                $box = $(elmt);
                                                $in=true;
                                                
                                        } else if ($(elmt).attr("class") == "puzzle-piece-box snapped"){
                                                //$("#coor").text($(elmt).attr("class"));
                                                $box = $(elmt);
                                        }
                                });
                               
                                
                        }
                       
                        else {
                                //$("#win").text("avois");
                                if($box != 0){
                                        $box.css("background-color", "aquamarine");
                                        //$("#win").text($box.attr("class"));
                                        if($box.attr("id")==$(this).attr("id") && $box.attr("class")=="puzzle-piece-box snapped"){
                                                $right--;
                                                //$box.removeClass("snapped");
                                                //$("#win").text($box.attr("class"));
                                        }
                                        else if ($box.attr("id")!=$(this).attr("id") && $box.attr("class")=="puzzle-piece-box snapped"){
                                                $wrong--;
                                                //$box.removeClass("snapped");
                                        }
                                        $box.removeClass("snapped");
                                        $box=0;
                                        //$snapped = false;
                                        //$("#win").text($box.attr("class"));
                                        $(this).css("border-color", "white");
                                        $("#points").text("Right: " + $right + "  Wrong: "+ $wrong);
                                }
                                $in=false;
                        }
                        
                }
        }
        }, ".puzzle-piece");
//690 should be but actually 500

$("#restart").click(function(){
        $in = false;
        $right = 0;
        $wrong = 0;
        
        $(".puzzle-piece").each(function(){
                $(this).offset(
                        {left: Math.floor(Math.random()*600)+126, top: Math.floor(Math.random()*600)+388}
                        )
                $(this).css("background-color", "red");
                $(this).css("border-color", "white");
        })
        $(".puzzle-piece-box").each(function(){
                $(this).css("background-color", "aquamarine");
                $(this).removeClass("snapped");
        })
})
$hover = false;
$on_top = false;
$station_l = $("#stationary").offset().left;
$station_t = $("#stationary").offset().top;
$("#boxes").on( {
        mouseenter: function(){
        $(this).css("background-color", "blue");
        },
        mouseleave: function(){
                $(this).css("background-color", "aqua");
        },
        mousedown: function(){
                $hover = true;
        },
        mouseup: function(){
                $hover = false;
                if($on_top){
                        alert($(this).find("p").text());
                        $(this).remove();
                        $on_top = false;
                        $("#stationary").css("background-color", "white");
                }
        },
        mousemove: function(e){
                if($hover){
                        $(this).offset({left: e.pageX-50, top: e.pageY-50});
                        $l = $(this).offset().left;
                        $t = $(this).offset().top;
                        if($l > $station_l && $l < $station_l+300 && $t>$station_t && $t<$station_t+300){
                                $("#stationary").css("background-color", "grey");
                                $on_top = true;
                        } else {
                                $("#stationary").css("background-color", "white");
                                $on_top = false;
                        }

                }
        }
}, ".move")
/*
$("#boxes").on({
        mouseenter: function(){
                
                        $(this).css("background-color", "grey");
                
        },
        mouseleave: function(){
                
                $(this).css("background-color", "white");
        
}

}, "#stationary")*/
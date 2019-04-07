$(document).ready(function(){
    $("#tombol-login").click(function(){
        $("#tombol-login").fadeOut("slow", function(){
            $("#login").fadeIn();
        });
    });

    $(".tombol-keluar").click(function(){
        $("#container, #forgotten").fadeOut(800, function(){
            $("tombol-login").fadeIn(800);
        });
    });

    $('#forgotten').click(function(){
        $("#container").fadeOut(function(){
          $("#forgotten-container").fadeIn();
        });
    });
});

$(document).ready(function(){
    $(".hiddenInfo").hide();
    $(".strong").hide();

    $(".box").mouseenter(function(){
        $(this).find(".hiddenInfo").fadeIn();
        $(this).find(".strong").fadeIn();
    })
    .mouseleave(function(){
        $(this).find(".hiddenInfo").fadeOut();
        $(this).find(".strong").fadeOut();
    })
});
$(document).ready(function(){
    $(".hiddenInfo").hide();

    var arrLen = $(".hiddenInfo").find(".INLen").html();
    var arr = $(".hiddenInfo").find(".INArr").html();


    var newArr = [];

    // $(".inner").find("#4").hide();

    console.log("arr here: ");
    console.log(arr);

    var prev;

    function toArr(string){
        for (var i = 0; i < string.length - 1; i++){
            if (Number.isInteger(parseInt(string[i]))){
                if (Number.isInteger(parseInt(string[i+1]))){
                    var newEl = string[i] + string[i+1];
                    prev = string[i+1];
                    newArr.push(parseInt(newEl));
                }
                else{
                    if (string[i] != prev){
                        newArr.push(parseInt(string[i]));
                    }

                }
            }
        }
    }

    toArr(arr);

    console.log("newArr here: ");
    console.log(newArr);


    function hideAll(){
        console.log("in function");
        for (var i = 0; i < newArr.length; i++){
            console.log(newArr[i]);
            console.log(newArr[0]);
            if (newArr[i] != newArr[0]){
                $(".inner").find(`#${newArr[i]}`).hide();
            }
        }
    }

    hideAll();

    var counter = 0;
    var done = false;

    $(document).delegate(".arrow_right", "click", function(){
        if(counter < newArr.length - 1){
            done = false;
            counter+=1;
        }
        else{
            done = true;
        }
        var hide = newArr[counter - 1];
        var show = newArr[counter];
        console.log(counter);
        console.log(newArr.length);
        console.log("Hide and show below: ");
        console.log(hide);
        console.log(show);
        if (!done){
            if (counter < newArr.length){
                console.log("in here");
                $(".inner").find(`#${hide}`).fadeOut();
                $(".inner").find(`#${show}`).fadeIn();
                
            }
        }
        
    });

    $(document).delegate(".arrow_left", "click", function(){
        if (counter > 0){
            counter-=1;
            done = false;
        }
        else if (counter == 0){
            done = true;
        }
        var hide = newArr[counter + 1];
        var show = newArr[counter];
        var widthX = $(`#${hide}`).width();
        console.log(counter);
        if (!done){
            if (counter >= 0){
                $(".inner").find(`#${hide}`).fadeOut();
                $(".inner").find(`#${show}`).fadeIn();
            }
        }
    });


});

//Arrow Right:

// .animate({left: $(`#${hide}`).width(), width: 0}, 800,function(){
//     $(".inner").find(`#${hide}`).hide();
// });
// function(){
//     $(this).animate({left: $(`#${show}`).width(), width: 452}, 800);
// }

//Arrow Left: 
// .animate({right: widthX, width: "0%"}, 800,function(){
//     $(".inner").find(`#${hide}`).hide(function(){
//     });
// });
// function(){
//     $(this).animate({left: $(`#${show}`).width(), width: 452}, 800);
// }

//Hide All function:
// css({"width": "0px"})
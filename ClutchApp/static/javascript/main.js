$(document).ready(function(){
    function isInViewport(element) {
        const rect = element.getBoundingClientRect();
        return (
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
            rect.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    }

    // function changeNav(element) {
    //     if (!isInViewport(element1)){

    //     }
    // }
    var navbar = document.getElementById("navbarhere");
    var width  = navbar.clientWidth;
    var height = navbar.clientHeight;
    // var style = 
    var element1 = document.getElementById("id1");
    console.log("***************IsInViewPort Below!********************");
    console.log(isInViewport(element1))
    console.log("Width: " + width + " " + "| Height: " + height);
});

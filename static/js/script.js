$(document).ready(function(){
    $(".dropdown").hover(
        function() {
            $('.dropdown-menu', this).not('.in .dropdown-menu').stop(true,true).fadeOut();
            $(this).toggleClass('open');
        },
        function() {
            $('.dropdown-menu', this).not('.in .dropdown-menu').stop(true,true).fadeIn();
            $(this).toggleClass('open');
        }
    );
});

$(document).ready(function(){
    $(".dropdown").focus(
        function() {
            $('.dropdown-menu', this).not('.in .dropdown-menu').stop(true,true).fadeOut();
            $(this).toggleClass('open');
        },
        function() {
            $('.dropdown-menu', this).not('.in .dropdown-menu').stop(true,true).fadeIn();
            $(this).toggleClass('open');
        }
    );
});


function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}
$(document).ready(function(){
    $("#div3").hide();
    $("#reg1").hide();
    $("#reg2").hide();
    $("#reg3").hide();
    $("#reg4").hide();
    $("#reg5").hide();
    $("#slid1").hide();
    $("#slid2").hide();
    $("#slid3").hide();
    $("#slid4").hide();
    $("#slid5").hide();
    $("#slid6").hide();
    $("#slid7").hide();
    $("#menu-items").hide();
    $("#b2").hide();
    $("#outer").hide();
    $("#er").hide();
    $("#e_text").hide();

    $("#e_text").fadeIn(1000);
    $("#outer").fadeIn(3000);
    $("#er").fadeIn(2000);
    $("#slid1").fadeIn(2000);
    $("#b2").fadeIn(2000);
    $("#slid2").fadeIn(2000);
    $("#slid3").fadeIn(2000);
    $("#slid4").fadeIn(2000);
    $("#slid5").fadeIn(2000);
    $("#slid5").attr("style","");
    $("#slid6").fadeIn(2000);
    $("#slid6").attr("style","");
    $("#slid7").fadeIn(2000);
    $("#slid7").attr("style","");
    $("#menu-items").fadeIn(2000);
    $("#div3").fadeIn(1000);
    $("#reg1").fadeIn(1000);
    $("#reg2").fadeIn(1000);
    $("#reg3").fadeIn(1000);
    $("#reg4").fadeIn(2000);
    $("#reg5").fadeIn(2000);

    if (readCookie('osat-visit') == null) {
        $('#logo-modal').modal('show');
        $("#log1").hide();
        $("#log2").hide();
        $("#s-text").hide();
        $("#log3").hide();
        $("#log4").hide();
        $("#nav1").hide();
        $("#nav2").hide();

        $("#log1").fadeIn(3000);
        $("#log2").fadeIn(3000);
        $("#s-text").fadeIn(3000);
        $("#log3").fadeIn(3000);
        $("#log4").fadeIn(3000);
        $("#nav1").fadeIn(10000);
        $("#nav2").fadeIn(10000);
        createCookie('osat-visit', '', 0.01);
    }
});


function createCookie(name,value,days) {
    var expires = "";
    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days*24*60*60*1000));
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + value + expires + "; path=/";
}

function readCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for(var i=0;i < ca.length;i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1,c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
    }
    return null;
}

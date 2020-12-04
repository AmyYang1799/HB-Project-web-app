'use strict';

$.get('/loged_in', (res) =>{
    
    var loged = $("#loged_in");
    
    loged.html(res ? "Log Out" : "Log In");
    loged.attr("href", res ? "/logout" : "/login");
 });

// $.get('/loged_in', (res) =>{
    
//     var loged = $("#logged_in");
    
//     var username = $_SESSION["user.fname"];
//     loged.html(res ? "Hi," + username : "");
//     loged.attr("href", res ? "/logout" : "/login");
// });
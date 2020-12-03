'use strict';

$.get('/loged_in', (res) =>{
    
    var loged = $("#loged_in");
    
    loged.html(res ? "Log Out" : "Log In");
    loged.attr("href", res ? "/logout" : "/login");
 });
'use strict';

$.get('/loged_in', (res) =>{
    $("#loged_in").html(res ? 'Yes' : 'No');
 });
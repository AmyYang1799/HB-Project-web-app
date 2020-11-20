"use strict";

$('#fav-form').on('submit', (evt) => {
    evt.preventDefault();
  
    // Get recipe info from a form
    const formData = {
      recipe_id: $('#submit').val(),
      
    };
  
    // Send formData to the server (becomes a query string)
    $.get('/favorite_recipe', formData, (res) => {
      // Display response from the server
      alert(`Hello`);
      
    });
  });
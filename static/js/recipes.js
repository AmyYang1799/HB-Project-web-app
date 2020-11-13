"use strict";

$('#recipes-form').on('submit', (evt) => {
    evt.preventDefault();
  
    // Get recipe info from a form
    const formData = {
      recipe_name: $('#title').val(),
      prep_time: $('#prep-time').val(),
      cook_time: $('#cook-time').val(),
      num_servings: $('#num-servings').val(),
      ingredients: $('#ingredients').val(),
      directions: $('#directions').val(),
    };
  
    // Send formData to the server (becomes a query string)
    $.get('/add_recipe', formData, (res) => {
      // Display response from the server
      alert(`Hello`);
      
    });
  });
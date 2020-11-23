"use strict";

$('#fav-form').on('submit', (evt) => {
    // evt.preventDefault();
  
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


  // document.querySelector('#login-button').addEventListener('click', (evt) => {
  //   const loginBtn = evt.target;
  //   console.log(evt.target);
  
  //   if (loginBtn.innerHTML === 'Log In') {
  //     loginBtn.innerHTML = 'Log Out';
  //   } else {
  //     loginBtn.innerHTML = 'Log In';
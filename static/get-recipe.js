// event handlers: 
// create a button to generate random recipes- in 3.0 version generate 
// recipes based on past saved recipes
'use strict';

// only returns/displays last response (directions)
function showRandRecipe(evt) {
    console.log("executing showRandRecipe");

    $.get('/generate_rand_recipe.json', response => {
        console.log("executing $.get('/generate_rand_recipe.json' ")

        $('#recipe-button-title').html(response.title);
        console.log(`recipe title = ${response.title}`)

        for (const ingredient of response.ingredients){
            $('#recipe-button-ingredients').append(`<li>${ingredient}</li>`);
        }
        
        for (const direction of response.directions){
                $('#recipe-button-directions').append(`<li>${direction}</li>`);
            }

    });
}

$('#rand-recipe-button').on('click', showRandRecipe);
  

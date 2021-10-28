// event handlers: 
// button to generate recipes based on past saved recipes- in 3.0 version generate 

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



$('button').on('click', evt => {
    evt.preventDefault()  

    const htmlData = {
        "recipe-title": evt.target.value
    }
    console.log(htmlData)
                                

        console.log($(`#${evt.target.id}`))
        console.log(evt.target.id)
        $(`#dropdown-content-id-${evt.target.id}`).slideToggle() 

});












// parse through for notes~


// $('button').on('click', evt => {
//     evt.preventDefault()  //target is an attribute
//     //need preventDefault it prevents default action of going straight to server
//     //"let me do some JS before going to server"

//     const htmlData = {
//         "recipe-title": evt.target.value
//     }
//     console.log(htmlData)
                                
//     // $.get('/show_fav_recipes_deets',  htmlData, response => {
//         // $('#dropdown-content-id').html(response.obj_ingredients);
//         console.log($(`#${evt.target.id}`))
//         console.log(evt.target.id)
//         $(`#dropdown-content-id-${evt.target.id}`).slideToggle() 

//         // need hashtag bc talking to an id
//         //classList get back list of class for element
// });




// function editAccount(evt) {
//     console.log("executing editAccount")

//     const formData = {'recipe-btn': $('#recipe-btn')}

//     $.post('/edit_account', response =>  {
//         $('#user-email-div').html(response)

//     });


// function showRecipeDetails(evt) {
//     evt.preventDefault()
//     console.log("excuting showRecipeDetails");
    
//     $.get('/show_fav_recipes_deets', response => {
//         console.log(`the response: ${response}`);
//         console.log(`response type: ${typeof response}`)
//         console.log(`response.obj_ingredients: ${response.obj_ingredients}`);
//         $('#dropdown-content-id').html(response.obj_ingredients);
//         console.log($('.dropdown-content'))
//         $('.dropdown-content').classList.remove("hide-recipe")
//         console.log("AAAAAAAAJJJJJJAAAAAAAAAAXXXXXXXX");
//     });
// }

// $('#recipe-btn-id').on('click', showRecipeDetails);

// literal button element (triggers evt);; evt is the literal action
// $('button').on('click', evt => {
//     evt.preventDefault()  //target is an attribute
//     //need preventDefault it prevents default action of going straight to server
//     //"let me do some JS before going to server"

//     const htmlData = {
//         "recipe-title": evt.target.value
//     }
//     console.log(htmlData)
                                
//     // $.get('/show_fav_recipes_deets',  htmlData, response => {
//         // $('#dropdown-content-id').html(response.obj_ingredients);
//         console.log($(`#${evt.target.id}`))
//         console.log(evt.target.id)
//         $(`#dropdown-content-id-${evt.target.id}`).slideToggle() 

//         // need hashtag bc talking to an id
//         //classList get back list of class for element
// });


// $('button').on('click', evt => {
//     evt.preventDefault()  //target is an attribute
//     //need preventDefault it prevents default action of going straight to server
//     //"let me do some JS before going to server"

//     const htmlData = {
//         "recipe-title": evt.target.value
//     }
//     console.log(htmlData)
                                
//     $.get('/show_fav_recipes_deets',  htmlData, response => {
//         // $('#dropdown-content-id').html(response.obj_ingredients);
//         console.log($(`#${evt.target.id}`))
//         console.log(evt.target.id)
//         $(`#dropdown-content-id-${evt.target.id}`).slideToggle() 

//         // need hashtag bc talking to an id
//         //classList get back list of class for element

//     });
// })





//only works for one id

//iterate through primary recipe keys in jinja in template- create unique recipe id

// const dropdown = document.querySelector(".dropdown-content-id");


// dropdown.addEventListener("click", function() {
//     console.log("hiding recipe details function")
//     dropdown.style.visibility = none;

// });

// function hideRecipeDetails(evt) {
//     console.log("executing hideRecipeDetails")

    
//     // $.get('/test_route', response => {
    
// }

// $('#recipe-button-id').on('click', hideRecipeDetails);






// //WORKED ON WITH SHAUNA 10/26
// function showRecipeDetails(evt) {
//     console.log("excuting %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% showRecipeDetails");
//     // evt.preventDefault()
//     // preventing the default state of the function which is to ?

//     const formData = {'recipe-btn': $('#recipe-btn').val()}
//     //formData executed what preventDefault() was doing
// //SELECTING ID RECIPE BUTTON from html, val() gets value from html element (button)
//     console.log(`formData: ${formData}`);
// //passing formData to server route, access values in server route. like submitting a html form w/o actual form. can use with GET as well, if server route making call to requires some form of data to work with
// //formData is taking place of form that is submitted to server route. equivalent form input, talks to request.form in server. Value in form data talks to server. Always needs to be in dictionary format.

//     $.post('/show_fav_recipes_deets', formData, response => {
//         console.log(`the response: ${response}`);
//         $('#dropdown-content-id').html(response);
//         console.log("AAAAAAAAJJJJJJAAAAAAAAAAXXXXXXXX");

//     });
// }

// $('#recipe-btn-id').on('click', showRecipeDetails);

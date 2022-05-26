// event handlers: 
// button to generate recipes based on past saved recipes- in 3.0 version generate 

'use strict';


function showRandRecipe(evt) {
    evt.preventDefault();
    console.log("executing showRandRecipe");

    $.get('/generate_rand_recipe.json', response => {
        console.log("executing $.get('/generate_rand_recipe.json' ")

        
        $('#wildcard-button-title').html(response.title);
        console.log(`recipe title = ${response.title}`);

    //    how to append and change html?????
        // const html = [];
        // for (const ingredient of response.ingredients){
        //     $('#wildcard-button-ingredients').append(`<li>${ingredient}</li>`);
        //     // $('#wildcard-button-ingredients').html(`<li>${ingredient}</li>`); lists last ingredient
        //     console.log(`recipe ingredients = ${response.ingredients}`)
        // }
        const recipe_ingredient_text = [];
        for (const ingredient of response.ingredients){

            recipe_ingredient_text.push(`<li>${ingredient}</li>`);
            $('#wildcard-button-ingredients').html(recipe_ingredient_text);
            // $('#wildcard-button-ingredients').html(`<li>${ingredient}</li>`); lists last ingredient
            console.log(`recipe ingredients = ${response.ingredients}`)
        }

        const recipe_direction_text = [];
        for (const direction of response.directions){
            recipe_direction_text.push(`<li>${direction}</li>`);
            $('#wildcard-button-directions').html(recipe_direction_text);
            console.log(`recipe directions = ${response.directions}`)
            }
        
        $('#add-to-fav-btn').html(`<form action="/add_wildcard_to_fav" method="POST">
        <button class="btn grnbutton recipe-jump-button" id="add-to-fav-btn" type="submit">Add To Recipe Book</button>
      </form> `);
        
        
    });
}

$('#wildcard-recipe-button').on('click', showRandRecipe);



function alertNoRecipes(evt) {
    evt.preventDefault();
    console.log("executing alertNoRecipes");
    $.post('/recipe_answers_msg', res => {
        alert(res.msg);

    });
}


$('.dropbtn').on('click', evt => {
    evt.preventDefault()  
    
    const htmlData = {
        "recipe-title": evt.target.value
    }
    console.log(htmlData);
                                

        console.log($(`#${evt.target.id}`));
        console.log(evt.target.id);
        $(`#dropdown-content-id-${evt.target.id}`).slideToggle(); 

});



$('#edit-fname-btn').on('click', evt => {
    evt.preventDefault()
    console.log('ran #edit-fname-button');
    $('#edit-fname-div').slideToggle();

});



$('#edit-lname-btn').on('click', evt => {
    evt.preventDefault();
    console.log('ran #edit-lname-button');
    $('#edit-lname-div').slideToggle();
});



$('#edit-email-btn').on('click', evt => {
    evt.preventDefault();
    console.log('ran #edit-email-button');
    $('#edit-email-div').slideToggle();
});



$('#edit-password-btn').on('click', evt => {
    evt.preventDefault();
    console.log('ran #edit-password-button');
    $('#edit-password-div').slideToggle();
});


$('#submit-edit-fname-btn').on('click', evt => {
    evt.preventDefault();
    console.log("edit-fname-button ENGAGE!!!!!!");

    const fnameInput = {
            fname_input: $("#fname-text-input").val()
    }

    $.post('/edit_account', fnameInput, res => {
        $('#fname-txt').html(fnameInput['fname_input']);
        alert(res.msg);

    });
});


$('#submit-edit-lname-btn').on('click', evt => {
    evt.preventDefault();
    console.log("edit-lname-button ENGAGE!!!!!!");

    const lnameInput = {
            lname_input: $("#lname-text-input").val()
    }
    console.log(lnameInput);
    $.post('/edit_account', lnameInput, res => {
        $('#lname-txt').html(lnameInput['lname_input']);
        alert(res.msg);

    });
});


$('#submit-edit-email-btn').on('click', evt => {
    evt.preventDefault();
    console.log("edit-email-button ENGAGE!!!!!!");

    const emailInput = {
            email_input: $("#email-text-input").val()
    }

    $.post('/edit_account', emailInput, res => {
        $('#email-txt').html(emailInput['email_input']);
        alert(res.msg);

    });
});


$('#submit-edit-password-btn').on('click', evt => {
    evt.preventDefault();
    console.log("edit-lname-button ENGAGE!!!!!!");

    const passwordInput = {
            password_input: $("#password-text-input").val()
    }

    console.log(passwordInput);
    $.post('/edit_account', passwordInput, res => {
        alert(res.msg);

    });
});



// element.addEventListener("click", myFunction);

// submitbtn = document.getElementById("submitbtn");

// function myFunction() {
//     if (submitbtn
//   alert ("Hello World!");
// }
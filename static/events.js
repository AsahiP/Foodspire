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



$('.dropbtn').on('click', evt => {
    evt.preventDefault()  
    
    const htmlData = {
        "recipe-title": evt.target.value
    }
    console.log(htmlData)
                                

        console.log($(`#${evt.target.id}`))
        console.log(evt.target.id)
        $(`#dropdown-content-id-${evt.target.id}`).slideToggle(); 

});


$('#edit-fname-btn').on('click', evt => {
    evt.preventDefault()
    console.log('ran #edit-fname-button')
    $('#edit-fname-div').slideToggle();

});



$('#edit-lname-btn').on('click', evt => {
    evt.preventDefault()
    console.log('ran #edit-lname-button')
    $('#edit-lname-div').slideToggle();
});



$('#edit-email-btn').on('click', evt => {
    evt.preventDefault()
    console.log('ran #edit-email-button')
    $('#edit-email-div').slideToggle();
});



$('#edit-password-btn').on('click', evt => {
    evt.preventDefault()
    console.log('ran #edit-password-button')
    $('#edit-password-div').slideToggle();
});

// const fnameText = document.querySelector('#fname-txt');
// const fnameTextInput = document.querySelector('#fname-text-input');
// const fnameButton = document.querySelector('#submit-edit-fname-btn')

// const changeFnameInput = {


// }

$('#submit-edit-fname-btn').on('click', evt => {
    evt.preventDefault();
    console.log("edit-fname-button ENGAGE!!!!!!")

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
    console.log("edit-lname-button ENGAGE!!!!!!")

    const lnameInput = {
            lname_input: $("#lname-text-input").val()
    }
    console.log(lnameInput)
    $.post('/edit_account', lnameInput, res => {
        $('#lname-txt').html(lnameInput['lname_input']);
        alert(res.msg);

    });
});

$('#submit-edit-email-btn').on('click', evt => {
    evt.preventDefault();
    console.log("edit-email-button ENGAGE!!!!!!")

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
    console.log("edit-lname-button ENGAGE!!!!!!")

    const passwordInput = {
            password_input: $("#password-text-input").val()
    }
    console.log(passwordInput)
    $.post('/edit_account', passwordInput, res => {
        alert(res.msg);

    });
});

$(document).ready(function() {
    let form = document.querySelector('#form-story');
    let alert = document.querySelector('#alert');
    let valid = [];
    let elements = null;

    if(form){

        elements = Array.from(form.elements);
        
        elements.forEach(input => {
            if(input.type === 'text'){
                input.addEventListener('keyup', function(e){
                    input.value = input.value.toLowerCase();
                })
            }
        });

        form.addEventListener('submit', function(e){
            e.preventDefault();
            elements.forEach(input => {
                if(input.type === 'text'){
                    valid.push(validateInput(input));
                }
            });
            if(valid.every(item => item === true)){
                alert.style.display = 'none';
                alert.hidden = 'true';
                valid = [];
                form.submit();
            }
            else{
                alert.style.display = 'block';
                alert.hidden = 'false';
                valid = [];
            }
        });
    }

});

const validateInput = (input) => {
    if(input.value && input.value.length >= 3)
        return true;
    return false;  
}
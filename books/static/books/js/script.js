// Bootstrap Form Validation js: grabs all forms, then when submit is clicked, if form is not valid, stops the submission until the validation is corrected 
// version from: https://www.youtube.com/watch?v=h4ZnxL0s_lY
(function(){
    'use strict';
    window.addEventListener('load', function(){
        var forms = document.getElementsByClassName('needs-validation');
        var validation = Array.prototype.filter.call(forms, function(form){
            form.addEventListener('keyup', function(event){
                if (form.checkValidity() === false){
                    event.preventDefault();
                    event.stopPropagation();
                }
                form.classList.add('was-validated');
            }, false);
            form.addEventListener('submit', function(event){
                if (form.checkValidity() === false){
                    event.preventDefault();
                    event.stopPropagation();
                }
                form.classList.add('was-validated');
            }, false);
        });
    }, false);
})();

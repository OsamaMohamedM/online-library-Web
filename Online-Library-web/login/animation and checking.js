const signinbutton = document.querySelector('.signIn-btn');
    const signup = document.querySelector('.signup-btn');
    const box1 = document.querySelector('.box1');
    const box2 = document.querySelector('.box2');

    signup.addEventListener('click', () => {
        box1.classList.toggle('active');
        box2.style.display = 'block';
        box1.style.display='none'
    });

    signinbutton.addEventListener('click', () => {
        box2.classList.toggle('active');
        box1.style.display='block';
        box2.style.display='none';


        
    });
    document.querySelectorAll('input[type="tel"]').forEach(input => {
        input.addEventListener('input', function() {
            this.value = this.value.replace(/[^0-9]/g, '');
        });
    });

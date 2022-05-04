const ignoreClickOnMeElement = document.querySelector('.profile'),
profileMenu = document.querySelector('.profile-menu'),
container = document.querySelector('.container'),
passwordShowHide = document.querySelectorAll('.showPass'),
passwordAreas = document.querySelectorAll('.password'),
changeFormBtns = document.querySelectorAll('a.signup-label'),
registerForm = document.querySelector('.form.register'),
loginForm = document.querySelector('.form.login'),
signInBtn = document.querySelector('.sign-in-btn'),
registerBtn = document.querySelector('.register-btn'),
authForm = document.querySelector('.auth-form');


const profileMenuToggle = () => {
	profileMenu.classList.toggle('active');
};

const popUpBlur = (element) => {
    element.style.display = 'block'
    authForm.classList.toggle('active')
};

const closeForms = () => {
    authForm.classList.remove('active')
    loginForm.style.display = 'none'
    registerForm.style.display = 'none'
}

document.body.addEventListener('click', (event) => {
	var isClickInsideElement = ignoreClickOnMeElement.contains(event.target);
	if (profileMenu.classList.contains('active') && !isClickInsideElement) profileMenuToggle()
});

signInBtn.addEventListener('click', () => {
    profileMenuToggle();
    popUpBlur(loginForm);
});

changeFormBtns.forEach(changeFormBtn => {
    changeFormBtn.addEventListener('click', () => {
        if (registerForm.style.display == 'none' || registerForm.style.display == '') {
            registerForm.style.display = 'block'
            loginForm.style.display = 'none'
        } else {
            registerForm.style.display = 'none'
            loginForm.style.display = 'block'
        }
    })
})


passwordShowHide.forEach(eyeIcon => {
    eyeIcon.addEventListener('click', (element) => {
        passwordAreas.forEach(passwordArea => {
            if (passwordArea.type == 'text') {
                passwordArea.type = 'password'
                this.classList.replace('uil-eye', 'uil-eye-slash')
            }
            else {
                passwordArea.type = 'text'
                this.classList.replace('uil-eye-slash', 'uil-eye')
            }

        });
    });
});

document.body.addEventListener('keydown', (e) => {
    if (authForm.classList.contains('active') && e.key == 'Escape') {
        closeForms()
    }
});

authForm.addEventListener('click', (event) => {
	var isClickInsideElement = loginForm.contains(event.target) || registerForm.contains(event.target);
	if (!isClickInsideElement) closeForms()
});
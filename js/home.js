const username = document.getElementById('username');
const password = document.getElementById('password');
const show_password = document.getElementById('show-password');

show_password.addEventListener('click', ()=> {
    if (password.type === "password") {
      password.type = "text";
    } else {
        password.type = "password";
    }
})


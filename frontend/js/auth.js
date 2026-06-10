const loginForm = document.getElementById("loginForm");
const registerForm = document.getElementById("registerForm");

if(loginForm){

    loginForm.addEventListener("submit", async(e)=>{

        e.preventDefault();

        const email = document.getElementById("email").value;
        const password = document.getElementById("password").value;

        const response = await fetch(
            "http://127.0.0.1:5000/login",
            {
                method:"POST",
                headers:{
                    "Content-Type":"application/json"
                },
                body:JSON.stringify({
                    email,
                    password
                })
            }
        );

        const data = await response.json();

        alert(data.message);
    });

}

if(registerForm){

    registerForm.addEventListener("submit", async(e)=>{

        e.preventDefault();

        const name = document.getElementById("name").value;
        const email = document.getElementById("email").value;
        const password = document.getElementById("password").value;

        const response = await fetch(
            "http://127.0.0.1:5000/register",
            {
                method:"POST",
                headers:{
                    "Content-Type":"application/json"
                },
                body:JSON.stringify({
                    name,
                    email,
                    password
                })
            }
        );

        const data = await response.json();

        alert(data.message);
    });

}
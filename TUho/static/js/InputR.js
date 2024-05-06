var username = document.getElementById("username");
var password1 = document.getElementById("password1");
var password2 = document.getElementById("password2");
var email = document.getElementById("email");
var boton =  document.getElementById("boton");

const errorContainer = document.querySelector("#error-container")
        const createMessage = (message) => {
            return `
            <div style=" position: absolute; right: 20px; top:10px; display: flex; align-items: center; padding-right: 0rem;margin-left:20px"
            class="alert alert-danger alert-dismissible fade show" role="alert">
            ${message}
                <button style="font-size: 10px; border-bottom: none; position: relative; box-shadow: none;" type="button"
                    class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                </button>
            </div>
            `
        }
        const c = (e)=>{
        let validador = /^\w+([.-_+]?\w+)*@\w+([.-]?\w+)*(\.\w{2,10})+$/
        if (!validador.test(email.value)) {
          errorContainer.innerHTML = createMessage("No es un correo valido")
          e.preventDefault()   
        }
        }
        
        boton.addEventListener("click", c, false)
           





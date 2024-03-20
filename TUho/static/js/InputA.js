var email = document.getElementById("email");
var pass = document.getElementById("pass");
var aceptar =  document.getElementById("aceptar");



const c = (e)=>{
  let validador = /^\w+([.-_+]?\w+)*@\w+([.-]?\w+)*(\.\w{2,10})+$/

  if(email.value == ""){
    email.className = "form-control is-invalid";
    e.preventDefault()
  }
  else{
    email.className = "form-control is-valid";
  }
  if(!validador.test(email.value)){
    email.className = "form-control is-invalid";
    e.preventDefault()
  }
  else{
    email.className = "form-control is-valid";
  }
  if(pass.value == ""){
    pass.className = "form-control is-invalid";
    e.preventDefault()
  }
  else{
    pass.className = "form-control is-valid";
  }
  if(email.value != "" && pass.value != ""){
  }

}


aceptar.addEventListener("click", c, false)
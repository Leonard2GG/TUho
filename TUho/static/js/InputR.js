var username = document.getElementById("username");
var password1 = document.getElementById("password1");
var password2 = document.getElementById("password2");
var email = document.getElementById("email");
var boton =  document.getElementById("boton");





const c = (e)=>{
  let validador = /^\w+([.-_+]?\w+)*@\w+([.-]?\w+)*(\.\w{2,10})+$/

  if(nombre.value == ""){
    nombre.className = "form-control is-invalid";
    e.preventDefault()
  }
  else{
    nombre.className = "form-control is-valid";
  }
  if(apellido.value == ""){
    apellido.className = "form-control is-invalid";
    e.preventDefault()
  }
  else{
    apellido.className = "form-control is-valid";
  }
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
  if(text.value == ""){
    text.className = "form-control is-invalid";
    e.preventDefault()
  }
  else{
    text.className = "form-control is-valid";
  }
  if(ci.value.length != 11 || ci.value == "" || isNaN(ci.value)){
    ci.className = "form-control is-invalid";
    e.preventDefault()
  }
  else{
    ci.className = "form-control is-valid";
  }
  if(tel.value.length != 8 || tel.value == "" || isNaN(tel.value)){
    tel.className = "form-control is-invalid";
    e.preventDefault()
  }
  else{
    tel.className = "form-control is-valid";
  }
  if(select.value == "0"){
    select.className = "form-control is-invalid";
    e.preventDefault()
  }
  else{
    select.className = "form-control is-valid";
  }
  if(nombre.value != "" && apellido.value != "" && email.value != "" && text.value != ""
    && ci.value != "" && tel.value != "" && select.value == "" || select.value == "0"){
  }

}


boton.addEventListener("click", c, false)
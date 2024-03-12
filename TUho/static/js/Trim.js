var ci = document.getElementById("inputCi");
var nombre = document.getElementById("inputName");
var tel = document.getElementById("inputNt");
var email = document.getElementById("inputEmail");


  const validate_space_trim = () => {
    ci.value = ci.value.trim();
    nombre.value = nombre.value.trim();
    tel.value = tel.value.trim();
    email.value = email.value.trim();
  }

ci.addEventListener("input",validate_space_trim);
nombre.addEventListener("input",validate_space_trim);
tel.addEventListener("input",validate_space_trim);
email.addEventListener("input",validate_space_trim);
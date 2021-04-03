/* Quando o usuário clica no botão,
alternar entre ocultar e mostrar o conteúdo suspenso  */
function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
}

function notification() {
  document
    .getElementById("myDropdown-notification")
    .classList.toggle("show-notification");

  var count_notification = document.getElementById("count-notification");

  if (count_notification) {
    count_notification.style.display = "none";
  }
}

// Feche a lista suspensa se o usuário clicar fora dela
window.onclick = function (e) {
  if (!e.target.matches(".dropbtn-img") && !e.target.matches(".dropbtn-seta")) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    for (var d = 0; d < dropdowns.length; d++) {
      var openDropdown = dropdowns[d];
      if (openDropdown.classList.contains("show")) {
        openDropdown.classList.remove("show");
      }
    }
  }

  if (!e.target.matches(".notification")) {
    var dropdowns = document.getElementsByClassName("dropdown-notification");
    for (var d = 0; d < dropdowns.length; d++) {
      var openDropdown = dropdowns[d];
      if (openDropdown.classList.contains("show-notification")) {
        openDropdown.classList.remove("show-notification");
      }
    }
  }
};

// Validador de senha no cadastro

var myInput = document.getElementById("id_new_password1");
var rsenha = document.getElementById('id_new_password2')

var letter = document.getElementById("letter");
var capital = document.getElementById("capital");
var number = document.getElementById("number");
var length = document.getElementById("length");
var repeat_password = document.getElementById("repeat-password");

if (myInput) {

  // Quando o usuário clica no campo de senha, mostra a caixa de mensagem
  // myInput.onfocus = function() {
  //   document.getElementById("Valid-password").style.display = "block";
  // }

  // Quando o usuário clicar fora do campo de senha, oculte a caixa de mensagem
  // myInput.onblur = function() {
  //   document.getElementById("Valid-password").style.display = "none";
  // }

  // Função execulta dentro do CADASTRO.
  // Quando o usuário começa a digitar algo dentro dos campos de senha e repetir senhas

  rsenha.onkeyup = function() {
    if(myInput.value == rsenha.value) {
      repeat_password.classList.remove("invalid");
      repeat_password.classList.add("valid");
    } else {
      repeat_password.classList.remove("valid");
      repeat_password.classList.add("invalid");
    }
  }

  myInput.onkeyup = function() {
    // Validar letra minúsculas
    var lowerCaseLetters = /[a-z]/g;
    if(myInput.value.match(lowerCaseLetters)) {  
      letter.classList.remove("invalid");
      letter.classList.add("valid");
    } else {
      letter.classList.remove("valid");
      letter.classList.add("invalid");
    }
    
    // Valida letras maiúsculas
    var upperCaseLetters = /[A-Z]/g;
    if(myInput.value.match(upperCaseLetters)) {  
      capital.classList.remove("invalid");
      capital.classList.add("valid");
    } else {
      capital.classList.remove("valid");
      capital.classList.add("invalid");
    }

    // Valida numeros
    var numbers = /[0-9]/g;
    if(myInput.value.match(numbers)) {  
      number.classList.remove("invalid");
      number.classList.add("valid");
    } else {
      number.classList.remove("valid");
      number.classList.add("invalid");
    }
    
    // Valida o comprimento
    if(myInput.value.length >= 8) {
      length.classList.remove("invalid");
      length.classList.add("valid");
    } else {
      length.classList.remove("valid");
      length.classList.add("invalid");
    }
    
    // Verica se as senhas são iguais
    if(myInput.value == rsenha.value) {
      repeat_password.classList.remove("invalid");
      repeat_password.classList.add("valid");
    } else {
      repeat_password.classList.remove("valid");
      repeat_password.classList.add("invalid");
    }
    rsenha
  }
}

// #####################
function mostraDiv(id, nome, count) {
  var container = document.getElementById(id);
  var button = document.getElementById(nome);

  if (container.style.display === "none") {
    container.style.display = "block";
    if (count == 1) {
      button.innerText = `Ocultar ${count} resposta`;

    } else if ( count > 1) {
      button.innerText = `Ocultar ${count} respostas`;
    }
  } else {
    container.style.display = "none";
    if (count == 1) {
      button.innerText = `Ver ${count} resposta`;
    } else if ( count > 1) {
      button.innerText = `Ocultar ${count} respostas`;
    }
  }
}

function mostraSenha() {
  var senha = document.getElementById("password")
  if (senha.type === "password") {
    senha.type = "text";
  } else {
    senha.type = "password";
  }
}

// Funciobalidade com Ajax e Django
// Quando o usuario fizer um comentário este código irá excultar
if(document.querySelector('#comment-form')){
  let form=document.querySelector('#comment-form');
  function sendForm(event)
  {
    event.preventDefault();
    let data = new FormData(form);
    let ajax = new XMLHttpRequest();
    let token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    ajax.open('POST', form.action);
    ajax.setRequestHeader('X-CSRF-TOKEN',token);
    ajax.onreadystatechange = function()
    {
      if(ajax.status === 200 && ajax.readyState === 4){
        let mensagem = document.querySelector(".mensagem");
        mensagem.innerHTML += `
          <div class="success">
            Comentário enviado para analise com sucesso.
          </div>
          `
      }
    }
    ajax.send(data);
    form.reset();
  }
  form.addEventListener('submit',sendForm,false);
}

// Função para habilitar o botão caso o usuario preencha todo o formulario
function enableButton() {
  document.querySelector('.button').removeAttribute('disabled')
  document.querySelector('.button').style.cursor = 'pointer'
}

// Função para pre-loader
if (document.querySelector(".container-loader")) {
  var loader = setInterval(function () {
    clearInterval(loader);
    document.querySelector(".container-loader").style.display = "none";
    document.querySelector(".content").style.display = "inline";
  
  }, 800);
}
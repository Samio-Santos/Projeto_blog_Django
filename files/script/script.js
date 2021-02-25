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

function mostraDiv(id, nome, count) {
  var container = document.getElementById(id);
  var button = document.getElementById(nome);

  if (container.style.display === "none") {
    container.style.display = "block";
    button.innerText = `Ocultar ${count} respostas`;
  } else {
    container.style.display = "none";
    button.innerText = `Ver ${count} respostas`;
  }
}

function search() {
  var container = document.getElementById("form-search");

  if (container.style.display === "none") {
    container.style.display = "inline-block";
    document.getElementById("title").style.display = "none";
  } else {
    container.style.display = "none";
    container.style.transition = "all 10s";
    document.getElementById("title").style.display = "inline-block";
  }
}

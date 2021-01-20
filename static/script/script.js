/* Quando o usuário clica no botão,
alternar entre ocultar e mostrar o conteúdo suspenso  */
function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
}

// Feche a lista suspensa se o usuário clicar fora dela
window.onclick = function(e) {
  if (!e.target.matches('.dropbtn-img') && !e.target.matches('.dropbtn-seta')) {

    var dropdowns = document.getElementsByClassName("dropdown-content");
    for (var d = 0; d < dropdowns.length; d++) {
      var openDropdown = dropdowns[d];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}
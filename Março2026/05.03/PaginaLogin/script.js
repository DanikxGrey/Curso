function validar() {

    let nome = document.getElementById("nome").value;
    let senha = document.getElementById("senha").value;

    if (nome == "admin" && senha == "1234") {
        window.location.href = "segundo.html";
        return false;
    }
    else {
        alert("Usuário ou senha incorretos!");
        return false;
    }

}
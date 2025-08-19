function VerificarLogin() {
    const acesso = [
        { login: "danikx", senha: "123" },
        { login: "ana", senha: "123" },
        { login: "joao", senha: "123" }
    ];

    const login = document.getElementById("login");
    const senha = document.getElementById("senha");
    const resultado = document.getElementById("resultado");

    let AcessoPermitido = false;

    for (let i = 0; i < acesso.length; i++) {
        if (login.value === acesso[i].login && senha.value === acesso[i].senha) {
            AcessoPermitido = true;
            break
        }
    }

    if (AcessoPermitido === true) {
        resultado.innerHTML = "Acesso Permitido";
    }
    else {
        resultado.innerHTML = "Acesso Negado";
    }
}

//    const input = document.getElementById("login").ariaValueMax;
//    const mensagem = document.getElementById("mensagem");
//    let encontrado = false;
//    for let i = 0(palavras.lenght);
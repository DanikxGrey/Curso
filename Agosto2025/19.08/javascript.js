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
        setTimeout(() => {
            resultado.innerHTML = "Redirecionando..."
        }, 500);

        setTimeout(() => {
            resultado.innerHTML = "Finalizado"
        }, 750);

        setInterval(() => {
            window.location.href = "https://deepwoken.co/builder"
        }, 1000);
    }

    else {
        resultado.innerHTML = "Acesso Negado";

        setTimeout(() => {
           resultado.innerHTML = "Tente novamente" 
        }, 1500);
        
// Limpa os campos de texto
        login.value = ""
        senha.value = ""

    }

} // fim da funçao


//    const input = document.getElementById("login").ariaValueMax;
//    const mensagem = document.getElementById("mensagem");
//    let encontrado = false;
//    for let i = 0(palavras.lenght);

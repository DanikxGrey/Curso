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
            window.location.href = "site2.html"
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
    
async function carregarCurso(curso) {
    const areaTexto = document.getElementById("explicacao");
    areaTexto.innerHTML = "Carregando informações...";

    try {
        await new Promise(resolve => setTimeout(resolve, 250));

        const mensagens = {
            "javascript": "Curso de JavaScript.",
            "py": "Curso de Python.",
            "html e css": "Curso de HTML e CSS.",
            "banco": "Curso de Banco de Dados MySql."
        };

        areaTexto.innerHTML = mensagens[curso] || "Curso não encontrado.";
    } catch (erro) {
        areaTexto.innerHTML = "Erro: " + erro.message;
        console.error("Erro capturado", erro);
    }
} //fim da função
<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Assistência</title>
    <link rel="stylesheet" href="style.css">
</head>


<body>
    <div class="container">
        <form action="result.php" method="post">
            <label>Nome:</label> <br>
            <input type="text" name="nome" placeholder="Nome"> <br> <br>

            <label>Telefone:</label> <br>
            <input type="text" name="telefone" placeholder="Telefone"> <br> <br>

            <label>Tipo de aparelho:</label> <br>
            <input type="text" name="aparelho" placeholder="Aparelho"> <br> <br>

            <label>Escolha uma data preferida para atendimento:</label> <br>
            <input type="date" min="2025-10-28" max="2026-01-01" name="date" placeholder="data"> <br> <br>

            <label>Escreva uma descrição do problema</label> <br>
            <input type="text" name="problema" placeholder="Descrição"> <br>
            <input type="submit" value="enviar"> <br>
        </form>
    </div>
</body>

</html>
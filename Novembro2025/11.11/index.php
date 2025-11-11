<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulario</title>
    <link rel="stylesheet" href="style.css">    
</head>

<body>
    <h1>Exame</h1>
    <form action="result.php" method="post">
        <label>Digite seu nome:</label> <br>
        <input type="text" name="nome" placeholder="nome"> <br>
        <label>Digite seu cpf:</label> <br>
        <input type="text" minlength="11" maxlength="11" name="cpf" placeholder="cpf"> <br>
        <label>Digite sua idade:</label> <br>
        <input type="number" step="1" min="0" max="200" name="idade" placeholder="idade"> <br>
        <label>Escolha uma data para consulta</label> <br>
        <input type="date" name="date" min="2025-01-01" max="2025-12-31" placeholder="date"> <br>
        <input type="submit" value="Enviar">
    </form>
</body>

</html>
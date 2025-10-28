<?php
$nome = $_POST["nome"];
$telefone = $_POST["telefone"];
$aparelho = $_POST["aparelho"];
$date = $_POST["date"];
$problema = $_POST["problema"];
?>

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resultado</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <p><strong>Nome:</strong> <?php echo $nome; ?></p>
        <p><strong>Telefone:</strong> <?php echo $telefone; ?></p>
        <p><strong>Aparelho:</strong> <?php echo $aparelho; ?></p>
        <p>Você agendou uma assistência técnica para o dia <strong><?php echo date("d/m/Y", strtotime($date)); ?></strong>.</p>
        <p><strong>Descrição do problema:</strong><br><?php echo $problema; ?></p>

        <a href="index.php" class="button">Voltar</a>
    </div>
</body>
</html>

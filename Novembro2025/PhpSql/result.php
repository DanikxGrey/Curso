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
        <?php
        if ($_SERVER["REQUEST_METHOD"] == "POST") {
            $nome = $_POST["nome"];
            $telefone = $_POST["telefone"];
            $aparelho = $_POST["aparelho"];
            $data = $_POST["data"];
            $descricao = $_POST["descricao"];
        }

        $conn = new mysqli("localhost", "root", "aluno", "assistencia", "3307"); //Necessario alterar os parametros

        if ($conn->connect_error) {
            die("<p style='color:red'>Erro na conexão com o banco de dados: " . $conn->connect_error . "</p>");
        }

        $sql = "insert into agendamentos (nome, telefone, aparelho, data, descricao)
values ('$nome', '$telefone', '$aparelho', '$data', '$descricao')";

        if ($conn->query($sql) === true) {
            echo "<p><strong>Nome:</strong> $nome </p>";
            echo "<p><strong>Telefone:</strong> $telefone </p>";
            echo "<p><strong>Aparelho:</strong>  $aparelho </p>";
            echo "<p>Você agendou uma assistência técnica para o dia <strong>" . date("d/m/Y", strtotime($data)) . "</strong>.</p>";
            echo "<p><strong>Descrição do problema: </strong><br> $descricao </p>";
        } else {
            echo "<p style='color:red;'>❌ Erro ao salvar: " . $conn->error . "</p>";
        }
        $conn->close();

        ?>
        <a href="index.php" class="button">Voltar</a>
    </div>
</body>

</html>
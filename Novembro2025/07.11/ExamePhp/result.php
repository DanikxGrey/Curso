<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exame</title>
</head>

<body>
    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $nome = $_POST["nome"];
        $cpf = $_POST["cpf"];
        $idade = $_POST["idade"];
        $data = $_POST["date"];

        if (!ctype_digit($cpf) || strlen($cpf) != 11) {
            echo "<p> O cpf deve conter 11 digitos</P>";
            exit;
        }

        $conn = new mysqli("localhost", "root", "", "danikx");
        if ($conn->connect_error) {
            die("<p>Erro na conexao sql: " . $conn->connect_error . "</p>");
        }

        $sql = "insert into agendamento (nome, cpf, idade, data)
        values ('$nome', '$cpf', '$idade', '$data')";

        if ($conn->query($sql) === true) {
            echo "<h1><strong>Agendamento concluído</strong></h1>";
            echo "<p>Nome: $nome</p>";
            echo "<p>Cpf: $cpf</P>";
            echo "<p>Idade: $idade</P>";
            echo "<p>Data do agendamento: $data</p> <br> <br>";
            echo "<h2>Informações sobre o Câncer de Próstata</h2>";
            echo "<p>O câncer de próstata é um dos tipos mais comuns entre os homens, especialmente a partir dos 50 anos.
            A detecção precoce aumenta muito as chances de tratamento bem-sucedido.</p> <br> <br>";
            echo "<h3>Prevenção</h3>";
            echo "<ul>
                <li>Mantenha uma alimentação saudável, rica em frutas, verduras e fibras</li>
                <li>Pratique exercícios físicos regularmente</li>
                <li>Evite o excesso de gordura e carnes processadas</li>
                <li>Realize exames de rotina a partir dos 50 anos (ou antes, se houver histórico familiar)</li>
                </ul>";
        } else {
            echo "<p style='color:red;'>Erro ao salvar os dados no banco de dados: " . $conn->error . "</p>";
        }

        $conn->close();
    }
    ?>
</body>

</html>
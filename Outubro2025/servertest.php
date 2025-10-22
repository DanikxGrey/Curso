<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nome = $_POST["nome"];
    $mamografia = $_POST["mamografia"];
    $email = $_POST["email"];
    $idade = $_POST["idade"];

    echo "<h3>Dados recebidos (POST)</h3>";
    echo "Nome: $nome <br>";
    echo "Email: $email <br>";
    echo "Idade: $idade <br>";
    echo "Fez mamografia: $mamografia";
} else {
?>
    <h2> Formulário </h2>
    <form action="servertest.php" method="post">
        <label> Nome: </label> <br>
        <input type="text" name="nome" required> <br> <br>
        <label> Email: </label> <br>
        <input type="text" name="email" required> <br> <br>
        <label> Idade: </label> <br>
        <input type="text" name="idade" required> <br> <br>

        <label> Já fez o exame? </label> <br>
        <input type="radio" name="mamografia" value="sim" required> Sim <br>
        <input type="radio" name="mamografia" value="nao" required> Não <br> <br>

        <input type="submit" value="Enviar">
    </form>
<?php
}
?>
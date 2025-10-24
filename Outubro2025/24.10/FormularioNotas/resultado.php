<?php
$nome = $_POST["nome"];
$idade = $_POST["idade"];
$turma = $_POST["turma"];
$nota = $_POST["nota"];
$nota1 = $_POST["nota1"];

$media = ($nota + $nota1) / 2;

if ($media >= 6) {
    echo "Aluno: $nome <br>
            idade: $idade <br>
            turma: $turma <br>
            média: $media <br>
            Você foi aprovado";
} else {
    echo "Aluno: $nome <br>
            idade: $idade <br>
            turma: $turma <br>
            média: $media <br>
            Você foi reprovado";
}

if (isset($_GET['campanha']) && isset ($_GET['versao']) ) {
    $campanha = $_GET['campanha'];
    $versao = $_GET['versao'];

    echo "<h3> Informações da campanha </h3>";
    echo "Campanha: $campanha <br>";
    echo "Versão do formulário: $versao <br>";
}

?>

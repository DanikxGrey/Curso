<?php 
$campanha = ["black friday", "natal", "carnaval"];

$produto = $_GET["produto"];
$categoria = $_GET["categoria"];
$preco =  $_GET["preco"];
$estoque = $_GET["estoque"];

echo "Produto: $produto <br>";
echo "Categoria: $categoria <br>";
echo "Preco: $preco <br>";
echo "Estoque: $estoque <br>";
echo "Campanha: " . $campanha[array_rand($campanha)];

?>
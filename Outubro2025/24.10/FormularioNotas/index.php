<h1>Formulario do aluno</h1>

<form action="resultado.php?campanha=Volta%20as%20aulas&Versao=1.0" method="post">
 <label> Nome: </label> <br>
 <input type="text" name="nome" required> <br><br>

 <label> Idade: </label> <br>
 <input type="number" min="0" step="1" name="idade" required> <br><br>

 <label> Turma: </label> <br>
 <input type="text" name="turma" required> <br><br>

 <label> Primeira nota: </label> <br>
 <input type="number" min="0" step="0.01" name="nota" required> <br><br>

 <label> Segunda nota: </label> <br>
 <input type="number" min="0" step="0.01" name="nota1" required> <br><br>
 <input type="submit" value="Enviar">
</form>
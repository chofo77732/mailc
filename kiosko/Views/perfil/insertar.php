

<?php

//Primero, arranca el bloque PHP y checkea si el archivo tiene nombre.  Si no fue asi, te remite de nuevo al formulario de inserción:
// No se comprueba aqui si se ha subido correctamente.
if (empty($_FILES['foto']['name'])){
echo "algo salio mal";//o como se llame el formulario ..
exit;
}

$binario_nombre_temporal=$_FILES['foto']['tmp_name'] ;

// leer del archvio temporal .. el binario subido.
// "rb" para Windows .. Linux parece q con "r" sobra ...
$binario_contenido = addslashes(fread(fopen($binario_nombre_temporal, "rb"), filesize($binario_nombre_temporal)));


//insertamos los datos en la BD.
$user=$_POST['user'];
$consulta_insertar = "UPDATE `perfil` SET `img_perfil`='$binario_contenido' WHERE `id_usuario`='$user'";

$mysqli = new mysqli('127.0.0.1', 'root', '', 'kiosko');

$mysqli->query($consulta_insertar);

header("location: index.php");  // si ha ido todo bien
exit;
?>


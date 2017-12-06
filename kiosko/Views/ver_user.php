<?php
if(isset($_GET['id'])) {

	include("../Controllers/conexion.php");

    

    $sql = "SELECT img_perfil FROM perfil WHERE id_usuario='".$_GET['id']."'";
    $valores2 = mysqli_query($link, $sql);

				$row=mysqli_fetch_array($valores2,MYSQLI_ASSOC);

        echo $row['img_perfil'];

 
}
?>
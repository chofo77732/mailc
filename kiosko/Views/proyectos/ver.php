<?php
if(isset($_GET['id'])) {

	include("../../Controllers/conexion.php");

    $sql = "SELECT imagen FROM proyecto WHERE id_proyecto='".$_GET['id']."'";
    $valores2 = mysqli_query($link, $sql);

				$row=mysqli_fetch_array($valores2,MYSQLI_ASSOC);

        echo $row['imagen'];

 
}
?>
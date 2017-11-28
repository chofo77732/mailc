<?php
if(isset($_GET['id'])) {

    // you may have to modify login information for your database server:
    $conexion=mysql_connect("localhost","root","") or die ("no se ha podido conectar a la BD");

    mysql_select_db("kiosko") or die ("no se ha podido seleccionar la BD");

    $sql = "SELECT img_perfil FROM perfil WHERE id_usuario='".$_GET['id']."'";
    $consulta = mysql_query($sql,$conexion);

    $datos = mysql_result($consulta,0,"img_perfil");

        echo $datos;

 
}
?>
<?php
	
		require_once('conexion.php');


		$boton=$_POST['boton'];

		switch ($boton) {

			case 'registrar':

			$archivo_temporal=$_FILES['archivo']['tmp_name'] ;
			$archivo_contenido = addslashes(fread(fopen($archivo_temporal, "rb"), filesize($archivo_temporal)));

             $tiempo=$_POST['tiempo'];

             $valores = "INSERT INTO `publicidad`(`archivo`, `tiempo`) VALUES ('$archivo_contenido','$tiempo')";

             $result = mysqli_query($link, $valores);
             if($result){
					echo "exito";
				
             }else{
             	echo "error";

             }

             break;

case 'editar':
	
    

			 $id_publicidad=$_POST['id_publicidad'];
			 $archivo_temporal=$_FILES['archivo']['tmp_name'] ;
			$archivo_contenido = addslashes(fread(fopen($archivo_temporal, "rb"), filesize($archivo_temporal)));

             $tiempo=$_POST['tiempo'];

             $valores = "UPDATE `proyecto` SET `archivo`='$archivo_contenido' ,`tiempo`='$tiempo' WHERE `id_publicidad`='$id_publicidad'";

             $result = mysqli_query($link, $valores);
             if($result){
					echo "exito";
				
             }else{
             	echo "error";

             }

break;
					case 'modificar':
					

$id_publicidad=$_POST['id_publicidad'];



$valores = "SELECT * FROM publicidad WHERE id_publicidad = '$id_publicidad'";
$valores2 = mysqli_query($link, $valores);

				$row=mysqli_fetch_array($valores2,MYSQLI_ASSOC);

$datos = array(
				
				0 => $row['id_publicidad'], 
				1 => $row['tiempo'],
				
				);
echo json_encode($datos);
					
				break;

		case 'eliminar':

					
					$id=$_POST['id'];

             $valores = "DELETE from publicidad WHERE `id_publicidad`='$id_publicidad'";

             $result = mysqli_query($link, $valores);
             if($result){
					echo "exito";
				
             }else{
             	echo "error";

             }


					
				break;

			default:
				# code...
				break;
		}

		
?>
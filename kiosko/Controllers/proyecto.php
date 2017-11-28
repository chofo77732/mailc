<?php
	
		require_once('conexion.php');


		$boton=$_POST['boton'];

		switch ($boton) {

			case 'registrar':
    

			 $nombre=$_POST['nombre'];
             $tipo=$_POST['tipo'];
             $descripcion=$_POST['descripcion'];
             $imagen_temporal=$_FILES['imagen']['tmp_name'] ;
			$imagen_contenido = addslashes(fread(fopen($imagen_temporal, "rb"), filesize($imagen_temporal)));

			$archivo_temporal=$_FILES['archivo']['tmp_name'] ;
			$archivo_contenido = addslashes(fread(fopen($archivo_temporal, "rb"), filesize($archivo_temporal)));
             // $imagen=$_POST['imagen'];
             // $archivo=$_POST['archivo'];
             $area=$_POST['area'];
             $fk_perfil=$_POST['fk_perfil'];

             $valores = "INSERT INTO `proyecto`(`nombre`, `tipo`, `descripcion`, `imagen`, `archivo`, `area`, `fk_perfil`) VALUES ('$nombre','$tipo','$descripcion','$imagen_contenido','$archivo_contenido','$area','$fk_perfil')";

             $result = mysqli_query($link, $valores);
             if($result){
					echo "exito";
				
             }else{
             	echo "error";

             }

             break;

case 'editar':
	
    

			 $id_proyecto=$_POST['id_proyecto'];
			 $nombre=$_POST['nombre'];
             $tipo=$_POST['tipo'];
             $descripcion=$_POST['descripcion'];
             $imagen_temporal=$_FILES['imagen']['tmp_name'] ;
			$imagen_contenido = addslashes(fread(fopen($imagen_temporal, "rb"), filesize($imagen_temporal)));

			$archivo_temporal=$_FILES['archivo']['tmp_name'] ;
			$archivo_contenido = addslashes(fread(fopen($archivo_temporal, "rb"), filesize($archivo_temporal)));
             // $imagen=$_POST['imagen'];
             // $archivo=$_POST['archivo'];
             $area=$_POST['area'];
             $fk_perfil=$_POST['fk_perfil'];

             $valores = "UPDATE `proyecto` SET `nombre`='$nombre' ,`tipo`='$tipo' ,`descripcion`='$descripcion' ,`imagen`='$imagen_contenido' ,`archivo`='$archivo_contenido' ,`area`='$area' WHERE `id_proyecto`='$id_proyecto'";

             $result = mysqli_query($link, $valores);
             if($result){
					echo "exito";
				
             }else{
             	echo "error";

             }

break;
					case 'modificar':
					

$id_proyecto=$_POST['id_proyecto'];



$valores = "SELECT * FROM proyecto WHERE id_proyecto = '$id_proyecto'";
$valores2 = mysqli_query($link, $valores);

				$row=mysqli_fetch_array($valores2,MYSQLI_ASSOC);

$datos = array(
				
				0 => $row['id_proyecto'], 
				1 => $row['nombre'], 
				2 => $row['tipo'], 
				3 => $row['descripcion'], 
				4 => $row['area'], 
				5 => $row['fk_perfil'], 
				
				);
echo json_encode($datos);
					
				break;

		case 'eliminar':

					
					$id=$_POST['id'];

             $valores = "DELETE from proyecto WHERE `id_proyecto`='$id'";

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
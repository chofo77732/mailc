<?php
	
		require_once('conexion.php');


		$boton=$_POST['boton'];
		session_start();

		switch ($boton) {

			case 'registrar':
    

			 // $tipo_p=$_POST['tipo_p'];
    //          $nombres=$_POST['nombres'];
    //          $apellido_p=$_POST['apellido_p'];
    //          $apellido_m=$_POST['apellido_m'];
    //          $email=$_POST['email'];
    //          $password=$_POST['password'];
    //          $direccion=$_POST['direccion'];
    //          $celular=$_POST['celular'];
    //          $telefono=$_POST['telefono'];

    //          $valores = "INSERT INTO `participante`(`tipo`, `nombre`, `paterno`, `materno`, `email`, `contra`, `direccion`, `celular`, `telefono`) VALUES ('$tipo_p', '$nombres', '$apellido_p', '$apellido_m', '$email','$password','$direccion','$celular','$telefono')";

    //          $result = mysqli_query($link, $valores);
    //          if($result){
				// 	echo "exito";
				
    //          }else{
    //          	echo "error";

    //          }
             // echo $tipo_p.$nombres.$apellido_p.$apellido_m.$email.$password.$direccion.$celular.$telefono;


             break;

case 'editar':
	
    

			 $id_usuario=$_SESSION['id'];
			 $nombre=$_POST['nombre'];
             $sexo=$_POST['sexo'];
             $ocupacion=$_POST['ocupacion'];
             $espec_ocupacion=$_POST['espec_ocupacion'];
             $carrera=$_POST['carrera'];
             $edad=$_POST['edad'];
             $intereses=$_POST['intereses'];
             $habilidades=$_POST['habilidades'];
             $autodescripcion=$_POST['autodescripcion'];
             $meta_vida=$_POST['meta_vida'];
             $telefono=$_POST['telefono'];
             $facebook=$_POST['facebook'];

             $valores = "UPDATE `perfil` SET `nombre`='$nombre', `sexo`='$sexo', `ocupacion`='$ocupacion', `espec_ocupacion`='$espec_ocupacion', `carrera`='$carrera', `edad`='$edad', `intereses`='$intereses', `habilidades`='$habilidades', `autodescripcion`='$autodescripcion', `meta_vida`='$meta_vida', `telefono`='$telefono', `facebook`='$facebook' WHERE `id_usuario`='$id_usuario'";

             $result = mysqli_query($link, $valores);
             if($result){
					echo $autodescripcion. $meta_vida. $telefono;
				
             }else{
             	echo "error";

             }

break;
					case 'modificar':
					

$id_usuario=$_SESSION['id'];



$valores = "SELECT * FROM perfil WHERE id_usuario = '$id_usuario'";
$valores2 = mysqli_query($link, $valores);

				$row=mysqli_fetch_array($valores2,MYSQLI_ASSOC);

$datos = array(
				
				0 => $row['id_usuario'], 
				1 => $row['nombre'], 
				2 => $row['apellidos'], 
				3 => $row['sexo'], 
				4 => $row['correo'], 
				5 => $row['contra'], 
				6 => $row['ocupacion'], 
				7 => $row['espec_ocupacion'], 
				8 => $row['carrera'], 
				9 => $row['edad'], 
				10 => $row['intereses'], 
				11 => $row['habilidades'], 
				12 => $row['autodescripcion'], 
				13 => $row['meta_vida'], 
				14 => $row['telefono'], 
				15 => $row['facebook'], 
				16 => $row['alias'], 
				
				);
echo json_encode($datos);
					
				break;

		case 'eliminar':

					$id=$_POST['id'];

             $valores = "DELETE from perfil WHERE `id_usuario`='$id_usuario'";

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
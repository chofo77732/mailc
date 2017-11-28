<?php 
	class usuario
	{
		private $conexion;
		public function __construct()
		{
			require_once('conexion.php');
			$this->conexion= new conexion();
			$this->conexion->conectar();
		}

		function identificar($email,$password)
		{
			$pass=sha1($password);
			$sql="SELECT * FROM `perfil` WHERE correo='$email' and contra='$password'";
			$resulatdos = $this->conexion->conexion->query($sql);
			if ($resulatdos->num_rows > 0) {
				$r=$resulatdos->fetch_array();
			}
			else{
				$r[0]=0;
			}
			return $r;
			$this->conexion->cerrar();
		}

				function hay($email)
		{
			$sql="SELECT * FROM `perfil` WHERE correo='$email'";
			$resulatdos = $this->conexion->conexion->query($sql);
			if ($resulatdos->num_rows > 0) {
				return false;
			}
			else{
				return true;
			}
			$this->conexion->cerrar();
		}
		
		function registrar($nombre,$apellido,$email,$password){
			$pass= sha1($password);
			$sql="INSERT INTO `perfil`( `nombre`, `apellidos`, `correo`, `contra`) VALUES ('$nombre', '$apellido', '$email', '$password')";
			if($this->conexion->conexion->query($sql)){
				return true;
			}
			else
			{
				return false;
			}
			$this->conexion->cerrar();
		}
	
	}

	
	
?>

<?php 
session_start();
  if (isset($_SESSION['nombre']) && $_SESSION['ingreso']=='YES') 
  {?>
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Aplicacion Web</title>

    <link rel="stylesheet" href="../Resources/css/bootstrap.css">
<link rel="stylesheet" href="../Resources/css/tema.css">
</head>
 
<body>
    <!--Barra de Navegacion-->


<?php include('nav.php') ?>
<br>
<br>
<br>
<br>

<h1>Información</h1>



    


</style>

<div class="row" id="info" style=" height: 600px; overflow: scroll;">
		

   <?php 

include('../Controllers/conexion.php');
$id_s=$_SESSION['id'];
$id_proyecto=$_GET['id_proyecto'];
$query = "SELECT proyecto.id_proyecto, proyecto.nombre as nombre_proyecto, proyecto.tipo as tipo_proyecto, proyecto.descripcion as descripcion_proyecto,  proyecto.area, perfil.id_usuario, perfil.nombre as nombre_usuario,  perfil.sexo, perfil.correo, perfil.ocupacion, perfil.espec_ocupacion, perfil.carrera, perfil.edad, perfil.intereses, perfil.habilidades, perfil.autodescripcion, perfil.meta_vida, perfil.telefono, perfil.facebook  from proyecto INNER JOIN perfil on proyecto.fk_perfil = perfil.id_usuario WHERE proyecto.id_proyecto = '$id_proyecto'";
    
$result = mysqli_query($link, $query);
if ($result) {
  # code...

            while($registro = mysqli_fetch_array($result, MYSQLI_ASSOC)){

echo '
               <div id="muro_bloques">
                <div class="col-md-2"></div>
            <div class="col-md-8">
<div class="panel panel-default">
                    <div class="panel-heading"><h3>'.$registro["nombre_proyecto"].'</h3></div>
                    <div class="panel-body">   
                    <div class="col-md-6">
                      <p>Tipo: '.$registro["tipo_proyecto"].'</p>
                      <p>Área: '.$registro["area"].'</p>
                      <p>Descripción:</p>
                      <p>'.$registro["descripcion_proyecto"].'</p>
                      <a href="javascript:unirse('.$registro["id_proyecto"].');" >Unirse</a>
                        <br>
                      
                      </div>
                      <div class="col-md-6">
               <img class="img-responsive img-portfolio img-hover" src="ver.php?id='.$registro["id_proyecto"].'">
                      </div>
                    </div>
                </div>
        </div>
        </div>

        <div id="muro_bloques" class="container">
                <div class="col-md-2"></div>
            <div class="col-md-8">
<div class="panel panel-default">
                    <div class="panel-heading">PERFIL</div>
                    <div class="panel-body">   
                    <div class="col-md-6">
               <h3>'.$registro["nombre_usuario"].'</h3>
                      <p>Ócupacion: '.$registro["ocupacion"].'</p>
                      <p>'.$registro["espec_ocupacion"].'</p>
                      <p>Carrera: '.$registro["carrera"].'</p>
                      <p>Intereses: '.$registro["intereses"].'</p>
                      <p>Habilidades: '.$registro["habilidades"].'</p>
                      <p>Córreo electrónico: '.$registro["correo"].'</p>
                      <p>Telefono: '.$registro["telefono"].'</p>
                      <p>facebook: '.$registro["facebook"].'</p>
                        
                        <br>

                      </div>
                      <div class="col-md-6">
               <img width="150" height="210" src="ver_user.php?id='.$registro["id_usuario"].'">
                      </div>
                    </div>
                </div>
        </div>
        </div>
        ';
         
    }
    }

    ?>
	
</div>

    <script src="../Resources/js/jquery.js"></script>
    <script src="../Resources/js/bootstrap.min.js"></script>
    <script>
        function cerrar()
        {
            $.ajax({
                url:'../Controllers/usuario.php',
                type:'POST',
                data:"mensaje=mensaje&boton=cerrar"
            }).done(function(resp){
                alert(resp);

            });
        }
    </script>
</body>
</html>

<?php

  }
  else
  {
    header("location: ./");
  }
 ?>
    
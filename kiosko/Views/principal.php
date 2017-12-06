
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

<div class="container">
        <div class="row">
            
            <div id="flotante_i">

    <div class="col-md-3" style="position: fixed;" >
            <div class="panel panel-default">
                    <div class="panel-heading">Bienvenido</div>
                    <div class="panel-body">  
                    <br>                   
                    <br>                   
                    <br>                   
                    <br>                   
                    <br>                   
                    <br>                   
                    <br>                   
                      <p>Estas a dentro!</p>
                    </div>
                </div>
            </div>

</div>

    <!-- <div id="buscar">
                    <div class="col-md-4"></div>
                <div class="col-md-8">
    <div class="panel panel-default">
                        <div class="panel-heading">Bienvenido</div>
                        <div class="panel-body">   
                   
                          <div class="form-group">
                                    <div class="col-xs-4  text-right">
                                        <label for="buscar" class="control-label">Buscar:</label>
                                    </div>
                                    <div class="col-xs-4">
                                        <input  type="text" name="buscar" id="buscar" class="form-control" onkeyup="lista_libros(this.value);" placeholder="Ingrese nombre o descripcion"/>
                                    </div>
                                </div>

                        </div>
                    </div>
            </div>
            </div>



            <div id="muro">
                    <div class="col-md-4"></div>
                <div class="col-md-8">
    <div class="panel panel-default">
                        <div class="panel-heading">Bienvenido</div>
                        <div class="panel-body">   
                   
                          <p>Estas a dentro!</p>
                          <div id="lista"></div>
                        </div>
                    </div>
            </div>
            </div>
 -->
<div class="col-md-4"></div>
<div class="col-md-4"></div>
<div class="col-md-4" >
    <form method="POST">
<div class="input-group">
      <input type="text" name="buscar_2" id="buscar_2" class="form-control"  placeholder="Ingrese nombre, area o descripcion" class="form-control" size="50" >
      <div class="input-group-btn">
        <button class="btn button-submit"  type="submit"><span class="glyphicon glyphicon-search"></span></button>
      </div>
    </div>
   </form>
   </div>
   <br>

<div class="container" id="info" style=" height: 650px; overflow: scroll;" >
    <br>
   <?php 
if (isset($_POST['buscar_2'])){

$valor= $_POST['buscar_2'];
include('../Controllers/conexion.php');
$id_s=$_SESSION['id'];
$query = "SELECT  `id_proyecto`, `nombre`, `tipo`, `descripcion`, `archivo`, `area`, `fk_perfil` FROM `proyecto` where nombre like '%".$valor."%' or tipo like '%".$valor."%' or descripcion like '%".$valor."%'";
    
$result = mysqli_query($link, $query);
if ($result) {
  # code...

            while($registro = mysqli_fetch_array($result, MYSQLI_ASSOC)){

echo '
                <div id="muro_bloques">
                <div class="col-md-4"></div>
            <div class="col-md-8">
<div class="panel panel-default">
                    <div class="panel-heading"><h3>'.$registro["nombre"].'</h3></div>
                    <div class="panel-body">   
                    <div class="col-md-6">
                      <p>Tipo: '.$registro["tipo"].'</p>
                      <p>Área: '.$registro["area"].'</p>
                      <p>Descripción:</p>
                      <p>'.$registro["descripcion"].'</p>
                      <a href="javascript:unirse('.$registro["id_proyecto"].');" >Unirse</a>
                        <br>
                      <a href="informacion.php?id_proyecto='.$registro["id_proyecto"].'" >Conoce Más</a>
                      </div>
                      <div class="col-md-6">
               <img class="img-responsive img-portfolio img-hover" src="ver.php?id='.$registro["id_proyecto"].'">
                      </div>
                    </div>
                </div>
        </div>
        </div>
        ';
         
    }
    
}else{

    echo '<div id="muro_bloques">
                <div class="col-md-4"></div>
            <div class="col-md-8">
<div class="panel panel-default">
                    <div class="panel-heading">Bienvenido</div>
                    <div class="panel-body">   
                    <div class="col-md-6">
               <h3>No hay proyectos con ese nombre o descripción</h3>
                     
                      </div>
                    </div>
                </div>
        </div>
        </div>';
}

}

    ?>


</div>

        </div>
        </div>

<!--     <div class="container">
        <div class="row">
            <div class="col-md-4"></div>
            <div class="col-md-4">
                <div class="panel panel-default">
                    <div class="panel-heading">Bienvenido</div>
                    <div class="panel-body">                     
                      <p>Estas a dentro!</p>
                    </div>
                </div>
            </div>
        </div>
    </div> -->

<?php 
// echo $_SESSION['nombre']; 
// echo $_SESSION['ingreso']; 

?>



  
    <script src="../Resources/js/jquery.js"></script>
    <script src="../Resources/js/bootstrap.min.js"></script>
    <script type="text/javascript">
        function unirse(id){

            var user=<?php echo $_SESSION['id']; ?>


                    $.ajax({
                        url:'../Controllers/grupos.php',
                        type:'POST',
                        data: 'user='+user+'&id_proyecto='+id+'&pro=unirse',
                    }).done(function(respuesta){
                        if (respuesta=='exito') {
                            $('#exito').show();
                            alert(respuesta);

                        }
                        else{
                            alert(respuesta);
                        }
                        
                    })  .always(function(data) {

        location.reload();
      });

        }

    </script>
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

    <script type="text/javascript">
        function lista_libros(valor){
    $.ajax({
        url:'../Controllers/libros.php',
        type:'POST',
        data:'valor='+valor+'&boton=buscar'
    }).done(function(resp){
        //alert(resp);
        var valores = eval(resp);
        html="<table class='table table-bordered'><thead><tr><th>#</th><th>ISBN</th>\
        <th>Titulo</th><th>Autor</th><th>Año de Publicacion</th><th>Nro de Paginas</th>\
        <th>Ediccion<</th><th>Idioma</th></tr></thead><tbody>";
        for(i=0;i<valores.length;i++){
            html+="<tr><td>"+(i+1)+"</td><td>"+valores[i][1]+"</td><td>"+valores[i][2]+
            "</td><td>"+valores[i][3]+"</td><td>img</td><td>"+valores[i][4]+
            "</td><td>"+valores[i][5]+"</td><td>"+valores[i][6]+"</td></tr>";
        }
        html+="</tbody></table>"
        $("#lista").html(html);
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
    
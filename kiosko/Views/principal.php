
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

<div id="muro">
                <div class="col-md-4"></div>
            <div class="col-md-8">
<div class="panel panel-default">
                    <div class="panel-heading">Bienvenido</div>
                    <div class="panel-body">   
               
                      <p>Estas a dentro!</p>
                    </div>
                </div>
        </div>
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

                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>                  
                    <br>   
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
    
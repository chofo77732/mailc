
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

<h1>Misión</h1>

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
    
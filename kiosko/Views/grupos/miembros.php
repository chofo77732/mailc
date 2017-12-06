
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

    <link rel="stylesheet" href="../../Resources/css/bootstrap.css">
<link rel="stylesheet" href="../../Resources/css/tema.css">
</head>
 
<body>
    <!--Barra de Navegacion-->


<?php include('../html/nav.php') ?>
<br>
<br>
<br>
<br>

<h1>Miembros</h1>


<div class="col-xs-1"></div>
<div class="col-xs-10">

<br>
     <!-- <button href="javascript:void(0)" data-toggle="modal" data-target="#responsive" type="button" class="btn btn-success">Agregar Grupo</button> -->
     <!-- <button OnClick="location.href='inicio2.php'" type="button" class="btn btn-success">Regresar</button>
       -->
    
<br>

    <div class="registros" id="tbl_actor">
<br>
        <table class="table table-striped table-condensed table-hover" >
            <tr>
                <!-- <th >id</th> -->
                <th >Nombre</th>
                <th >Descripcion</th>
                <th >Tipo</th>
                <th >Miembros</th>

                <th >Opciones</th>
            </tr>





        <?php


include('../../Controllers/conexion.php');
$id_s=$_SESSION['id'];
$id_proyecto=$_GET['id_proyecto'];
// echo $id_proyecto;
$query = "SELECT perfil.nombre, perfil.correo, perfil.carrera from perfil INNER JOIN user_grupo on perfil.id_usuario = user_grupo.fk_perfil where user_grupo.fk_proyecto = '$id_proyecto'";
    
$result = mysqli_query($link, $query);
if ($result) {
  # code...

            while($registro = mysqli_fetch_array($result, MYSQLI_ASSOC)){

                echo "<tr>
                        <td>".$registro['nombre']."</td>
                        <td>".$registro['correo']."</td>
                        <td>".$registro['carrera']."</td>
                        
</tr>
";
    

            }
            }else{
              echo "<h1>No tienes Proyectos registrados</h1>";
            }

             // <td><img src=\"ver.php?id=".$registro['id_curso']."\"  width='150' height='100'></td>
                         // <td><img src=\"ver.php?id=".$registro['id_curso']."\"  width='150' height='100'></td>

 
        ?>
        </table>
    </div>
    </div>


<!-- Modal      111111111111111111111111111111111111111111111111111111111 -->

        <div class="modal fade" id="responsive" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" onclick="location.reload();"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>
                <h2 class="modal-title">Curso</h2>
              </div>
              <div class="modal-body">
                <div class="alert alert-success text-center" id="exito" style="display:none;">
                  <span class="glyphicon glyphicon-ok"> </span><span>Grupo Registrado</span>
                </div>
                <!-- <form enctype="multipart/form-data" class="form-horizontal" method="post" id="formCliente" > -->
                 <form enctype="multipart/form-data" class="form-horizontal" method="post" id="formProyecto" >
                  <div class="form-group">
                    <label for="proceso" class="control-label col-xs-4">proceso :</label>
                    <div class="col-xs-6">
                      <input id="pro" name="pro" type="text" class="form-control" readonly="readonly" value="registrar">
                    </div>
                  </div>

                  <div class="form-group">
                    <label for="id" class="control-label col-xs-4">id :</label>
                    <div class="col-xs-6">
                      <input id="id" name="id" type="text" class="form-control" readonly="readonly" value="">
                    </div>
                  </div>

                  <div class="form-group">
                    <label for="nombre" class="control-label col-xs-4">Nombre:</label>
                    <div class="col-xs-6">
                        <input id="nombre" name="nombre" type="text" class="form-control" required autocomplete="off">

                    </div>
                  </div>

                  <div class="form-group">
                    <label for="tipo" class="control-label col-xs-4">Tipo:</label>
                    <div class="col-xs-6">
                        <input id="tipo" name="tipo" type="text" class="form-control" required autocomplete="off">

                    </div>
                  </div>


                  <div class="form-group">
                    <label for="descripcion" class="control-label col-xs-4">Descripción:</label>
                    <div class="col-xs-6">
                        <!-- <input id="desc" name="desc" type="text" class="form-control" > -->
                        <textarea id="descripcion" name="descripcion" type="text" class="form-control" required autocomplete="off"></textarea>
                    </div>
                  </div>

<input type="text" hidden name="fk_proyecto" value="<?php echo $_GET['id_proyecto']; ?>">

<button  type="button" class="btn btn-danger right" data-dismiss="modal" onclick="location.reload();">Cerrar</button>
                <!-- <button onclick="registrar();" type="button" class="btn btn-success">Guardar</button> -->
                <button type="submit" onclick="registrar()" class="btn btn-success right">Guardar</button>
                </form>
              </div>
              <div class="modal-footer">  

              </div>
            </div><!-- /.modal-content -->
          </div><!-- /.modal-dialog -->
        </div><!-- /.modal -->



    <script src="../../Resources/js/jquery.js"></script>
    <script src="../../Resources/js/bootstrap.min.js"></script>
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
      

// objetivo--objetivo--objetivo--objetivo--objetivo--objetivo--objetivo--objetivo--objetivo--objetivo--
          
  function registrar(){


            var id=$('#id').val();
            var nombre=$('#nombre').val();
            var tipo=$('#tipo').val();
            var descripcion=$('#descripcion').val();
            var opcion=$('#pro').val();

var parametros = new FormData($('#formProyecto')[0]);

                    $.ajax({
                        url:'../../Controllers/grupos.php',
                        type:'POST',
                        data: parametros,
                        contentType: false,
                        processData: false,
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

function modificar(id){
    //$('#responsive')[0].reset();
     var url = '../../Controllers/grupos.php';
        $.ajax({
        type:'POST',
        url:url,
        data:'id='+id+'&pro=modificar',
        success: function(valores){

                var datos = JSON.parse(valores);

                $('#pro').val('editar');
                $('#id').val(id);
                $('#nombre').val(datos[1]);
                $('#tipo').val(datos[2]);
                $('#descripcion').val(datos[3]);

                $('#responsive').modal({
                    show:true,
                    backdrop:'static'
                });

            return false;

        }
    });
    return false;
}

function eliminar(id){
    //$('#responsive')[0].reset();
      var url = '../../Controllers/grupos.php';
        $.ajax({
        type:'POST',
        url:url,
        data:'id='+id+'&pro=eliminar'
    }).done(function(respuesta){
                    if (respuesta=='exito') {
                        $('#exito').show();

                    }
                    else{
                        alert(respuesta);
                    }
                    
                })  .always(function(data) {

    location.reload();
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
    

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
 
<body onload="modificar()">
    <!--Barra de Navegacion-->


<?php include('../html/nav.php') ?>

    <div class="container">


        <!-- Encabezado de página / Breadcrumb -->
       <br>
       <br>
       <br>

        <div class="row">
            <div class="col-md-12">
                <h1 class="page-header">Perfil de usuario
                    <small>editando datos</small>
                </h1>
                <ol class="breadcrumb">
                    <li><a href="index.html">Inicio</a></li>
                    <li><a href="#">Perfil de usuario</a></li>
                    <li class="active">Editando datos</li>
                </ol>
            </div>
        </div>

        <!-- Fin Encabezado de página / Breadcrumb -->
               
        <!-- Contact Form -->
        <!-- Campos del formulario de contacto con validación de campos-->
        <div class="row" style=" height: 650px; overflow: scroll;">
            <!-- Columna de la izquierda -->
            <div class="col-md-3">
                <div class="col-md-12" align="center">
<?php

echo "<img class='img-responsive img-portfolio img-hover' src=\"ver.php?id=".$_SESSION['id']."\">";
   // echo $datos;

?>


                    <!-- <img class="img-responsive img-portfolio img-hover" src="profile.jpg"> -->
                </div>
                <div class="col-md-12">
                    <p class="text-center"><strong>Nombre Apellido</strong></p>
                    <p class="text-center"><em>Título del perfil de usuario</em></p>
                </div>

                <div class="col-md-12 text-center">
                   <!-- Redes sociales-->
                   <ul class="list-unstyled list-inline list-social-icons">
                        <li>
                            <a href="#"><i class="editIcons icon-facebook-square editSizeIcons"></i></a>
                        </li>
                       
                        <li>
                            <a href="#"><i class="editIcons icon-google-plus-square editSizeIcons"></i></a>
                        </li>
                    </ul>
                    <!-- Fin redes sociales -->
                </div>

                <div class="col-md-12">
                <!-- Barra vertical de opciones del perfil de usuairo -->
                    <br >
                    <ul class="list-group list-primary">
                        <a href="#" class="list-group-item">Ver perfil público</a>
                        <a href="#" class="list-group-item">Mi perfil</a>
                        <a href="javascript:void(0)" data-toggle="modal" data-target="#responsive" type="button" class="list-group-item">Fotografia</a>
                        <a href="#" class="list-group-item">Cuenta</a>
                        <a href="#" class="list-group-item">Preferencias</a>
                        <a href="#" class="list-group-item">Configurar Github</a>
                    </ul>
                </div>
                <!-- Fin Barra vertical de opciones del perfil de usuario -->
            </div>
            <!-- Fin de Columna de la izquierda -->

            <!-- Parte central -->
            <div class="col-md-9">
                <div class="col-md-12" style="border-width: 1px 1px 0px 1px; border-style: solid; border-color: lightgrey;">
                    <!-- <img src="FMUNIFERCOM2.png" class="img-responsive img-rounded"> -->
                    <h3 style="text-align: center">Mi perfil <p><small>Añade información personal para compartir tu perfil</small></p></h3>
                </div>
                <!-- Se inicia el form (ojo todos los elementos de formulario deben ir dentro de esta etiqueta-->
                <form name="modifyProfile" id="profileForm" novalidate>
                <!-- Inicio del div central parte de formulario información básica -->
                <div class="col-md-12" style="border-width: 1px 1px 0px 1px; border-style: solid; border-color: lightgrey; background: #f1f3f6;">
                    <div class="col-md-8 col-md-offset-2">
                        
<div class="control-group form-group">
<div class="controls">
    <br >
    <label>Información básica</label>
    <span id="alertName" data-toggle="popover" data-trigger="hover" data-placement="right" title="" data-content="">
        <input type="text" class="form-control" name="nombre" id="nombre" placeholder="Introduzca su nombre" required data-validation-required-message="Por favor introduzca su nombre.">
    </span>
    <br>
     <span  <div class="form-group">
     <label>Sexo: </label>
     <input type="radio" name="sexo" value="h"> Hombre
     <input type="radio" name="sexo" value="m"> Mujer 
    </span>
    <br >
     <br >

    <span id="alertQualification" data-toggle="popover" data-trigger="hover" data-placement="right" title="" data-content="">
        <input type="text" class="form-control" id="ocupacion" name="ocupacion" placeholder="Introduzca su ocupación" required data-validation-required-message="Por favor introduzca su ocupación.">
    </span>
    <br >
    <span id="alertQualification" data-toggle="popover" data-trigger="hover" data-placement="right" title="" data-content="">
        <input type="text" class="form-control" id="espec_ocupacion" name="espec_ocupacion" placeholder="Introduzca su especificación de ocupación" required data-validation-required-message="Por favor introduzca su especificación de ocupación.">
    </span>
    <br >
    <span id="alertQualification" data-toggle="popover" data-trigger="hover" data-placement="right" title="" data-content="">
        <input type="text" class="form-control" id="carrera" placeholder="Introduzca su carrera" required data-validation-required-message="Por favor introduzca su Carrera.">
    </span>
    <br >
    <span div class="control-group">
      <label class="control-label" for="edad">Edad</label>
      <div class="controls">
        <input id="edad" name="edad" type="text" placeholder="" class="input-xlarge">
        
      </div>
    </div>
 </span>
    <br >
    <span id="alertQualification" data-toggle="popover" data-trigger="hover" data-placement="right" title="" data-content="">
        <input type="text" class="form-control" id="intereses" placeholder="Introduzca sus interes " required data-validation-required-message="Por favor introduzca sus interes.">
    </span>
    <br >
    <span id="alertQualification" data-toggle="popover" data-trigger="hover" data-placement="right" title="" data-content="">
        <input type="text" class="form-control" id="habilidades" placeholder="Introduzca sus habilidades" required data-validation-required-message="Por favor introduzca sus habilidades.">
        <br >
    <div class="controls">
    <label>Auto descripción:</label>
    
        <textarea rows="6" cols="30" class="form-control" id="autodescripcion" name="autodescripcion" required maxlength="999" placeholder="Por favor introduzca su autodescripción."></textarea>
    
    <br >
     <div class="controls">
    <label>Introduzca Meta de vida:</label>
    
        <textarea rows="6" cols="30" class="form-control" id="meta_vida" name="meta_vida" required placeholder="Por favor introduzca su meta de vida."></textarea>
        <br>
    
    <span id="telefono" data-toggle="popover" data-trigger="hover" data-placement="right" title="" data-content="">
        <input type="text" class="form-control" id="telefono" placeholder="Introduzca su telefono" required>
    </span>
    
                                    <p class="help-block"></p>
                                </div>
                            </div>
                           
                                            
                                        </select>
                                    </span>
                                    <br >
                                </div>
                            </div>
                    </div>
                </div>
                <!-- Fin del div central parte de formulario información básica -->

                <!-- Parte central - enlaces -->
                <div class="col-md-12" style="border: 1px solid lightgrey; background: #e5eaf2;">
                    <!-- Parte de redes sociales en el alta de perfil -->
                    <div class="col-md-8 col-md-offset-2">
                        <div class="control-group form-group">
                            <div class="controls">
                                <br >
                                <label>Enlaces:</label>
                                <input type="text" class="form-control" id="txtMyWeb" placeholder="Introduzca su web personal o profesional">
                                <br>
                                <div class="input-group">
                                    <span class="input-group-addon">https://plus.google.com</span><input type="text" class="form-control" id="txtPlus" placeholder="Introduzca su usuario de Google+">
                                </div>
                                <br>
                                <div class="input-group">
                                    <span class="input-group-addon">https://www.facebook.com</span><input type="text" class="form-control" id="facebook" placeholder="Introduzca su usuario de Facebook">
                                </div>
                                <br>

                                <br >
                            </div>
                        </div>
                    </div>
                    <!-- Fin Parte de redes sociales en el alta de perfil -->
                    
                    <!-- Botones formulario -->
                    <div class="col-md-12 container allFormButtons">
                        <br >
                        <div class="col-md-2 col-md-offset-2">
                            <div class="form-group">
                              <button type="button" id="btnCancel" class="btn btn-danger">Cancelar</button>
                            </div>
                        </div>
                        <div class="col-md-5 col-md-offset-3">
                            <div class="form-group">
                                <button type="button" id="btnClean" class="btn btn-warning">Limpiar</button>
                                <button type="submit" id="btnEnviar" onclick="registrar()" class="btn btn-primary">Actualizar</button>
                            </div>
                        </div>
                        &nbsp;
                    </div>
                    <!-- Fin botones formulario -->
                </div>
                <!-- Fin Parte central - enlaces -->
            </form>
            <!-- Fin del form -->
            </div>  
            <!-- Fin del div de parte central -->
        </div>
        <!-- Fin Campos del formulario de contacto con validación de campos -->
        &nbsp;
        <hr>

        <!-- Footer -->
        <footer>
            <div class="row">
                <div class="col-lg-12 footer-align">
                    <p>Universidad Politecnica de Amozoc</p>
                </div>
            </div>
        </footer>

    </div>
    <!-- /.container -->

        <div class="modal fade" id="responsive" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" onclick="location.reload();"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>
                <h2 class="modal-title">Imagen</h2>
              </div>
              <div class="modal-body">
                <!-- <form enctype="multipart/form-data" class="form-horizontal" method="post" id="formCliente" > -->
                    <FORM enctype="multipart/form-data" method="post" action="insertar.php">
Archivo: <INPUT type="file" name="foto" size="30">
<input type="text" name="user" id="user" value="<?php echo $_SESSION['id']?>" hidden>

<button  type="button" class="btn btn-danger right" data-dismiss="modal" onclick="location.reload();">Cerrar</button>
                <!-- <button onclick="registrar();" type="button" class="btn btn-success">Guardar</button> -->
                <button type="submit" class="btn btn-success right">Guardar</button>
                </form>
              </div>
              <div class="modal-footer">  
              </div>
            </div><!-- /.modal-content -->
          </div><!-- /.modal-dialog -->
        </div><!-- /.modal -->
 <!-- <button onclick="guardar();" class="btn btn-success right">Guardar</button> -->
    <script src="../../Resources/js/jquery.js"></script>
    <script src="../../Resources/js/bootstrap.min.js"></script>
    <script type="text/javascript">

        $(document).ready(function () {

   //Código para que la web muestre el popover
    $('[data-toggle="popover"]').popover();
})


        function cerrar()
        {
            $.ajax({
                url:'../../Controllers/perfil.php',
                type:'POST',
                data:"mensaje=mensaje&boton=cerrar"
            }).done(function(resp){
                alert(resp);

            });
        }
    </script>

<script type="text/javascript">
    

  function registrar(){

            var nombre=$('#nombre').val();
            var sexo=$('#sexo').val();
            var ocupacion=$('#ocupacion').val();
            var espec_ocupacion=$('#espec_ocupacion').val();
            var carrera=$('#carrera').val();
            var edad=$('#edad').val();
            var intereses=$('#intereses').val();
            var habilidades=$('#habilidades').val();
            var autodescripcion=$('#autodescripcion').val();
            var meta_vida=$('#meta_vida').val();
            var telefono=$('#telefono').val();
            var facebook=$('#facebook').val();


        $.ajax({
            url:'../../Controllers/perfil.php',
            type:'POST',
            data:'nombre='+nombre+ '&sexo='+sexo+ '&ocupacion='+ocupacion+ '&espec_ocupacion='+espec_ocupacion+ '&carrera='+carrera+ '&edad='+edad+ '&intereses='+intereses+ '&habilidades='+habilidades+ '&autodescripcion='+autodescripcion+ '&meta_vida='+meta_vida+ '&telefono='+telefono+ '&facebook='+facebook+'&boton=editar'
        }).done(function(respuesta){
            if (respuesta=='exito') {
                // $('#exito').show();

            }
            else{
                alert(respuesta);
            }
            
        })  .always(function(data) {

    location.reload();
  });
}

function modificar(){
    //$('#responsive')[0].reset();
   
    var url = '../../Controllers/perfil.php';
        $.ajax({
        type:'POST',
        url:url,
        data:'boton=modificar',
        success: function(valores){

                var datos = JSON.parse(valores);

                $('#nombre').val(datos[1]);
                $('#sexo').val(datos[3]);
                $('#ocupacion').val(datos[6]);
                $('#espec_ocupacion').val(datos[7]);
                $('#carrera').val(datos[8]);
                $('#edad').val(datos[9]);
                $('#intereses').val(datos[10]);
                $('#habilidades').val(datos[11]);
                $('#autodescripcion').val(datos[12]);
                $('#meta_vida').val(datos[13]);
                $('#telefono').val(datos[14]);
                $('#facebook').val(datos[15]);

                
            return false;

        }
    });
    return false;
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
    
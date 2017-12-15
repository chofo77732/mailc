$(document).ready(function(){
    cargarItems();
    cargarItems2();
    cargarItems3();
    cargarItems4();
  });
function cargarItems(){
  	$.get("http://localhost/UPREM/controllers/plantillaTiposYasocController.php","",function(data,status)
  	{
		var p=JSON.parse(data);
		var datoshtml="";
		for(i=0;i<p.actividades.length;i++){
			datoshtml="<tr>";
			datoshtml+="<td>"+p.actividades[i].id_ATA+"</td>";
			datoshtml+="<td>"+p.actividades[i].tipo_atributo+"</td>";
			datoshtml+="<td>"+p.actividades[i].descripcion+"</td>";
			datoshtml+="<td>"+p.actividades[i].tipo_ocl+"</td>";
			datoshtml+="<td>"+p.actividades[i].valor_inicial+"</td>";
			datoshtml+="<td>"+p.actividades[i].expresion+"</td>";
			datoshtml+="<td>"+p.actividades[i].comentarios+"</td>";
			datoshtml+="<td>"+p.actividades[i].id_proyecto+"</td>";
			datoshtml+="<td><a onclick='GetPlantillaDetails("+p.actividades[i].id_ATA+")' class='modal-action waves-effect waves-green btn-flat' style='background-color:  #4da6ff'><i class='material-icons right'>edit</i></a></td>";			
			datoshtml+="<td><button onclick='remueveItem("+p.actividades[i].id_ATA+")' class='btn waves-effect waves-light' type='button'><i class='material-icons right'>delete_forever</i></button>";
			datoshtml+="</tr>";
			$("#tablaAtributos").append(datoshtml); 
		}
	});
}

function GetPlantillaDetails(id_ATA) {
    // Add User ID to the hidden field for furture usage
    $("#UpidATA").val(id_ATA);
    $.post("http://localhost/UPREM/controllers/readPlantillaDetails.php", {
            id_ATA: id_ATA
        },
        function (data, status) {
            // PARSE json data
            var actividades = JSON.parse(data);
            // Assing existing values to the modal popup fields
            $("#UpTipoAtrib").val(actividades.tipo_atributo);
            $("#UpdescripcionAtrib").val(actividades.descripcion);
            $("#UpTOAtrib").val(actividades.tipo_ocl);
            $("#UpVIAtrib").val(actividades.valor_inicial);
            $("#UpXPAtrib").val(actividades.expresion);
            $("#UpcometariosAtrib").val(actividades.comentarios);
            $("#Upid_proyectoAtrib").val(actividades.id_proyecto);
        }
    );
    // Open modal popup
    $('#modalUpdateAtrib').modal('open');
}

function agregaPlantilla(){
	var tipo_atributo=$("#TipoAtrib").val();
	var descripcion=$("#descripcionAtrib").val();
	var tipo_ocl=$("#TOAtrib").val();
	var valor_inicial=$("#VIAtrib").val();
	var expresion=$("#XPAtrib").val();
	var comentarios=$("#cometariosAtrib").val();
	var id_proyecto=$("#id_proyectoAtrib").val();

	var actividad={      //La variable actor contiene los datos del json
				tipo_atributo:tipo_atributo,
				descripcion:descripcion,
				tipo_ocl:tipo_ocl,
				valor_inicial:valor_inicial,
				expresion:expresion,
				comentarios:comentarios,
				id_proyecto:id_proyecto
			};
			
	$.ajax({
		type: "POST",
		url: "http://localhost/UPREM/controllers/plantillaTiposYasocController.php",
		data: JSON.stringify(actividad), //hacer la conversion a JSON para poder consumir el JSON
		dataType: "json",
		success: function(data,status){
			alert(data.mensaje);
			cargarItems();
		}
	});
	$('#modal1').modal('close');
}

function remueveItem(itemid){
  	$.get("http://localhost/UPREM/controllers/plantillaTiposYasocController2.php?id_ATA="+itemid,function(data,status){
  	var mensaje=JSON.parse(data);
	alert(mensaje.mensaje);
	cargarItems();
  	});

}

function modificarPlatilla(){
	var tipo_atributo=$("#UpTipoAtrib").val();
	var descripcion=$("#UpdescripcionAtrib").val();
	var tipo_ocl=$("#UpTOAtrib").val();
	var valor_inicial=$("#UpVIAtrib").val();
	var expresion=$("#UpXPAtrib").val();
	var comentarios=$("#UpcometariosAtrib").val();
	var id_proyecto$=$("#Upid_proyectoAtrib").val();
	var id_ATA=$("#UpidATA").val();

	var actividad={      //La variable actor contiene los datos del json
				tipo_atributo:tipo_atributo,
				descripcion:descripcion,
				tipo_ocl:tipo_ocl,
				valor_inicial:valor_inicial,
				expresion:expresion,
				comentarios:comentarios,
				id_proyecto:id_proyecto,
				id_ATA:id_ATA
			};
			
	$.ajax({
		type: "POST",
		url: "http://localhost/UPREM/controllers/plantillaTiposYasocController2.php",
		data: JSON.stringify(actividad), //hacer la conversion a JSON para poder consumir el JSON
		dataType: "json",
		success: function(data,status){
			alert(data.mensaje);
			cargarItems();
		}
	});
	//$('#modal2').modal('close');
}
/*------------------------------------------------------------------------------------------------------------------------------------------*/
function cargarItems2(){
  	$.get("http://localhost/UPREM/controllers/plantillaEnlaceTiposYasocController.php","",function(data,status)
  	{
		var p=JSON.parse(data);
		var datoshtml="";
		for(i=0;i<p.actividades.length;i++){
			datoshtml="<tr>";
			datoshtml+="<td>"+p.actividades[i].id_ETA+"</td>";
			datoshtml+="<td>"+p.actividades[i].nombre+"</td>";
			datoshtml+="<td>"+p.actividades[i].tipo_enlace+"</td>";
			datoshtml+="<td>"+p.actividades[i].descripcion+"</td>";
			datoshtml+="<td>"+p.actividades[i].tipo_ocl+"</td>";
			datoshtml+="<td>"+p.actividades[i].asosioacion+"</td>";
			datoshtml+="<td>"+p.actividades[i].valor_inicial+"</td>";
			datoshtml+="<td>"+p.actividades[i].expresion+"</td>";
			datoshtml+="<td>"+p.actividades[i].comentarios+"</td>";
			datoshtml+="<td>"+p.actividades[i].id_proyecto+"</td>";
			datoshtml+="<td><a onclick='GetPlantillaEnlaceDetails("+p.actividades[i].id_ETA+")' class='modal-action waves-effect waves-green btn-flat' style='background-color:  #4da6ff'><i class='material-icons right'>edit</i></a></td>";			
			datoshtml+="<td><button onclick='remueveItem1("+p.actividades[i].id_ETA+")' class='btn waves-effect waves-light' type='button'><i class='material-icons right'>delete_forever</i></button>";
			datoshtml+="</tr>";
			$("#tablaEnlace").append(datoshtml); 
		}
	});
}

function GetPlantillaEnlaceDetails(id_ETA) {
    // Add User ID to the hidden field for furture usage
    $("#UpidETA").val(id_ETA);
    $.post("http://localhost/UPREM/controllers/readPlantillaEnlaceDetails.php", {
            id_ETA: id_ETA
        },
        function (data, status) {
            // PARSE json data
            var plantillaenlace = JSON.parse(data);
            // Assing existing values to the modal popup fields
            $("#UpNom").val(plantillaenlace.nombre);
            $("#UpTE1").val(plantillaenlace.tipo_enlace);
            $("#Updescripcion1").val(plantillaenlace.descripcion);
            $("#UpTO1").val(plantillaenlace.tipo_ocl);
            $("#UpAsoc").val(plantillaenlace.asosioacion);
            $("#UpValIni").val(plantillaenlace.valor_inicial);
            $("#UpExpre").val(plantillaenlace.expresion);
            $("#Upcomentario1").val(plantillaenlace.comentarios);
            $("#Upid_proyectoEnlace").val(plantillaenlace.id_proyecto);
        }
    );
    // Open modal popup
    $('#modalUpdateEnlace').modal('open');
}

function agregaPlantilla1(){
	var nombre=$("#Nom").val();
	var tipo_enlace=$("#TE1").val();
	var descripcion=$("#descripcion1").val();
	var tipo_ocl=$("#TO1").val();
	var asosioacion=$("#Asoc").val();
	var valor_inicial=$("#ValIni").val();
	var expresion=$("#Expre").val();
	var comentarios=$("#comentario1").val();
	var id_proyecto=$("#id_proyectoEnlace").val();

	var actividad={      //La variable actor contiene los datos del json
				nombre:nombre,
				tipo_enlace:tipo_enlace,
				descripcion:descripcion,
				tipo_ocl:tipo_ocl,
				asosioacion:asosioacion,
				valor_inicial:valor_inicial,
				expresion:expresion,
				comentarios:comentarios,
				id_proyecto:id_proyecto
			};
			
	$.ajax({
		type: "POST",
		url: "http://localhost/UPREM/controllers/plantillaEnlaceTiposYasocController.php",
		data: JSON.stringify(actividad), //hacer la conversion a JSON para poder consumir el JSON
		dataType: "json",
		success: function(data,status){
			alert(data.mensaje);
			cargarItems();
		}
	});
	$('#modal1').modal('close');
}

function remueveItem1(itemid){
  	$.get("http://localhost/UPREM/controllers/plantillaEnlaceTiposYasocController2.php?id="+itemid,function(data,status){
  	var mensaje=JSON.parse(data);
	alert(mensaje.mensaje);
	cargarItems();
  	});

}

function modificarPlatilla1(){
	var nombre=$("#UpNom").val();
	var tipo_enlace=$("#UpTE1").val();
	var descripcion=$("#Updescripcion1").val();
	var tipo_ocl=$("#UpTO1").val();
	var asociacion=$("#UpAsoc").val();
	var valor_inicial=$("#UpValIni").val();
	var expresion=$("#UpExpre").val();
	var comentarios=$("#Upcomentario1").val();
	var id_proyecto$=$("#Upid_proyectoAtrib").val();
	var id_ETA=$("#UpidETA").val();

	var actividad={      //La variable actor contiene los datos del json
				nombre:nombre,
				tipo_enlace:tipo_enlace,
				descripcion:descripcion,
				tipo_ocl:tipo_ocl,
				asociacion:asociacion,
				valor_inicial:valor_inicial,
				expresion:expresion,
				comentarios:comentarios,
				id_proyecto:id_proyecto,
				id_ETA:id_ETA
			};
			
	$.ajax({
		type: "POST",
		url: "http://localhost/UPREM/controllers/plantillaEnlaceTiposYasocController2.php",
		data: JSON.stringify(actividad), //hacer la conversion a JSON para poder consumir el JSON
		dataType: "json",
		success: function(data,status){
			alert(data.mensaje);
			cargarItems();
		}
	});
	///$('#modal2').modal('close');
}
/*------------------------------------------------------------------------------------------------------------------------------------------*/
function cargarItems3(){
  	$.get("http://localhost/UPREM/controllers/plantillaInvarianteController.php","",function(data,status)
  	{
		var p=JSON.parse(data);
		var datoshtml="";
		for(i=0;i<p.actividades.length;i++){
			datoshtml="<tr>";
			datoshtml+="<td>"+p.actividades[i].id_ITA+"</td>";
			datoshtml+="<td>"+p.actividades[i].nombre+"</td>";
			datoshtml+="<td>"+p.actividades[i].descripcion+"</td>";
			datoshtml+="<td>"+p.actividades[i].expresion+"</td>";
			datoshtml+="<td>"+p.actividades[i].comentarios+"</td>";
			datoshtml+="<td>"+p.actividades[i].id_proyecto+"</td>";
			datoshtml+="<td><a onclick='GetPlantillaInvarianteDetails("+p.actividades[i].id_ITA+")' class='modal-action waves-effect waves-green btn-flat' style='background-color:  #4da6ff'><i class='material-icons right'>edit</i></a></td>";			
			datoshtml+="<td><button onclick='remueveItem2("+p.actividades[i].id_ITA+")' class='btn waves-effect waves-light' type='button'><i class='material-icons right'>delete_forever</i></button>";
			datoshtml+="</tr>";
			$("#tablaInvariante").append(datoshtml); 
		}
	});
}

function GetPlantillaInvarianteDetails(id_ITA) {
    // Add User ID to the hidden field for furture usage
    $("#UpidITA").val(id_ITA);
    $.post("http://localhost/UPREM/controllers/readInvarianteDetails.php", {
            id_ITA: id_ITA
        },
        function (data, status) {
            // PARSE json data
            var plantillaenlace = JSON.parse(data);
            // Assing existing values to the modal popup fields
            $("#UpNomI").val(plantillaenlace.nombre);
            $("#UpdescripcionInv").val(plantillaenlace.descripcion);
            $("#UpExpreInv").val(plantillaenlace.expresion);
            $("#UpcomentarioInv").val(plantillaenlace.comentarios);
            $("#Upid_proyectoInvar").val(plantillaenlace.id_proyecto);
        }
    );
    // Open modal popup
    $('#modalUpdateInvariante').modal('open');
}

function agregaPlantilla2(){
	var nombre=$("#NomI").val();
	var descripcion=$("#descripcionInv").val();
	var expresion=$("#ExpreInv").val();
	var comentarios=$("#comentarioInv").val();
	var id_proyecto=$("#id_proyectoInvar").val();
	var plantillaenlace={      //La variable actor contiene los datos del json
				nombre:nombre,
				descripcion:descripcion,
				expresion:expresion,
				comentarios:comentarios,
				id_proyecto:id_proyecto
			};
			
	$.ajax({
		type: "POST",
		url: "http://localhost/UPREM/controllers/plantillaInvarianteController.php",
		data: JSON.stringify(plantillaenlace), //hacer la conversion a JSON para poder consumir el JSON
		dataType: "json",
		success: function(data,status){
			alert(data.mensaje);
			cargarItems();
		}
	});
	$('#modal1').modal('close');
}

function remueveItem2(itemid){
  	$.get("http://localhost/UPREM/controllers/plantillaInvarianteController2.php?id_ITA="+itemid,function(data,status){
  	var mensaje=JSON.parse(data);
	alert(mensaje.mensaje);
	cargarItems();
  	});

}

function modificarPlatilla2(){
	var nombre=$("#UpNomI").val();
	var descripcion=$("#UpdescripcionInv").val();
	var expresion=$("#UpExpreInv").val();
	var comentarios=$("#UpcomentarioInv").val();
	var id_proyecto=$("#Upid_proyectoInvar").val();
	var id_ITA=$("#UpidITA").val();

	var plantillaenlace={      //La variable actor contiene los datos del json
				nombre:nombre,
				descripcion:descripcion,
				expresion:expresion,
				comentarios:comentarios,
				id_proyecto:id_proyecto,
				id_ITA:id_ITA
			};
			
	$.ajax({
		type: "POST",
		url: "http://localhost/UPREM/controllers/plantillaInvarianteController2.php",
		data: JSON.stringify(plantillaenlace), //hacer la conversion a JSON para poder consumir el JSON
		dataType: "json",
		success: function(data,status){
			alert(data.mensaje);
			cargarItems();
		}
	});
	//$('#modal2').modal('close');
}
/*------------------------------------------------------------------------------------------------------------------------------------------*/
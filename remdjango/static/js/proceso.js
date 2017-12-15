$(document).ready(function(){
    cargar1();
    cargar2();
    cargar3();
  });
function cargar1(){
	  $.get("descripcion_asociacion/control_asoc.php","",function(data,status){


	  	//alert(data);
		  var p=JSON.parse(data);
		//$("#tablafilm").html("");
		  var datoshtml="";
		  for(i=0;i<p.film.length;i++){
			  datoshtml="<tr>"
		  	  datoshtml+="<td>"+p.film[i].id_DesAs+"</td>";
			  datoshtml+="<td>"+p.film[i].tipo_asoc+"</td>";
			  datoshtml+="<td>"+p.film[i].numero_version+"</td>";
			  datoshtml+="<td>"+p.film[i].requisitos+"</td>";
			  datoshtml+="<td>"+p.film[i].descripcion+"</td>";
			  datoshtml+="<td>"+p.film[i].comentarios+"</td>";

			  datoshtml+="<td><button onclick='llenarItem1("+p.film[i].id_DesAs+")'  type='button'><i>Editar</i></button>";
			  datoshtml+="<td><button onclick='remueveItem1("+p.film[i].id_DesAs+")' type='button'><i>Eliminar</i></button>";
			  datoshtml+="</tr>";
			  $("#tbl_des").append(datoshtml); 
		  }
		  
	  });
  }
  
  function remueveItem1(itemid){
	  //alert(itemid);
	  $.get("descripcion_asociacion/control_eliminar_asoc.php?id="+itemid,function(data,status){
		  var mensaje=JSON.parse(data);
		  $('#alta_descr1').modal('close');
		  
		  $('#descrip1').modal('close');
		  //cargar1();
		 // alert(mensaje.mensaje);
	  });
  }
  
  
  function llenarItem1(id){
	  
	  $.get("descripcion_asociacion/control_getbyid.php?id="+id,function(data,status){
		  //alert(data);
		  var p=JSON.parse(data);
		  $("#a1").val(p.film.tipo_asoc);
	  	  $("#a2").val(p.film.numero_version);
	  	  $("#a3").val(p.film.requisitos);
	  	  $("#a4").val(p.film.descripcion);
	  	  $("#a5").val(p.film.comentarios);
	  	  $("#a6").val(p.film.id_DesAs);
		  //cargarItems();
		  
	  });
	  
	  $('#alta_descr1').modal('open');		  
  }

function actualizarItem1(){

  	  var v1=$("#a1").val();
	  var v2=$("#a2").val();
	  var v3=$("#a3").val();
	  var v4=$("#a4").val();
	  var v5=$("#a5").val();
	  var v6=$("#a6").val();

	  
	  var film={ 
		 	"t1": v1,
			"t2": v2,
			"t3": v3,
			"t4": v4,
			"t5": v5,
			"t6": v6
		};	

		$.ajax({
		  	type: "POST",
				url: "descripcion_asociacion/control_update.php",
				data: JSON.stringify(film), //hacer la conversion a JSON para poder consumir el JSON
		  	dataType: "json",
				success: function(data,status){
		  		alert(data.mensaje);
	  		}
	  	});	
	
	  
	  $('#alta_descr1').modal('close');
	  $('#descrip1').modal('close');
}


// ************SECUENCIA *********************

function cargar2(){
	  $.get("diagrama_secuencia/control_secu.php","",function(data,status){


	  	//alert(data);
		var p=JSON.parse(data);
		  
		//$("#tablafilm").html("");
		  var datoshtml="";
		  for(i=0;i<p.film.length;i++){
			  datoshtml="<tr>"
		  	  datoshtml+="<td>"+p.film[i].id_DS+"</td>";
			  datoshtml+="<td>"+p.film[i].descripcion+"</td>";

			  datoshtml+="<td><button onclick='llenarItem2("+p.film[i].id_DS+")'  type='button'><i>Editar</i></button>";
			  datoshtml+="<td><button onclick='remueveItem2("+p.film[i].id_DS+")' type='button'><i>Eliminar</i></button>";
			  datoshtml+="</tr>";
			  $("#tbl_di_tipo").append(datoshtml); 
		  }
		  
	  });
  }
  
  function remueveItem2(itemid){
	  //alert(itemid);
	  $.get("diagrama_secuencia/control_eliminar_secu.php?id="+itemid,function(data,status){
		  var mensaje=JSON.parse(data);
		  //cargar1();
		 // alert(mensaje.mensaje);
	  });
  }
  
  
  function llenarItem2(id){
	  
	  $.get("diagrama_secuencia/control_getbyid.php?id="+id,function(data,status){
		  //alert(data);
		  var p=JSON.parse(data);
		  $("#dgr_desc").val(p.film.descripcion);
	  	  $("#dgrid").val(p.id_DS);
		  //cargarItems();
		  
	  });
	  
	  $('#actualizar_diag').modal('open');		  
  }

function actualizarItem2(){

  	  var v1=$("#dgr_desc").val();
	  var v2=$("#dgrid").val();

	  
	  var film={ 
		 	"t1": v1,
			"t2": v2
		};	

		$.ajax({
		  	type: "POST",
				url: "diagrama_secuencia/control_update.php",
				data: JSON.stringify(film), //hacer la conversion a JSON para poder consumir el JSON
		  	dataType: "json",
				success: function(data,status){
		  		alert(data.mensaje);
	  		}
	  	});	
	
	  
	  $('#actualizar_diag').modal('close');
	  $('#secu1').modal('close');

}


// ---------------ROL----------------------

function cargar3(){
	  $.get("roles_asociacion/control_rol.php","",function(data,status){


	  	//alert(data);
		  var p=JSON.parse(data);
		//$("#tablafilm").html("");
		  var datoshtml="";
		  for(i=0;i<p.film.length;i++){
			  datoshtml="<tr>"
		  	  datoshtml+="<td>"+p.film[i].id_RA+"</td>";
			  datoshtml+="<td>"+p.film[i].descripcion+"</td>";
			  datoshtml+="<td>"+p.film[i].tipo_ocl+"</td>";
			  datoshtml+="<td>"+p.film[i].multiplicidad+"</td>";
			  datoshtml+="<td>"+p.film[i].comentarios+"</td>";

			  datoshtml+="<td><button onclick='llenarItem3("+p.film[i].id_RA+")'  type='button'><i>Editar</i></button>";
			  datoshtml+="<td><button onclick='remueveItem3("+p.film[i].id_RA+")' type='button'><i>Eliminar</i></button>";
			  datoshtml+="</tr>";
			  $("#tbl_rol").append(datoshtml); 
		  }
		  
	  });
  }
  
  function remueveItem3(itemid){
	  //alert(itemid);
	  $.get("roles_asociacion/control_eliminar_rol.php?id="+itemid,function(data,status){
		  var mensaje=JSON.parse(data);
		  $('#rol1').modal('close');
		  
		  //cargar1();
		 // alert(mensaje.mensaje);
	  });
  }
  
  
  function llenarItem3(id){
	  
	  $.get("roles_asociacion/control_getbyid.php?id="+id,function(data,status){
		  //alert(data);
		  var p=JSON.parse(data);
		  $("#r1").val(p.film.descripcion);
	  	  $("#r2").val(p.film.tipo_ocl);
	  	  $("#r3").val(p.film.multiplicidad);
	  	  $("#r4").val(p.film.comentarios);
	  	  $("#r5").val(p.film.id_RA);
	  	  
		  //cargarItems();
		  
	  });
	  
	  $('#modal_rol_asoc').modal('open');		  
  }

function actualizarItem3(){

  	  var v1=$("#r1").val();
	  var v2=$("#r2").val();
	  var v3=$("#r3").val();
	  var v4=$("#r4").val();
	  var v5=$("#r5").val();

	  
	  var film={ 
		 	"t1": v1,
			"t2": v2,
			"t3": v3,
			"t4": v4,
			"t5": v5
		};	

		$.ajax({
		  	type: "POST",
				url: "roles_asociacion/control_update.php",
				data: JSON.stringify(film), //hacer la conversion a JSON para poder consumir el JSON
		  	dataType: "json",
				success: function(data,status){
		  		alert(data.mensaje);
	  		}
	  	});	
	
	  
	  $('#modal_rol_asoc').modal('close');
	  $('#rol1').modal('close');
}


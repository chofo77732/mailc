    <nav class="navbar navbar-default navbar-fixed-top" >
        <div class="navbar-header">
            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-ex1-collapse">
                <span class="sr-only">Cambiar Navegacion</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a href="#" class="navbar-brand">MALIC</a>
        </div>

        <div class="collapse navbar-collapse navbar-ex1-collapse">

                  <ul class="nav navbar-nav navbar-right">
        <li><a href="principal.php">HOME</a></li>

        <li><a href="javascript: void(0)" class="dropdown-toggle" data-toggle="dropdown">Quienes Somos<span class="caret"></span></a>
        
        <ul class="dropdown-menu">
        <li><a href="mision.php">Misión</a></li>
        <li><a href="vision.php">Visión</a></li>
        </ul>
        </li>
        
        <li class="dropdown">
          <a class="dropdown-toggle" data-toggle="dropdown" href="#">Más
          <span class="caret"></span></a>
          <ul class="dropdown-menu">
            <li><a href="mas/colaborar.php">Como colaborar</a></li>
            <li><a href="mas/contacto.php">Contactos</a></li>
            <li><a href="mas/publicidad.php">Publicidad</a></li> 
          </ul>
        </li>

            <!-- Buscar -->
 <!--        <li class="nav-item">
            <form class="form-inline">
              <div class="input-group">
                <input type="text" class="form-control" placeholder="Search for...">
                <span class="input-group-btn">
                  <button class="btn btn-default" type="button">
                    <span class="glyphicon glyphicon-search"></span>
                  </button>
                </span>
              </div>
            </form>
          </li> -->
      
                <li><a href="javascript: void(0)" class="dropdown-toggle" data-toggle="dropdown"><?php echo $_SESSION['nombre']; ?><span class="caret"></span></a>
                     <ul class="dropdown-menu">
                        <li><a href="perfil/">Mi Perfil</a></li>
                        <li><a href="proyectos/">Mis Proyectos</a></li> 
                        <li><a href="grupos/">Mis Grupos</a></li>
                        <li>
                        <!-- <a href="javascript: void(0)" onclick='cerrar();'>Cerrar Session</a> -->
                        <a href="javascript: void(0)" onclick=" location.href='logout.php' ">Cerrar Session</a>

                        </li>
                     
                    </ul>
                </li>
                
            </ul>
        </div>
    </nav>
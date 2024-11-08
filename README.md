# Mascotas Felices

Sistema para controlar y registrar los datos generales de los clientes y sus mascotas en la clínica veterinaria "Mascotas Felices".

Guía para iniciar el Proyecto

1.Instalar Python: Asegúrate de tener Python 3.11 o superior instalado en tu sistema. Puedes verificarlo con:
python3 --version

Si no lo tienes, descárgalo de Python.org.

2.Instalar Git: Asegúrate de tener Git instalado para clonar el repositorio. Verifica con:
git --version
Si no está instalado, descárgalo de git-scm.com.


3.Clonar el Repositorio o descargarlo en caso de la ultima opcion Abre una terminal y ejecuta:
git clone git@github.com:JeskHD/MascotasFelices.git
Esto descargará el proyecto en tu máquina.

4.Entrar al Directorio del Proyecto Cambia al directorio del proyecto clonado:
cd MascotasFelices

en caso de que se te dificulte la busqueda abres el folder y en el propio buscador de donde abriste el archivo te sale la direccion concreta
copias esa direccion y la pones despues del cd, ejemplo:

cd /Desktop/MascotasFelices

El orden es asi:
1.Abrir el folder
2.Copiar direccion en la que te encuentras mirando el folder
3.Pegar la direccion despues de cd en el terminal

5.Crear un Entorno Virtual 
Es recomendable crear un entorno virtual para instalar las dependencias sin afectar otros proyectos en tu sistema:

Crear el entorno virtual:
python3 -m venv env

Activar el Entorno Virtual:

En macOS/Linux:
source env/bin/activate

En Windows:
.\env\Scripts\activate

Esto instalará Django y cualquier otra dependencia necesaria para ejecutar el proyecto.

Configurar la Base de Datos para aplicar las migraciones para configurar la base de datos:
python manage.py migrate

Crear un Usuario Administrador (Opcional) 

Si deseas acceder a la interfaz de administración, crea un usuario administrador:

python manage.py createsuperuser

Sigue las instrucciones para crear el usuario.

Ejecutar el Servidor de Desarrollo Inicia el servidor local de Django:

python manage.py runserver
Esto te permitirá ver el proyecto en tu navegador en http://127.0.0.1:8000.

Ver el Proyecto en el Navegador
Abre un navegador y visita http://127.0.0.1:8000 para ver la página principal del proyecto.


#Flujo del proyecto:

Una vez dentro aparecera lo que es una interfaz mockup de centro de veterinaria con una interfaz simple, los unicos enlaces que
funcionan son 

Inicio y Ir a Portal

Ir a portal llevara a una sesion de login con usuario y contraseña

solo puse 2 usuarios que en este caso son:

   usuario | contraseña
   daniel    12345
   kali      umpalumpa28

   cualquier otro intento llevaria a la pagina mandando error, o dando error de CSRF

En cualquier caso en caso de que no quieran intentar el login simplemente ponen /dashboard/ al lado de la ip para acceder a la otra pagina ahi donde esta el sistema.
## Instalación

1. **Para Clonar el repositorio**:

   ```bash
   git clone https://github.com/tu_usuario/mascotas-felices.git

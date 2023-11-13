# Registro de Estudiantes (Python Sockets)

- Este proyecto consiste en un sistema cliente-servidor para el registro de datos de estudiantes. Los datos de los estudiantes se pueden enviar al servidor a través de un **socket TCP** o guardarlos localmente en un archivo CSV. Tambien cuenta con visualización de gráficos basados en los datos recopilados.

## Archivos
- **ingresos_estudiantes.py** : Este archivo contiene el código del cliente encargado de recopilar información sobre los estudiantes, validarla y enviarla al servidor a través de un socket TCP.
  
- **servidor.py** : Este archivo implementa el servidor que recibe los datos de los estudiantes a través de un socket TCP y los almacena en un archivo CSV.

- **graficos.py** : Este archivo se encarga de generar gráficos o visualizaciones basadas en los datos recopilados. Puede incluir funciones para crear representaciones visuales de estadísticas o rendimiento académico.

## Tecnologías Utilizadas
- **Python** : Lenguaje de programación utilizado para implementar el proyecto.
- **Socket** : Para la comunicación entre el cliente y el servidor.
- **Matplotlib** : Biblioteca de visualización para generar gráficos.

## Versiones
- **Python** : Se recomienda utilizar Python 3.x
- **Matplotlib** : Puede requerir la instalación de Matplotlib. Utiliza el siguiente comando
  
    ```bash
      pip install matplotlib

## Instalación
- **Clona o descarga el repositorio** :

     ```bash
      git clone https://github.com/tu_usuario/tu_proyecto.git
     
- **Accede al directorio del proyecto** :

     ```bash
      cd tu_proyecto
## Uso
- **Ejecuta el servidor en un terminal** :
  
    ```bash
    python servidor.py

- **En otro terminal, ejecuta el cliente para ingresar datos de estudiantes** :

    ```bash
    python ingresos_estudiantes.py

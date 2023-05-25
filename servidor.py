import socket
import csv

def guardar_datos_csv(nombre, notas):
    # Abre el archivo CSV en modo de escritura.
    with open('datos_estudiantes.csv', 'a', newline='') as file:
        writer = csv.writer(file)

        # Escribe una nueva fila con los datos del estudiante.
        writer.writerow([nombre] + notas)

def recibir_datos():
    # Crea un socket TCP IPv4 para establecer una conexión de red.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Vincula el socket a una dirección IP y un puerto específicos para que el servidor pueda escuchar conexiones entrantes.
    server_address = ('localhost', 12345)
    sock.bind(server_address)

    # Escucha conexiones entrantes.
    sock.listen(1)

    estudiantes_recibidos = 0  # Contador de estudiantes recibidos

    while estudiantes_recibidos < 10:
        print("Esperando estudiantes para recibir datos...")

        # Acepta una conexión entrante
        connection, client_address = sock.accept()

        try:
            print("Conexión establecida desde ->", client_address)

            # Recibe los datos del estudiante
            datos = connection.recv(1024).decode()
            nombre, *notas = datos.split('_')

            print("Nombre del estudiante:", nombre)
            print("Notas:", " ".join(notas))

            # Guarda los datos en el archivo CSV
            guardar_datos_csv(nombre, notas)

            # Incrementa el contador de estudiantes recibidos
            estudiantes_recibidos += 1

        finally:
            # Cierra la conexión
            connection.close()

    # Cierra el socket del servidor después de recibir 10 estudiantes
    sock.close()

# Inicia el servidor para recibir datos
recibir_datos()

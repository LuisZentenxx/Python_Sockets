import socket

def enviar_datos(nombre, notas):
    # Crea un socket (AF_INET = IP , SOCK_STREAM = TCP)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conecta el socket al servidor en el puerto deseado
    server_address = ('localhost', 12345)
    sock.connect(server_address)

    try:
        # Concatena los datos en un solo string (Trama nombre_n1_n2_n3_n4_n5_n6)
        datos = nombre + "_" + "_".join(str(nota) for nota in notas)

        # Envia los datos al servidor (encode = codifica el string a UTF-8)
        sock.sendall(datos.encode())

    finally:
        # Cierra la conexión
        sock.close()

# Solicita al usuario la cantidad de estudiantes a ingresar
cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes -> "))

estudiantes = {}  # Diccionario para almacenar los nombres de estudiantes ingresados
contador = 1  # Contador incremental

print("\nINGRESO DE DATOS DEL ESTUDIANTE")
print("================================================")
for _ in range(cantidad_estudiantes):
    # Solicitar al usuario el nombre del estudiante
    nombre = input(f"Ingrese el nombre del estudiante {contador} -> ")

    # Valida si el nombre ha sido registrado previamente
    while nombre in estudiantes:
        print("\nEl nombre ya ha sido registrado previamente. Por favor, ingrese otro nombre.")
        nombre = input(f"Ingrese el nombre del estudiante {contador} -> ")

    # Agrega el nombre al diccionario de estudiantes
    estudiantes[nombre] = True

    # Solicita al usuario las 5 notas del estudiante
    notas = []
    for i in range(5):
        nota = float(input(f"Ingrese la nota {i+1} -> "))

        # Valida si la nota está dentro del rango determinado
        while nota < 1.0 or nota > 7.0:
            print("\nLa nota debe estar entre 1.0 y 7.0. Por favor, ingrese otra nota.")
            nota = float(input(f"Ingrese la nota {i+1} -> "))

        notas.append(nota)

    # Enviar los datos al servidor
    enviar_datos(nombre, notas)

    contador += 1

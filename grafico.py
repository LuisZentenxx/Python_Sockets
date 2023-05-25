import csv
import matplotlib.pyplot as plt

def mostrar_grafico_notas(nombre):
    #Esto lee los datos del archivo .csv
    with open('datos_estudiantes.csv', 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Leer los encabezados del archivo
        notas = []

        # Buscar el estudiante por nombre
        for row in reader:
            if row[0].strip() == nombre.strip():
                # Obtener las notas del estudiante
                notas = [float(nota) for nota in row[1:6]]
                break

        if notas:
            # Generar el gráfico de evolución de notas
            plt.plot(range(1, 6), notas)
            plt.xlabel('Evaluación')
            plt.ylabel('Nota')
            plt.title('Evolución de notas de ' + nombre)
            plt.show()
        else:
            print("No se encontraron datos para el estudiante:", nombre)

# Solicitar al usuario el nombre del estudiante
nombre_estudiante = input("Ingrese el nombre del estudiante registrado: ")

# Mostrar el gráfico de evolución de notas
mostrar_grafico_notas(nombre_estudiante)

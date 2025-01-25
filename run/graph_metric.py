import matplotlib.pyplot as plt
means = []
with open("TIME_200_complete_route_2_a_6_ports.txt", "r") as archivo:
    for linea in archivo:
        tiempos = linea.split(",")
        tiempos = [int(tiempo) for tiempo in tiempos]
        mean =  sum(tiempos) / len(tiempos)
        means.append(mean)


print(means)


# Crear valores para el eje x (comenzando en 2 y avanzando)
x = range(2, 2 + len(means))

# Graficar
plt.plot(x, means, marker='o', linestyle='-', color='black', label='Valores')

plt.yscale('log')
# Etiquetas y título
plt.xlabel('Número de puertos')
plt.ylabel('Tiempo Promedio Termino itinerario barcos')
plt.title('Metrica tiempo itinerarios promedio')
plt.legend()

# Mostrar la gráfica
plt.grid(True)  # Agregar una cuadrícula opcional
plt.savefig("Metrica-Itinerario.png")

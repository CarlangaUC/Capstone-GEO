import matplotlib.pyplot as plt

with open("TIME_200_complete_route_2_a_6_ports.txt", "r") as archivo:
    times = [float(linea.strip()) for linea in archivo]

# Crear valores para el eje x (comenzando en 2 y avanzando)
x = range(2, 2 + len(times))

# Graficar
plt.plot(x, times, marker='o', linestyle='-', color='black', label='Valores')

# Etiquetas y título
plt.xlabel('Número de puertos')
plt.ylabel('Tiempo Simulación')
plt.title('Metrica tiempo simulación')
plt.legend()

# Mostrar la gráfica
plt.grid(True)  # Agregar una cuadrícula opcional
plt.savefig("Metrica-Tiempo-Sim.png")

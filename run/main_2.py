from clases.manager import Manager


manager = Manager()



# Considerando largo itinerario maximo 3

# Las rutas fueron acortadas por unf actor de 1000


############### Input automatico ###########

n_ports = 2

t_simulacion = 200

times = []
# Consideramos un tiempo t_sim de 200 inicial incrementandolo en 200 x numero ports
for port in range(2, 200):
    manager.add(n_ports=n_ports)
    print(port)
    manager.processes()
    manager.step_run(t_simulacion, sleep_time=0)
    time = manager.elapsed_time()
    times.append(time)
    t_simulacion += 200

with open("TIME_200_complete_route_2_a_6_ports.txt", "w") as archivo:
    for time in times:
        print(time, file=archivo)

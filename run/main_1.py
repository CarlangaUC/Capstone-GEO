from clases.manager import Manager


manager = Manager()



# Considerando largo itinerario maximo 3

# Las rutas fueron acortadas por unf actor de 1000


############### Input automatico ###########

n_ports = 2

t_simulacion = 200

wait_times = []
times = []
# Consideramos un tiempo t_sim de 200 inicial incrementandolo en 200 x numero ports
for port in range(2, 100):
    manager.add(n_ports=n_ports)
    print(port)
    manager.processes()
    manager.step_run(t_simulacion, sleep_time=0)
    wait_time = manager.calculate_metrics()
    time = manager.elapsed_time()
    wait_times.append(wait_time)
    times.append(time)
    t_simulacion += 200

with open("WAITTIME_200_complete_route_2_a_6_ports.txt", "w") as archivo:
    for wait_time in wait_times:
        # print(wait_time)
        print(",".join(map(str, wait_time)), file=archivo)

with open("TIME_200_complete_route_2_a_6_ports.txt", "w") as archivo:
    for time in times:
        print(time, file=archivo)

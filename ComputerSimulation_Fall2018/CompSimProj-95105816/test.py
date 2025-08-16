import numpy as np
from random import choices
import simpy as sp
import matplotlib.pyplot as plt

#کران بالا و کران پایین بازه را به مقدار یکسان زیاد یا کم می کنیم تا بدون تغییر دادن واریانس، بازه بهینه را بدست بیاوریم
def generate_interarrival():
    return choices(range(1,6),[0.2,0.2,0.2,0.2,0.2])[0]

def generate_service():
    return choices([2, 3, 5, 6, 9], [0.28, 0.19, 0.23, 0.18, 0.12])[0]

def bank_run(env):
    i = 0
    while i < 200:
        i+=1
        yield env.timeout(generate_interarrival())
        env.process(customer(env,i, servers))

wait_time = []
service_time = []
observation_times = []
q_length = []

def customer(inv,i, servers):
    with servers.request() as request:
        t_arrival = env.now
        observation_times.append(env.now)
        q_length.append(len(servers.queue))
        simulation_table.append(str(env.now) + "    Customer " + str(i) + " arrives.")
        observation_times.append(env.now)
        q_length.append(len(servers.queue))
        yield request
        observation_times.append(env.now)
        q_length.append(len(servers.queue))
        simulation_table.append(str(env.now) + "    Customer " + str(i) + "'s service time starts")
        t_startOfService = env.now
        yield env.timeout(generate_service())
        simulation_table.append(str(env.now) + "    Customer " + str(i) + " Departs")
        t_departure = env.now

        wait_time.append(t_startOfService - t_arrival)
        service_time.append(t_departure-t_startOfService)

simulation_table = list()
env = sp.Environment()
servers = sp.Resource(env, capacity = 1)
env.process(bank_run(env))
env.run()

#ذخیره کردن جدول شبیه سازی در فایل
with open('Customer_based Simulation_table.txt', 'w') as f:
    f.write("ID     wait time   service time")
    for i in range(min(len(wait_time), len(service_time))):
        f.write("\n" + str(i + 1) + "       " + str(wait_time[i]) + "           " + str(service_time[i]))


wait_time.sort()
wait_time = list(set([(o, wait_time.count(o)) for o in wait_time]))

Average_Waiting_Time, Average_Queue_Length = 0, 0
Average_Queue_Length = float(sum(float(observation_times[i + 1] - observation_times[i]) * float(q_length[i]) for i in range(len(q_length) - 2)) / float(observation_times[len(observation_times) - 1] - observation_times[0]))
Average_Waiting_Time = float(sum(i[0] * i [1] for i in wait_time)) / float(sum(i[1] for i in wait_time))
print("Average_Queue_Length: ", Average_Queue_Length)
print("Average_Waiting_Time: ", Average_Waiting_Time)






#ذخیره کردن جدول شبیه سازی در فایل
with open('Time_based Simulation_table.txt', 'w') as f:
    for item in simulation_table:
        f.write("%s\n" % item)




#نمودار تعداد افرادی که زمان انتظار آنها t بوده بر حسب t
plt.figure()
plt.bar([wait_time[i][0] for i in range(len(wait_time))], [wait_time[i][1] for i in range(len(wait_time))])
plt.show()

#نمودار تغییرات طول صف برحسب زمان
plt.plot(observation_times, q_length)
plt.show()

from ConwayGame import ConwayVerifier, ShowCode
import time
import matplotlib.pyplot as plt


sizes = [10, 100, 150, 200, 250, 300, 500, 750, 1000, 1200, 1500,
         1750, 2000, 2250, 2500, 2750, 2800, 2850, 2900, 2950, 3000]

time_list = []
cracking_prob = []
mem_size = []

for size in sizes:
    print(f"Generating: {size}", end=' --> ')
    maths = ConwayVerifier(100, size)
    start_time = time.time()
    key = maths.GenerateKey()
    end_time = time.time()
    print("Generated")
    mem_size.append(key.nbytes)
    ShowCode(key)
    elapsed_time = end_time - start_time
    time_list.append(elapsed_time)

    cracking_prob.append(0.5**(size*size))


plt.figure()
plt.plot(sizes, time_list, c='g', label='Time')
plt.xlabel('Size')
plt.ylabel('Time (Seconds)')
plt.legend()
plt.show()

plt.figure()
plt.plot(sizes, cracking_prob, c='r', label='Hacking Probability')
plt.xlabel('Size')
plt.ylabel('Probability')
plt.legend()
plt.show()

plt.figure()
plt.plot(sizes, mem_size, c='r', label='Key Size')
plt.xlabel('Size')
plt.ylabel('Memory in Bytes')
plt.legend()
plt.show()



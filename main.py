log = open("NASA_access_log_jul95")
ip_addresses =[]

try:
    for line in log:
        ip_addresses.append(line.split(" ")[0])
except:
    print("Uh-Oh")


from collections import Counter
import matplotlib.pyplot as plt

c = Counter(ip_addresses)

log_counter = Counter(ip_addresses)

print(log_counter.keys())
print(log_counter.values())

f = plt.figure()

plt.bar(log_counter.keys(), log_counter.values())

plt.xticks(rotation=30, ha='left')

plt.show()



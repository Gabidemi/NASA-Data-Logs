log = open("NASA_access_log_jul95")
ip_addresses =[]
Files = []
Time = []
FileType = []

try:
    for line in log:
        ip_addresses.append(line.split(" ")[0])
        Files.append(line.split(" ")[6])
        Time.append(line.split(" ")[3].split(":")[0])
except:
    print("Uh-Oh")


from collections import Counter

c = Counter(ip_addresses).most_common(3)
f = Counter(Files).most_common(3)
t = Counter(Time).most_common(3)

print(c)
print(f)
print(t)

log = open("NASA_access_log_jul95")
ip_addresses =[]

try:
    for line in log:
        ip_addresses.append(line.split(" ")[0])
except:
    print("Uh-Oh")

print(ip_addresses)
def most_frequent(ip_addresses):
    return max(set(ip_addresses), key = ip_addresses.count)
 
ip_addresses = []
print(most_frequent(ip_addresses.count))
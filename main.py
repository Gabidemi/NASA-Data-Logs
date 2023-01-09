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
import matplotlib.pyplot as plt

c = Counter(ip_addresses)
f = Counter(Files)
t = Counter(Time)

log_counter = Counter(ip_addresses)
log_file = Counter(Files)

print(log_counter.keys())
print(log_counter.values())
print(log_file.keys())
print(log_file.keys())

plt.subplots_adjust(bottom=0.31)
plt.subplots_adjust(left=0.22)


newDict = dict()
for (key,value) in log_counter.items():
    if value >= 6500: # If the number of times the IP has been accessed is over 6500, only display the ones 6500 or over.
        newDict[key] = value

c = ['red', 'yellow', 'black', 'blue', 'orange'] # This is the list of colors to make the graph colors all be different


plt.bar(newDict.keys(), sorted(newDict.values()), color = c, width = 1)
plt.xticks(rotation=30, ha='right') # Makes the labels slanted to the right
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'cornflowerblue','size':12}
plt.title("Most accessed IP Addresses", fontdict = font1)
plt.xlabel("Ip Adresses", fontdict = font2) 
plt.ylabel("# of times Accessed", fontdict = font2)
plt.show()

plt.subplots_adjust(bottom=0.350)
plt.subplots_adjust(left=0.22)
newDict = dict()
for (key,value) in log_file.items():
    if value >= 45000: #If the number of times accessed is over 45000, only display the ones over 45000
        newDict[key] = value

d = ['black', 'yellow', 'red', 'cornflowerblue', 'coral', 'beige']

plt.bar(newDict.keys(), sorted(newDict.values()), color = d, width = 1)
plt.xticks(rotation=30, ha='right')

font1 = {'family':'serif','color':'coral','size':20}
font2 = {'family':'serif','color':'darkred','size':12}
plt.title("Most commonly used filetypes", fontdict = font1)
plt.xlabel("filetypes", fontdict = font2)
plt.ylabel("# of times Accessed", fontdict = font2)

plt.show()



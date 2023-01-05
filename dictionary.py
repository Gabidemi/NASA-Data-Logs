from collections import Counter
import matplotlib.pyplot as plt


fruits = ['apple', 'oranges', 'grapes', 'kiwi', 'banana', 'apple', 'apple', 'oranges', 'grapes', 'cherry']


fruit_counter = Counter(fruits)

print(fruit_counter.keys())
print(fruit_counter.values())
newDict = dict()
for (key,value) in fruit_counter.items():
    if value <= 2:
        newDict[key] = value


plt.bar(newDict.keys(), newDict.values())


plt.show()

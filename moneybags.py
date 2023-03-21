"""
--------------------------------------------
Name: Het Bharatkumar Patel
SID: 1742431
CCID: hetbhara
AnonID: 1000348298
CMPUT 274, Fall 2022
Assessment: Weekly Exercise 06 - Dr. Moneybags
--------------------------------------------
"""

n = int(input())
net_worths = []
for i in range(n):
    worth = int(input())
    net_worths.append(worth)

net_worths.sort()
threshold = 0
index = 0

while threshold <= len(net_worths) and index < len(net_worths):
    if net_worths[index] >= threshold:
        threshold = net_worths[index]

    if threshold >= len(net_worths) - index:
        threshold = len(net_worths) - index
        break
    index += 1

print(threshold)

#def values[] # adding later
baseCost = 100
firstUpgrade = 56
totalCost = 0
counter = 0
currentTotalCost = 0
costRemaining = 0
upgrades = 304 #insert your remaining upgrades here

for i in range(upgrades):
    firstUpgrade = int(firstUpgrade * 1.0318)
    if firstUpgrade >= 500:
        firstUpgrade = 500
    baseCost = baseCost + firstUpgrade
    totalCost = totalCost + baseCost
    counter = counter + 1
    if counter == 172:
        currentTotalCost = currentTotalCost + totalCost
    print(totalCost)
if counter == upgrades:
    costRemaining = totalCost - currentTotalCost
    print(totalCost)
    print(costRemaining)

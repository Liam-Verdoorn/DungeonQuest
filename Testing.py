# stat = 30
# maxUpgrades = 124
# calc = 1
#
# for i in range(upgrades):
    # calc = int(stat * 0.05)
    # if calc >= 10:
        # calc = 10
    # stat = stat + calc

    # 1. 100    + 56 = 156
    # 2. 156    + (56 * 1.0618) = 215 from 2/3 is 215 and from we don't have 3/4 4/5 is 344 from upgrade 2 to upgrade 3 costs is what it means
    # 3. 215    + (56 * 1.0618) = 274  is the line itself even correct would it output 274
    # 4. 274    + (56 * 1.0618) = 333  print(274.4608    + (56 * 1.242))


startingCost = 100 # add upgradeCost and multiply by 1.0618
upgradeCost = 56
upgradeLevel = 0
totalCost = 0
upgrades = 30 #user inputs their current upgrade level here

for i in range(upgrades):
    upgradeCost = int(round((startingCost + upgradeCost) * 1.0618))

    if upgradeCost >= 500:
        upgradeCost = 500   
    startingCost = startingCost + upgradeCost
    totalCost = startingCost + upgradeCost
    currentUpgradeLevel = currentUpgradeLevel + 1
    if currentUpgradeLevel == (upgrades):
        currentUpgradeLevel = currentUpgradeLevel + totalCost - currentUpgradeLevel
print(totalCost)

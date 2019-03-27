baseStat = 32
maxUpgrades = 31 #input your max upgrade level here
upgradeLevel = 1

for i in range(maxUpgrades):
    upgradeLevel = int(baseStat * 0.05)
    if upgradeLevel >= 10:
        upgradeLevel = 10
    baseStat = baseStat + upgradeLevel
    print(baseStat)

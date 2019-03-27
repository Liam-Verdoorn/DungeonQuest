baseStat = 3326 #input the base value of your weapon here
maxUpgrades = 336 #input your max upgrade level here
upgradeLevel = 1 #don't touch this line

for i in range(maxUpgrades):
    upgradeLevel = int(baseStat * 0.05)
    if upgradeLevel >= 10:
        upgradeLevel = 10
    else:
        print(upgradeLevel)
    baseStat = baseStat + upgradeLevel
print(f'Your item\'s max potential is {baseStat}.')

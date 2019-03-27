baseStat = 39 #input the base value of your weapon here
maxUpgrades = 60 #input your max upgrade level here
upgradeLevel = 1 #don't touch this line
counter = 0
i = 1
upgrade = 1
timesIncreasedByTen = 0

for i in range(maxUpgrades):
    upgradeLevel = baseStat * 0.05
    counter = counter + 1
    upgrade = counter
    if upgradeLevel >= 10:
        timesIncreasedByTen += 1
        upgradeLevel = 10
    else:
        print(f'Item stats increased by {round(upgradeLevel)} at level {upgrade}! ({round(baseStat)} total)')
    baseStat = baseStat + upgradeLevel
if timesIncreasedByTen:
    print(f'Item stats reached max increment (10); increased by 10 {timesIncreasedByTen} times. ({upgrade} times in total)')
print(f'Your item\'s max potential is {round(baseStat)}.')

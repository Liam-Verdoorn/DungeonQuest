stat = 30
upgrades = 124
math = 1

for i in range (upgrades):
    math = int(stat * 0.05)
    if math >= 10:
        math = 10
    stat = stat + math
    print(stat)

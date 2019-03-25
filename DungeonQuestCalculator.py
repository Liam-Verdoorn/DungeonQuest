a: int = 52
upgradesApplied: int = 1

userInput = input('Your item\'s damage can be increased by ')
try:
    int(userInput)
except ValueError as error:
    print('Input must be an integer.')

for i in range(int(userInput)):
    b = a * 0.05
    if b >= 10:
        b = 10
    a += b
a: int = round(a)
print(a)

# cd /home/liam/git/dungeonquest && git add . && git commit -m"Initial commit." && git push origin master

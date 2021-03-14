import time
Secretn = 10
guessN= input('enter any number: ')

def function():
    for guessN in range(1, 7):
        print("GUESS")
    if guessN > Secretn:
        print("TOO HIGH")
    elif guessN < Secretn:
        print("TOO LOW")
if guessN == Secretn:
    print("ITS RIGHT !")
else:
    print("SIKE U SUCK" + str(Secretn))

time.sleep(5)
print("nooo")
print("lsoefd")
print("sdwew")
print(function())
def printBlue():
    print('you chose Blue!\n')
    return
def printRed():
    print('you chose Red!\n')
    return
def printOrange():
    print('you chose Orange!\n')
    return
def printYellow():
    print('you chose Yellow!\n')
    return
def choice():
    print("0:Blue")
    print("1:Red")
    print("2:Orange")
    print("3:Yellow")
    print("4:Quit")
    return
ColorSelect={0:printBlue, 1:printRed, 2:printOrange, 3:printYellow}
selection=0
while True:
    if selection==4:break
    choice()
    selection=int(input("selet a color option:"))
    if (selection>=0) and (selection<4):
        ColorSelect[selection]()

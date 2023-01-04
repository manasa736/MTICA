def printSunday():
    print('you chose Sunday!\n')
    return
def printMonday():
    print('you chose Monday!\n')
    return
def printTuesday():
    print('you chose Tuesday!\n')
    return
def printWednesday():
    print('you chose Wednesday!\n')
    return
def printThursday():
    print('you chose Thursday!\n')
    return
def printFriday():
    print('you chose Friday!\n')
    return
def printSaturday():
    print('you chose Saturday!\n')
    return
def choice():
    print("enter day number between 0-6")
dayDict={0:printSunday, 1:printMonday,2:printTuesday,3:printWednesday,
           4:printThursday,5:printFriday,6:printSaturday}
choice()
dayNo=int(input())
if(dayNo>=1 and dayNo<=7):
    dayDict[dayNo]()
else:
    print("Invalid")

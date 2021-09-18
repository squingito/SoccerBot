from openpyxl import load_workbook

workbook = load_workbook(filename='PL_dataset.xlsx')
workbook.sheetnames

sheet = workbook.active


#sheet["A"]
def findIndexOf(name):
    i = 1
    valueFound = False
    for value in sheet.iter_rows(min_row = 1, max_row = 572,
                                 min_col = 1, max_col = 1,
                                 values_only = True):
        tempValue = value[0]
        if (name.lower() == tempValue.lower()):
            rowVar1 = i
            valueFound = True
            break
        i = i + 1
    if valueFound:
        return i
    else:
        return None

def getStats(name):
    if(len(name.split(" ")) >= 2):
        name = name[10:]
        print(name)
        num = findIndexOf(name)
        if(num != None):
            text = formatGetStats(num) + "\n"
            if sheet["D" + str(num)].value == "Goalkeeper":
                text = text + "\n" + sheet["D" + str(num)].value + " Stats:\n"
                text = text + goalkeeperFormatGetStats(num)
            elif sheet["D" + str(num)].value == "Defender":
                text = text + "\n" + sheet["D" + str(num)].value + " Stats:\n"
                text = text + defenderFormatGetStats(num)
            elif sheet["D" + str(num)].value == "Forward":
                print('here')
                text = text + "\n" + sheet["D" + str(num)].value + " Stats:\n"
                text = text + forwardFormatGetStats(num)
            elif sheet["D" + str(num)].value == "Midfielder":
                text = text + "\n" + sheet["D" + str(num)].value + " Stats:\n"
                text = text + midfeildFormatGetStats(num)
            return text
        else:
            return '"' + name + '"' + " does not exist"
    else:
        return "please write a person after the space"

def compare(names):
    name1 = names.split("|")[0][9:]
    name2 = names.split("|")[1]
    while(1):
        if name1[-1] == " ":
            name1 = name1[:-1]
        else:
            break
    while(1):
        if name2[0] == " ":
            name2 = name2[1:]
        else:
            break
    num1 = findIndexOf(name1)
    num2 = findIndexOf(name2)
    if num1 != None and num2 != None:
        return formatGetStats(num1) + "\n" + "\n" + formatGetStats(num2)
    elif num1 == None and num2 == None:
        return '"' + name1 + '"'+ ' and ' +  '"' + name2 + '"'  + " do not exist"
    elif num1 == None:
        return '"' + name1 + '"' + " does not exist"
    else:
        return '"' + name2 + '"' + " does not exist"
        


def formatGetStats(index):
    return "Name: {}\nGoals: {}\nAssists: {}\nYellow Cards: {}\nRed Cards: {}\nPasses: {}\nFouls: {}\nOffsides: {}\nAppearances: {}\nAge: {}"\
        .format(sheet["A"+ str(index)].value,sheet["J"+ str(index)].value, \
        sheet["AC"+ str(index)].value,sheet["AL"+ str(index)].value, sheet["AM"+ str(index)].value, sheet["AD"+ str(index)].value, \
        sheet["AN" + str(index)].value, sheet["AO" + str(index)].value, sheet["G" + str(index)].value, sheet["F" + str(index)].value) 

def forwardFormatGetStats(index):
    return "Shots on Target: {}\nShooting Accuracy (%): {}\nAerial Battles Won: {}\nAerial Battles Lost: {}\nBig Chances Created: {}\nCrosses: {}".format(sheet["L"+ str(index)].value,sheet["M"+ str(index)].value,sheet["Y"+ str(index)].value,sheet["Z"+ str(index)].value,sheet["AE"+ str(index)].value,sheet["AF"+ str(index)].value)
    
def midfeildFormatGetStats(index):
    return "Tackles: {}\nTackle Success (%): {}\nThrough Balls: {}\nInterceptions: {}\nRecoveries: {}\nBig Chances Created: {}\nCrosses: {}\nAccurate Long Balls: {}".format(sheet["P" + str(index)].value,sheet["Q" + str(index)].value,sheet["AH" + str(index)].value,sheet["S" + str(index)].value,sheet["U" + str(index)].value,sheet["AE" + str(index)].value,sheet["AF" + str(index)].value,sheet["AI" + str(index)].value)

def defenderFormatGetStats(index):
    return "Clean Sheets {}\nGoals Conceded {}\nTackles {}\nTackle Success % {}\nBlocked Shots {}\nInterceptions {}\nClearances {}\nOwn Goals {}\nErrors Leading to Goal {}"\
    .format(sheet["N" + str(index)], sheet["O" + str(index)], sheet["P" + str(index)], sheet["Q" + str(index)],\
    sheet["R" + str(index)], sheet["S" + str(index)], sheet["T" + str(index)], sheet["AA" + str(index)], sheet["AB" + str(index)])

def goalkeeperFormatGetStats(index):
    return "Clean Sheets {}\nGoals Conceded {}\nSaves {}\nPenalties Saved {}"\
    .format(sheet["N" + str(index)], sheet["O" + str(index)], sheet["AJ" + str(index)], sheet["AK" + str(index)])
from openpyxl import load_workbook
workbook = load_workbook(filename='PL_dataset.xlsx')
workbook.sheetnames

sheet = workbook.active

print(sheet["B4"].value)

#sheet["A"]
def findIndexOf(name):
    i = 1
    valueFound = False
    for value in sheet.iter_rows(min_row = 1, max_row = 572,
                                 min_col = 1, max_col = 1,
                                 values_only = True):
        tempValue = value[0]
        if (userInput == tempValue):
            rowVar1 = i
            valueFound = True
            break
        i = i + 1
    if valueFound:
        return i
    else:
        return None

def getStats(name):
    print("here")
    name = name.split(" ")[1]
    num = findIndexOf(name)
    if(num != None):
        return formatGetStats(num)
    else:
        return '"' + name + '"' + " does not exist"

def compare(names):
    name1 = names.split(" ")[1]
    name2 = names.split(" ")[2]
    num1 = findIndexOf(name1)
    num2 = findIndexOf(name2)
    if num1 != None and num2 != None:
        return formatCompare(num1,num2)
    elif num1 == None and num2 == None:
        return '"' + name1 + '"'+ ' and ' +  '"' + name2 + '"'  + " do not exist"
    elif num1 == None:
        return '"' + name1 + '"' + " does not exist"
    else:
        return '"' + name2 + '"' + " does not exist"
        


def formatGetStats(index):
    return "Name: {}/nGoals: {}/nAsists: {}".format(sheet[" "+ index],sheet[" "+ index],sheet[" "+ index])  
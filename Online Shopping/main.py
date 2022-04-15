# Assignment -1

# Lab Professor: Ms. Laily Ajellu

#  Yagnik Patel - 101324163

# using classes instead of the dictionary

# class- 1 Employee class for storing the data about each Employee

class Employee:
    def __init__(self, employeeID, employeeName, employeeType, yearsWorked, totalPurchased, totalDiscounts,
                 employeeDiscount):
        self.totalDiscounts = totalDiscounts
        self.totalPurchased = totalPurchased
        self.yearsWorked = yearsWorked
        self.employeeType = employeeType
        self.employeeName = employeeName
        self.employeeDiscount = employeeDiscount
        self.employeeID = employeeID


# class - 2  Item class to store Item information
class Item:
    def __init__(self, itemNumber, itemName, itemCost):
        self.itemNumber = itemNumber
        self.itemName = itemName
        self.itemCost = itemCost


# class- 3 Employee Manger class to store all the objects of Employee class and to add New Employee
class EmployeeManger:

    def __init__(self):
        self.employees = []

    def add_employee(self, employeeID, employeeName, employeeType, yearsWorked, totalPurchased, totalDiscounts,
                     employeeDiscount):
        newEmployee = Employee(employeeID, employeeName, employeeType, yearsWorked, totalPurchased, totalDiscounts,
                               employeeDiscount)

        return self.employees.append(newEmployee)

    # Function to Calculate the discount of the Item user is purchasing
    def calculate_discount(self, employeeDiscount, itemCost):
        index = 0
        # looping through the list
        for employee in self.employees:

            if employeeDiscount == employee.employeeDiscount:
                index = self.employees.index(employee)
                break
            else:
                index = None

        # assigning the value to mangerdis(10%)and hourlydis(2%) if the employee is one of them

        mangerDis = 0
        hourlyDis = 0

        if index is not None:
            # 2% for each year
            yearsDis = 2 * self.employees[index].yearsWorked
            if yearsDis >= 10:
                yearsDis = 10
            if self.employees[index].employeeType == "manager":
                # 10% more discount for Manger
                mangerDis = 10
                # 2% more discount for Hourly worker
            elif self.employees[index].employeeType == "hourly":
                hourlyDis = 2

            # Total discount percentage Employee will receive RIGHT now on Item.
            totalDis = yearsDis + mangerDis + hourlyDis
            # Total discount Employee will receive RIGHT now on Item.
            disAmount = itemCost * (totalDis / 100)

            if self.employees[index].totalDiscounts == 200:
                # If the Employee already have received the total 200$ discount he will not get any discount.
                finalPrice = itemCost
                print("-- Sorry You Can not have any discount On the Item You are purchasing--")
                print(" You have already received $200 discount so your Final price of item will be $", finalPrice, ".")
                print("\nThank You for Purchasing the Item.")
                self.employees[index].totalPurchased += finalPrice

                return finalPrice

            elif self.employees[index].totalDiscounts < 200:
                # possible Discount Amount employee can receive
                possibleDis = abs(self.employees[index].totalDiscounts - 200)
                # If the dis amount is greater than the possible then employee will receive only the possible dis for final price
                if possibleDis <= disAmount:
                    disAmount = possibleDis
                    print("4", disAmount)

                finalPrice = itemCost - disAmount
                self.employees[index].totalDiscounts += disAmount
                self.employees[index].totalPurchased += finalPrice
                print(" You have  received $" + str(
                    possibleDis - abs(200)) + " discount so your Final price of item will be $", finalPrice, ".")
                print("\nThank You for Purchasing the Item.")
                return finalPrice

        else:
            print("Can Not purchase Item Bc of some Reasons Try New One:-")


class ItemManger:

    def __init__(self):
        self.items = []

    def add_items(self, itemNumber, itemName, itemCost):
        newItem = Item(itemNumber, itemName, itemCost)

        return self.items.append(newItem)

    def view(self):
        for item in self.items:
            print(item.itemNumber)


# Below are the all the Functions of the Assignment

# 1 -  Function for validating Integer input.

def validateInt(name):
    goToMenu = True

    nameValue = input("Enter the  " + str(name.capitalize()) + "-:")
    # while loop to ensure numeric value from user
    while not nameValue.isnumeric():

        if nameValue.lower() == "no":
            return goToMenu
        print(" --INPUT FIELD REQUIRES A INTEGER VALUE--")
        nameValue = input("Enter the  " + str(name.capitalize()) + "-:")

    # breaks if the input is no

    if nameValue.lower() == "no":
        return goToMenu
    nameValue = int(nameValue)
    return nameValue


# 1 -  Function for validating STRING input.
def validateStr(name):
    goToMenu = True
    nameValue = input("Enter the " + str(name.capitalize()) + ":- ")
    # while loop to ensure the string value from user
    while not nameValue.isalpha():
        print("--- INPUT FIELD REQUIRES A STRING VALUE ---")
        nameValue = input("Enter the " + str(name.capitalize()) + ":- ")
    # breaks if input is no
    if nameValue.isalpha() and nameValue.lower() == "no":

        return goToMenu
    else:
        nameValue = str(nameValue)
        return nameValue


# Checking if the Employee exists in list
def checkEm(employeeEntity, value):
    EXIST = False

    for employee in employeeManger.employees:

        if employeeEntity == "employeeID":
            if employee.employeeID == value:
                EXIST = True
                return EXIST

        elif employeeEntity == "employeeDiscount":
            if employee.employeeDiscount == value:
                EXIST = True
                return EXIST

    return EXIST


# checking if the Item is in the list

def checkItem(itemNumber, value):
    EXIST = False
    for item in itemManger.items:

        if item.itemNumber == value:
            EXIST = True
            return EXIST

    return EXIST


def menu():
    options = [
        ['1- Create Employee         '],
        ["2- Create Item             "],
        ['3- Make Purchase           '],
        ['4-All Employee Summary     '],
        ['5-Exit                     ']

    ]
    print("+-----------------------------------+")
    print("|               MENU                |")
    print("+-----------------------------------+")
    for row in options:
        print("| {: >33} | ".format(*row))
    print("+-----------------------------------+")


def employeePage():
    goToMenu = 0
    while goToMenu == 0:
        print(" ENTER 'NO' TO DIRECTLY EXIT FUNCTION.")
        EmployeeId = validateInt("Employee Id")
        # below line breaks code and function if user enters "NO"
        if EmployeeId is True:
            break
        else:
            while checkEm("employeeID", EmployeeId) is True:
                print("Employee ID already Exists...Enter Valid ID")
                EmployeeId = validateInt("Employee Id")
                if EmployeeId is True:
                    break

        EmployeeName = validateStr("Employee Name ")
        if EmployeeName is True:
            break

        EmployeeType = validateStr("Employee Type ..(choose from two option 'manger' and 'hourly') ")
        if EmployeeType is True:
            break

        elif EmployeeType != bool:
            while EmployeeType.lower() != "manager" and EmployeeType.lower() != "hourly":
                EmployeeType = validateStr("Employee Type ..(choose from two option 'manger' and 'hourly') ")
        YearsWorked = validateInt(" Years worked")
        if YearsWorked is True:
            break

        TotalPurchase = 0
        TotalDiscounts = 0

        EmployeeDiscount = validateInt("Employee Discount")
        if EmployeeDiscount is True:
            break

        else:
            while checkEm("employeeDiscount", EmployeeDiscount) is True:
                print("Employee Discount number Already Exists -- Enter Valid one")
                EmployeeDiscount = validateInt("Employee Discount")
                if EmployeeDiscount is True:
                    goToMenu = 1
                    break

        employeeManger.add_employee(EmployeeId, EmployeeName, EmployeeType, YearsWorked, TotalPurchase, TotalDiscounts,
                                    EmployeeDiscount)
        ans = str(input("DO you want to add more employee? yes or no : - "))

        if ans == "yes":
            continue
        elif ans.lower() == "no":
            break

    tem = validateInt("Ans '1' for yes and '0' for No:- DO you want to Go to Menu ?")
    if int(tem) == 1:
        return 1
    else:
        return 0


def itemPage():
    goToMenu = 0
    while goToMenu == 0:

        ItemNumber = validateInt("Item  Number")
        if ItemNumber is True:
            break
        else:

            while checkItem("ItemNumber", ItemNumber) is True:
                print("--ItemNumber Already Exists , Please Enter valid ItemNumber--")
                ItemNumber = validateInt("Item  Number")
                if ItemNumber is True:
                    goToMenu = 1
                    break

        ItemName = validateStr("Item Name ")
        if ItemName is True:
            break
        ItemCost = validateInt("Item Cost ")
        if ItemCost is True:
            break

        itemManger.add_items(ItemNumber, ItemName, ItemCost)

        ans = str(input("DO you want to add Another Item? yes or no : - "))

        if ans == "yes":
            continue
        elif ans.lower() == "no":
            break

    tem = validateInt("Ans '1' for yes and '0' for No:- DO you want to Go to Menu ?")
    if int(tem) == 1:
        return 1
    else:
        return 0


# Function to display the Items
def display_items():
    print("  +---------------------------+----------ITEM LIST---------+---------------------------+")

    print("  +---------------------------+----------------------------+---------------------------+")

    table_data2 = [
        ['Item Number   ', 'Item Name   ', 'Item Cost   ']
    ]
    for row in table_data2:
        print("  |       {: <20}|       {: <20} |       {: <20}|".format(*row))

    print("  +---------------------------+----------------------------+---------------------------+")
    table_data = []
    print("  +---------------------------+----------------------------+---------------------------+")
    for item in itemManger.items:
        table_data += [

            [str(item.itemNumber), item.itemName.capitalize(), "$" + str(item.itemCost) + ".00"]
        ]

    for row in table_data:
        print("  | {: <25} | -{: <25} | {: >25} |".format(*row))
    print("  +---------------------------+----------------------------+---------------------------+")

    goToMenu = 0
    while goToMenu == 0:

        print(
            "TO purchase the Items from List Enter the Item number From List and Your (Valid)Employee Discount Number")
        print("\n")
        choseItem = validateInt(" Item Number from above list to purchase:--")
        if choseItem is True:
            return 1
        else:

            while checkItem("ItemNumber", choseItem) is not True:
                print(" --Entered Item Number does not Exists--")
                choseItem = validateInt(" Item Number from above list to purchase:--")
                if choseItem is True:
                    return 1

        emDiscount = validateInt("Valid Employee Discount Number of yours --")
        if emDiscount is True:
            return 1

        else:
            while checkEm("employeeDiscount", emDiscount) is not True:
                print(" --Entered Employee Discount Number does not Exists--")
                emDiscount = validateInt("Valid Employee Discount Number of yours --")
                if emDiscount is True:
                    return 1
        cost = 0
        for item in itemManger.items:

            if item.itemNumber == choseItem:
                cost = item.itemCost
                # this breaks the for loop

        employeeManger.calculate_discount(emDiscount, cost)
        # Summary Of employees
        displayEmployee(True)
        ans = str(input("DO you want to Purchase Another Item? yes or no : - "))

        if ans == "yes":
            continue
        elif ans.lower() == "no":
            goToMenu = 1
            break

    tem = validateInt("Ans '1' for yes and '0' for No:- DO you want to Go to Menu ?")
    if int(tem) == 1:
        return 1
    else:
        return 0


# all Employees List

def displayEmployee(bool):
    print(
        "<----------------------------------------------------ALL Employee List ------------------------------------------------------>")
    print(
        '+-------------+---------------+---------------+---------------+-----------------+-----------------+--------------------------+')

    t1 = [
        ['Employee ID', 'Employee Name', 'Employee Type', 'Years Worked', 'Total Purchased', 'Total Discounts',
         'Employee Discount Number']]

    for row in t1:
        print("| {: <12}| {: <13} | {: <12} | {: <13} | {: <12} | {: <12} | {: <20} |".format(*row))
    print(
        '+-------------+---------------+---------------+---------------+-----------------+-----------------+--------------------------+')

    table_data = []
    for employee in employeeManger.employees:
        table_data += [

            ["{0:d}".format(employee.employeeID), employee.employeeName.capitalize(),
             "{0:3s}".format(employee.employeeType.capitalize()),
             employee.yearsWorked, "${0:3.2f}".format(employee.totalPurchased),
             "${0:3.2f}".format(employee.totalDiscounts),
             employee.employeeDiscount]
        ]

    for row in table_data:
        print("| {: <12}| {: <13} | {: <12}  | {: <13} | {: <14}  | {: <14}  | {: <25}|".format(*row))

    print(
        '+-------------+---------------+---------------+---------------+-----------------+-----------------+--------------------------+')

    if bool is True:
        return 0
    else:
        tem = validateInt("Ans '1' for yes and '0' for No:- DO you want to Go to Menu ?")
        if int(tem) == 1:
            return 1
        else:
            return 0


# ---Main program starts below---


# Creating the Objects OF two mangers classes

employeeManger = EmployeeManger()
itemManger = ItemManger()
# ADDING THE VALUES INTO LIST JUST FOR TASTING PURPOSE FOR USER
itemManger.add_items(11526, "Nike shoes", 120)
itemManger.add_items(11849, "Trampoline", 180)
itemManger.add_items(11966, "Mercury Bicycle", 150)
itemManger.add_items(11334, "Necklace Set", 80)

employeeManger.add_employee(1001, "John Alber", "hourly", 8, 0, 0, 22737)
employeeManger.add_employee(1002, " Sarah Rose", "manager", 12, 0, 0, 22344)
employeeManger.add_employee(1003, "Alex Folen", "manager", 5, 0, 0, 2222)
employeeManger.add_employee(1004, "Pola Sahari", "hourly", 1, 0, 0, 22488)

GoToMenu = True
while GoToMenu:

    menu()

    option = validateInt("One Option to go to each page --")
    if option == 1:
        page1 = employeePage()
        if page1 == 1:

            continue
        else:

            break

    if option == 2:

        page2 = itemPage()
        if page2 == 1:
            continue
        else:

            break

    if option == 3:
        page3 = display_items()
        if page3 == 1:
            continue
        else:

            break

    if option == 4:
        page4 = displayEmployee(False)
        if page4 == 1:
            continue
        else:

            break
    if option == 5:
        GoToMenu = False

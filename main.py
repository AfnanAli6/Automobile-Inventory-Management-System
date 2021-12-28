# AHMED AFNAN ALI BIN AMEER ALI

############ FUNCTIONS ############

def mainMenu():     # Function for displaying list of command selection menu
    print ("-"*45)
    print ("\t   Royaton Motors Sdn Bhd")
    print ("AUTOMOBILE PARTS INVENTORY MANAGEMENT SYSTEM")
    print ("-"*45)
    print ("MENU SELECTIONS :")
    print ("A    - New Parts Inventory Creation")
    print ("B    - Parts Inventory Update (Receive/Release)")
    print ("C    - List Available Quantity of All Parts")
    print ("D    - Parts Stock Less Quantity")
    print ("E    - Track Parts & Quantity Released")
    print ("F    - Search a Part & Supplier Record")
    print ("G    - List Parts Supplied by a Supplier")
    print ("X    - Quit")
    print ("HELP - Display main menu again\n")
    print ("WAREHOUSE CODE :")
    print ("[BIOS 1.5cc - WBS]\t[AMBRY 1.5cc - WAY]\t[BARRIER 1.6cc - WBR]\n")
    print ("ASSEMBLY SECTION :")
    print ("[FRAME & BODY - FB]\t[INTERIOR ASSEMBLY - IA]\n[ENGINE SYSTEM - EN]\t[AIR-CONDITIONING SYSTEM - AC]")
    print ("-"*45)


def createPartsFunction():      # Function for creating new parts into the inventory
    numOfItem = int(input("How many new parts do you want to create? : "))

    if (numOfItem > 0):

        for i in range(numOfItem):  # To loop the set of instructions to create multiple parts
            partList = []   # Creating an empty Array to append parts creation data
            print ("\nChoose Warehouse Code")
            print ("1) WBS")
            print ("2) WAY")
            print ("3) WBR")

            warehouseCode = int(input("\nKey in the specified digit : "))

            if (warehouseCode == 1):
                warehouseCode = ("WBS")

            elif (warehouseCode == 2):
                warehouseCode = ("WAY")

            elif (warehouseCode == 3):
                warehouseCode = ("WBR")

            else:
                print ("Digit entered invalid!") # Error message printed to validate input by user
                break

            print ("")

            print ("Choose Assembly Section")
            print ("1) FB")
            print ("2) IA")
            print ("3) EN")
            print ("4) AC")

            assemblyCode = int(input("\nKey in the specified digit : "))

            if (assemblyCode == 1):
                assemblyCode = ("FB")

            elif (assemblyCode == 2):
                assemblyCode = ("IA")

            elif (assemblyCode == 3):
                assemblyCode = ("EN")

            elif (assemblyCode == 4):
                assemblyCode = ("AC")

            else:
                print ("Digit entered invalid!") # Error message printed to validate input by user
                break

            wareAssemblyCode = str(warehouseCode + assemblyCode)

            partNumber = int(input("\nGive part a new unique number : "))
            partID = (wareAssemblyCode + (str(partNumber)))
            partList.append(partID)

            fHandler = open('PARTS_RECORD.txt' , 'r')

            data = fHandler.readlines()
            killFunction = 0 # Assingned value to peform the function
            for line in data:
                line = line.rstrip()
                newLine = line.split("\t")

                if newLine[0] == partID: # Validating the existance of user inputted Part-ID in the text file
                    print ("PART-ID ALREADY EXIST, TRY AGAIN")
                    killFunction = 1 # Sentinel value to terminate the function
            fHandler.close()
            if killFunction == 0 :

                partName = str.upper(input("Enter new part name : "))
                partList.append(partName)

                priceValue = float(input("Enter new part price value : RM"))
                partPrice = ("RM")+str(priceValue)
                partList.append(partPrice)

                print ("")

                print ("Choose a supplier : ")
                print ("1) Sun Hup Auto Sdn Bhd    (SUP_ID_SSHA1)")
                print ("2) ERA Auto Spares Sdn Bhd (SUP_ID_SAFN2)")
                print ("3) KevTEC Malaysia Sdn Bhd (SUP_ID_KTMB3)")

                supplierID = int(input("\nKey in the specified digit : "))

                if (supplierID == 1):
                    supplierID = ("SUP_ID_SSHA1")
                    supplierName = ("Sun Hup Auto Sdn Bhd")
                    stringVerContact = ("+6019-5098897")

                elif (supplierID == 2):
                    supplierID = ("SUP_ID_SAFN2")
                    supplierName = ("ERA Auto Spares Sdn Bhd")
                    stringVerContact = ("+6012-3054467")

                elif (supplierID == 3):
                    supplierID = ("SUP_ID_KTMB3")
                    supplierName = ("KevTEC Malaysia Sdn Bhd")
                    stringVerContact = ("+6017-8022394")

                else:
                    print ("Digit entered invalid!")
                    break

                partList.append(supplierID)
                partList.append(supplierName)
                partList.append(stringVerContact)

                partQuantity = int(input("Enter new part quantity : "))
                partList.append(str(partQuantity))
                print ("Parts has been added to the inventory successfully !")

                fileHandler = open('PARTS_RECORD.txt' ,'a') # Opening Part's Record text file in append mode

                for partList in partList: # Appending the user input from partList Array into the text file
                    fileHandler.write(partList)
                    fileHandler.write('\t')
                fileHandler.write('\n')

                fileHandler.close()
    else:
        print ("Sorry input invalid, try again") # Error message printed to not allow negative input by user


def updatePartsQuantity():      # Function for updating parts quantity (increase/decrease)
    print ("\nCurrent Records of Part Quantity : ")
    listPartsRecord()

    warehouseCode = str.upper(input("\nEnter warehouse code : "))
    assemblyCode = str.upper(input("Enter assembly section code : "))
    wareAssemblyCode = str(warehouseCode + assemblyCode)

    partNumber = int(input("Enter the shown unique number of part : "))
    partID = (wareAssemblyCode) + str(partNumber)

    fileHandler = open('PARTS_RECORD.txt' ,'r')

    oldData = fileHandler.readlines()
    newData = []

    for line in oldData:
        line = line.rstrip()
        newLine = line.split("\t")

        if (partID.upper() == newLine[0].upper()):

            print ("\n1) Receive Parts from Supplier")
            print ("2) Release Parts to the Assembly Section")
            updateChoice = int(input('Press 1 or 2 to continue : '))
            print ("")

            if (updateChoice == 1):
                receivedQuantity = int(input('How many units do you want to receive? : '))
                newQuantity = int(newLine[6]) + (receivedQuantity)
                newLine[6] = str(newQuantity)
                print ("Successfully updated part quantity!")

            elif (updateChoice == 2):
                releasedQuantity = int(input('How many units do you want to release? : '))
                newQuantity = int(newLine[6]) - (releasedQuantity)
                newLine[6] = str(newQuantity)
                print ("Successfully updated part quantity!")

                fHand = open('TRACKING_RECORD.txt' , 'a')

                records = []
                content = (str(releasedQuantity)," QUANTITY OF ",(newLine[0]),(newLine[1])," PARTS HAS BEEN RELEASED TO WAREHOUSE ",(warehouseCode)," BUILDING SECTION ",(assemblyCode))
                records.append(content)

                for records in records:

                    for item in records:
                        fHand.write(item)
                        fHand.write('\t')
                    fHand.write('\n')

                fHand.close()

            else:
                print ("\nChoice entered invalid, part quantity is not changed")

        newData.append(newLine)

    fileHandler.close()

    fileHandler = open('PARTS_RECORD.txt' , 'w')

    for line in newData:
        for item in line:
            fileHandler.write(item)
            fileHandler.write('\t')
        fileHandler.write('\n')

    fileHandler.close()


def listPartsRecord():      # Function for listing all the available parts sorted by its part-ID
    fileHandler = open('PARTS_RECORD.txt' ,'r')

    print ("")
    lines = sorted(fileHandler)
    for line in lines:
        newLine = line.split("\t")
        line = line.rstrip()
        print ("Part ID : " , newLine[0] , " Part Name : " , newLine[1] , " Part Quantity : " , newLine[6])

    fileHandler.close()


def lessPartQuantity():     # Function for listing all the available parts that has less than 10 quantities
    fileHandler = open('PARTS_RECORD.txt' ,'r')

    oldData = fileHandler.readlines()
    newData = []
    for line in oldData:
        line = line.rstrip()
        newLine = line.split("\t")
        lessQuantity = int(newLine[6])
        if (lessQuantity < 10):
            print ("\nParts with less than 10 quantities :")
            print ("Part ID : " , newLine[0] , " Part Name : " , newLine[1] , " Part Quantity : " , newLine[6] , " Supplier ID : " , newLine[3])
        else:
            print ("\nPart ID : " , newLine[0] , " has more than 10 quantities")


    fileHandler.close()


def trackReleasedParts():       # Function for displaying the track records of released parts to specific warehouse and assembly section
    fileHandler = open('TRACKING_RECORD.txt' , 'r')

    for line in fileHandler:
        line = line.rstrip()
        print(line)

    fileHandler.close()


def searchPartsDetail():        # Function for displaying respective part and supplier details by searching using its part-ID
    fileHandler = open('PARTS_RECORD.txt' , 'r')
    data = fileHandler.readlines()
    print ("Current list of parts :")
    listPartsRecord()
    partID = str.upper(input("\nEnter Part ID to search : "))

    for line in data:
        newLine = line.split("\t")

        if newLine[0] == partID:
            line = line.rstrip()
            print ("")
            print ("Part ID          : " , newLine[0])
            print ("Part Name        : " , newLine[1])
            print ("Part Quantity    : " , newLine[6])
            print ("Supplier ID      : " , newLine[3])
            print ("Supplier Company : " , newLine[4])
            print ("Supplier Contact : " , newLine[5])

    fileHandler.close()


def searchSuppliers():      # Function for displaying supplier that supplies more than one part, to several different warehouse or different assembly section within a warehouse
    print ("Choose a supplier : ")
    print ("1) Sun Hup Auto Sdn Bhd    (SUP_ID_SSHA1)")
    print ("2) ERA Auto Spares Sdn Bhd (SUP_ID_SAFN2)")
    print ("3) KevTEC Malaysia Sdn Bhd (SUP_ID_KTMB3)")

    supplierID = int(input("\nKey in the specified digit : "))

    if (supplierID == 1):
        supplierID = ("SUP_ID_SSHA1")

    elif (supplierID == 2):
        supplierID = ("SUP_ID_SAFN2")

    elif (supplierID == 3):
        supplierID = ("SUP_ID_KTMB3")

    else:
        print ("Digit entered invalid!")


    fileHandler = open('PARTS_RECORD.txt' , 'r')
    data = fileHandler.readlines()

    for line in data:
        newLine = line.split("\t")

        if newLine[3] == supplierID:
            print ("")
            line = line.rstrip()
            print(supplierID , ' supplies the following part :')
            print (newLine[0] , newLine[1])

    fileHandler.close()



############ MAIN PROGRAM ############

command = str("run")
mainMenu()  # calling the command selection menu

while(command != "X"):
    command = str.upper(input("\nEnter a command based on menu to proceed : "))

    if (command == "X"):
        print ("\nSuccessfully signed out, program terminated")

    elif (command == "A"):
        createPartsFunction()

    elif (command == "B"):
        updatePartsQuantity()

    elif (command == "C"):
        listPartsRecord()

    elif (command == "D"):
        lessPartQuantity()

    elif (command == "E"):
        trackReleasedParts()

    elif (command=="F"):
        searchPartsDetail()

    elif (command=="G"):
        searchSuppliers()

    elif (command == "HELP"):
        print (""), mainMenu()

    else:
        print ("Command entered invalid, try again")

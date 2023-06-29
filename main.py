def patientIDGenerator(noOfLines=1):
    patientFile = open('patients.txt', 'r')
    lines = patientFile.readlines()
    last_lines = lines[-noOfLines:]
    for line in last_lines:
        line = line.split()
        patientIDNum = line[0]
        try:
            if int(line[0]) >= 1:
                patientIDNum = int(patientIDNum) + 1
                patientIDNum = str(patientIDNum)
                patientIDNum = patientIDNum.zfill(6)
                patientFile.close()
                return patientIDNum
        except:
            patientIDNum = '1'
            patientIDNum = str(patientIDNum)
            patientIDNum = patientIDNum.zfill(6)
            patientFile.close()
            return patientIDNum


def patientFileDataCheck():
    patientFile = open("patients.txt", "r")
    patientFileRead = patientFile.read()
    if '000001' in patientFileRead:
        patientIDNum = patientIDGenerator()
    else:
        patientIDNum = '000001'
    return patientIDNum


# def conversionDateString(date1):
#     from datetime import timedelta, date
#     import datetime
#     year, month, day = map(int, date1.split('-'))
#     date1 = datetime.date(year, month, day)
#     return date1


def vaccinationCenterInput():
    vcCenterOptions = ["VC1", "VC2"]
    vcCenter = input("\nEnter preferred vaccination center [VC1 or VC2]: ")
    while vcCenter not in vcCenterOptions:
        print("\nPlease input a valid vaccination center according to the options.")
        vcCenter = input("Enter preferred vaccination center  [VC1 or VC2]: ")
    return vcCenter


def patientNameInput(name):
    Name = True
    while Name:
        name = input("\nEnter name [AlexSmith]: ")
        if name.isalpha() and 3 <= len(name) <= 30:
            Name = False
        elif not name.isalpha():
            print("Only alphabets are allowed. Please do not use spaces.")
            continue
        elif not 3 <= len(name) <= 30:
            print("Name must be more than 4 characters and less than 10 characters.")
            continue
    return name


def patientAgeInput():
    try:
        age = int(input("\nEnter age [example: 19]: "))
    except:
        print("Invalid value. Please enter a proper age value.")
        age = int(input("\nEnter age [example: 19]: "))
    return age


def patientContactNumberInput(contactNum):
    number = True
    while number:
        contactNum = int(input("\nEnter contact number [example: 60123456789]: "))
        while len(str(contactNum)) != 11:
            print("\nInvalid contact number. Please try again with only numbers and no spaces.")
            contactNum = int(input("Enter contact number [example: 60123456789]: "))
        number = False
    return contactNum


def patientEmailInput():
    import re
    regex = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    emailAddress = True
    while emailAddress:
        userEmail = input("\nEnter email address [example: programuser@gmail.com]: ")
        if re.fullmatch(regex, userEmail):
            emailAddress = False
        else:
            print("Invalid email. Please enter a valid email address.")
            continue
        return userEmail


def ageVaccineChoices(age, vaccineChoice):
    if 12 <= age < 18:
        vaccineChoices = ["AF", "CZ", "DM"]
        print("\nVaccine choices:\n1. Vaccine AF \n2. Vaccine CZ \n3. Vaccine DM")
        vaccineChoice = input("Enter vaccine choice [AF,CZ,DM]: ")
        while vaccineChoice not in vaccineChoices:
            print("Invalid option. Please try again.")
            print("\nVaccine choices: \n1. Vaccine AF \n2. Vaccine CZ \n3. Vaccine DM")
            vaccineChoice = input("Enter vaccine choice [AF,CZ,DM]: ")

    elif 18 <= age <= 45:
        vaccineChoices = ["AF", "BV", "CZ", "DM", "EC"]
        print("\nVaccine choices: \n1. Vaccine AF \n2. Vaccine BV "
              "\n3. Vaccine CZ \n4. Vaccine DM \n5. Vaccine EC")
        vaccineChoice = input("Enter vaccine choice [AF,BV,CZ,DM,EC]: ")
        while vaccineChoice not in vaccineChoices:
            print("Invalid option. Please try again.")
            print("\nVaccine choices: \n1. Vaccine AF \n2. Vaccine BV \n3. Vaccine CZ \n4. Vaccine DM \n5. "
                  "Vaccine EC")
            vaccineChoice = input("Enter vaccine choice [AF,BV,CZ,DM,EC]: ")

    elif 45 < age < 100:
        vaccineChoices = ["AF", "BV", "CZ", "EC"]
        print("Vaccine choices: \n1. Vaccine AF \n2. Vaccine BV \n3. Vaccine CZ \n4. Vaccine EC")
        vaccineChoice = input("Enter vaccine choice [AF,BV,CZ,EC]: ")
        while vaccineChoice not in vaccineChoices:
            print("Invalid option. Please try again.")
            print("Vaccine choices: 1. Vaccine AF \n2. Vaccine CZ \n3. Vaccine DM \n4. Vaccine EC")
            vaccineChoice = input("Enter vaccine choice [AF,BV,CZ,EC]: ")

    elif age < 12:
        print("Age is too young. Patient ineligible for vaccine.")

    elif age > 100:
        print("Too old for vaccination. Patient ineligible for vaccine.")

    return vaccineChoice


def dateConversion(doseDate):
    from datetime import timedelta, date
    import datetime
    dateValue = doseDate
    year, month, day = map(int, dateValue.split('-'))
    dateValue = datetime.date(year, month, day)
    return dateValue


def firstDoseCalculator():
    from datetime import timedelta, date
    import datetime
    dateValue = str(date.today() + timedelta(days=3))
    return dateValue


def secondDoseCalculatorAF(date1):
    from datetime import timedelta, date
    import datetime
    dateValue = date1
    year, month, day = map(int, dateValue.split('-'))
    dateValue = datetime.date(year, month, day)
    dateValue2 = dateValue + timedelta(days=14)
    return dateValue2


def secondDoseCalculatorBVAndCZ(date1):
    from datetime import timedelta, date
    import datetime
    dateValue = date1
    year, month, day = map(int, dateValue.split('-'))
    dateValue = datetime.date(year, month, day)
    dateValue2 = dateValue + timedelta(days=21)
    return dateValue2


def secondDoseCalculatorDM(date1):
    from datetime import timedelta, date
    import datetime
    dateValue = date1
    year, month, day = map(int, dateValue.split('-'))
    dateValue = datetime.date(year, month, day)
    dateValue2 = dateValue + timedelta(days=28)
    return dateValue2


def displayPatientDetails(detail1, detail2, detail3, detail4, detail5, detail6, detail7):
    print("\nFull Patient Details: ")
    print("Patient ID               : " + str(detail1))
    print("Patient name             : " + str(detail2))
    print("Chosen vaccination center: " + str(detail3))
    print("Patient age              : " + str(detail4))
    print("Patient contact number   : " + str(detail5))
    print("Patient email address    : " + str(detail6))
    print("Patient vaccine choice   : " + str(detail7))
    return detail1, detail2, detail3, detail4, detail5, detail6, detail7


def patientIDInput(patientIDCode):
    userID = True
    while userID:
        patientIDCode = str(input("Please enter your patient ID [example: 0123456]: "))
        if patientIDCode.isnumeric():
            userID = False
        elif not patientIDCode.isnumeric():
            print("Invalid patient ID number.")
            continue
    return patientIDCode


def doseNumberInput(doseNumber):
    doseNumbers = ["D1", "D2"]
    doseNumber = input("Please enter your current status [example: 'D1' if  Dose 1 received and 'D2' for Dose 2 received]: ")
    while doseNumber not in doseNumbers:
        print("Invalid dose number.")
        doseNumber = input("Please enter your current status [example: 'D1' if  Dose 1 received and 'D2' for Dose 2 received]: ")
    return doseNumber


def recordPatientRegistrationDetails(detail1, detail2, detail3, detail4, detail5, detail6, detail7, detail8, detail9):
    patientLog = open("patients.txt", "a")
    patientLog.write("\n" + str(detail1))
    patientLog.write("\t" + str(detail2))
    patientLog.write("\t" + str(detail3))
    patientLog.write("\t" + str(detail4))
    patientLog.write("\t" + str(detail5))
    patientLog.write("\t" + str(detail6))
    patientLog.write("\t" + str(detail7))
    patientLog.write("\t" + str(detail8))
    patientLog.write("\t" + str(detail9) + "\n")
    patientLog.close()
    return detail1, detail2, detail3, detail4, detail5, detail6, detail7, detail8


def recordPatientVaccinationDetails(detail1, detail2, detail3, detail4, detail5, detail6, detail7, detail8, detail9):
    patientLog = open("vaccination.txt", "a")
    patientLog.write("\n" + str(detail1))
    patientLog.write("\t" + str(detail2))
    patientLog.write("\t" + str(detail3))
    patientLog.write("\t" + str(detail4))
    patientLog.write("\t" + str(detail5))
    patientLog.write("\t" + str(detail6))
    patientLog.write("\t" + str(detail7))
    patientLog.write("\t" + str(detail8))
    patientLog.write("\t" + str(detail9) + "\n")
    patientLog.close()


def statusValidation(patientIDCode):
    patientFile = open("vaccination.txt", "r")
    patientFileRead = (patientFile.read())
    patientFileRead = patientFileRead.split()
    count = 0
    for ID in patientFileRead:
        if ID == patientIDCode:
            count += 1
    patientFile.close()
    return count


def displayPatientStatus(detail1, detail2, detail3, detail4, detail5, detail6, detail7, detail8):
    print("\nFull patient details: ")
    print("Patient ID               : " + str(detail1))
    print("Patient name             : " + str(detail2))
    print("Chosen vaccination center: " + str(detail3))
    print("Patient age              : " + str(detail4))
    print("Patient contact number   : " + str(detail5))
    print("Patient email address    : " + str(detail6))
    print("Patient vaccine choice   : " + str(detail7))
    print("Patient vaccine status   : " + str(detail8))

    if detail7 == 'EC':
        print("Required dosage          : 1 ")
    elif detail7 != 'EC':
        print("Required dosage          : 2 ")

    if detail8 == 'D1':
        print(" ------------------COMPLETED D1--------------- ")
    elif detail8 == 'D2':
        print(" ------------------COMPLETED D2--------------- ")


def vaccinationStatistics():
    vaccinationFile = open("vaccination.txt", "r")
    vc2D1Count = 0
    vc2D2Count = 0
    vc2ECCount = 0
    vc1D1Count = 0
    vc1D2Count = 0
    vc1ECCount = 0

    vaccinationStats = True
    while vaccinationStats:
        vaccinationStats = vaccinationFile.readline()
        fileContents = vaccinationStats.split()

        if 'D2' in fileContents:
            if 'VC2' in fileContents:
                vc2D2Count += 1
            elif 'VC1' in fileContents:
                vc1D2Count += 1
        elif 'D1' in fileContents:
            if 'VC2' in fileContents:
                vc2D1Count += 1
                if 'EC' in fileContents:
                    vc2ECCount += 1
            elif 'VC1' in fileContents:
                vc1D1Count += 1
                if 'EC' in fileContents:
                    vc1ECCount += 1


    print("\n__________________ VACCINATION CENTER 1 STATISTICS __________________")
    print(f"Number of patients who received both doses              : {vc1D2Count}")
    print(f"Number of patients who are waiting for Dose 2           : {vc1D1Count - vc1D2Count - vc1ECCount}")
    print(f"Number of patients who received EC vaccine              : {vc1ECCount}")
    print(f"Number of patients who completed the vaccination process: {vc1D2Count + vc1ECCount}")

    print("\n__________________ VACCINATION CENTER 2 STATISTICS __________________ ")
    print(f"Number of patients who received both doses              : {vc2D2Count}")
    print(f"Number of patients who are waiting for Dose 2           : {vc2D1Count - vc2D2Count - vc2ECCount}")
    print(f"Number of patients who received EC vaccine              : {vc2ECCount}")
    print(f"Number of patients who completed the vaccination process: {vc2D2Count + vc2ECCount}")


def menu():
    print("\nWelcome to the COVID-19 Vaccination Record Management System.")
    while True:
        print("\nPlease select your purpose based on the options below.")
        print("\nSystem Options: \n1. Patient Registration \n2. Vaccine Administration "
              "\n3. Patient Records and Vaccination Status \n4. Vaccination Statistics \n5. End Program")
        appOptions = input("\nEnter your purpose here [1, 2, 3, 4 or 5]: ")

        if appOptions == '1':
            patientID = patientFileDataCheck()
            vcOption = vaccinationCenterInput()
            patientName = patientNameInput(name=1)
            patientAge = patientAgeInput()
            patientContactNum = patientContactNumberInput(contactNum=1)
            patientEmail = patientEmailInput()
            vaccine = ageVaccineChoices(patientAge, vaccineChoice=1)
            dose1Date = firstDoseCalculator()
            displayPatientDetails(patientID, patientName, vcOption, patientAge, patientContactNum, patientEmail,
                                  vaccine)
            print("Patient vaccine status   : D0")
            print("Vaccination Date         : " + dose1Date)
            recordPatientRegistrationDetails(patientID, patientName, vcOption, patientAge, patientContactNum,
                                             patientEmail, vaccine, "D0", dose1Date)

        elif appOptions == '2':
            print("\nWelcome to the Vaccine Administration Section.")
            doseOne = ["D1"]
            doseTwo = ["D2"]
            patientID = patientIDInput(patientIDCode=1)
            doseNumber = doseNumberInput(doseNumber=1)
            repetitionCounter = statusValidation(patientID)
            if repetitionCounter == 2:
                patientFile = open("vaccination.txt", "r")
                vaccinationInfo = []
                for vaccinationInfo in patientFile:
                    vaccinationInfo = vaccinationInfo.split()
                    if str(patientID) in str(vaccinationInfo):
                        if "D2" in str(vaccinationInfo):
                            print("\nYou have already received both doses. Please stay safe and have a nice day.")
                            displayPatientDetails(vaccinationInfo[0], vaccinationInfo[1], vaccinationInfo[2],
                                                  vaccinationInfo[3], vaccinationInfo[4], vaccinationInfo[5],
                                                  vaccinationInfo[6])
                            print("Patient vaccine status   : " + vaccinationInfo[7])
                            print("\n--------------Vaccination Completed--------------")

            elif repetitionCounter == 1:
                patientFile = open("vaccination.txt", "r")
                vaccinationInfo = []
                for vaccinationInfo in patientFile:
                    vaccinationInfo = vaccinationInfo.split()
                    if str(patientID) in str(vaccinationInfo):
                        if "D1" in vaccinationInfo and doseNumber in doseOne:
                            if 'EC' not in vaccinationInfo:
                                if 'AF' == vaccinationInfo[6]:
                                    dose2Date = secondDoseCalculatorAF(vaccinationInfo[8])
                                if 'BV' == vaccinationInfo[6] or 'CZ' == vaccinationInfo[6]:
                                    dose2Date = secondDoseCalculatorBVAndCZ(vaccinationInfo[8])
                                if 'DM' == vaccinationInfo[6]:
                                    dose2Date = secondDoseCalculatorDM(vaccinationInfo[8])
                                print("\nDose 1 has already been received. You are supposed to receive your 2nd dose.")
                                print("Please enter patient ID again and enter the correct vaccination status.")

                            elif 'EC' in vaccinationInfo:
                                print("\nEC vaccine only requires one dose. Stay safe and have a nice day.\n")
                                displayPatientDetails(vaccinationInfo[0], vaccinationInfo[1], vaccinationInfo[2],
                                                      vaccinationInfo[3], vaccinationInfo[4], vaccinationInfo[5],
                                                      vaccinationInfo[6])
                                print("Patient vaccine status   : " + "D1")
                                print("\n--------------Vaccination Completed--------------")

                        elif "D1" in vaccinationInfo and doseNumber in doseTwo:
                            if 'EC' not in vaccinationInfo:
                                if 'AF' == vaccinationInfo[6]:
                                    dose2Date = secondDoseCalculatorAF(vaccinationInfo[8])
                                if 'BV' == vaccinationInfo[6] or 'CZ' == vaccinationInfo[6]:
                                    dose2Date = secondDoseCalculatorBVAndCZ(vaccinationInfo[8])
                                if 'DM' == vaccinationInfo[6]:
                                    dose2Date = secondDoseCalculatorDM(vaccinationInfo[8])
                                print("\nYou have already received both doses. Please stay safe and have a nice day.")
                                displayPatientDetails(vaccinationInfo[0], vaccinationInfo[1], vaccinationInfo[2],
                                                      vaccinationInfo[3], vaccinationInfo[4], vaccinationInfo[5],
                                                      vaccinationInfo[6])
                                print("Patient vaccine status   : " + "D2")
                                print("Dose 2 vaccination date  : " + str(dose2Date))
                                print("\n--------------Vaccination Completed--------------")
                                recordPatientVaccinationDetails(vaccinationInfo[0], vaccinationInfo[1],
                                                                vaccinationInfo[2], vaccinationInfo[3],
                                                                vaccinationInfo[4], vaccinationInfo[5],
                                                                vaccinationInfo[6], "D2", dose2Date)
                            elif 'EC' in vaccinationInfo:
                                displayPatientDetails(vaccinationInfo[0], vaccinationInfo[1], vaccinationInfo[2],
                                                      vaccinationInfo[3], vaccinationInfo[4], vaccinationInfo[5],
                                                      vaccinationInfo[6])
                                print("Patient vaccine status   : " + "D1")
                                print("\n--------------Vaccination Completed--------------")
                            break

            elif repetitionCounter == 0:
                patientFile = open("patients.txt", "r")
                vaccinationInfo = []
                for vaccinationInfo in patientFile:
                    vaccinationInfo = vaccinationInfo.split()
                    if str(patientID) in str(vaccinationInfo):
                        if doseNumber in doseOne:
                            if 'EC' in vaccinationInfo:
                                dose1Date = dateConversion(vaccinationInfo[8])
                                displayPatientDetails(vaccinationInfo[0], vaccinationInfo[1], vaccinationInfo[2],
                                                      vaccinationInfo[3], vaccinationInfo[4], vaccinationInfo[5],
                                                      vaccinationInfo[6])
                                print("Patient vaccine status   : " + "D1")
                                print("\n--------------Vaccination Completed--------------")
                                recordPatientVaccinationDetails(vaccinationInfo[0], vaccinationInfo[1],
                                                                vaccinationInfo[2], vaccinationInfo[3],
                                                                vaccinationInfo[4], vaccinationInfo[5],
                                                                vaccinationInfo[6], "D1", dose1Date)

                            elif 'EC' not in vaccinationInfo:
                                dose1Date = dateConversion(vaccinationInfo[8])
                                if 'AF' == vaccinationInfo[6]:
                                    dose2Date = secondDoseCalculatorAF(vaccinationInfo[8])
                                if 'BV' == vaccinationInfo[6] or 'CZ' == vaccinationInfo[6]:
                                    dose2Date = secondDoseCalculatorBVAndCZ(vaccinationInfo[8])
                                if 'DM' == vaccinationInfo[6]:
                                    dose2Date = secondDoseCalculatorDM(vaccinationInfo[8])
                                print(f"\nPlease visit {vaccinationInfo[2]} for your second dose on {dose2Date}.\n")
                                displayPatientDetails(vaccinationInfo[0], vaccinationInfo[1], vaccinationInfo[2],
                                                      vaccinationInfo[3], vaccinationInfo[4], vaccinationInfo[5],
                                                      vaccinationInfo[6])
                                print("Patient vaccine status   : " + "D1")
                                print("Dose 1 vaccination date  : " + str(dose1Date))
                                print("Dose 2 vaccination date  : " + str(dose2Date))
                                recordPatientVaccinationDetails(vaccinationInfo[0], vaccinationInfo[1],
                                                                vaccinationInfo[2], vaccinationInfo[3],
                                                                vaccinationInfo[4], vaccinationInfo[5],
                                                                vaccinationInfo[6], "D1", dose1Date)

                        if doseNumber in doseTwo:
                            print("\nFirst dose must be taken before second dose.")

        elif appOptions == '3':
            patientID = patientIDInput(patientIDCode=1)
            doseCount = statusValidation(patientID)
            if doseCount >= 1:
                vaccinationFile = open("vaccination.txt", "r")
                vaccinationInfo = []
                for vaccinationInfo in vaccinationFile:
                    vaccinationInfo = vaccinationInfo.split()
                    if str(patientID) in str(vaccinationInfo):
                        if doseCount >= 1:
                            displayPatientStatus(vaccinationInfo[0], vaccinationInfo[1], vaccinationInfo[2],
                                                 vaccinationInfo[3], vaccinationInfo[4], vaccinationInfo[5],
                                                 vaccinationInfo[6], vaccinationInfo[7])

            elif doseCount == 0:
                patientFile = open("patients.txt", "r")
                patientInfo = []
                for patientInfo in patientFile:
                    patientInfo = patientInfo.split()
                    if str(patientID) in str(patientInfo):
                        displayPatientStatus(patientInfo[0], patientInfo[1], patientInfo[2], patientInfo[3],
                                             patientInfo[4], patientInfo[5], patientInfo[6], patientInfo[7])

        elif appOptions == '4':
            vaccinationStatistics()

        elif appOptions == '5':
            print("Thank you for using the program. Have a nice day.")
            exit()

        else:
            print("\nThe app has no such option. Please try again with one of the system options given.")


menu()
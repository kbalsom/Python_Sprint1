# Program written for NL Chocolate Company to Process Travel Claims.
# Written by: Ian Collins & Kara Balsom
# Date Written: February 25 - March 1, 2022
# Main menu, and Options 1 and 2 created by Ian Collins
# Options 2 and 3 created by Kara Balsom

# Import Libraries:

import datetime as DT
import matplotlib.pyplot as plt

# Constants:
DAILYRATE = 85.00
# To be multiplied by the total days
MILEAGEOWNED = 0.17
# per KM if employee used their own vehicle
MILEAGERENT = 65.00
# per day if employee rented vehicle
BONUS3DAYS = 100.00
# added to bonus if number of days is greater than 3
BONUSKMOWN = .04
# per kilometer if kilometers are over 1000 and employee used their own car
BONUSEXEC = 45.00
# per day if the claim type is executive
BONUSHOLIDAY = 50.00
# per day if between Dec 15th and 22nd
HSTRATE = .15
# HST rate to be multiplied by per diem.

# Functions for Program:

def fDollar(DollarValue):
    # Function to set up Dollar value formats.
    # Parameter: DollarValue
    # Return Value: DollarValueDSP

    DollarValueDSP = f"${DollarValue:,.2f}"
    return DollarValueDSP

def IsPhone(PhoneNum):
    # Function to validate Phone Number
    # Parameter: PhoneNum
    # Return Value: PhoneNum


    if PhoneNum == "":
        print("Phone Number cannot be blank -Please re-enter.")
    elif len(PhoneNum) != 10:
        print("Phone number must be 10 digits - Please re-enter.")
    elif PhoneNum.isdigit() == False:
        print("Phone number can only contain numbers - Please re-enter.")
    else:
        return PhoneNum


selection = []

# Program for Option 1 - Employee Travel Claims:

def OptionOne():


    # Start Loop:
    while True:

        # Input prompts for the user and validations:
        while True:
            # The employee number, limited to 5 characters.
            empNumber = input("Enter the Employee Number (11111): ").upper()
            if len(empNumber) != 5:
                print("Employee Number must be 5 characters - Please re-enter.")
            else:
                break

        while True:
            # The first name of the employee.
            empNameFirst = input("Enter the Employee's First Name: ").title()
            if empNameFirst == "":
                print("Employee Name can not be Blank - Please re-enter.")
            else:
                break

        while True:
            # The last name of the employee.
            empNameLast = input("Enter the Employee's Last Name: ").title()
            if empNameLast == "":
                print("Employee Name can not be Blank - Please re-enter.")
            else:
                break

        while True:
            # Location of trip input.
            tripLoc = input("Enter the Location of the Trip: ").title()
            if tripLoc == "":
                print("Trip Location can not be Blank - Please re-enter.")
            else:
                break

        while True:
            # Start date calculations.
            try:
                dateStart = input("Enter the Start Date of the Trip (DD-MM-YYY): ")
                dateStart = DT.datetime.strptime(dateStart, "%d-%m-%Y")
            except:
                print("Start Date not entered in Valid Format (DD-MM-YYY) - Please re-enter.")
            else:
                break

        while True:
            # End date and Difference in date calculations
            try:
                dateEnd = input("Enter the End Date of the Trip (DD-MM-YYYY): ")
                dateEnd = DT.datetime.strptime(dateEnd, "%d-%m-%Y")
                dateDiff = (dateEnd - dateStart).days
            except:
                print("End Date not entered in Valid Format (DD-MM-YYY) - Please re-enter.")
            if dateDiff < 1:
                print("End Date can not be Earlier than or the Same Date as the Start Date - Please re-enter.")
            elif dateDiff > 7:
                print("End Date can not be Greater than Seven Days - Please re-enter.")
            else:
                break

        while True:
            # Did the employee use their own car or rent one?
            carStatus = input("Enter if the Employee used their Own Car, or a Rental (O or R): ").upper()
            if carStatus != "O" and carStatus != "R":
                print("\"O\" or \"R\" Not Entered - Please re-enter.")
            elif carStatus == "O":
                while True:
                    # Only needed if employee used their own car
                    totKM = input("Enter the Total Kilometers Travelled (Must not Exceed 2000): ")
                    if totKM.isdigit() == False:
                        print("Total kilometers must be Entered as a Number - Please re-enter.")
                    elif int(totKM) > 2000:
                        print("Total Kilometers must Not Exceed 2000 - Please re-enter.")
                    else:
                        totKM = int(totKM)
                        break
                break
            else:
                break

        while True:
            # Is the claim executive or standard?
            claimType = input("Enter if the Claim is Executive or Standard (E or S): ").upper()
            if claimType != "E" and claimType != "S":
                print("\"E\" or \"S\" Not Entered - Please re-enter.")
            else:
                if claimType == "E":
                    claimPrint = "Executive"
                else:
                    claimPrint = "Standard"
                break

        # Calculations:

        perDiem = dateDiff * DAILYRATE
        if carStatus == "O":
            milAmt = MILEAGEOWNED * totKM
        else:
            milAmt = MILEAGERENT * dateDiff
        if dateDiff > 3:
            bonusDate = BONUS3DAYS
        else:
            bonusDate = 0
        if carStatus == "O" and totKM > 1000:
            bonusKM = BONUSKMOWN * totKM
        else:
            bonusKM = 0
        if claimType == "E":
            bonusClaim = BONUSEXEC * dateDiff
        else:
            bonusClaim = 0
        if dateStart.month == 12 and 22 >= dateStart.day >= 15:
            bonusHoliday = BONUSHOLIDAY * dateDiff
        else:
            bonusHoliday = 0
        bonusTotal = bonusKM + bonusDate + bonusHoliday + bonusClaim
        HST = perDiem * HSTRATE
        claimAmt = perDiem + milAmt + bonusTotal
        claimTotal = claimAmt + HST
        if carStatus == "O":
            rentalUsed = "No"
        else:
            rentalUsed = "Yes"

        # Output to the user.
        print()
        print("NL Chocolate Company Travel Claim")
        print("-" * 40)
        print(f"Employee: {empNameFirst} {empNameLast}")
        print(f"Number:   {empNumber}")
        print("-" * 40)
        print(f"Trip Location:{tripLoc:>26}")
        print(f"Rental used:{rentalUsed:>28}")
        while True:
            if carStatus == "O":
                print(f"Total Kilometers Travelled:{totKM:>13}")
                break
            else:
                break
        dateStartDSP = f"{dateStart:%d-%m-%Y}"
        print(f"Start date of trip:{dateStartDSP:>21}")
        dateEndDSP = f"{dateEnd:%d-%m-%Y}"
        print(f"End date of trip:  {dateEndDSP:>21}")
        if dateDiff > 1:
            print(f"Total trip length: {dateDiff:>16} days")
        else:
            print(f"Total trip length: {dateDiff:>17} day")
        if carStatus == "O":
            print(f"Number of Km travelled:{totKM:>17}")
        else:
            pass
        print("-" * 40)
        print(f"{claimPrint} claim")
        print("Bonuses")
        print(f"Fourth day bonus:{fDollar(bonusDate):>23}")
        print(f"Over 1000 Km bonus:{fDollar(bonusKM):>21}")
        print(f"Executive bonus:{fDollar(bonusClaim):>24}")
        print(f"Holiday bonus:{fDollar(bonusHoliday):>26}")
        print("{:>40}".format("---------"))
        print(f"Total Bonuses:{fDollar(bonusTotal):>26}")
        print("-" * 40)
        print(f"Mileage Rate:{fDollar(milAmt):>27}")
        print(f"Per Diem:{fDollar(perDiem):>31}")
        print(f"HST:{fDollar(HST):>36}")
        print(f"Claim Amount:{fDollar(claimAmt):>27}")
        print(f"Claim Total:{fDollar(claimTotal):>28}")
        print("-" * 40)
        # End statement to stay in claim program.
        contORquit = input("Enter another claim (Y or N)? ").upper()
        while True:
            if contORquit != "Y" and contORquit != "N":
                print("\"Y\" or \"N\" not entered, please re-enter.")
            elif contORquit == "Y":
                break
            else:
                return

selection.append(OptionOne)

# Program for Option 2 - FizzBuzz:
def OptionTwo():


    # Print numbers 1-100, with numbers divisible by 5 as Fizz,
    # divisible by 8 as Buzz, and divisible by both 8 and 5 as FizzBuzz.
    for num in range(1, 101):
        numFive = num / 5
        numEight = num / 8
        if numFive - int(numFive) == 0 and numEight - int(numEight) == 0:
            print("FizzBuzz")
        elif numFive - int(numFive) == 0:
            print("Fizz")
        elif numEight - int(numEight) == 0:
            print("Buzz")
        else:
            print(num)

    AnyKey = input("Press Any Key to Continue.")
    print()

selection.append(OptionTwo)

# Program for Option 3 - Cool Things with Dates and Strings:
def OptionThree():


    # Gather User Input and Validate:
    while True:
        EmpFirstName = input("Enter the Employee's First Name: ").title()
        if EmpFirstName == "":
            print("Employee's First Name cannot be blank - Please re-enter.")
        else:
            break

    while True:
        EmpLastName = input("Enter the Employee's Last Name: ").title()
        if EmpLastName == "":
            print("Employee's Last Name cannot be blank - Please re-enter.")
        else:
            break

    while True:
        PhoneNum = input("Enter Employee's Phone Number (0000000000): ")
        PhoneNumValid = IsPhone(PhoneNum)
        if PhoneNumValid == PhoneNum:
            break

    while True:
        try:
            EmpStartDate = input("Enter Employee Start Date (YYYY-MM-DD): ")
            EmpStartDate = DT.datetime.strptime(EmpStartDate, "%Y-%m-%d")
        except:
            print("Employee Start Date is not a valid format (YYYY-MM-DD) - Please re-enter.")
        else:
            break

    while True:
        try:
            EmpBirthDate = input("Enter Employee Birthdate (YYYY-MM-DD): ")
            EmpBirthDate = DT.datetime.strptime(EmpBirthDate, "%Y-%m-%d")
        except:
            print("Employee Birthdate is not a valid format (YYYY-MM-DD) - Please re-enter.")
        else:
            break

    # Cool Things with Dates and Strings (Calculations and Outputs):

    # Greet Employee with first initial and last name:
    print()
    print("Hello " + EmpFirstName[0] + ". " + EmpLastName)
    print()

    # Ask Employee if they are on a first name basis with the Program:
    while True:
        Polite = input("Can I call you {}? ( Y / N ): ".format(EmpFirstName)).upper()
        if Polite == "":
            print("Please enter Y for Yes, or N for No.")
        elif Polite != "Y" and Polite != "N":
            print("Please enter Y for Yes, or N for No.")
        else:
            break

    if Polite == "Y":
        PoliteDsp = "Hello {}! Here are some facts about you: ".format(EmpFirstName)
    else:
        PoliteDsp = "Forgive me for being presumptuous. Here are some facts about you: "

    print()
    print(PoliteDsp)
    print("----------------------------------------------------------------------------")

    # Display Employee ID (First Initial + Last Initial - Last Four Digits of Phone Number):

    EmpID = EmpFirstName[0] + EmpLastName[0] + "-" + PhoneNumValid[6: 11]
    print("Your ID Number is " + EmpID + ".")

    # Display how many days Employee has been alive:
    TimeSinceBirth = DT.datetime.today() - EmpBirthDate
    MinAlive = TimeSinceBirth.days

    print()
    print("You have been alive for " + str(MinAlive) + " days.")

    # How many days Employee has worked for company:

    TimeWorked = DT.datetime.today() - EmpStartDate
    MinWorked = TimeWorked.days

    print()
    print("You have worked here for " + str(MinWorked) + " days.")

    # What percent of their lives in days Employee has worked for company:

    PerLifeWorked = (MinWorked / MinAlive) * 100
    PerLifeWorkedDsp = round(PerLifeWorked, 2)
    print()

    if PerLifeWorked < 50:
        print("You have worked here for " + str(PerLifeWorkedDsp) + "% of your life. Keep going!")
    else:
        print("You have worked here for " + str(PerLifeWorkedDsp) + "% of your life. That's a long time!")

    # Program to find out what day of the week Employee was born on:
    print()
    DayBorn = DT.datetime.strftime(EmpBirthDate, "%A")
    print("You were born on a " + str(DayBorn) + ".")

    # Program to calculate Employee Horoscope:
    print()
    if EmpBirthDate.month == 1:
        if EmpBirthDate.day <= 19:
            print("You are a Capricorn.")
        else:
            print("You are an Aquarius.")
    elif EmpBirthDate.month == 2:
        if EmpBirthDate.day <= 18:
            print("You are an Aquarius.")
        else:
            print("You are a Pisces.")
    elif EmpBirthDate.month == 3:
        if EmpBirthDate.day <= 20:
            print("You are a Pisces.")
        else:
            print("You are an Aries.")
    elif EmpBirthDate.month == 4:
        if EmpBirthDate.day <= 19:
            print("You are an Aries.")
        else:
            print("You are a Taurus.")
    elif EmpBirthDate.month == 5:
        if EmpBirthDate.day <= 20:
            print("You are a Taurus.")
        else:
            print("You are a Gemini.")
    elif EmpBirthDate.month == 6:
        if EmpBirthDate.day <= 20:
            print("You are a Gemini.")
        else:
            print("You are a Cancer.")
    elif EmpBirthDate.month == 7:
        if EmpBirthDate.day <= 22:
            print("You are a Cancer.")
        else:
            print("You are a Leo.")
    elif EmpBirthDate.month == 8:
        if EmpBirthDate.day <= 22:
            print("You are a Leo.")
        else:
            print("You are a Virgo.")
    elif EmpBirthDate.month == 9:
        if EmpBirthDate.day <= 22:
            print("You are a Virgo.")
        else:
            print("You are a Libra.")
    elif EmpBirthDate.month == 10:
        if EmpBirthDate.day <= 22:
            print("You are a Libra.")
        else:
            print("You are a Scorpio.")
    elif EmpBirthDate.month == 11:
        if EmpBirthDate.day <= 21:
            print("You are a Scorpio.")
        else:
            print("You are a Sagittarius.")
    if EmpBirthDate.month == 12:
        if EmpBirthDate.day <= 21:
            print("You are a Sagittarius.")
        else:
            print("You are a Capricorn.")

    #  Program to calculate which Chinese Zodiac Year Employee was born in:
    print()
    if (EmpBirthDate.year - 2000) % 12 == 0:
        print("You were born in the Year of the Dragon. Your lucky numbers are 1, 6, and 7.")
    elif (EmpBirthDate.year - 2000) % 12 == 1:
        print("You were born in the Year of the Snake. Your lucky numbers are 2, 8, and 9.")
    elif (EmpBirthDate.year - 2000) % 12 == 2:
        print("You were born in the Year of the Horse. Your lucky numbers are 2, 3, and 7.")
    elif (EmpBirthDate.year - 2000) % 12 == 3:
        print("You were born in the Year of the Goat. Your lucky numbers are 2, and 7.")
    elif (EmpBirthDate.year - 2000) % 12 == 4:
        print("You were born in the Year of the Monkey. Your lucky numbers are 4, and 9.")
    elif (EmpBirthDate.year - 2000) % 12 == 5:
        print("You were born in the Year of the Rooster. Your lucky numbers are 5, 7, and 8.")
    elif (EmpBirthDate.year - 2000) % 12 == 6:
        print("You were born in the Year of the Dog. Your lucky numbers are 3, 4, and 9.")
    elif (EmpBirthDate.year - 2000) % 12 == 7:
        print("You were born in the Year of the Pig. Your lucky numbers are 2, 5, and 8.")
    elif (EmpBirthDate.year - 2000) % 12 == 8:
        print("You were born in the Year of the Rat. Your lucky numbers are 2, and 3.")
    elif (EmpBirthDate.year - 2000) % 12 == 9:
        print("You were born in the Year of the Ox. Your lucky numbers are 1, and 4.")
    elif (EmpBirthDate.year - 2000) % 12 == 10:
        print("You were born in the Year of the Tiger. Your lucky numbers are 1, 3, and 4.")
    else:
        print("You were born in the Year of the Rabbit. Your lucky numbers are 3, 4, and 6.")

    print()

    # Use AnyKey to Continue the Program:
    AnyKey = input("Press Any Key to Continue.")
    print()
selection.append(OptionThree)

# Program for Option 4 - Graph Monthly Claims Totals:
def OptionFour():


    # Gather the Total Sales Data for each month from user:
    print()
    print("Total Monthly Sales Graph")
    print("------------------------------------------------")
    while True:
        try:
            JanTot = float(input("Enter the Total Monthly Sales for January: "))
        except ValueError:
            print("Total Sales for January must be a number - Please re-enter.")
        else:
            break

    while True:
        try:
            FebTot = float(input("Enter the Total Monthly Sales for February: "))
        except ValueError:
            print("Total Sales for February must be a number - Please re-enter.")
        else:
            break

    while True:
        try:
            MarTot = float(input("Enter the Total Monthly Sales for March: "))
        except ValueError:
            print("Total Sales for March must be a number - Please re-enter.")
        else:
            break

    while True:
        try:
            AprTot = float(input("Enter the Total Monthly Sales for April: "))
        except ValueError:
            print("Total Sales for April must be a number - Please re-enter.")
        else:
            break

    while True:
        try:
            MayTot = float(input("Enter the Total Monthly Sales for May: "))
        except ValueError:
            print("Total Sales for May must be a number - Please re-enter.")
        else:
            break

    while True:
        try:
            JunTot = float(input("Enter the Total Monthly Sales for June: "))
        except ValueError:
            print("Total Sales for June must be a number - Please re-enter.")
        else:
            break

    while True:
        try:
            JulTot = float(input("Enter the Total Monthly Sales for July: "))
        except ValueError:
            print("Total Sales for July must be a number - Please re-enter.")
        else:
            break

    while True:
        try:
            AugTot = float(input("Enter the Total Monthly Sales for August: "))
        except ValueError:
            print("Total Sales for August must be a number - Please re-enter.")
        else:
            break

    while True:
        try:
            SepTot = float(input("Enter the Total Monthly Sales for September: "))
        except ValueError:
            print("Total Sales for September must be a number - Please re-enter.")
        else:
            break

    while True:
        try:
            OctTot = float(input("Enter the Total Monthly Sales for October: "))
        except ValueError:
            print("Total Sales for October must be a number - Please re-enter.")
        else:
            break

    while True:
        try:
            NovTot = float(input("Enter the Total Monthly Sales for November: "))
        except ValueError:
            print("Total Sales for November must be a number - Please re-enter.")
        else:
            break

    while True:
        try:
            DecTot = float(input("Enter the Total Monthly Sales for December: "))
        except ValueError:
            print("Total Sales for December must be a number - Please re-enter.")
        else:
            break

    # Make the list of data for the x-axis and y-axis
    x_axis = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    y_axis = [JanTot, FebTot, MarTot, AprTot, MayTot, JunTot, JulTot, AugTot, SepTot, OctTot, NovTot, DecTot]

    # Format the graph:
    plt.title("Total Sales by Month")
    plt.plot(x_axis, y_axis, color='red', marker='x')
    plt.xlabel("Month")
    plt.ylabel("Total Sales (dollars)")
    plt.grid(True)

    # Display the graph:
    plt.show()

    # Use AnyKey to Continue the program:
    AnyKey = input("Press Any Key to Continue.")
    print()


selection.append(OptionFour)

def OptionFive():


    print("Goodbye!")
    exit()

selection.append(OptionFive)

# Main menu for the program:
while True:
    print("---------------------------------------")
    print("         NL Chocolate Company")
    print("   Travel Claims Processing System")
    print("---------------------------------------")
    print("1. Enter an Employee Travel Claim.")
    print("2. Fun Interview Questions.")
    print("3. Cool Stuff with Strings and Dates.")
    print("4. Graph Monthly Claim Totals.")
    print("5. Quit Program.")
    print("---------------------------------------")
    print()
    while True:
        choice = input("Enter choice (1-5): ")
        if choice.isdigit() == False:
            print("Not a valid response, please re-enter.")
        else:
            choice = int(choice)
            if choice > 5 or choice < 1:
                print("Not a valid response, please re-enter.")
            else:
                break
    print()

    choice = selection[choice-1]
    choice()

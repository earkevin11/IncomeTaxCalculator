# input annual salary
# FICA, 401k, Insurance deductions
# need to calculate taxable income
import sys

GA_TAX = 0.0536 # GA STATE TAX
FICA = 0.0765 #this includes SSN and medicare
ga_taxDeductions = 0
fica_deductions = 0
# you are paid every other week. Some companies use this for hourly workers.
biweekly = 26
# this means twice a month so you are paid twice a month no matter what.
semimonthly = 24

grossmonthlyPaycheck = 0


def get_grossTakeHomePay():
    while True:
        income = input("What is your (before tax) gross yearly income? $")
        if income.isdigit():
            grossincome = int(income)
            break
        else:
            print("Please enter a valid input")
    return grossincome

    #         userPaycycle = input("Enter '1' if you are paid semi-monthly or Enter '2' if you are paid bi-weekly:")
    #         if int(userPaycycle) == 1:
    #             grossmonthlyPaycheck = int(income) / semimonthly
    #             break
    #
    #         if int(userPaycycle) == 2:
    #             grossmonthlyPaycheck = int(income) / biweekly
    #             break
    #
    #         else:
    #             print("Please enter a valid response.")
    #         # you must return the variable if you want to print it out in main
    #     else:
    #         print("Please enter a valid number for your gross yearly income")
    # return grossmonthlyPaycheck

def getContributionRate():
    while True:
        usercontributionRate = input("401k Contribution Rate:\n")
        if usercontributionRate.isdigit():
            contributionRate = int(usercontributionRate) / 100
            break
        else:
            print("Enter a valid contribution rate: ")
    return contributionRate

# calculates your federal income tax
def calculateTax (x):

    #this try block is where the error will occur. We want to check to see if the user inputs a number or string
    # try:
    #     income = int(input('What is your annual income? Please enter your taxable income please: '))
    # except ValueError: #this runs when there is an erroor
    #     print("Sorry, you must enter your income.")
    # else: #this follows the try block and runs if there is not error

        #2023 income tax bracket
        #10%
        #only the your income up to 11000 is taxed at 10%.
        # 10% of 11000 = 1100
        if x <= 11000:
            tax = (.10 * x)


        #12% of the difference of (44726-11001) = $33725 will be taxed.
        # (44726-11001) = $33725
        #12% of 33725 = $4047
        # 1100 + 4,047 = 5147
        elif x <= 44725:
            tax = 1100 + (.12 * (x - 1100))

        #22%
        # 95376 - 44726 = 50650
        # 22 of 50650 is 11,143
        elif x <= 95375:
            tax = 5147 + (.22 * (x - 44725))
            # 5147 + 11143 = 16,290
        #24%
        # 182101 - 95376 = 86725
        # 24% of 86725 = 20,814
        #20814 + 16290 = 37,104
        elif x <= 182100:
            tax = 16290 + (.24 * (x - 95375))
        #32%
        # 231251 - 182101 = 49,150
        # 49150 + 37104 = 86,254
        elif x <= 231250:
            tax = 37104 + (.32 * (x - 182100))

        #35% of
        # 578126 - 231251 = 346,875
        # 346,875 + 86254 = 433,129
        elif x <= 578125:
            tax = 86254 + (.35 * (x - 231250))
        #37%
        elif x >= 578125:
            tax = 433129 + (.37 * (x - 578125))

        remainder = (x - tax)
        effectiveTaxRate = round(tax / x, 2)

        return tax


def main():
    while True:
        choice = input("Would you like to calculate your take home pay? Enter (Yes) or (No) \n")

        if choice == "no":
            print("You entered 'No.' Have a good one!")
            return False

        if choice.lower() == "yes":
            grossPay = round(get_grossTakeHomePay(),2)
            retirementContributions = round((getContributionRate() * grossPay),2)
            #401k deductions reduces the taxable income****
            taxableIncome = grossPay - retirementContributions

            # Taxes on your taxable income
            ga_taxDeductions = round((taxableIncome * GA_TAX))
            #FICA = SSN, Medicare tax
            fica_deductions = round((taxableIncome * FICA),2)
            #federalIncomeTax = round(grossPay * calculateTax(taxableIncome))
            federalIncomeTax = round(calculateTax(taxableIncome))
            payCheck = round(taxableIncome - (ga_taxDeductions + fica_deductions + federalIncomeTax),2)
            #effectibe tax rate = total federal tax / taxable income
            effectiveTaxRate = round(federalIncomeTax/taxableIncome,2)
            uncleSamloot = str(federalIncomeTax + fica_deductions + ga_taxDeductions)

            print("\n")
            print("Gross Take Home Pay: $" + str(grossPay))
            print("401k contributions: $" + str(retirementContributions))
            print("Taxable Income: $" + str(taxableIncome))
            print("\n")
            print("Tax Details:")
            print("Federal Income Tax: $" + str(federalIncomeTax))
            print("Georgia State Income Tax: $" + str(ga_taxDeductions))

            print("FICA Taxes: $" + str(fica_deductions))
            print("Uncle Sam took: $" + uncleSamloot)


            print("Net Income: $" + str(payCheck))
            print("Effective Tax Rate: " + str(effectiveTaxRate) + "%")



            #print("Your Gross Take Home Pay is " + str(get_grossTakeHomePay()))


            #deductions = (get_grossTakeHomePay() * retirementcontributions()) - get_grossTakeHomePay()
            #print(str(deductions))
            #print(str(contributions()))

            #if input is numeric, request user to enter 'Yes' or 'No'
        elif choice.isnumeric():
            print(choice +" is a number. Please enter 'Yes' or 'No'.")

        elif choice != 'yes' or 'no':
            print(choice + " is not a valid response. Please enter 'Yes' or 'No'.")

main()





   #income = input("What is your gross yearly (before tax) income? $")
    #userOption = input("Are you paid twice a month (semi-monthly) or bi-weekly?")
    #contributions = input("Are you contributing to a 401k? Type Y or N.")



    #if contributions.lower() == 'y':
        #contributionRate = input("What is your contribution rate? ")
       # if contributionRate.isdigit():
            #takeHomePay = monthlyPaycheck - (monthlyPaycheck * int(contributionRate) / 100)
           # break

        #else:
          #  print("Please enter a digit for your 401k contribution rate. ")
  #  else: #this part still needs to be processed even though user may not contribute to 401k.
  #      ga_taxDeductions = monthlyPaycheck - (monthlyPaycheck*GA_TAX)
  #      fica_deductions = monthlyPaycheck - (monthlyPaycheck*FICA)
   #     takeHomePay = (ga_taxDeductions + fica_deductions) - monthlyPaycheck
  #  break


#print("Your Gross Annual Income:$", income)
#print("")
#print("Your Gross Income Per Paycheck is $" + str(monthlyPaycheck))
#print("")
#print("Your Take Home Pay is $" + str(takeHomePay))

#print("Tax Bill:$", tax, )
#print("Net income: $", remainder)

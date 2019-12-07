print("Welcome to the credit card eligibility analyzer")
print("*"*50)
try:
    age = int(input("Enter your age   "))
    is_valid_age = bool(age >= 18 and age <=65)
    if is_valid_age == False:
        while is_valid_age == False:
            print("Please provide the correct age")
            age = int(input("Enter your age   "))
            is_valid_age = bool(age >= 18 and age <=65)
    
except NameError:
    print("You did not enter the valid age.")
except ValueError:
    print("You did not enter the valid age")

monthly_income = int(input("Enter your monthy income  "))
annual_income = monthly_income*12
print(f"your annual income is {annual_income}")
high_income = annual_income >= 300000

credit_score = True

student = False

if is_valid_age and high_income and credit_score and not student:
    print("You are eligible for credit card")
else:
    print("You are not eligible for credit card")
print("Thank you for analyzing you credit card eligibility")
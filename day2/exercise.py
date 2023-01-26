# "Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old."

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

limit_day = 32850
limit_week = 4680
limit_month = 1080

current_day = int(age) * 365
current_week = int(age) * 52
current_month = int(age) * 12

remaining_days = limit_day - current_day
remaining_weeks = limit_week - current_week
remaining_months = limit_month - current_month

print(f'You have {remaining_days} days, {remaining_weeks} weeks, and {remaining_months} months left.')   

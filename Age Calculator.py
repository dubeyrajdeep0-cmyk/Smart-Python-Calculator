birth_day = int(input("Enter birth day : "))
birth_month = int(input("Enter birth month : "))
birth_year = int(input("Enter birth year : "))
today_day = int(input("Enter today day : "))
today_month = int(input("Enter today month : "))
today_year = int(input("Enter today year : "))

age_year = today_year - birth_year
if (today_month, today_day) < (birth_month, birth_day):
    age_year -= 1
if birth_month == today_month :
    if birth_day < today_day :
         age_month = 0
    else :
        age_month = 11
elif birth_month < today_month :
    if today_month - birth_month == 1 :
        if today_day < birth_day :
            age_month = 0
        else :
            age_month = 1
    else :
        age_month = today_month - birth_month
else :
    if birth_day - today_day == 1 :
        if today_day < birth_day :
            age_month = 0
        else :
            age_month = 1
    else :
        age_month = 12 + today_month - birth_month
age_day = birth_day - today_day

if birth_day < today_day :
    age_day = today_day - birth_day
else :
    age_day = 30 - birth_day + today_day

print("Your age is", age_year ,"year", age_month ,"month", age_day ,"day")
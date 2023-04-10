#functions with output
#def formar_name(f_name, l_name):
    #to format a name the fuction title can be used
#    fname = f_name.title()
#    lname = l_name.title()
#    print(f"{fname} {lname}")
#formar_name('HUZZAIN', "OLAIde")


#def formar_name(f_name, l_name):
    #to format a name the fuction title can be used and printed using return fuction
#    fname = f_name.title()
#    lname = l_name.title()
#    return f"{fname} {lname}"
#print(formar_name('HUZZAIN', "OLAIde"))

def is_leap (year):
    if year % 4 == 0:
        return True
    if not year % 4 == 0:
        return False
    
        
    
def days_in_month(year,month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year)== True and month == 2:
        return 29
    return month_days[month - 1]

#    return f"there are {current_month} days in the month"

year = int(input("Enter a year"))
month = int(input("Enter a month"))
days = days_in_month(year, month)
print (days)


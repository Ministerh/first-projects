#dicttionaies
#Dictionary_in_programming = {'bug':'An error in a programming that prevents the program from running as expected', 'function':'a piece of code that can easily be called over and over again.', }

#to display a particular word in programming dictionary use the keyword
#print(Dictionary_in_programming['bug'])

#To add a new word to the dictionary
#Dictionary_in_programming['loop'] = 'The action of doing samething over and over again'
#print(Dictionary_in_programming)

#to create an empty dictionary i.e things will be added later
#empty_dictionary = {}

#to wipe existing dictionary
#Dictionary_in_programming = {}
#print(Dictionary_in_programming)

#To edit existong value in the dcitonary, tap into the dic. using keyword and then redefine
#Dictionary_in_programming['bug'] = 'A moth the computer'
#print(Dictionary_in_programming)

#to loop through a dictionary
#for key in Dictionary_in_programming:
#    print(key)
#    prin t(Dictionary_in_programming[key])

#grading students
student_scores = {'Harry':81, 'Ron':78, 'Hermione': 99, 'Draco':74, 'Neville':62}
student_grades = {}
#for student in student_scores:
#    score = student_scores[student] 
#    if score > 90:
#        student_grades[student] = 'Outstanding'
#    elif score > 80:
#        student_grades[student] ='Exceeds expectation'
#    elif score > 70:
#        student_grades[student] = 'Acceptable'
#    else:
#        student_grades[student] = 'Fail'
#print(student_grades)

#Nesting a list in a dictionary

#travel_logs = {'Ogun': ['Abeokuta', 'Sango', "Ifo", 'Agbara' ],
#'Lagos':['Ikeja', 'V.I', 'Alaba', 'Oshodi']}

#Nesting dictionaries inside dictonary

#travel_logs = {"Ogun": {'cities_visited':['Abeokuta', 'Sango', "Ifo", 'Agbara' ], "total_visits": 10},
#'Lagos':{'cities_visited':['Ikeja', 'V.I', 'Alaba', 'Oshodi'], 'total_visits': 7}}

#nesting a dictionary in a list

#travel_logs = [
#    {'state':'Ogun' ,
#'cities_visited':['Abeokuta', 'Sango', "Ifo", 'Agbara' ], 
#'toatal_visits':10
#},
#{
#    'state':'Lagos',
#    'cities_visited':['Ikeja', 'V.I', 'Alaba', 'Oshodi'],
#     'total_visits': 7}
#]

#travel_logs.append({'state':'Abuja', "cities_visited":['madachi','masaru', 'inna'], 'total_visits': 5})
#def add_new_log(country_visited, cities_visite, num_of_times):
#    new_log = {}
#    new_log['state'] = country_visited
#    new_log['cities_visited'] = cities_visite
#    new_log['total_visits'] = num_of_times
#    travel_logs.append(new_log) 

#add_new_log('Abuja',['madachi','masaru', 'inna'], 5)

#print(travel_logs)


from auctionart import logo
print (logo)
print("Welcome to the secret auction program")
def highest_bidder(bidder):
    highest  = 0
    winner = ""
    for key in bids:
        current_bid = bids[key]
        if current_bid > highest:
            highest = current_bid
            winner = highest
    print(winner)
bids = {}
bidding = True
while bidding:
    user_name  = input("what is your name?: ")
    user_bid = int(input("What is your bid: $"))
    bids[user_name] = user_bid
    rebid = input("Are there any other bidders? type 'yes' or 'no'").lower()
    if rebid == 'no':
        bidding = False
        highest_bidder(bids)
    elif rebid == 'yes':
        print('restart')

#for n in diction:
#        if n > highest:
#                highest = n
#                print(highest)
   






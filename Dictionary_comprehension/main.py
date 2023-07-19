import random
name = ["Alex", "Bath", "caroline", "Dave", "Eleanor", "Freddle", "Kessie"]
students_score ={student: random.randint(1, 100)for student in name}
promtoted_student = {student:score for (student, score) in students_score.items() if score >= 60}
#print(promtoted_student)
#print(students_score)
# print out the number of each words
sentence =  "What is the Airspeed Velocity of an Unladen Swallow?"
num_of_word = {word:len(word) for word in sentence.split()}
#print(num_of_word)

weather_c= {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday":15,
    "Thursday":14,
    "Friday":21,
    "Saturday": 22,
    "Sunday":24
}

weather_f = {day:(temp * 9/5) + 32 for (day, temp) in weather_c.items()
}
#print(weather_f)
student_dic = {
    "student": ["Huzzain", "Wahab", "Malik", "sherifdeen"],
    "score": [55, 60, 75, 40]
}
#for looping thorugh dictionary
#for (key, value) in student_dic.items():
    #print(key)

import pandas

#student_data_frame = pandas.DataFrame(student_dic)
#print(student_data_frame)

#To loop thorugh data frame
#for (key, value) in student_data_frame.items():
#    print(value)

#Using pandas in built iterrows to iterate throug dataframe
#for (index, row) in student_data_frame.iterrows():
    #the returned row is a panda series datarame
#    print(row.student)

data = pandas.read_csv("./Dictionary_comprehension/nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

def phonetic():
    word = input("Enter a word from A to T ").upper()
    try:
    #to create a list of phonetic codeANT words from the input
        output = [phonetic_dict[letter] for letter in word]

    except KeyError:
        print("Sorry only letters in the alphabet please")
    else:
        print(output)
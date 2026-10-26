students = [
    {"name": "Lara",  "age": 23, "track": "AI",   "hours_studied": 40, "scores": [85, 90, 78]},
    {"name": "Omar",  "age": 31, "track": "Data", "hours_studied": 12, "scores": [60, 55, 70]},
    {"name": "Rim",   "age": 27, "track": "AI",   "hours_studied": 55, "scores": [95, 88, 92]},
    {"name": "Karim", "age": 19, "track": "Web",  "hours_studied": 8,  "scores": [50, 65, 40]},
    {"name": "Nour",  "age": 25, "track": "AI",   "hours_studied": 30, "scores": [75, 80, 85]},
    {"name": "Sami",  "age": 35, "track": "Data", "hours_studied": 48, "scores": [88, 91, 79]},
]

# #Print the name of the first student and the name of the last student
print(students[0]["name"])
print(students[-1]["name"])

# #Print Rim's scores.

Rim_record = students[2]
Rim_score = Rim_record["scores"]

print(Rim_record)
print(Rim_score)

# #loop through all students
for student in students :
    print(f'{student["name"]} is {student["age"]} years old and studies {student["track"]}.')


# # #Use a loop to build a new list containing only the students in the  AI track
new_list = []
for student in students : 
    
    if student["track"] == "AI" : 
        new_list.append(student)
print(new_list)
print(f'number of students in AI is {len(new_list)}')        
        


# # #list comprehension
new_list = [student for student in students if student["track"] == "AI"]
print(new_list) 
print(f'number of students in AI is {len(new_list)}')


# # #list of the **names** of all students who studied more than 30 hours.
names_list = [student["name"] for student in students if student["hours_studied"] >30]
print(names_list)

# # # list of students who are older than 24 AND in the AI track
age_track_list = [student for student in students if student["age"] > 24 and student["track"] == "AI"]
print(age_track_list)


# #the average age of all students
avr_age = sum(student["age"] for student in students)/len(students)
print(avr_age)


# # total hours studied across the whole cohort.
total_hrs = sum(student["hours_studied"] for student in students)
print(total_hrs)


# #the student who studied the most hours
max_hours = max(student["hours_studied"] for student in students)
print(max_hours)

top_student = max(students, key = lambda student : student["hours_studied"])
# print(top_student)
print(f"top student is {top_student['name']}, max hours is {top_student['hours_studied']}")


# #their final grade is the average of their `scores`
for student in students :
    avr_score = sum(student['scores'])/len(student['scores'])   
    final_grade = round(avr_score, 1)
    
    print(f"{student['name']}: {final_grade}")
    
# #list comprehension that produces a new list of dictionaries, each with only two keys: `name` and `average_score`
new_list2 = [{'name' : student['name'],
            'average_score': sum(student['scores'])/3} 
            for student in students
            ]
print(new_list2)


#Create a set of all the unique tracks in the dataset.
# Explain in a comment why a set is the right tool here instead of a list.

unique_track = {student['track'] for student in students}
print(unique_track) # we choose a set because it doesn't allow duplicate and repeated values like a list.


# #Reusable Functions 
def filter_by_track(students, track) :

    filtered_list =  []   
    for student in students :
        if student["track"] == track :
            filtered_list.append(student)
    return filtered_list

filter_by_track(students, 'AI')
filter_by_track(students, 'Data')


def average_score(student) :
    avrg_score = sum(student['scores'])/ len(student["scores"])
    return avrg_score
    
print(average_score(students[0]))

#top_student(students)
def top_student(students) :
    best_student = students[0]
    for student in students :
        if average_score(student) > average_score(best_student) :
            best_student = student
            
    return best_student['name']    

print(top_student(students))    


#summary(students)
def summary(students): 
    total_student = len(students)
    average_age = sum(student['age'] for student in students)/ total_student
    tracks = {student['track'] for student in students}
    
    return {
        "total student" : total_student,
        "average age" : average_age,
        "tracks" : tracks
    }
    
print(summary(students))    
    
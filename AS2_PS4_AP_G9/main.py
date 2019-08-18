import assign_subject

# Given subjects
# 1. Data mining
# 2. NLP
# 3. AI
# 4. Spatial Data Analysis
# 5. Image processing
# 6. Big-Data
# 7. Graph Mining
# 8. Machine Learning
# 9. E-commerce
# 10. Wireless Mobile communication
# 11. Cloud computing

#  Creating an array for subjects for mapping
subjects = ['DM', 'NLP', 'AI', 'SDA', 'IP',
            'BD', 'GM', 'ML', 'EC', 'WMC', 'CC']
prefrences = []

try:
    asubj = assign_subject.AssignSubject()
    input_file = open("../inputPS4.txt")
    studentPreference = {}
    for record in input_file.readlines():
        student = record.split(" / ")
        studentPref = [0] * 11
        for pref in student[1:]:
            studentPref[subjects.index(pref.strip())] = 1
        prefrences.append(studentPref)
    allocations = asubj.count_allocations(prefrences)
except FileNotFoundError as fe:
    print(fe)
except IOError as ioe:
    print(ioe)
finally:
    input_file.close()

try:
    output_file = open("../outputPS4.txt", "w+")
    output_file.write(
        'The total number of allocations possible is: ' + str(allocations))
    output_file.close()
except FileNotFoundError as fe:
    print(fe)
except IOError as ioe:
    print(ioe)
finally:
    output_file.close()


class AssignSubject:
    # Initialize variables 
    def __init__(self): 
  
            self.allmask = 0
            self.total_subjects = 11

    #  Mask is the set of persons, i is the current cap number. 
    def countAllocationRec(self, allocations, preferences, subjects, mask, sub_no): 
          
        # If all persons are wearing a cap so we 
        # are done and this is one way so return 1 
        if mask == self.allmask: 
            return 1
  
        # If not everyone is wearing a cap and also there are no more 
        # caps left to process, so there is no way, thus return 0; 
        print('---'+ str(sub_no))
        if sub_no + 2> self.total_subjects: 
            return 0
  
        # If we have already solved this subproblem, return the answer. 
        print(sub_no)
        if allocations[mask][sub_no]!= -1 : 
            return allocations[mask][sub_no] 
  
        # Ways, when we don't include this cap in our arrangement 
        # or solution set 
        ways = self.countAllocationRec(allocations, preferences, subjects, mask, sub_no + 1) 
          
        # assign ith cap one by one  to all the possible persons 
        # and recur for remaining caps. 
  
        for stud in preferences[sub_no]: 
                
            # if person 'ppl' is already wearing a cap then continue 
            if mask & (1 << stud) : continue
                
            # Else assign him this cap and recur for remaining caps with 
            # new updated mask vector 
            ways += self.countAllocationRec(allocations, preferences, subjects, mask | (1 << stud), sub_no + 1)  

            ways = ways % (10**9 + 7) 
  
        # Save the result and return it 
        allocations[mask][sub_no-1] = ways 
  
        return allocations[mask][sub_no] 

    def count_allocations(self, no_of_students, preferences, subjects):
        # allmask is used to check if all persons 
        # are included or not, set all n bits as 1 
        self.allmask = (1 << no_of_students) -1
  
        # Initialize all entries in allocations as -1 
        allocations = [[-1 for j in range(self.total_subjects + 1)] for i in range(2 ** no_of_students)] 
  
        # Call recursive function countWaysUtil 
        # result will be in allocations[0][1] 
        print (self.countAllocationRec(allocations, preferences, subjects, 0, 0))


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
prefrences = [[] for x in subjects] 

try:
    student_no = 0
    input_file = open("../inputPS4.txt")
    for record in input_file.readlines():
        student_no += 1
        student = record.split(" / ")
        for pref in student[1:]:
            prefrences[subjects.index(pref.strip())].append(student_no)
    AssignSubject().count_allocations(student_no, prefrences, subjects)
except FileNotFoundError as fe:
    print(fe)
except IOError as ioe:
    print(ioe)
finally:
    input_file.close()
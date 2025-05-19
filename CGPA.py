import math
def weighted_score(grade , unit):
        match grade:
            case 'A':
                 return 5 * unit
            case 'B':
                return 4 * unit
            case 'C':
                return 3 * unit
            case 'D':
                return 2 * unit
            case 'F':
                return 0 * unit    
units=0 
score=0            
courses = int(input("How many courses are you taking? ="))

for i in range(courses):
    unit= int(input("Course " + str(i+1) + " No. of units ?=" ))
    units=units + unit
    
    grade= input("What was your grade ? =").upper()
    score = score + weighted_score(grade , unit)

grade_total= units * 5
gpa = round(float(score / grade_total) * 5 , 2)
print("Your gpa is = " + str(gpa))
             
        

    

s_information = {
    "name": input("enter student name: "),
    "roll": int(input("enter student roll: ")),
    "id": int(input("enter student id: "))
}

sub_marks = {
    "math": int(input("enter your math marks: ")),
    "english": int(input("enter your english marks: ")),
    "physics": int(input("enter your physics marks: ")),
    "chamestry": int(input("enter your chamestry marks: ")),
    "bengali": int(input("enter your bengali marks: "))
}

# all subjects Letter Grade and Grade Point
def get_gpa(marks):
        if marks >= 80 and marks <= 100:
            return ["A+", 4]
        elif marks >= 75:
            return ["A", 3.75]
        elif marks >= 70:
            return ["A-", 3.5]
        elif marks >= 65:
            return ["B+", 3.25]
        elif marks >= 60:
            return ["B", 3]
        elif marks >= 55:
            return ["B-", 2.75]
        elif marks >= 50:
            return ["C+", 2.5]
        elif marks >= 45:
            return ["C", 2.25]
        elif marks >= 40:
            return ["D", 2]
        else:
            return ["F", 0]


# individual Letter Grade and Grade Point
bengali = get_gpa(sub_marks["bengali"])
math = get_gpa(sub_marks["math"])
chemistry = get_gpa(sub_marks["chamestry"])
physics = get_gpa(sub_marks["physics"])
english = get_gpa(sub_marks["english"])

# Sum of total marks
all_subject_marks = [sub_marks["bengali"], sub_marks["chamestry"], sub_marks["english"], sub_marks["math"], sub_marks["physics"]]

#  Check pass failed
def check_pass_fail(marks):
    new_marks_table = []
    for i in marks:
        if i > 39:
            new_marks_table.append(i)
    if len(new_marks_table) == 5:
        return sum(new_marks_table) 
    else:
        return ('failed')
total_marks = check_pass_fail(all_subject_marks)

# Total result
def total_result(marks):
    if marks != 'failed':
        average = marks / 5
        total_gpa = get_gpa(average)
        return total_gpa
    else:
        return marks

main_result =  total_result(total_marks)
letter_grade = main_result[0]
grade_point = main_result[1]

if main_result == 'failed':
    letter_grade = "Failed"
    grade_point = 0




print(f'''
                                  full markshit

 Name: {s_information["name"]}                  Roll: {s_information["roll"]}                   Id: {s_information["id"]}


 All Subjects Marks                        Letter Grade                        Grade Point      
 
 Physic = {sub_marks["physics"]}                                    {physics[0]}                                  {physics[1]}
 Chemistry = {sub_marks["chamestry"]}                                 {chemistry[0]}                                  {chemistry[1]}
 Math = {sub_marks["math"]}                                      {math[0]}                                  {math[1]}
 English = {sub_marks["english"]}                                   {english[0]}                                  {english[1]}
 Bengali = {sub_marks["bengali"]}                                   {bengali[0]}                                  {bengali[1]}

                                                                 Result: ({letter_grade})
                                                                 GPA   : {grade_point}
''')
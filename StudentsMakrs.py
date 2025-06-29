nList={"Alice":85,"Sanjay":90,"Ram":78,"Pappu":88,"Kalu":92,"Frank":80,"Grace":95,"Hank":85,"Ivy":89,"Jack":91}

def get_student_marks():
    student_name = input("Enter the student's name: ")
    marks = nList.get(student_name)
    
    if marks is not None:
        print(f"{student_name}'s marks: {marks}")
    else:
        print(f"Student not found.")

get_student_marks()
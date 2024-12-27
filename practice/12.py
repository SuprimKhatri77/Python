std_marks = int(input("Enter your total marks in 5 subjects:"))
total_subj = 5

def avg_marks():
    average_marks = 0
    if std_marks < 0:
        print("Marks cannot be less than zero")
    else:
        average_marks = std_marks / total_subj
        print(average_marks)
avg_marks()
def collect_student_data():
    average_marks = float(input("Enter Average Marks(%): "))
    highest_marks = float(input("Enter your Highest subject marks(%): "))
    lowest_marks = float(input("Enter your lowest subject marks(%): "))
    failed_subjects = int(input("Enter number of Failed subjects: "))
    backlogs = int(input("Enter number of backlogs: "))
    quiz_average = float(input("Enter Quiz/Test average(%): "))
    assignment_completion = float(input("Enter assignmemt completion(%): "))

    study_hours = float(input("Enter study hours per day: "))
    self_study_hours = float(input("Enter self-study hours per week: "))
    regularity = input("How regular is your study? (Regular/Sometimes/Rarely): ").strip().capitalize()
    difficulty = input("How difficult is it to understand your subjects? (LOW/Medium/High): ").strip().capitalize()

    attendance = float(input("Enter attendance(%): "))
    screen_time = float(input("Enter daily screen time (hours): "))
    sleep_hours = float(input("Enter sleep hours per day: "))

    exam_preparation = input("How is your exam preparation? (Good/Average/Poor): ").strip().capitalize()
    academic_help = input("Do you need academic help? (Yes/No): ").strip().capitalize()

    student = {}
    student["average_marks"] = average_marks
    student["highest_marks"] = highest_marks
    student["lowest_marks"] = lowest_marks
    student["failed_subjects"] = failed_subjects
    student["backlogs"] = backlogs
    student["quiz_average"] = quiz_average
    student["assignment_completion"] = assignment_completion
    student["study_hours"] = study_hours
    student["self_study_hours"] = self_study_hours
    student["regularity"] = regularity
    student["difficulty"] = difficulty
    student["attendance"] = attendance
    student["screen_time"] = screen_time
    student["sleep_hours"] = sleep_hours
    student["exam_preparation"] = exam_preparation
    student["academic_help"] = academic_help

    return student
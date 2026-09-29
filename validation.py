def check_range(value, minimum, maximum):
    return minimum <= value <= maximum

def validate_student_data(student):
    if not check_range(student["average_marks"], 0, 100):
        return False

    if not check_range(student["attendance"], 0, 100):
        return False

    if student["failed_subjects"] < 0:
        return False

    if student["backlogs"] < 0:
        return False

    if student["highest_marks"] < 0 or student["highest_marks"] > 100:
        return False

    if student["lowest_marks"] < 0 or student["lowest_marks"] > 100:
        return False

    if student["quiz_average"] < 0 or student["quiz_average"] > 100:
        return False

    if student["assignment_completion"] < 0 or student["assignment_completion"] > 100:
        return False

    if student["study_hours"] < 0:
        return False

    if student["self_study_hours"] < 0:
        return False

    if student["screen_time"] < 0:
        return False

    if student["sleep_hours"] < 0:
        return False

    if student["regularity"] not in ["Regular", "Sometimes", "Rarely"]:
        return False

    if student["difficulty"] not in ["Low", "Medium", "High"]:
        return False

    if student["exam_preparation"] not in ["Good", "Average", "Poor"]:
        return False

    if student["academic_help"] not in ["Yes", "No"]:
        return False
    
    return True
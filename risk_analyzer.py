def analyze_risk(student):
    score = 0
    risk_factors = []

    if student["average_marks"] < 60:
        score += 10
        risk_factors.append("Low Average Marks")

    if student["highest_marks"] < 60:
            score += 10
            risk_factors.append("Low highest subject marks")  
          

    if student["lowest_marks"] < 40:
            score += 10
            risk_factors.append("Very low marks in a subject")  
          
    if student["failed_subjects"] > 0:
        score += 10
        risk_factors.append("Failed subjects")  

    if student["backlogs"] > 0:
        score += 10
        risk_factors.append("Backlogs")

    if student["attendance"] < 75:
        score += 10
        risk_factors.append("Low Attendance")  

    if student["quiz_average"] < 50:
        score += 10
        risk_factors.append("Low quiz/test average")

    if student["assignment_completion"] < 70:
        score += 10
        risk_factors.append("Low assignment completion")

    if student["study_hours"] < 4:
        score += 10
        risk_factors.append("Low study hours")

    if student["self_study_hours"] < 8:
        score += 10
        risk_factors.append("Low self-study hours")  
              
    if student["regularity"] == "Rarely":
        score += 10
        risk_factors.append("Irregular study")  
          
    if student["difficulty"] == "High":
        score += 10
        risk_factors.append("Difficulty understanding subjects")

    if student["exam_preparation"] == "Poor":
            score += 10
            risk_factors.append("Poor exam preparation")

    if student["academic_help"] == "Yes":
            score += 10
            risk_factors.append("Needs academic help")

    if score <= 40:
         level = "Low Risk"
    elif score <= 80:
         level = "Medium Risk"
    else:
         level = "High Risk"  

    return score, level, risk_factors           
            
          
      
      


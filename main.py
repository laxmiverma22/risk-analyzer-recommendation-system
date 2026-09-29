from input_handler import collect_student_data
from risk_analyzer import analyze_risk
from recommendation import generate_recommendations 
from report import display_report
from validation import validate_student_data
from utils import risk_level_description

def main():
    student = collect_student_data()
    validation__result = validate_student_data(student)

    if validation__result == False:
        print("Invalid student data. Please enter valid values.")
        return
    print("Data validation", validation__result) 
    score, level, risk_factors = analyze_risk(student)
    risk_description = risk_level_description(level)
    print(risk_description)
    recomendations = generate_recommendations(risk_factors)
    display_report(score, level, risk_factors, recomendations) 

main()
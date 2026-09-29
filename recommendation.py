def generate_recommendations(risk_factors):
    recommendations = []

    for factor in risk_factors:
        if factor == "Low average marks":
            recommendations.append("Improve your overall marks through regular study.")

        if factor == "Failed subjects":
            recommendations.append("Focus on Failed subjects and seek extra academic support")

        if factor == "Backlogs":
            recommendations.append("Clear your backlogs by giving extra attention to pending subjects")

        if factor == "Low attendance":
            recommendations.append("Attend classes regularly to improve attendance")

        if factor == "Low Quiz/Test average":
            recommendations.append("Practice regularly and revise topics before quizes and tests. ")

        if factor == "Low assignment completion":
            recommendations.append("Complete assignments on time and regularly.")

        if factor == "Low study hours":
            recommendations.append("Increase your daily study time gradually.")

        if factor == "Low self-study hours":
            recommendations.append("increase your weekly self-study time.")

        if factor == "Irregular study":
            recommendations.append("Follow a regular study schedule.")

        if factor == "Difficulty understanding subjects":
            recommendations.append("Ask teachers or classmates for help with difficult topics.")

        if factor == "Poor exam preparation":
            recommendations.append("Start preparing for exams early and revise regularly.")

        if factor == "Needs academic help":
            recommendations.append("seek guidance from teachers or academic mentors.")


    return recommendations 
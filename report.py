def display_report(score, level, risk_factors, recommendations):
    print("\n---Student Risk Report ---")
    print("Risk Score: ", score)
    print("Risk Level: ", level)
    print("\nRisk Factors: ")

    for factor in risk_factors:
        print("-", factor) 

    print("\nRecommendations")

    for recommendations in recommendations:
        print("-", recommendations)

    print("-------------------------")
    print("Report generated successfully")
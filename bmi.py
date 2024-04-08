def calculate_bmi(height_feet, height_inches, weight_pounds):

    height_inches_total = height_feet * 12 + height_inches
    bmi = (weight_pounds / (height_inches_total ** 2)) * 703
    
    # Determine BMI category
    if bmi < 18.5:
        category = 'Underweight'
    elif bmi < 24.9:
        category = 'Normal weight'
    elif bmi < 30:
        category = 'Overweight'
    else:
        category = 'Obese'
    
    return bmi, category

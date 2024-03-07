# In main.py

from bmi import calculate_bmi

def main():
    print("Enter your height and weight to calculate your BMI.")
    height_feet = int(input("Height in feet: "))
    height_inches = int(input("Height in inches: "))
    weight_pounds = float(input("Weight in pounds: "))
    
    bmi, category = calculate_bmi(height_feet, height_inches, weight_pounds)
    
    print(f"Your BMI is: {bmi:.1f}")
    print(f"You are in the '{category}' category.")

if __name__ == "__main__":
    main()

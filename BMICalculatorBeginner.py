# BMI Calculation function
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# BMI Categorization function
def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Main function
def main():
    try:
        # User input with validation
        weight = float(input("Enter your weight (in kg): "))
        height = float(input("Enter your height (in meters): "))
        
        if weight <= 0 or height <= 0:
            raise ValueError("Height and weight must be positive values.")
        
        # Calculate BMI
        bmi = calculate_bmi(weight, height)
        category = bmi_category(bmi)
        
        # Display results
        print(f"Your BMI is: {bmi:.2f}")
        print(f"Health category: {category}")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

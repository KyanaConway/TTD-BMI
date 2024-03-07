import pytest
from bmi import calculate_bmi  # Import from the correct module

def test_calculate_bmi_underweight():
    # Test for a BMI value corresponding to underweight category
    bmi, category = calculate_bmi(5, 7, 100)  # height: 5 feet 7 inches, weight: 100 pounds
    assert bmi == pytest.approx(15.6, 0.1)  # Approximate BMI value
    assert category == 'Underweight'  # Verify the BMI category

def test_calculate_bmi_normal_weight():
    # Test for a BMI value corresponding to normal weight category
    bmi, category = calculate_bmi(6, 0, 160)  # height: 6 feet 0 inches, weight: 160 pounds
    assert bmi == pytest.approx(21.7, 0.1)  # Approximate BMI value
    assert category == 'Normal weight'  # Verify the BMI category

def test_calculate_bmi_overweight():
    # Test for a BMI value corresponding to overweight category
    bmi, category = calculate_bmi(5, 5, 180)  # height: 5 feet 5 inches, weight: 180 pounds
    assert bmi == pytest.approx(29.9, 0.1)  # Approximate BMI value
    assert category == 'Overweight'  # Verify the BMI category

def test_calculate_bmi_obese():
    # Test for a BMI value corresponding to obese category
    bmi, category = calculate_bmi(5, 0, 200)  # height: 5 feet 0 inches, weight: 200 pounds
    assert bmi == pytest.approx(39.2, 0.1)  # Approximate BMI value
    assert category == 'Obese'  # Verify the BMI category

# Add more test cases as needed for edge cases, boundary conditions, and other scenarios

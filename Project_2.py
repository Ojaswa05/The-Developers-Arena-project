def calculate_grade(marks):
    if marks >= 90:
        grade = 'A+'
        message = "Outstanding performance! Keep shining!"
    elif marks >= 80:
        grade = 'A'
        message = "Excellent work! You're doing great!"
    elif marks >= 70:
        grade = 'B'
        message = "Good job! A little more effort will make it perfect!"
    elif marks >= 60:
        grade = 'C'
        message = "Nice effort! Keep improving!"
    elif marks >= 50:
        grade = 'D'
        message = "You passed! Try to aim higher next time!"
    else:
        grade = 'F'
        message = "Don't give up! Learn from mistakes and try again!"
    
    return grade, message
try:
    marks = float(input("Enter your marks (out of 100): "))

    if 0 <= marks <= 100:
        grade, message = calculate_grade(marks)
        print(f"\nYour Grade: {grade}")
        print(message)
    else:
        print("❌ Please enter marks between 0 and 100.")
except ValueError:
    print("⚠️ Invalid input! Please enter a numeric value.")
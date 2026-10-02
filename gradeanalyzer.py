print(" ==== GRADE ANALYZER ====")
name = input("Student Name: ")
print("Hello " + name + "!")
grades = []
while True:
    try:
        number_of_grades = int(input("Enter the number of grades you want to input: "))
        if number_of_grades <= 0:
            print("Please enter a positive integer.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
for i in range(number_of_grades):
    while True:
        try:
            grade = float(input("Enter grade " + str(i + 1) + ": "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue
        if 0 <= grade <= 100:
            grades.append(grade)
            break
        else:
            print("Invalid grade. Please enter a grade between 0 and 100.")
average = sum(grades) / len(grades)
highest = max(grades)
lowest = min(grades)
print("\n==== RESULTS ====")
print("Average Grade:" ,(round(average, 2)))
print("Highest Grade:" ,(highest))
print("Lowest Grade:" ,(lowest))
if average >= 90:
    Letter = "A"
elif average >= 80:
    Letter = "B"
elif average >= 70:
    Letter = "C"
elif average >= 60:
    Letter = "D"
else:
    Letter = "F"

if average >=60:
    status = "PASS"
else:
    status = "FAIL"
print("Letter Grade:" ,(Letter))
print("Status:" ,(status))

print("\n=== RECOMMENDATIONS ===")
if average >=90:
    print("Excellent work! You achieved an A. Keep it up!")
elif average >=80:
    print("Good job! You achieved a B. Aim for an A next time!")
elif average >=70:
    print("You passed with a C. Consider reviewing the material to improve your grade.")
elif average >=60:
    print("You passed, but there is room for improvement.")
else:
    print("Keep working hard and don't give up! You can improve your grade with dedication and effort.")

print("\nThank you for using the Grade Analyzer!")   
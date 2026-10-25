Marks_obtained = int(input("What are your marks?"))
if Marks_obtained < 0 or Marks_obtained > 100:
    Grade = "Invalid marks"
elif Marks_obtained >= 80:
    Grade = "Excellent"
elif Marks_obtained >= 70:
    Grade = "Good"
elif Marks_obtained >= 50:
    Grade = "Pass"
else:
    Grade = "Fail"

print("Grade =" , Grade)
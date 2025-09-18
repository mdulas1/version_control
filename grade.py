# school grading system
print("school grading system")

student_score = float(input("enter your score here\n>>"))
if student_score >= 70 and student_score <= 100:
  print("A")
elif student_score >= 60 and student_score <= 69:
  print("B")
elif student_score >= 50 and student_score  <= 59:
  print("C")
elif student_score >= 40 and student_score <= 49:
  print("D")
else:
  print("F9")
  
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

print(max(student_scores))

y = 0
for score in student_scores:
    if score >= y:
        y = score

print(y)



# Write your code below this row 👇
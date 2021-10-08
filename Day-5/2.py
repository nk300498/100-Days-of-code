student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

b=0
for sum in student_heights:
    a=int(sum)
    b=b+a
avg=round(b/len(student_heights))
print(avg)

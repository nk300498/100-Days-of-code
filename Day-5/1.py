
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])


b=0
for sum in student_heights:
    b+=sum

k=0
for t in student_heights:
    k+=1
avg=round(b/k)
print(avg)



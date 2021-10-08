student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

h=0
for s in student_scores:
    if s>h:
       h=s
    else:
       h=s
print(f"{h} IS LARGEST")     



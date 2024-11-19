from idlelib.editor import keynames

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = ['Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron']
students.sort() #сортировкa по порядку
students_1 = list(students)
#print(students_1)


students_score = {}
students_score.update({students_1[0]:sum(grades[0])/len(grades[0]),
                    students_1[1]:sum(grades[1])/len(grades[1]),
                    students_1[2]:sum(grades[2])/len(grades[2]),
                    students_1[3]:sum(grades[3])/len(grades[3]),
                    students_1[4]:sum(grades[4])/len(grades[4])
                       })

# students_score = {k: v for k, v in zip(students_1 , sum(grades[:-1])/len(grades[:-1]))}
print(students_score)

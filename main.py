
# * sort() method = used with lists
# * funtion = used with iterables

# students = ["Squidward", "Sandy", "Patrick", "Spongebob", "Mr.Krabs"]

# students.sort()
# students.sort(reverse=True)

# sorted_students = sorted(students)

# for i in students:
#     print(i)

# for i in sorted_students:
#     print(i)


students = [("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrik", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr.Krabs", "C", 78)]

grade = lambda grades:grades[1]

students.sort(key=grade, reverse=True)
for i in students:
    print(i)

age = lambda ages:ages[2]
sorted_students = sorted(students, key=age)

for i in sorted_students:
    print(i)
courses = ["Java", "Python", "FastAPI"]
courses.append("AI")
courses[2] = ("Spring AI")
print(len(courses))
for course in courses:
    print(course)

courses.reverse()

for course in courses:
    print(course)
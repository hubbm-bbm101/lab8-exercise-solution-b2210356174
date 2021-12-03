import sys
searched_students = [i.strip() for i in sys.argv[2].split(",") if i.strip()]
f = open(sys.argv[1])
content = f.read().splitlines()
f.close()
students = {i.split(":")[0].strip():i.split(":")[1].strip().split(",") for i in content}
for student in searched_students:
    try:
        value = students[student]
        print("Name: {}, University: {},{}".format(student, value[0], value[1]))
    except KeyError:
        print("No record of '{}' was found!".format(student))
        
import mysql.connector
isTeacher=True
grades=False
def connectToDatabase():
    connection = mysql.connector.connect(user='emilm24',
                                         password='247075393',
                                         host='10.8.37.226',
                                         database='emilm24_db')
    return connection

def execute(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    results=[]
    for row in cursor:
        results.append(row)
    cursor.close()
    connection.close()
    return results

def get_student_schedule(student_id):
    isTeacher=False
    query = f"CALL GetSchedule('{student_id}');"
    return execute(connectToDatabase(), query)
def get_grades(student_id, course_id):
    grades=True
    query = f"CALL GetGrades('{student_id, course_id}');"
    return execute(connectToDatabase(), query)
def get_teacher_schedule(teacher_id):
    isTeacher = True
    query = f"CALL GetTeacherSchedule('{teacher_id}');"
    return execute(connectToDatabase(), query)

results=[]
role=input("Log in as student or teacher? ")
if role.lower()=="student":
    student_id = input("Enter a student id: ")
    action = input("s - view schedule\ng - view grades\nEnter an option: ")
    if action == "s":
        results = get_student_schedule(student_id)
    if action == "g":
        course_id = input("Enter a specific course section id: ")
        results = get_grades(student_id, course_id)
else:
    if role.lower()=="teacher":
        teacher_id = input("Enter a teacher id: ")
        results = get_teacher_schedule(teacher_id)
def teacher_operation():
    for result in results:
        class_name = str(result[1])
        room = str(result[0])
        period = str(result[2])
        teacher = str(result[3])
        print("Period: " + period)
        print("Course:" + class_name)
        print("Room:" + room)
        print("Department:" + teacher)
        print()
def student_operation():
    for result in results:
        class_name = str(result[1])
        room = str(result[3])
        period = str(result[2])
        teacher = str(result[4])
        id = str(result[0])
        print("Period: " + period)
        print("Course:" + class_name)
        print("Room:" + room)
        print("Teacher:" + teacher)
        print("Id:" + id)
        print()
if isTeacher:
    teacher_operation()
else:
    student_operation()

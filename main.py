import mysql.connector

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
    query = f"CALL GetSchedule('{student_id}')"
    return execute(connectToDatabase(), query)

def get_teacher_schedule(teacher_id):
    query = f"CALL GetTeacherSchedule('{teacher_id}')"
    return execute(connectToDatabase(), query)

results=[]
role=input("Log in as student or teacher? ")
if role.lower()=="student":
    student_id = input("Enter a student id: ")
    results = get_student_schedule(student_id)
elif role.lower()=="teacher":
    teacher_id = input("Enter a teacher id: ")
    results = get_teacher_schedule(teacher_id)
else:
    print("Invalid input.")
for result in results:
    class_name=str(result[0])
    room=str(result[1])
    period=str(result[2])
    teacher=str(result[3])
    print("Period: " + period)
    print("Course:" + class_name)
    print("Room:" + room)
    print("Teacher:" + teacher)
    print()

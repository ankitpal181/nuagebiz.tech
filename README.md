# nuagebiz.tech
Interview Assignment

Setup:
- clone the repo
- activate venv
- or create a new venv and install all the dependencies from requirements.txt
- now run migrations, which will create default admin user for us

APIs (description) (method) (url):

USER MODULE
- add user: POST http://ams.nuagebiz.tech:8000/user/
- edit user: PUT http://ams.nuagebiz.tech:8000/user/{user_id}/
- fetch single user by id: GET http://ams.nuagebiz.tech:8000/user/?id={user_id}
- fetch all users: GET http://ams.nuagebiz.tech:8000/user/
- fetch user by name: GET http://ams.nuagebiz.tech:8000/user/?name={full_name}
- fetch user by username: GET http://ams.nuagebiz.tech:8000/user/?username={username}
- fetch user by email: GET http://ams.nuagebiz.tech:8000/user/?email={email}
- fetch user by submitted_by: GET http://ams.nuagebiz.tech:8000/user/?submitted_by={user_id}

STUDENT MODULE
- add student: POST http://ams.nuagebiz.tech:8000/user/student/
- edit student: PUT http://ams.nuagebiz.tech:8000/user/student/{student_id}/
- fetch single student by id: GET http://ams.nuagebiz.tech:8000/user/student/?id={student_id}
- fetch all students: GET http://ams.nuagebiz.tech:8000/user/student/
- fetch student by name: GET http://ams.nuagebiz.tech:8000/user/student/?name={full_name}
- fetch student by department_id: GET http://ams.nuagebiz.tech:8000/user/student/?department={department_id}
- fetch student by submitted_by: GET http://ams.nuagebiz.tech:8000/user/student/?submitted_by={user_id}

DEPARTMENT MODULE
- add department: POST http://ams.nuagebiz.tech:8000/department/
- edit department: PUT http://ams.nuagebiz.tech:8000/department/{department_id}/
- fetch single department by id: GET http://ams.nuagebiz.tech:8000/department/?id={department_id}
- fetch all departments: GET http://ams.nuagebiz.tech:8000/department/
- fetch department by name: GET http://ams.nuagebiz.tech:8000/department/?name={name}
- fetch department by submitted_by: GET http://ams.nuagebiz.tech:8000/department/?submitted_by={user_id}

COURSE MODULE
- add course: POST http://ams.nuagebiz.tech:8000/department/course/
- edit course: PUT http://ams.nuagebiz.tech:8000/department/course/{course_id}/
- fetch single course by id: GET http://ams.nuagebiz.tech:8000/department/course/?id={course_id}
- fetch all courses: GET http://ams.nuagebiz.tech:8000/department/course/
- fetch course by name: GET http://ams.nuagebiz.tech:8000/department/course/?name={name}
- fetch course by department_id: GET http://ams.nuagebiz.tech:8000/department/course/?department={department_id}
- fetch course by submitted_by: GET http://ams.nuagebiz.tech:8000/department/course/?submitted_by={user_id}

ATTENDANCE MODULE
- add attendance: POST http://ams.nuagebiz.tech:8000/attendance/
- edit attendance: PUT http://ams.nuagebiz.tech:8000/attendance/{attendance_id}/
- fetch single attendance by id: GET http://ams.nuagebiz.tech:8000/attendance/?id={attendance_id}
- fetch all attendances: GET http://ams.nuagebiz.tech:8000/attendance/
- fetch attendance by student_id: GET http://ams.nuagebiz.tech:8000/attendance/?student={student_id}
- fetch attendance by course_id: GET http://ams.nuagebiz.tech:8000/attendance/?course={course_id}
- fetch attendance by submitted_by: GET http://ams.nuagebiz.tech:8000/attendance/?submitted_by={user_id}


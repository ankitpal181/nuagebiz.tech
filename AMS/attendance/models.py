from django.db import models

# Create your models here.
USER_TYPE = [
    (0, "admin"),
    (1, "management"),
    (2, "staff_member"),
    (3, "student")
]
CLASS = [
    (0, "A"),
    (1, "B"),
    (2, "C")
]

class Users(models.Model):
    type = models.IntegerField(choices=USER_TYPE, default=2, null=False)
    full_name = models.CharField(max_length=128, null=False)
    username = models.CharField(max_length=100, null=False)
    email = models.TextField(null=False)
    password = models.TextField(null=False)
    submitted_by = models.ForeignKey(
        "self", related_name="users_submitted", on_delete=models.DO_NOTHING, null=False, default=1
    )
    updated_at = models.DateTimeField(auto_now=True)


class Departments(models.Model):
    department_name = models.CharField(max_length=100, default="science", null=False)
    submitted_by = models.ForeignKey(
        Users, related_name="departments_submitted", on_delete=models.DO_NOTHING, null=False
    )
    updated_at = models.DateTimeField(auto_now=True)


class Students(models.Model):
    full_name = models.CharField(max_length=128, null=False)
    department_id = models.ForeignKey(Departments, on_delete=models.DO_NOTHING, null=False)
    class_name = models.IntegerField(choices=CLASS, default=0, null=False)
    submitted_by = models.ForeignKey(
        Users, related_name="students_submitted", on_delete=models.DO_NOTHING, null=False
    )
    updated_at = models.DateTimeField(auto_now=True)


class Courses(models.Model):
    course_name = models.CharField(max_length=150, null=False)
    department_id = models.ForeignKey(
        Departments, related_name="related_courses", on_delete=models.CASCADE, null=False
    )
    semester = models.IntegerField(default=1, null=False)
    class_name = models.IntegerField(choices=CLASS, default=0, null=False)
    lecture_hours = models.IntegerField(default=60)
    submitted_by = models.ForeignKey(
        Users, related_name="courses_submitted", on_delete=models.DO_NOTHING, null=False
    )
    updated_at = models.DateTimeField(auto_now=True)

class AttendanceLog(models.Model):
    student_id = models.ForeignKey(
        Students, related_name="attendance_records", on_delete=models.DO_NOTHING, null=False
    )
    course_id = models.ForeignKey(
        Courses, related_name="course_attendance", on_delete=models.DO_NOTHING, null=False
    )
    present = models.BooleanField(default=False, null=False)
    submitted_by = models.ForeignKey(
        Users, related_name="attendances_submitted", on_delete=models.DO_NOTHING, null=False
    )
    updated_at = models.DateTimeField(auto_now=True)

# Generated by Django 5.0.6 on 2024-05-08 11:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(default='science', max_length=100)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(0, 'admin'), (1, 'management'), (2, 'staff_member'), (3, 'student')], default=2)),
                ('full_name', models.CharField(max_length=128)),
                ('username', models.CharField(max_length=100)),
                ('email', models.TextField()),
                ('password', models.TextField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('submitted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='users_submitted', to='attendance.users')),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=128)),
                ('class_name', models.IntegerField(choices=[(0, 'A'), (1, 'B'), (2, 'C')], default=0)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('department_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='attendance.departments')),
                ('submitted_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='students_submitted', to='attendance.users')),
            ],
        ),
        migrations.AddField(
            model_name='departments',
            name='submitted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='departments_submitted', to='attendance.users'),
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=150)),
                ('semester', models.IntegerField(default=1)),
                ('class_name', models.IntegerField(choices=[(0, 'A'), (1, 'B'), (2, 'C')], default=0)),
                ('lecture_hours', models.IntegerField(default=60)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('department_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_courses', to='attendance.departments')),
                ('submitted_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='courses_submitted', to='attendance.users')),
            ],
        ),
        migrations.CreateModel(
            name='AttendanceLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('present', models.BooleanField(default=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='course_attendance', to='attendance.courses')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='attendance_records', to='attendance.students')),
                ('submitted_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='attendances_submitted', to='attendance.users')),
            ],
        ),
    ]

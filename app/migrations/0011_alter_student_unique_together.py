# Generated by Django 4.1.3 on 2022-12-01 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_student_school_student_teacher_alter_student_user'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='student',
            unique_together={('school', 'user', 'teacher')},
        ),
    ]

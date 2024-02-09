# Generated by Django 5.0.1 on 2024-02-09 20:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_question_assesment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student_progress',
            old_name='user_name',
            new_name='student',
        ),
        migrations.RemoveField(
            model_name='student_progress',
            name='course',
        ),
        migrations.RemoveField(
            model_name='student_progress',
            name='progressPercentage',
        ),
        migrations.AddField(
            model_name='student_progress',
            name='assessments',
            field=models.ManyToManyField(to='courses.assessment'),
        ),
        migrations.AddField(
            model_name='student_progress',
            name='ativities',
            field=models.ManyToManyField(to='courses.activities'),
        ),
        migrations.AddField(
            model_name='student_progress',
            name='courses',
            field=models.ManyToManyField(to='courses.course'),
        ),
        migrations.AddField(
            model_name='student_progress',
            name='lessons',
            field=models.ManyToManyField(to='courses.lesson'),
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=10000)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.lesson')),
            ],
        ),
        migrations.CreateModel(
            name='StudentActivityProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=False)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.activities')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.users')),
            ],
        ),
        migrations.CreateModel(
            name='StudentAssessmentProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=False)),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.assessment')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.users')),
            ],
        ),
        migrations.CreateModel(
            name='StudentInfoProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=False)),
                ('info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.info')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.users')),
            ],
        ),
        migrations.CreateModel(
            name='StudentLessonProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=False)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.lesson')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.users')),
            ],
        ),
    ]
import pandas as pd
from django.core.management.base import BaseCommand
from data.models import Student, Teacher

class Command(BaseCommand):
    help = 'Load data from CSV files into the database'

    def handle(self, *args, **kwargs):
        # Load students CSV
        students_df = pd.read_csv('path_to_csv/students.csv')
        for _, row in students_df.iterrows():
            Student.objects.create(
                name=row['name'],
                age=row['age'],
                student_class=row['class'],
                enrollment_date=row['enrollment_date']
            )

        # Load teachers CSV
        teachers_df = pd.read_csv('path_to_csv/teachers.csv')
        for _, row in teachers_df.iterrows():
            Teacher.objects.create(
                name=row['name'],
                subject=row['subject'],
                hire_date=row['hire_date']
            )

# Generated by Django 2.2.6 on 2020-03-10 00:29

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('elprofessor', '0004_auto_20200307_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='proj_dept',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('CSE', 'Computer Science and Engineering'), ('ECE', 'Electronics & Commmunication  Engineering'), ('EEE', 'Electrical & Electronics Engineering'), ('ME', 'Mechanical Engineering'), ('CST', 'Chemical Science and Technology'), ('CL', 'Chemical Engineering'), ('MNC', 'Maths and Computing'), ('CE', 'Civil Engineering'), ('BT', 'Bio Technology'), ('EP', 'Engineering Physics')], max_length=34),
        ),
        migrations.AlterField(
            model_name='project',
            name='proj_status',
            field=models.CharField(choices=[('NA', 'Not Assigned'), ('OG', 'Ongoing'), ('CP', 'Completed')], default='na', max_length=2),
        ),
    ]
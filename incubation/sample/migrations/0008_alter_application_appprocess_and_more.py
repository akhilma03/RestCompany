# Generated by Django 4.0.6 on 2022-07-26 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0007_alter_application_appprocess_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='AppProcess',
            field=models.CharField(choices=[('Registration_Approved', 'Registration_Approved'), ('Under_Process ', 'Under_Process'), ('Approved', 'Approved')], default='Registration Approved', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='incubationtype',
            field=models.CharField(choices=[('Physical_Incubation', 'Physical_Incubation'), ('Virtual_Incubation ', 'Virtual_Incubation')], max_length=100),
        ),
    ]
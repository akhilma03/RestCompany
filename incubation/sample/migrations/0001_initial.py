# Generated by Django 4.0.6 on 2022-07-23 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('Address', models.TextField()),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('company_name', models.CharField(max_length=200)),
                ('compay_logo', models.ImageField(upload_to='uploads/')),
                ('team_background', models.TextField()),
                ('about_companyProducts', models.TextField()),
                ('problems', models.TextField()),
                ('uniqueSolution', models.TextField()),
                ('valueProposition', models.TextField()),
                ('competativeAdvantage', models.TextField()),
                ('revenue', models.CharField(max_length=200)),
                ('marketsize', models.CharField(max_length=200)),
                ('marketplan', models.TextField()),
                ('incubationtype', models.CharField(choices=[('PI', 'Physical Incubation'), ('VI', 'Virtual Incubation ')], max_length=100)),
                ('detailProposal', models.TextField()),
            ],
        ),
    ]

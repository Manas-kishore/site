# Generated by Django 4.0 on 2022-01-02 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vac',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=122)),
                ('email1', models.CharField(max_length=122)),
                ('phone1', models.CharField(max_length=12)),
                ('desc1', models.TextField()),
                ('date1', models.DateField()),
            ],
        ),
    ]

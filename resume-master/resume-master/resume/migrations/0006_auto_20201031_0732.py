# Generated by Django 3.1.2 on 2020-10-31 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0005_auto_20201031_0646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='degree',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='education',
            name='passing_year',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='projectorjob',
            name='end_date',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='projectorjob',
            name='start_date',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='projectorjob',
            name='work',
            field=models.CharField(max_length=200),
        ),
    ]

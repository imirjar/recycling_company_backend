# Generated by Django 3.1.7 on 2021-06-08 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='performer',
            old_name='representative',
            new_name='second_name',
        ),
        migrations.AlterField(
            model_name='requisitionanswer',
            name='accepted_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='requisitionanswer',
            name='created_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
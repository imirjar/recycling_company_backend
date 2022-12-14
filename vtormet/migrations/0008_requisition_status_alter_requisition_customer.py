# Generated by Django 4.0.2 on 2022-05-02 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vtormet', '0007_requisitionbid'),
    ]

    operations = [
        migrations.AddField(
            model_name='requisition',
            name='status',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='requisition',
            name='customer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='vtormet.customer'),
        ),
    ]

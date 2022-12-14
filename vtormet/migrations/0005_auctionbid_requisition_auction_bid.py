# Generated by Django 4.0.2 on 2022-03-28 09:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vtormet', '0004_requisitionitem_requisition'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuctionBid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid_sum', models.IntegerField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='requisition',
            name='auction_bid',
            field=models.ManyToManyField(default=None, to='vtormet.AuctionBid'),
        ),
    ]

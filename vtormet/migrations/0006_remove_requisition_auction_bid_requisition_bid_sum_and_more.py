# Generated by Django 4.0.2 on 2022-04-04 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vtormet', '0005_auctionbid_requisition_auction_bid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requisition',
            name='auction_bid',
        ),
        migrations.AddField(
            model_name='requisition',
            name='bid_sum',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='AuctionBid',
        ),
    ]
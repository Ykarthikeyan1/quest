# Generated by Django 4.1.5 on 2023-01-06 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0005_alter_ticket_ticket_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='Dev_des',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
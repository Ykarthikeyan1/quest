# Generated by Django 4.1.5 on 2023-01-06 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_rename_project_name_ticket_developer_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='Ticket_Id',
            field=models.CharField(max_length=20, null=True),
        ),
    ]

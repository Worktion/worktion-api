# Generated by Django 3.1.7 on 2021-03-13 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_customuser_email_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='token_confirmation_email',
            field=models.UUIDField(blank=True, null=True),
        ),
    ]
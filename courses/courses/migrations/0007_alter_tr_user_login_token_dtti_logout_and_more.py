# Generated by Django 5.0.1 on 2024-02-05 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_alter_tr_user_login_token_dtti_logout_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tr_user_login_token',
            name='dtti_logout',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tr_user_login_token',
            name='dtti_updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

# Generated by Django 5.0 on 2024-02-04 06:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_useraccount_balance'),
        ('borrow_books', '0003_alter_borrowbook_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowbook',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.useraccount'),
        ),
    ]

# Generated by Django 5.0 on 2024-02-04 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borrow_books', '0015_borrowbook_user'),
        ('transactions', '0003_alter_transactions_transaction_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrowbook',
            name='balance_transaction',
        ),
        migrations.AddField(
            model_name='borrowbook',
            name='balance_transaction',
            field=models.ManyToManyField(to='transactions.transactions'),
        ),
    ]

# Generated by Django 4.2.2 on 2023-06-19 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_alter_entry_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='is_tracked',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 4.1.7 on 2023-05-01 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Recette', '0003_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='ingredients',
            new_name='dish',
        ),
    ]
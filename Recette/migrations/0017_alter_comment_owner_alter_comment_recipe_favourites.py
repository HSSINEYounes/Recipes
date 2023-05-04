# Generated by Django 4.1.7 on 2023-05-03 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Recette', '0016_rename_post_comment_recipe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Recette.user'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Recette.recipe'),
        ),
        migrations.CreateModel(
            name='favourites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ReqUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Recette.user')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Recette.recipe')),
            ],
        ),
    ]
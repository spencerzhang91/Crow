# Generated by Django 2.0.7 on 2018-07-11 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordcards', '0004_image_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='image_id',
            new_name='word',
        ),
        migrations.RemoveField(
            model_name='word',
            name='word_image_id',
        ),
        migrations.AlterField(
            model_name='image',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='word',
            name='word_def',
            field=models.TextField(),
        ),
    ]

# Generated by Django 3.1.7 on 2022-09-15 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fun', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fun',
            old_name='choi',
            new_name='choi1',
        ),
        migrations.AddField(
            model_name='fun',
            name='choi2',
            field=models.TextField(default=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fun',
            name='choi3',
            field=models.TextField(default=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fun',
            name='choi4',
            field=models.TextField(default=100),
            preserve_default=False,
        ),
    ]

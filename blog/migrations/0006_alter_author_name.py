# Generated by Django 4.2.4 on 2023-08-22 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_author_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Author Name'),
        ),
    ]

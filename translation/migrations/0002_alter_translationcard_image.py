# Generated by Django 4.1.4 on 2023-01-02 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='translationcard',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='uploaded'),
        ),
    ]
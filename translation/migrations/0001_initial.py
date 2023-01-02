# Generated by Django 4.1.4 on 2023-01-02 10:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TranslationCard',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('translate_request', models.TextField(blank=True, max_length=2000, null=True)),
                ('image', models.ImageField(default='default.jpg', upload_to='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
# Generated by Django 4.2.2 on 2023-06-06 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='photo')),
            ],
        ),
    ]

# Generated by Django 4.0.1 on 2022-02-02 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomm', '0002_upload_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
# Generated by Django 4.0.1 on 2022-02-01 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='upload_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='upload/product')),
            ],
        ),
    ]

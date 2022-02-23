# Generated by Django 4.0.1 on 2022-02-03 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecomm', '0004_upload_image_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='upload/product')),
                ('price', models.IntegerField(default=100)),
                ('description', models.CharField(default='good', max_length=255)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ecomm.category')),
            ],
        ),
        migrations.DeleteModel(
            name='upload_image',
        ),
    ]

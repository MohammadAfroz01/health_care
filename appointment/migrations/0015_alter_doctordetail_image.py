# Generated by Django 5.0.2 on 2024-08-04 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0014_doctordetail_image_alter_list_departments_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctordetail',
            name='image',
            field=models.ImageField(upload_to='doctor_images/'),
        ),
    ]

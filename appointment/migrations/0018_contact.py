# Generated by Django 5.0.2 on 2024-08-07 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0017_alter_list_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_name', models.CharField(max_length=150)),
                ('Email_id', models.CharField(max_length=100)),
                ('Query', models.CharField(max_length=100)),
                ('Ph_number', models.BigIntegerField()),
                ('Message', models.TextField()),
            ],
        ),
    ]

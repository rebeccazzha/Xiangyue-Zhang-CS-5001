# Generated by Django 4.2 on 2023-04-15 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_thumbnail_remove_userinfo_depart_delete_department_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=16, verbose_name='Base')),
            ],
        ),
    ]

# Generated by Django 3.2.18 on 2023-05-03 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allocation', '0003_auto_20230503_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='courses',
            field=models.ManyToManyField(blank=True, related_name='courseload', to='allocation.Course'),
        ),
    ]

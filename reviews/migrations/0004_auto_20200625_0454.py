# Generated by Django 3.0.7 on 2020-06-25 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20200625_0452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='image',
            field=models.FileField(upload_to='city/04:54:03'),
        ),
        migrations.AlterField(
            model_name='review',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='reviews/04:54:03'),
        ),
    ]
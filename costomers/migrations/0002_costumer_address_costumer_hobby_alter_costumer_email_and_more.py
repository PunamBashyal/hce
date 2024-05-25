# Generated by Django 5.0.6 on 2024-05-12 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costomers', '0001_initial'),
        ]

    operations = [
        
        
        migrations.AddField(
            model_name='costomer',
            name='address',
            field=models.CharField(default=0, max_length=100),
        ),
        
        
        migrations.AlterField(
            model_name='costomer',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='costomer',
            name='phone',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 4.0.2 on 2022-02-20 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mbkkaround',
            name='mbkword',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='mbkkaround',
            name='mbtype',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]

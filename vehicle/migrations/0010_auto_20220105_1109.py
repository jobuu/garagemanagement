# Generated by Django 3.2.9 on 2022-01-05 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0009_attendance'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='paymentmethod',
            field=models.CharField(blank=True, choices=[('manual payment', 'manual pay'), ('insurance', 'insurance ')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='mechanic',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='request',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

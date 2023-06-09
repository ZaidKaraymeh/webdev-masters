# Generated by Django 4.2 on 2023-04-23 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_courseregistration_bundle'),
    ]

    operations = [
        migrations.CreateModel(
            name='BundleRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('bundle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.bundle')),
            ],
        ),
    ]

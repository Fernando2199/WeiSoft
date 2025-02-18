# Generated by Django 5.1.2 on 2024-10-13 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(choices=[('motion_detected', 'Motion Detected'), ('car_moved', 'Car Moved Without Key')], max_length=50)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]

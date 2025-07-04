# Generated by Django 5.2.1 on 2025-06-17 14:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_alter_committee_chair_alter_committee_shorthand_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('file', models.FileField(upload_to='reports/')),
                ('uploaded_at', models.DateTimeField(auto_now=True)),
                ('committee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='base.committee')),
            ],
        ),
    ]

# Generated by Django 3.0 on 2019-12-27 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_maint'),
    ]

    operations = [
        migrations.AddField(
            model_name='maint',
            name='motorcycle',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='main_app.Motorcycle'),
            preserve_default=False,
        ),
    ]

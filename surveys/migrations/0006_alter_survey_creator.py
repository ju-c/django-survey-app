# Generated by Django 3.2.3 on 2021-05-27 12:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('surveys', '0005_alter_survey_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customuser'),
        ),
    ]

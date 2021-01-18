# Generated by Django 3.1.2 on 2020-12-08 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dtp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full', models.CharField(max_length=30)),
                ('short', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='title',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='dtp.doctortitle'),
        ),
    ]
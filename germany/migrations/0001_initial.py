# Generated by Django 4.1.6 on 2023-02-13 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('c_name', models.CharField(max_length=200, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('l_name', models.CharField(max_length=255)),
                ('c_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='germany.country')),
            ],
        ),
        migrations.CreateModel(
            name='BusinessPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('value1', models.PositiveIntegerField()),
                ('value2', models.PositiveIntegerField()),
                ('value3', models.PositiveIntegerField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='germany.location')),
            ],
        ),
    ]
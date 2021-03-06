# Generated by Django 3.2.3 on 2021-06-11 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('fill_priority', models.IntegerField()),
                ('motorcycle_spaces', models.IntegerField()),
                ('car_spaces', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LevelSpace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variety', models.CharField(max_length=150)),
                ('level_name', models.CharField(max_length=150)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='level_spaces', to='levels.level')),
            ],
        ),
    ]

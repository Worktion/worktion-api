# Generated by Django 3.1.3 on 2020-11-27 01:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0001_initial'),
        ('routines', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExecutionBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('routine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blocks_routine', to='routines.routine')),
            ],
        ),
        migrations.CreateModel(
            name='ExecutionExercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('typeExecution', models.CharField(choices=[('secs', 'Seconds'), ('reps', 'Repetitions')], max_length=11)),
                ('execution_block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='executions_block', to='routines.executionblock')),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='execution_exercise', to='exercises.exercise')),
            ],
        ),
    ]

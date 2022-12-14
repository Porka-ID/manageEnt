# Generated by Django 4.1.1 on 2022-10-05 06:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('birthdate', models.DateField()),
                ('birthplace', models.CharField(max_length=30)),
                ('sex', models.BooleanField()),
                ('nationality', models.CharField(max_length=60)),
                ('numRegNat', models.IntegerField()),
                ('numAccount', models.CharField(max_length=40)),
                ('stateCivil', models.CharField(max_length=60)),
                ('adresse', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Entreprise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('logopath', models.ImageField(upload_to='uploads/')),
                ('numeroEnt', models.IntegerField()),
                ('namePDG', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='rank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('levelRank', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='relationnel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idEmploye', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entreprise.employe')),
                ('idEnt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entreprise.entreprise')),
                ('idRank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entreprise.rank')),
            ],
        ),
    ]

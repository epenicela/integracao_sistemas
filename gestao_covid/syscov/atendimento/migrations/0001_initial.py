# Generated by Django 4.1.1 on 2022-10-02 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('nacionalidade', models.CharField(max_length=50)),
                ('naturalidade', models.CharField(max_length=50)),
                ('data_nascimento', models.DateField()),
                ('sexo', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Vacina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_vac', models.CharField(max_length=255)),
                ('nr_dose', models.IntegerField()),
                ('validade', models.DateField()),
                ('quantidade', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Vacinacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_vacinacao', models.DateField()),
                ('nr_dose', models.CharField(max_length=255)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atendimento.paciente')),
                ('vacina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atendimento.vacina')),
            ],
        ),
        migrations.CreateModel(
            name='Saida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_saida', models.DateField()),
                ('quantidade_saida', models.IntegerField(default=1)),
                ('vacina_saida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atendimento.vacina')),
            ],
        ),
        migrations.CreateModel(
            name='Exame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_exame', models.DateField()),
                ('resultado_exame', models.BooleanField(default=False)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atendimento.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_entrada', models.DateField()),
                ('quantidade_entrada', models.IntegerField(default=1)),
                ('vacina_entrada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atendimento.vacina')),
            ],
        ),
    ]

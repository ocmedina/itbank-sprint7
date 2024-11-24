# Generated by Django 4.2.15 on 2024-11-22 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tipo_cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_surname', models.CharField(max_length=100)),
                ('customer_DNI', models.CharField(max_length=10, unique=True)),
                ('branch_id', models.IntegerField()),
                ('dob', models.DateField()),
                ('tipo_cliente', models.ForeignKey(db_column='tipo_cliente_id', on_delete=django.db.models.deletion.CASCADE, to='tipo_cliente.tipocliente')),
            ],
        ),
    ]
# Generated by Django 4.1.5 on 2023-08-07 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('atm_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='trans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_date', models.DateTimeField()),
                ('t_type', models.CharField(blank=True, max_length=50)),
                ('t_amount', models.CharField(blank=True, max_length=50)),
                ('p_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atm_app.tb_atm')),
            ],
        ),
    ]

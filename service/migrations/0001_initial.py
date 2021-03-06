# Generated by Django 2.2.7 on 2020-11-03 03:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('contact', models.IntegerField()),
                ('city', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('service_id', models.AutoField(primary_key=True, serialize=False)),
                ('company', models.CharField(max_length=200)),
                ('registation_no', models.IntegerField()),
                ('service_date', models.DateField()),
                ('service_time', models.TimeField()),
                ('delivery_type', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('panding', 'panding'), ('apsept', 'apsept'), ('reject', 'reject')], max_length=200)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.User')),
            ],
        ),
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parts_price', models.IntegerField()),
                ('mekenic_charge', models.IntegerField()),
                ('status', models.BooleanField(default=True)),
                ('service_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.Service')),
            ],
        ),
    ]

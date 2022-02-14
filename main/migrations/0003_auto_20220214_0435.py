# Generated by Django 3.2.9 on 2022-02-14 04:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_employee_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit',
            name='employee',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='main.employee', verbose_name='Сотрудник'),
        ),
        migrations.AlterField(
            model_name='visit',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.store'),
        ),
    ]
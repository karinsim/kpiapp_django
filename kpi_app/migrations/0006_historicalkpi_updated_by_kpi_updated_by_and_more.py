# Generated by Django 4.2.5 on 2023-10-30 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kpi_app', '0005_historicalkpi_month_historicalkpi_year_kpi_month_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalkpi',
            name='updated_by',
            field=models.CharField(default='johndoe', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kpi',
            name='updated_by',
            field=models.CharField(default='johndoe', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='historicalkpi',
            name='month',
            field=models.IntegerField(choices=[(1, 'Jan'), (2, 'Feb'), (3, 'Mar'), (4, 'Apr'), (5, 'May'), (6, 'Jun'), (7, 'Jul'), (8, 'Aug'), (9, 'Sep'), (10, 'Oct'), (11, 'Nov'), (12, 'Dec')], default=1),
        ),
        migrations.AlterField(
            model_name='historicalkpi',
            name='year',
            field=models.IntegerField(default=2023),
        ),
        migrations.AlterField(
            model_name='kpi',
            name='month',
            field=models.IntegerField(choices=[(1, 'Jan'), (2, 'Feb'), (3, 'Mar'), (4, 'Apr'), (5, 'May'), (6, 'Jun'), (7, 'Jul'), (8, 'Aug'), (9, 'Sep'), (10, 'Oct'), (11, 'Nov'), (12, 'Dec')], default=1),
        ),
        migrations.AlterField(
            model_name='kpi',
            name='year',
            field=models.IntegerField(default=2023),
        ),
    ]

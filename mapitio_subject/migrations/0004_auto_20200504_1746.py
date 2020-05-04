# Generated by Django 3.0.4 on 2020-05-04 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapitio_subject', '0003_auto_20200504_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='deathreport',
            name='death_cause_known',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=15, verbose_name='Is the cause of death known?'),
        ),
        migrations.AddField(
            model_name='historicaldeathreport',
            name='death_cause_known',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=15, verbose_name='Is the cause of death known?'),
        ),
        migrations.AlterField(
            model_name='deathreport',
            name='death_cause',
            field=models.TextField(blank=True, null=True, verbose_name='The cause of death as recorded in the patient notes'),
        ),
        migrations.AlterField(
            model_name='historicaldeathreport',
            name='death_cause',
            field=models.TextField(blank=True, null=True, verbose_name='The cause of death as recorded in the patient notes'),
        ),
    ]

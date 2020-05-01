# Generated by Django 3.0.4 on 2020-04-30 17:49

from django.db import migrations, models
import edc_model.validators.date


class Migration(migrations.Migration):

    dependencies = [
        ("mapitio_screening", "0002_auto_20200430_0315"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalsubjectscreening",
            name="file_number",
            field=models.CharField(
                default="0",
                help_text="Patient file number from Hindu Mandal Hospital",
                max_length=25,
                verbose_name="Patient File number",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="subjectscreening",
            name="file_number",
            field=models.CharField(
                default="0",
                help_text="Patient file number from Hindu Mandal Hospital",
                max_length=25,
                verbose_name="Patient File number",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="historicalsubjectscreening",
            name="confirm_hospital_identifier",
            field=models.CharField(
                help_text="Retype the Hindu Mandal Hospital Identifier",
                max_length=25,
                verbose_name="Confirm HMS Identifier",
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectscreening",
            name="hospital_identifier",
            field=models.CharField(
                db_index=True,
                help_text="Hindu Mandal Hospital Identifier",
                max_length=25,
                verbose_name="HMS Identifier",
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectscreening",
            name="last_clinic_date",
            field=models.DateField(
                help_text="Date last seen according to information on the patient chart.",
                validators=[edc_model.validators.date.date_is_past],
                verbose_name="Date patient was <u>last</u>> seen at this clinic",
            ),
        ),
        migrations.AlterField(
            model_name="subjectscreening",
            name="confirm_hospital_identifier",
            field=models.CharField(
                help_text="Retype the Hindu Mandal Hospital Identifier",
                max_length=25,
                verbose_name="Confirm HMS Identifier",
            ),
        ),
        migrations.AlterField(
            model_name="subjectscreening",
            name="hospital_identifier",
            field=models.CharField(
                help_text="Hindu Mandal Hospital Identifier",
                max_length=25,
                unique=True,
                verbose_name="HMS Identifier",
            ),
        ),
        migrations.AlterField(
            model_name="subjectscreening",
            name="last_clinic_date",
            field=models.DateField(
                help_text="Date last seen according to information on the patient chart.",
                validators=[edc_model.validators.date.date_is_past],
                verbose_name="Date patient was <u>last</u>> seen at this clinic",
            ),
        ),
    ]

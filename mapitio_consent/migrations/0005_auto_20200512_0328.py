# Generated by Django 3.0.4 on 2020-05-12 00:28

from django.db import migrations
import edc_visit_tracking.managers
import mapitio_consent.models.subject_consent


class Migration(migrations.Migration):

    dependencies = [
        ("mapitio_consent", "0004_auto_20200512_0309"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="subjectconsent",
            managers=[
                ("on_site", edc_visit_tracking.managers.CurrentSiteManager()),
                (
                    "objects",
                    mapitio_consent.models.subject_consent.SubjectConsentManager(),
                ),
            ],
        ),
    ]

# Generated by Django 3.0.4 on 2020-03-29 01:38

import _socket
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_audit_fields.fields.hostname_modification_field
import django_audit_fields.fields.userfield
import django_audit_fields.fields.uuid_auto_field
import django_audit_fields.models.audit_model_mixin
import django_crypto_fields.fields.encrypted_char_field
import django_crypto_fields.fields.identity_field
import django_revision.revision_field
import edc_model.models.fields.height
import edc_model.models.fields.waist_circumference
import edc_model_fields.fields.date_estimated
import edc_sites.models
import edc_utils.date
import simple_history.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("sites", "0002_alter_domain_unique"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("mapitio_subject", "0003_historicalsubjectrequisition_subjectrequisition"),
    ]

    operations = [
        migrations.CreateModel(
            name="Enrolment",
            fields=[
                (
                    "revision",
                    django_revision.revision_field.RevisionField(
                        blank=True,
                        editable=False,
                        help_text="System field. Git repository tag:branch:commit.",
                        max_length=75,
                        null=True,
                        verbose_name="Revision",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        blank=True,
                        default=django_audit_fields.models.audit_model_mixin.utcnow,
                    ),
                ),
                (
                    "modified",
                    models.DateTimeField(
                        blank=True,
                        default=django_audit_fields.models.audit_model_mixin.utcnow,
                    ),
                ),
                (
                    "user_created",
                    django_audit_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user created",
                    ),
                ),
                (
                    "user_modified",
                    django_audit_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user modified",
                    ),
                ),
                (
                    "hostname_created",
                    models.CharField(
                        blank=True,
                        default=_socket.gethostname,
                        help_text="System field. (modified on create only)",
                        max_length=60,
                    ),
                ),
                (
                    "hostname_modified",
                    django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                        blank=True,
                        help_text="System field. (modified on every save)",
                        max_length=50,
                    ),
                ),
                ("device_created", models.CharField(blank=True, max_length=10)),
                ("device_modified", models.CharField(blank=True, max_length=10)),
                (
                    "id",
                    django_audit_fields.fields.uuid_auto_field.UUIDAutoField(
                        blank=True,
                        editable=False,
                        help_text="System auto field. UUID primary key.",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("subject_identifier", models.CharField(max_length=50, unique=True)),
                (
                    "subject_identifier_as_pk",
                    models.UUIDField(default=uuid.uuid4, editable=False),
                ),
                (
                    "subject_identifier_aka",
                    models.CharField(
                        editable=False,
                        help_text="track a previously allocated identifier.",
                        max_length=50,
                        null=True,
                        verbose_name="Subject Identifier a.k.a",
                    ),
                ),
                (
                    "identity",
                    django_crypto_fields.fields.identity_field.IdentityField(
                        help_text=" (Encryption: RSA local)",
                        max_length=71,
                        verbose_name="Identity number",
                    ),
                ),
                (
                    "identity_type",
                    models.CharField(
                        choices=[
                            ("country_id", "Country ID number"),
                            ("drivers", "Driver's license"),
                            ("passport", "Passport"),
                            ("hospital_no", "Hospital number"),
                            ("country_id_rcpt", "Country ID receipt"),
                            ("mobile_no", "Mobile number"),
                            ("OTHER", "Other"),
                        ],
                        max_length=25,
                        verbose_name="What type of identity number is this?",
                    ),
                ),
                (
                    "confirm_identity",
                    django_crypto_fields.fields.identity_field.IdentityField(
                        help_text="Retype the identity number (Encryption: RSA local)",
                        max_length=71,
                        null=True,
                    ),
                ),
                (
                    "report_datetime",
                    models.DateTimeField(
                        default=edc_utils.date.get_utcnow,
                        help_text="Date and time of this report.",
                        verbose_name="Report Date and Time",
                    ),
                ),
                (
                    "initials",
                    django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                        blank=True,
                        help_text="Use UPPERCASE letters only. May be 2 or 3 letters. (Encryption: RSA local)",
                        max_length=71,
                        validators=[
                            django.core.validators.RegexValidator(
                                "[A-Z]{1,3}", "Invalid format"
                            ),
                            django.core.validators.MinLengthValidator(2),
                            django.core.validators.MaxLengthValidator(3),
                        ],
                    ),
                ),
                ("dob", models.DateField(verbose_name="Date of birth")),
                (
                    "is_dob_estimated",
                    edc_model_fields.fields.date_estimated.IsDateEstimatedField(
                        choices=[
                            ("-", "No"),
                            ("D", "Yes, estimated the Day"),
                            ("MD", "Yes, estimated Month and Day"),
                            ("YMD", "Yes, estimated Year, Month and Day"),
                        ],
                        help_text="If the exact date is not known, please indicate which part of the date is estimated.",
                        max_length=25,
                        verbose_name="Is date of birth estimated?",
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female")], max_length=10
                    ),
                ),
                (
                    "age_in_years",
                    models.IntegerField(
                        editable=False,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(110),
                        ],
                    ),
                ),
                (
                    "hospital_identifier",
                    django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                        blank=True,
                        help_text=" (Encryption: RSA local)",
                        max_length=71,
                        unique=True,
                    ),
                ),
                (
                    "clinic_registration_datetime",
                    models.DateTimeField(
                        default=edc_utils.date.get_utcnow,
                        verbose_name="Date patient enrolled at the clinic",
                    ),
                ),
                (
                    "crf_status",
                    models.CharField(
                        choices=[
                            ("incomplete", "Incomplete (some data pending)"),
                            ("complete", "Complete"),
                        ],
                        max_length=25,
                        verbose_name="CRF status",
                    ),
                ),
                ("comments", models.TextField(blank=True, null=True)),
                (
                    "site",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="sites.Site",
                    ),
                ),
            ],
            options={"verbose_name": "Enrolment", "verbose_name_plural": "Enrolment",},
            managers=[("on_site", edc_sites.models.CurrentSiteManager()),],
        ),
        migrations.CreateModel(
            name="HistoricalEnrolment",
            fields=[
                (
                    "revision",
                    django_revision.revision_field.RevisionField(
                        blank=True,
                        editable=False,
                        help_text="System field. Git repository tag:branch:commit.",
                        max_length=75,
                        null=True,
                        verbose_name="Revision",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        blank=True,
                        default=django_audit_fields.models.audit_model_mixin.utcnow,
                    ),
                ),
                (
                    "modified",
                    models.DateTimeField(
                        blank=True,
                        default=django_audit_fields.models.audit_model_mixin.utcnow,
                    ),
                ),
                (
                    "user_created",
                    django_audit_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user created",
                    ),
                ),
                (
                    "user_modified",
                    django_audit_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user modified",
                    ),
                ),
                (
                    "hostname_created",
                    models.CharField(
                        blank=True,
                        default=_socket.gethostname,
                        help_text="System field. (modified on create only)",
                        max_length=60,
                    ),
                ),
                (
                    "hostname_modified",
                    django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                        blank=True,
                        help_text="System field. (modified on every save)",
                        max_length=50,
                    ),
                ),
                ("device_created", models.CharField(blank=True, max_length=10)),
                ("device_modified", models.CharField(blank=True, max_length=10)),
                (
                    "id",
                    django_audit_fields.fields.uuid_auto_field.UUIDAutoField(
                        blank=True,
                        db_index=True,
                        editable=False,
                        help_text="System auto field. UUID primary key.",
                    ),
                ),
                ("subject_identifier", models.CharField(db_index=True, max_length=50)),
                (
                    "subject_identifier_as_pk",
                    models.UUIDField(default=uuid.uuid4, editable=False),
                ),
                (
                    "subject_identifier_aka",
                    models.CharField(
                        editable=False,
                        help_text="track a previously allocated identifier.",
                        max_length=50,
                        null=True,
                        verbose_name="Subject Identifier a.k.a",
                    ),
                ),
                (
                    "identity",
                    django_crypto_fields.fields.identity_field.IdentityField(
                        help_text=" (Encryption: RSA local)",
                        max_length=71,
                        verbose_name="Identity number",
                    ),
                ),
                (
                    "identity_type",
                    models.CharField(
                        choices=[
                            ("country_id", "Country ID number"),
                            ("drivers", "Driver's license"),
                            ("passport", "Passport"),
                            ("hospital_no", "Hospital number"),
                            ("country_id_rcpt", "Country ID receipt"),
                            ("mobile_no", "Mobile number"),
                            ("OTHER", "Other"),
                        ],
                        max_length=25,
                        verbose_name="What type of identity number is this?",
                    ),
                ),
                (
                    "confirm_identity",
                    django_crypto_fields.fields.identity_field.IdentityField(
                        help_text="Retype the identity number (Encryption: RSA local)",
                        max_length=71,
                        null=True,
                    ),
                ),
                (
                    "report_datetime",
                    models.DateTimeField(
                        default=edc_utils.date.get_utcnow,
                        help_text="Date and time of this report.",
                        verbose_name="Report Date and Time",
                    ),
                ),
                (
                    "initials",
                    django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                        blank=True,
                        help_text="Use UPPERCASE letters only. May be 2 or 3 letters. (Encryption: RSA local)",
                        max_length=71,
                        validators=[
                            django.core.validators.RegexValidator(
                                "[A-Z]{1,3}", "Invalid format"
                            ),
                            django.core.validators.MinLengthValidator(2),
                            django.core.validators.MaxLengthValidator(3),
                        ],
                    ),
                ),
                ("dob", models.DateField(verbose_name="Date of birth")),
                (
                    "is_dob_estimated",
                    edc_model_fields.fields.date_estimated.IsDateEstimatedField(
                        choices=[
                            ("-", "No"),
                            ("D", "Yes, estimated the Day"),
                            ("MD", "Yes, estimated Month and Day"),
                            ("YMD", "Yes, estimated Year, Month and Day"),
                        ],
                        help_text="If the exact date is not known, please indicate which part of the date is estimated.",
                        max_length=25,
                        verbose_name="Is date of birth estimated?",
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female")], max_length=10
                    ),
                ),
                (
                    "age_in_years",
                    models.IntegerField(
                        editable=False,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(110),
                        ],
                    ),
                ),
                (
                    "hospital_identifier",
                    django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                        blank=True,
                        db_index=True,
                        help_text=" (Encryption: RSA local)",
                        max_length=71,
                    ),
                ),
                (
                    "clinic_registration_datetime",
                    models.DateTimeField(
                        default=edc_utils.date.get_utcnow,
                        verbose_name="Date patient enrolled at the clinic",
                    ),
                ),
                (
                    "crf_status",
                    models.CharField(
                        choices=[
                            ("incomplete", "Incomplete (some data pending)"),
                            ("complete", "Complete"),
                        ],
                        max_length=25,
                        verbose_name="CRF status",
                    ),
                ),
                ("comments", models.TextField(blank=True, null=True)),
                (
                    "history_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "site",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="sites.Site",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical Enrolment",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.RemoveField(model_name="historicalenrollment", name="history_user",),
        migrations.RemoveField(model_name="historicalenrollment", name="site",),
        migrations.AlterField(
            model_name="baselinedata",
            name="height",
            field=edc_model.models.fields.height.HeightField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="baselinedata",
            name="waist_circumference",
            field=edc_model.models.fields.waist_circumference.WaistCircumferenceField(
                blank=True, null=True
            ),
        ),
        migrations.AlterField(
            model_name="historicalbaselinedata",
            name="height",
            field=edc_model.models.fields.height.HeightField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="historicalbaselinedata",
            name="waist_circumference",
            field=edc_model.models.fields.waist_circumference.WaistCircumferenceField(
                blank=True, null=True
            ),
        ),
        migrations.DeleteModel(name="Enrollment",),
        migrations.DeleteModel(name="HistoricalEnrollment",),
    ]

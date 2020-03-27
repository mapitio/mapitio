from django.db import models
from edc_constants.choices import YES_NO, YES_NO_NA
from edc_constants.constants import NOT_APPLICABLE
from edc_crf.model_mixins import CrfModelMixin
from edc_model.models.base_uuid_model import BaseUuidModel
from mapitio_subject.choices import CRF_STATUS

from .subject_visit import SubjectVisit


class FollowUp(CrfModelMixin, BaseUuidModel):

    subject_visit = models.ForeignKey(SubjectVisit, on_delete=models.PROTECT)

    diabetes = models.CharField(
        verbose_name="Since the patient started at this clinic, have they developed diabetes?",
        max_length=25,
        choices=YES_NO,
    )

    diabetes_dx_date = models.DateField(
        verbose_name="If YES, when was the diagnosis of diabetes made?",
        null=True,
        blank=True,
    )

    diabetes_rx = models.TextField(
        verbose_name="List of diabetes treatment", null=True, blank=True,
    )

    hypertension = models.CharField(
        verbose_name="Since the patient started at this clinic, have they developed hypertension?",
        max_length=25,
        choices=YES_NO,
    )

    hypertension_dx_date = models.DateField(
        verbose_name="If YES, when was the hypertension of diabetes made?",
        null=True,
        blank=True,
    )

    hypertension_rx = models.TextField(
        verbose_name="List of hypertension treatment", null=True, blank=True,
    )

    stroke = models.CharField(
        verbose_name="Stroke", max_length=25, choices=YES_NO_NA, default=NOT_APPLICABLE
    )

    stroke_dx_date = models.DateField(
        verbose_name="If YES, date of stroke diagnosis", null=True, blank=True,
    )

    diabetic_foot = models.CharField(
        verbose_name="Diabetic Foot",
        max_length=25,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
    )

    diabetic_foot_dx_date = models.DateField(
        verbose_name="If YES, date of diabetic foot", null=True, blank=True,
    )

    chronic_heart_failure = models.CharField(
        verbose_name="Chronic Heart Failure",
        max_length=25,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
    )

    chronic_heart_failure_dx_date = models.DateField(
        verbose_name="If YES, date of chronic heart failure", null=True, blank=True,
    )

    chronic_renal_failure = models.CharField(
        verbose_name="Chronic Renal Failure",
        max_length=25,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
    )

    chronic_renal_failure_dx_date = models.DateField(
        verbose_name="If YES, date of chronic renal failure", null=True, blank=True,
    )

    crf_status = models.CharField(
        verbose_name="CRF status", max_length=25, choices=CRF_STATUS
    )

    comments = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Follow Up"
        verbose_name_plural = "Follow Ups"

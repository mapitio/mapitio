from copy import copy
from edc_auth.codenames import clinic as default


default += [
    "mapitio_lists.view_arvregimens",
    "mapitio_lists.view_chestxrayfindings",
    "mapitio_lists.view_cholesterolmedications",
    "mapitio_lists.view_conditions",
    "mapitio_lists.view_diabetesmedications",
    "mapitio_lists.view_ecgfindings",
    "mapitio_lists.view_echofindings",
    "mapitio_lists.view_hypertensionmedications",
    "mapitio_lists.view_offstudyreasons",
    "mapitio_prn.add_endofstudy",
    "mapitio_prn.add_losstofollowup",
    "mapitio_prn.add_onschedule",
    "mapitio_prn.add_protocoldeviationviolation",
    "mapitio_prn.change_endofstudy",
    "mapitio_prn.change_losstofollowup",
    "mapitio_prn.change_onschedule",
    "mapitio_prn.change_protocoldeviationviolation",
    "mapitio_prn.delete_endofstudy",
    "mapitio_prn.delete_losstofollowup",
    "mapitio_prn.delete_onschedule",
    "mapitio_prn.delete_protocoldeviationviolation",
    "mapitio_prn.view_endofstudy",
    "mapitio_prn.view_historicalendofstudy",
    "mapitio_prn.view_historicallosstofollowup",
    "mapitio_prn.view_historicalonschedule",
    "mapitio_prn.view_historicalprotocoldeviationviolation",
    "mapitio_prn.view_losstofollowup",
    "mapitio_prn.view_onschedule",
    "mapitio_prn.view_protocoldeviationviolation",
    "mapitio_prn.view_unblindingrequestoruser",
    "mapitio_prn.view_unblindingrevieweruser",
    "mapitio_subject.add_biomedicalhistory",
    "mapitio_subject.add_biomedicalfollowup",
    "mapitio_subject.add_complications",
    "mapitio_subject.add_deathreport",
    "mapitio_subject.add_followup",
    "mapitio_subject.add_hivhistory",
    "mapitio_subject.add_indicators",
    "mapitio_subject.add_investigations",
    "mapitio_subject.add_ncdfollowup",
    "mapitio_subject.add_ncdhistory",
    "mapitio_subject.add_subjectrequisition",
    "mapitio_subject.add_subjectvisit",
    "mapitio_subject.change_biomedicalhistory",
    "mapitio_subject.change_biomedicalfollowup",
    "mapitio_subject.change_complications",
    "mapitio_subject.change_deathreport",
    "mapitio_subject.change_followup",
    "mapitio_subject.change_hivhistory",
    "mapitio_subject.change_indicators",
    "mapitio_subject.change_investigations",
    "mapitio_subject.change_ncdfollowup",
    "mapitio_subject.change_ncdhistory",
    "mapitio_subject.change_subjectrequisition",
    "mapitio_subject.change_subjectvisit",
    "mapitio_subject.delete_biomedicalhistory",
    "mapitio_subject.delete_biomedicalfollowup",
    "mapitio_subject.delete_complications",
    "mapitio_subject.delete_deathreport",
    "mapitio_subject.delete_followup",
    "mapitio_subject.delete_hivhistory",
    "mapitio_subject.delete_indicators",
    "mapitio_subject.delete_investigations",
    "mapitio_subject.delete_ncdfollowup",
    "mapitio_subject.delete_ncdhistory",
    "mapitio_subject.delete_subjectrequisition",
    "mapitio_subject.delete_subjectvisit",
    "mapitio_subject.view_biomedicalhistory",
    "mapitio_subject.view_biomedicalfollowup",
    "mapitio_subject.view_complications",
    "mapitio_subject.view_deathreport",
    "mapitio_subject.view_followup",
    "mapitio_subject.view_historicalbiomedicalhistory",
    "mapitio_subject.view_historicalbiomedicalfollowup",
    "mapitio_subject.view_historicalcomplications",
    "mapitio_subject.view_historicaldeathreport",
    "mapitio_subject.view_historicalfollowup",
    "mapitio_subject.view_historicalhivhistory",
    "mapitio_subject.view_historicalindicators",
    "mapitio_subject.view_historicalinvestigations",
    "mapitio_subject.view_historicalncdfollowup",
    "mapitio_subject.view_historicalncdhistory",
    "mapitio_subject.view_historicalsubjectrequisition",
    "mapitio_subject.view_historicalsubjectvisit",
    "mapitio_subject.view_hivhistory",
    "mapitio_subject.view_indicators",
    "mapitio_subject.view_investigations",
    "mapitio_subject.view_ncdfollowup",
    "mapitio_subject.view_ncdhistory",
    "mapitio_subject.view_subjectrequisition",
    "mapitio_subject.view_subjectvisit",
]

default.sort()
clinic = copy(default)

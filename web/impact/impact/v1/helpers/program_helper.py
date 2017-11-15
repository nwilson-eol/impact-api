from impact.models import Program
from impact.v1.helpers.model_helper import (
    FLOAT_FIELD,
    INTEGER_FIELD,
    ModelHelper,
    PK_FIELD,
    STRING_FIELD,
)

PROGRAM_FIELDS = {
    "id": PK_FIELD,
    "name": STRING_FIELD,
    "program_family_id": INTEGER_FIELD,
    "program_family_name": STRING_FIELD,
    "cycle_id": INTEGER_FIELD,
    "cycle_name": STRING_FIELD,
    "description": STRING_FIELD,
    "start_date": STRING_FIELD,
    "end_date": STRING_FIELD,
    "location": STRING_FIELD,
    "currency_code": STRING_FIELD,
    "regular_application_fee": FLOAT_FIELD,
    "url_slug": STRING_FIELD,
    "overview_start_date": STRING_FIELD,
    "overview_deadline_date": STRING_FIELD,
}


class ProgramHelper(ModelHelper):
    model = Program

    @classmethod
    def fields(cls):
        return PROGRAM_FIELDS

    @property
    def cycle_name(self):
        if hasattr(self.subject, "cycle"):
            cycle = self.subject.cycle
            if cycle:
                return cycle.name

    @property
    def program_family_name(self):
        if hasattr(self.subject, "program_family"):
            program_family = self.subject.program_family
            if program_family:
                return program_family.name

# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

import re
from django.utils.text import camel_case_to_spaces

LABEL_LENGTH = 255


def is_managed(db_table):
    return False


def model_name_to_snake(value):
    original_model_string = camel_case_to_spaces(value)
    new_model_string = original_model_string.replace(" ", "_")
    return new_model_string


def snake_to_model_name(value):
    old_value = value.split('_')
    new_value = ""
    for word in old_value:
        new_value += (word[0].upper() + word[1:])
    return new_value

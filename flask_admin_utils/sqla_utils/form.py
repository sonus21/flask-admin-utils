from fields import SelectField

from wtforms import PasswordField

from flask.ext.admin.model.form import converts
from flask.ext.admin.contrib.sqla.form import AdminModelConverter as Converter


class AdminModelConverter(Converter):
    @converts("ChoiceType")
    def convert_choice_type(self, field_args, **extra):
        field_args['choices'] = extra['column'].type.choices
        field_args['coerce'] = extra['column'].type.impl.python_type
        return SelectField(**field_args)

    @converts("PasswordType")
    def convert_password(self, field_args, **extra):
        return PasswordField()
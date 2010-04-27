#coding:utf-8

from wtforms import Form, TextField, validators
from wtforms.validators import ValidationError
import wtforms

class AlunoForm(Form):
    nome = TextField('Nome', [validators.Required(), validators.Length(min=3, max=200)])
    data_nascimento = TextField('Data de nascimento', [validators.Required()])

    def validate_data_nascimento(form, field):
        import time
        try:
            time.strptime(field.data, '%Y-%m-%d')
        except ValueError:
            raise ValidationError('Formato inválido de data')

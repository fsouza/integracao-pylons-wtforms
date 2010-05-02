#coding:utf-8

from wtforms import Form, TextField, DateField, validators
from wtforms.validators import ValidationError
import wtforms

class AlunoForm(Form):
    nome = TextField('Nome', [validators.Required(), validators.Length(min=3, max=200)])
    data_nascimento = DateField('Data de nascimento', [validators.Required()], format = '%Y-%m-%d')


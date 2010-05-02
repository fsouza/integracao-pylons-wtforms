import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from wtforms_pylons_academico.lib.base import BaseController, render
from wtforms_pylons_academico.model.forms import AlunoForm
from wtforms_pylons_academico.model import Aluno
from wtforms_pylons_academico.model.meta import Session

from datetime import date

import time

log = logging.getLogger(__name__)

class AlunosController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/alunos.mako')
        # or, return a response
        return 'Hello World'

    def cadastrar_aluno(self):
        c.form = AlunoForm()
        return render('/novo_aluno.mako')

    def cadastrar(self):
        c.form = AlunoForm(request.params)
        if request.method == 'POST' and c.form.validate():
            aluno = Aluno()
            c.form.populate_obj(aluno)
            Session.add(aluno)
            Session.commit()
        else:
            return render('/novo_aluno.mako')
        return 'Aluno inserido com sucesso!'

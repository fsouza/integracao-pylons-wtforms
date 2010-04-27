import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from wtforms_pylons_academico.lib.base import BaseController, render
from wtforms_pylons_academico.model.forms import AlunoForm

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

from wtforms_pylons_academico.tests import *

class TestAlunosController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='alunos', action='index'))
        # Test response...

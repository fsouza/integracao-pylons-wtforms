from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1272734202.0504849
_template_filename='/home/francisco/Projetos/wtforms_pylons_academico/wtforms_pylons_academico/templates/novo_aluno.mako'
_template_uri='/novo_aluno.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<html>\n    <head>\n      <meta http-equiv="Content-type" content="text/html; charset=utf-8"/>\n      <title>Cadastro de novo aluno</title>\n      \n    </head>\n    <body id="">\n        <form action="/alunos/cadastrar" method="post" accept-charset="utf-8">\n          <div class="">\n')
        # SOURCE LINE 10
        if c.form.nome.errors:
            # SOURCE LINE 11
            __M_writer(u'                <div class="erros">\n')
            # SOURCE LINE 12
            for error in c.form.nome.errors:
                # SOURCE LINE 13
                __M_writer(u'                      ')
                __M_writer(escape( error ))
                __M_writer(u'<br />\n')
            # SOURCE LINE 15
            __M_writer(u'                </div>\n')
        # SOURCE LINE 17
        __M_writer(u'            ')
        __M_writer(escape( c.form.nome.label ))
        __M_writer(u': ')
        __M_writer(escape( c.form.nome))
        __M_writer(u'\n          </div>\n\n          <div class="">\n')
        # SOURCE LINE 21
        if c.form.data_nascimento.errors:
            # SOURCE LINE 22
            __M_writer(u'                <div class="erros">\n')
            # SOURCE LINE 23
            for error in c.form.data_nascimento.errors:
                # SOURCE LINE 24
                __M_writer(u'                      ')
                __M_writer(escape( error ))
                __M_writer(u'<br />\n')
            # SOURCE LINE 26
            __M_writer(u'                </div>\n')
        # SOURCE LINE 28
        __M_writer(u'            ')
        __M_writer(escape( c.form.data_nascimento.label ))
        __M_writer(u': ')
        __M_writer(escape( c.form.data_nascimento ))
        __M_writer(u'\n          </div>\n        \n          <p><input type="submit" value="Continue &rarr;"/></p>\n        </form>\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()



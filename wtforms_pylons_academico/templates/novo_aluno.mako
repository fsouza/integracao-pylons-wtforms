<html>
    <head>
      <meta http-equiv="Content-type" content="text/html; charset=utf-8"/>
      <title>Cadastro de novo aluno</title>
      
    </head>
    <body id="">
        <form action="/alunos/cadastrar" method="post" accept-charset="utf-8">
          <div class="">
            % if c.form.nome.errors:
                <div class="erros">
                  % for error in c.form.nome.errors:
                      ${ error }<br />
                  % endfor
                </div>
            % endif
            ${ c.form.nome.label|n,unicode }: ${ c.form.nome|n,unicode }
          </div>

          <div class="">
            % if c.form.data_nascimento.errors:
                <div class="erros">
                  % for error in c.form.data_nascimento.errors:
                      ${ error }<br />
                  % endfor
                </div>
            % endif
            ${ c.form.data_nascimento.label|n,unicode }: ${ c.form.data_nascimento|n,unicode }
          </div>
        
          <p><input type="submit" value="Continue &rarr;"/></p>
        </form>
    </body>
</html>

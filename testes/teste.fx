def func():
    return 42 # identação não funcionou automaticamente

# Isto é um comentário

/* isto não ficou como comentário */

{} # auto-closing funcionou
() # auto-closing funcionou
[] # auto-closing funcionou
'' # auto-closing funcionou mas não assumiu forma de texto (com cor diferente e etc)
"" # auto-closing não funcionou mas assumiu forma de texto
/* */ # auto-closing não funcionou e nem assumiu forma de comentário
# assumiu forma de comentário


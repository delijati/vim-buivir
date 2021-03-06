if has('python3')
    command! -nargs=1 Python python3 <args>
elseif has('python')
    command! -nargs=1 Python python <args>
else
    echo "Error: Requires Vim compiled with +python or +python3"
    finish
endif

fun! BuiVirActivate(...)
Python << EOF
import vim
if 'vimbuivir' not in sys.modules:
    import vimbuivir
else:
    import imp
    # Reload python module to avoid errors when updating plugin
    vimbuivir = imp.reload(vimbuivir)
vimbuivir.activate(vim.eval('get(a:, 1, ".")'))
EOF
endfun

" init load script parent path :h:h
execute "Python import sys"
execute "Python sys.path.append(r'" . expand("<sfile>:p:h:h") . "')"

" register command
command! -nargs=? BuiVirActivate call BuiVirActivate(<f-args>)
" call BuiVirActivate()

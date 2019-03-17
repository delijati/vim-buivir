import os

import sys
import vim


def activate():
    buildout_path = os.path.join(os.path.abspath("."), "bin", "py")
    envdir = os.path.join(os.path.abspath("."), "env")
    virtualenv_path = os.path.join(envdir, "bin", "activate_this.py")

    # XXX the global is anyway activated
    # if 'VIRTUAL_ENV' in os.environ:
    # project_base_dir = os.environ['VIRTUAL_ENV']

    if os.path.isfile(buildout_path):
        print("Buildout found (%s)" % buildout_path)
        with open(buildout_path) as f:
            data = f.read()
            data = data.replace('_interactive = True', '_interactive = False')
            exec(data)
    elif os.path.isfile(virtualenv_path):
        sys.path.insert(0, envdir)
        vim.command("let g:python3_host_prog = '%s'" % os.path.join(
            envdir, "bin", "python"))
        print("Virtualenv found: (%s)" % virtualenv_path)
        with open(virtualenv_path) as f:
            exec(f.read(), dict(__file__=virtualenv_path))

    for p in sys.path:
        if os.path.isdir(p):
            vim.command(r"set path+=%s" % (p.replace(" ", r"\ ")))

    for p in sys.path:
        print("Path: %s" % p)

import os
from cuda_fmt import get_config_filename
import cudatext as app

try:
    import pyastyle
except:
    pyastyle = None
    app.msg_box('For AStyle formatter, you need the "pyastyle" Python library. See instruction in the file [CudaText]/py/cuda_fmt_astyle/readme/readme.txt.',
        app.MB_OK+app.MB_ICONERROR)

def options():
    ini = get_config_filename('AStyle Format')
    if os.path.isfile(ini):
        s = open(ini).read()
    else:
        s = ''
    return s

def do_format(text):
    if pyastyle is None:
        return
    opt = options()
    #print('AStyle options:', opt)
    return pyastyle.format(text, opt)

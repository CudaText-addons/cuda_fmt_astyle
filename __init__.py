import os
from cuda_fmt import get_config_filename
import cudatext as app

if os.name=='nt':
    from . import pyastyle
else:
    try:
        import pyastyle
    except:
        pyastyle = None
        app.msg_box('For "AStyle Format", you need to install "pyastyle" Python module in OS. Run:\nsudo pip3 install pyastyle',
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

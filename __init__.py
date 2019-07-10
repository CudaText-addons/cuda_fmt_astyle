import os
from cuda_fmt import get_config_filename

if os.name=='nt':
    from . import pyastyle
else:
    try:
        import pyastyle
    except:
        pyastyle = None
        msg_box('For "AStyle Format", you need to install "pyastyle" Python module in OS. Run:\nsudo pip3 install pyastyle',
            MB_OK+MB_ICONERROR)

def options():
    ini = get_config_filename('AStyle Format')
    if os.path.isfile(ini):
        s = open(ini).read()
    else:
        s = ''
    return s

def do_format(text):
    opt = options()
    #print('AStyle options:', opt)
    return pyastyle.format(text, opt)

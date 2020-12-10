from os.path import expanduser, join
import yoro

exportStr = ('export yoro_api_DIR=\"%s\"' %
             join(yoro.__path__[0], 'lib/cmake/yoro_api'))

with open(expanduser('~/.bashrc'), 'r+') as f:
    content = f.readlines()
    if exportStr not in content:
        f.write('\n')
        f.write('# YORO API CMake module path\n')
        f.write(exportStr + '\n')

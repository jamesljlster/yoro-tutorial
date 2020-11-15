from os.path import join
import yoro

yoroDir = join(yoro.__path__[0], 'lib/cmake/yoro_api')
print('export yoro_api_DIR=%s' % yoroDir)

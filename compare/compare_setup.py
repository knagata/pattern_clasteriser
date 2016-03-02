from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [Extension('compare', ['compare.pyx'])]   #assign new.pyx module in setup.py.
setup(
      name        = 'compare app',
      cmdclass    = {'build_ext':build_ext},
      ext_modules = ext_modules
      )
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [Extension('Cluster', ['Cluster.pyx'])]   #assign new.pyx module in setup.py.
setup(
      name        = 'Cluster app',
      cmdclass    = {'build_ext':build_ext},
      ext_modules = ext_modules
      )
# encoding: utf-8
# module cytoolz.utils
# from C:\Users\Doly\Anaconda3\lib\site-packages\cytoolz\utils.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import os as os # C:\Users\Doly\Anaconda3\lib\os.py
import cytoolz as cytoolz # C:\Users\Doly\Anaconda3\lib\site-packages\cytoolz\__init__.py

# Variables with simple values

no_default = '__no__default__'

# functions

def consume(seq): # real signature unknown; restored from __doc__
    """
    consume(seq)
    
        Efficiently consume an iterable
    """
    pass

def include_dirs(): # real signature unknown; restored from __doc__
    """
    include_dirs()
     Return a list of directories containing the *.pxd files for ``cytoolz``
    
        Use this to include ``cytoolz`` in your own Cython project, which allows
        fast C bindinds to be imported such as ``from cytoolz cimport get``.
    
        Below is a minimal "setup.py" file using ``include_dirs``:
    
            from distutils.core import setup
            from distutils.extension import Extension
            from Cython.Distutils import build_ext
    
            import cytoolz.utils
    
            ext_modules=[
                Extension("mymodule",
                          ["mymodule.pyx"],
                          include_dirs=cytoolz.utils.include_dirs()
                         )
            ]
    
            setup(
              name = "mymodule",
              cmdclass = {"build_ext": build_ext},
              ext_modules = ext_modules
            )
    """
    pass

def raises(err, lamda): # real signature unknown; restored from __doc__
    """ raises(err, lamda) """
    pass

# no classes
# variables with complex values

__all__ = [
    'raises',
    'no_default',
    'include_dirs',
    'consume',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x00000231724C3EB8>'

__pyx_capi__ = {
    'consume': None, # (!) real value is '<capsule object "PyObject *(PyObject *, int __pyx_skip_dispatch)" at 0x0000023172389F60>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='cytoolz.utils', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x00000231724C3EB8>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\cytoolz\\\\utils.cp37-win_amd64.pyd')"

__test__ = {}


# encoding: utf-8
# module scipy.integrate.vode
# from C:\Users\Doly\Anaconda3\lib\site-packages\scipy\integrate\vode.cp37-win_amd64.pyd
# by generator 1.147
"""
This module 'vode' is auto-generated with f2py (version:2).
Functions:
  y,t,istate = dvode(f,jac,y,t,tout,rtol,atol,itask,istate,rwork,iwork,mf,f_extra_args=(),jac_extra_args=(),overwrite_y=0)
  y,t,istate = zvode(f,jac,y,t,tout,rtol,atol,itask,istate,zwork,rwork,iwork,mf,f_extra_args=(),jac_extra_args=(),overwrite_y=0)
.
"""
# no imports

# Variables with simple values

__version__ = b'$Revision: $'

# functions

def dvode(f, jac, y, t, tout, rtol, atol, itask, istate, rwork, iwork, mf, f_extra_args=None, jac_extra_args=None, overwrite_y=None): # real signature unknown; restored from __doc__
    """
    y,t,istate = dvode(f,jac,y,t,tout,rtol,atol,itask,istate,rwork,iwork,mf,[f_extra_args,jac_extra_args,overwrite_y])
    
    Wrapper for ``dvode``.
    
    Parameters
    ----------
    f : call-back function
    jac : call-back function
    y : input rank-1 array('d') with bounds (neq)
    t : input float
    tout : input float
    rtol : input rank-1 array('d') with bounds (*)
    atol : input rank-1 array('d') with bounds (*)
    itask : input int
    istate : input int
    rwork : input rank-1 array('d') with bounds (lrw)
    iwork : input rank-1 array('i') with bounds (liw)
    mf : input int
    
    Other Parameters
    ----------------
    f_extra_args : input tuple, optional
        Default: ()
    jac_extra_args : input tuple, optional
        Default: ()
    overwrite_y : input int, optional
        Default: 0
    
    Returns
    -------
    y : rank-1 array('d') with bounds (neq)
    t : float
    istate : int
    
    Notes
    -----
    Call-back functions::
    
      def f(t,y): return ydot
      Required arguments:
        t : input float
        y : input rank-1 array('d') with bounds (n)
      Return objects:
        ydot : rank-1 array('d') with bounds (n)
      def jac(t,y): return jac
      Required arguments:
        t : input float
        y : input rank-1 array('d') with bounds (n)
      Return objects:
        jac : rank-2 array('d') with bounds (nrowpd,n)
    """
    pass

def zvode(f, jac, y, t, tout, rtol, atol, itask, istate, zwork, rwork, iwork, mf, f_extra_args=None, jac_extra_args=None, overwrite_y=None): # real signature unknown; restored from __doc__
    """
    y,t,istate = zvode(f,jac,y,t,tout,rtol,atol,itask,istate,zwork,rwork,iwork,mf,[f_extra_args,jac_extra_args,overwrite_y])
    
    Wrapper for ``zvode``.
    
    Parameters
    ----------
    f : call-back function
    jac : call-back function
    y : input rank-1 array('D') with bounds (neq)
    t : input float
    tout : input float
    rtol : input rank-1 array('d') with bounds (*)
    atol : input rank-1 array('d') with bounds (*)
    itask : input int
    istate : input int
    zwork : input rank-1 array('D') with bounds (lzw)
    rwork : input rank-1 array('d') with bounds (lrw)
    iwork : input rank-1 array('i') with bounds (liw)
    mf : input int
    
    Other Parameters
    ----------------
    f_extra_args : input tuple, optional
        Default: ()
    jac_extra_args : input tuple, optional
        Default: ()
    overwrite_y : input int, optional
        Default: 0
    
    Returns
    -------
    y : rank-1 array('D') with bounds (neq)
    t : float
    istate : int
    
    Notes
    -----
    Call-back functions::
    
      def f(t,y): return ydot
      Required arguments:
        t : input float
        y : input rank-1 array('D') with bounds (n)
      Return objects:
        ydot : rank-1 array('D') with bounds (n)
      def jac(t,y): return jac
      Required arguments:
        t : input float
        y : input rank-1 array('D') with bounds (n)
      Return objects:
        jac : rank-2 array('D') with bounds (nrowpd,n)
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001EB6B594208>'

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.integrate.vode', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001EB6B594208>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\scipy\\\\integrate\\\\vode.cp37-win_amd64.pyd')"


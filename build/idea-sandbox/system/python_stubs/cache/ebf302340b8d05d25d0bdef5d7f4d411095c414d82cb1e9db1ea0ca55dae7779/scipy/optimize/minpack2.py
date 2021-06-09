# encoding: utf-8
# module scipy.optimize.minpack2
# from C:\Users\Doly\Anaconda3\lib\site-packages\scipy\optimize\minpack2.cp37-win_amd64.pyd
# by generator 1.147
"""
This module 'minpack2' is auto-generated with f2py (version:2).
Functions:
  stp,f,g,task = dcsrch(stp,f,g,ftol,gtol,xtol,task,stpmin,stpmax,isave,dsave)
  stx,fx,dx,sty,fy,dy,stp,brackt = dcstep(stx,fx,dx,sty,fy,dy,stp,fp,dp,brackt,stpmin,stpmax)
.
"""
# no imports

# Variables with simple values

__version__ = b'$Revision: $'

# functions

def dcsrch(stp, f, g, ftol, gtol, xtol, task, stpmin, stpmax, isave, dsave): # real signature unknown; restored from __doc__
    """
    stp,f,g,task = dcsrch(stp,f,g,ftol,gtol,xtol,task,stpmin,stpmax,isave,dsave)
    
    Wrapper for ``dcsrch``.
    
    Parameters
    ----------
    stp : input float
    f : input float
    g : input float
    ftol : input float
    gtol : input float
    xtol : input float
    task : input string(len=60)
    stpmin : input float
    stpmax : input float
    isave : in/output rank-1 array('i') with bounds (2)
    dsave : in/output rank-1 array('d') with bounds (13)
    
    Returns
    -------
    stp : float
    f : float
    g : float
    task : string(len=60)
    """
    pass

def dcstep(stx, fx, dx, sty, fy, dy, stp, fp, dp, brackt, stpmin, stpmax): # real signature unknown; restored from __doc__
    """
    stx,fx,dx,sty,fy,dy,stp,brackt = dcstep(stx,fx,dx,sty,fy,dy,stp,fp,dp,brackt,stpmin,stpmax)
    
    Wrapper for ``dcstep``.
    
    Parameters
    ----------
    stx : input float
    fx : input float
    dx : input float
    sty : input float
    fy : input float
    dy : input float
    stp : input float
    fp : input float
    dp : input float
    brackt : input int
    stpmin : input float
    stpmax : input float
    
    Returns
    -------
    stx : float
    fx : float
    dx : float
    sty : float
    fy : float
    dy : float
    stp : float
    brackt : int
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001F87ECEB518>'

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.optimize.minpack2', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001F87ECEB518>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\scipy\\\\optimize\\\\minpack2.cp37-win_amd64.pyd')"


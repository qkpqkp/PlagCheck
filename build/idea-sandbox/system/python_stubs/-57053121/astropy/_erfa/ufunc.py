# encoding: utf-8
# module astropy._erfa.ufunc
# from C:\Users\Doly\Anaconda3\lib\site-packages\astropy\_erfa\ufunc.cp37-win_amd64.pyd
# by generator 1.147
"""
Ufunc wrappers of the ERFA routines.

These ufuncs vectorize the ERFA functions assuming structured dtypes
for vector and matrix arguments. Status codes are vectors as well.
Python wrappers are also provided, which convert between
trailing dimensions and structured dtypes where necessary,
and combine status codes.
"""
# no imports

# functions

def a2af(x1, x2, out1=None, out2=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    a2af(x1, x2[, out1, out2], / [, out=(None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraA2af
    """
    pass

def a2tf(x1, x2, out1=None, out2=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    a2tf(x1, x2[, out1, out2], / [, out=(None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraA2tf
    """
    pass

def ab(x1, x2, x3, x4, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    ab(x1, x2, x3, x4, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraAb
    """
    pass

def af2a(x1, x2, x3, x4, out1=None, out2=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    af2a(x1, x2, x3, x4[, out1, out2], / [, out=(None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraAf2a
    """
    pass

def anp(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    anp(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraAnp
    """
    pass

def anpm(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    anpm(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraAnpm
    """
    pass

def apcg(x1, x2, x3, x4, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    apcg(x1, x2, x3, x4, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraApcg
    """
    pass

def apcg13(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    apcg13(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraApcg13
    """
    pass

def apci(x1, x2, x3, x4, x5, x6, x7, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    apci(x1, x2, x3, x4, x5, x6, x7, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraApci
    """
    pass

def apci13(x1, x2, out1=None, out2=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    apci13(x1, x2[, out1, out2], / [, out=(None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraApci13
    """
    pass

def apco(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    apco(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraApco
    """
    pass

def apco13(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, out1=None, out2=None, out3=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    apco13(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12[, out1, out2, out3], / [, out=(None, None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraApco13
    """
    pass

def apcs(x1, x2, x3, x4, x5, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    apcs(x1, x2, x3, x4, x5, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraApcs
    """
    pass

def apcs13(x1, x2, x3, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    apcs13(x1, x2, x3, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraApcs13
    """
    pass

def aper(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    aper(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraAper
    """
    pass

def aper13(x1, x2, x3, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    aper13(x1, x2, x3, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraAper13
    """
    pass

def apio(x1, x2, x3, x4, x5, x6, x7, x8, x9, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    apio(x1, x2, x3, x4, x5, x6, x7, x8, x9, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraApio
    """
    pass

def apio13(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, out1=None, out2=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    apio13(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12[, out1, out2], / [, out=(None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraApio13
    """
    pass

def atci13(x1, x2, x3, x4, x5, x6, x7, x8, out1=None, out2=None, out3=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    atci13(x1, x2, x3, x4, x5, x6, x7, x8[, out1, out2, out3], / [, out=(None, None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraAtci13
    """
    pass

def atciq(x1, x2, x3, x4, x5, x6, x7, out1=None, out2=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    atciq(x1, x2, x3, x4, x5, x6, x7[, out1, out2], / [, out=(None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraAtciq
    """
    pass

def atciqn(x1, x2, x3, x4, x5, x6, x7, x8, out1=None, out2=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    atciqn(x1, x2, x3, x4, x5, x6, x7, x8[, out1, out2], / [, out=(None, None)], *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraAtciqn
    """
    pass

def atciqz(x1, x2, x3, out1=None, out2=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    atciqz(x1, x2, x3[, out1, out2], / [, out=(None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraAtciqz
    """
    pass

def atco13(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, out1=None, out2=None, out3=None, out4=None, out5=None, out6=None, out7=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    atco13(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18[, out1, out2, out3, out4, out5, out6, out7], / [, out=(None, None, None, None, None, None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraAtco13
    """
    pass

def atic13(x1, x2, x3, x4, out1=None, out2=None, out3=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    atic13(x1, x2, x3, x4[, out1, out2, out3], / [, out=(None, None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraAtic13
    """
    pass

def aticq(x1, x2, x3, out1=None, out2=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    aticq(x1, x2, x3[, out1, out2], / [, out=(None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraAticq
    """
    pass

def aticqn(x1, x2, x3, x4, out1=None, out2=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    aticqn(x1, x2, x3, x4[, out1, out2], / [, out=(None, None)], *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraAticqn
    """
    pass

def atio13(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, out1=None, out2=None, out3=None, out4=None, out5=None, out6=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    atio13(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14[, out1, out2, out3, out4, out5, out6], / [, out=(None, None, None, None, None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraAtio13
    """
    pass

def atioq(x1, x2, x3, out1=None, out2=None, out3=None, out4=None, out5=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    atioq(x1, x2, x3[, out1, out2, out3, out4, out5], / [, out=(None, None, None, None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraAtioq
    """
    pass

def atoc13(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, out1=None, out2=None, out3=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    atoc13(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15[, out1, out2, out3], / [, out=(None, None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraAtoc13
    """
    pass

def atoi13(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, out1=None, out2=None, out3=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    atoi13(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15[, out1, out2, out3], / [, out=(None, None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraAtoi13
    """
    pass

def atoiq(x1, x2, x3, x4, out1=None, out2=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    atoiq(x1, x2, x3, x4[, out1, out2], / [, out=(None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraAtoiq
    """
    pass

def bi00(out1=None, out2=None, out3=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    bi00([, out1, out2, out3], / [, out=(None, None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraBi00
    """
    pass

def bp00(x1, x2, out1=None, out2=None, out3=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    bp00(x1, x2[, out1, out2, out3], / [, out=(None, None, None)], *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraBp00
    """
    pass

def bp06(x1, x2, out1=None, out2=None, out3=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    bp06(x1, x2[, out1, out2, out3], / [, out=(None, None, None)], *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraBp06
    """
    pass

def bpn2xy(x, out1=None, out2=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    bpn2xy(x[, out1, out2], / [, out=(None, None)], *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraBpn2xy
    """
    pass

def c2i00a(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    c2i00a(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraC2i00a
    """
    pass

def c2i00b(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    c2i00b(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraC2i00b
    """
    pass

def c2i06a(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    c2i06a(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraC2i06a
    """
    pass

def c2ibpn(x1, x2, x3, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    c2ibpn(x1, x2, x3, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraC2ibpn
    """
    pass

def c2ixy(x1, x2, x3, x4, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    c2ixy(x1, x2, x3, x4, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraC2ixy
    """
    pass

def c2ixys(x1, x2, x3, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    c2ixys(x1, x2, x3, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraC2ixys
    """
    pass

def c2s(x, out1=None, out2=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    c2s(x[, out1, out2], / [, out=(None, None)], *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraC2s
    """
    pass

def c2t00a(x1, x2, x3, x4, x5, x6, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    c2t00a(x1, x2, x3, x4, x5, x6, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraC2t00a
    """
    pass

def c2t00b(x1, x2, x3, x4, x5, x6, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    c2t00b(x1, x2, x3, x4, x5, x6, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraC2t00b
    """
    pass

def c2t06a(x1, x2, x3, x4, x5, x6, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    c2t06a(x1, x2, x3, x4, x5, x6, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraC2t06a
    """
    pass

def c2tcio(x1, x2, x3, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    c2tcio(x1, x2, x3, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraC2tcio
    """
    pass

def c2teqx(x1, x2, x3, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    c2teqx(x1, x2, x3, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraC2teqx
    """
    pass

def c2tpe(x1, x2, x3, x4, x5, x6, x7, x8, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    c2tpe(x1, x2, x3, x4, x5, x6, x7, x8, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraC2tpe
    """
    pass

def c2txy(x1, x2, x3, x4, x5, x6, x7, x8, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    c2txy(x1, x2, x3, x4, x5, x6, x7, x8, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraC2txy
    """
    pass

def cal2jd(x1, x2, x3, out1=None, out2=None, out3=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    cal2jd(x1, x2, x3[, out1, out2, out3], / [, out=(None, None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraCal2jd
    """
    pass

def cp(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    cp(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraCp
    """
    pass

def cpv(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    cpv(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraCpv
    """
    pass

def cr(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    cr(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraCr
    """
    pass

def d2dtf(x1, x2, x3, x4, out1=None, out2=None, out3=None, out4=None, out5=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    d2dtf(x1, x2, x3, x4[, out1, out2, out3, out4, out5], / [, out=(None, None, None, None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraD2dtf
    """
    pass

def d2tf(x1, x2, out1=None, out2=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    d2tf(x1, x2[, out1, out2], / [, out=(None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraD2tf
    """
    pass

def dat(x1, x2, x3, x4, out1=None, out2=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    dat(x1, x2, x3, x4[, out1, out2], / [, out=(None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraDat
    """
    pass

def dtdb(x1, x2, x3, x4, x5, x6, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    dtdb(x1, x2, x3, x4, x5, x6, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraDtdb
    """
    pass

def dtf2d(x1, x2, x3, x4, x5, x6, x7, out1=None, out2=None, out3=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    dtf2d(x1, x2, x3, x4, x5, x6, x7[, out1, out2, out3], / [, out=(None, None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraDtf2d
    """
    pass

def eceq06(x1, x2, x3, x4, out1=None, out2=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    eceq06(x1, x2, x3, x4[, out1, out2], / [, out=(None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraEceq06
    """
    pass

def ecm06(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    ecm06(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraEcm06
    """
    pass

def ee00(x1, x2, x3, x4, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    ee00(x1, x2, x3, x4, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraEe00
    """
    pass

def ee00a(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    ee00a(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraEe00a
    """
    pass

def ee00b(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    ee00b(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraEe00b
    """
    pass

def ee06a(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    ee06a(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraEe06a
    """
    pass

def eect00(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    eect00(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraEect00
    """
    pass

def eform(x, out1=None, out2=None, out3=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    eform(x[, out1, out2, out3], / [, out=(None, None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraEform
    """
    pass

def eo06a(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    eo06a(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraEo06a
    """
    pass

def eors(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    eors(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraEors
    """
    pass

def epb(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    epb(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraEpb
    """
    pass

def epb2jd(x, out1=None, out2=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    epb2jd(x[, out1, out2], / [, out=(None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraEpb2jd
    """
    pass

def epj(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    epj(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraEpj
    """
    pass

def epj2jd(x, out1=None, out2=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    epj2jd(x[, out1, out2], / [, out=(None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraEpj2jd
    """
    pass

def epv00(x1, x2, out1=None, out2=None, out3=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    epv00(x1, x2[, out1, out2, out3], / [, out=(None, None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraEpv00
    """
    pass

def eqec06(x1, x2, x3, x4, out1=None, out2=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    eqec06(x1, x2, x3, x4[, out1, out2], / [, out=(None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraEqec06
    """
    pass

def eqeq94(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    eqeq94(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraEqeq94
    """
    pass

def era00(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    era00(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraEra00
    """
    pass

def fad03(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    fad03(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraFad03
    """
    pass

def fae03(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    fae03(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraFae03
    """
    pass

def faf03(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    faf03(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraFaf03
    """
    pass

def faju03(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    faju03(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraFaju03
    """
    pass

def fal03(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    fal03(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraFal03
    """
    pass

def falp03(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    falp03(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraFalp03
    """
    pass

def fama03(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    fama03(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraFama03
    """
    pass

def fame03(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    fame03(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraFame03
    """
    pass

def fane03(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    fane03(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraFane03
    """
    pass

def faom03(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    faom03(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraFaom03
    """
    pass

def fapa03(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    fapa03(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraFapa03
    """
    pass

def fasa03(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    fasa03(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraFasa03
    """
    pass

def faur03(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    faur03(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraFaur03
    """
    pass

def fave03(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    fave03(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraFave03
    """
    pass

def fk52h(x1, x2, x3, x4, x5, x6, out1=None, out2=None, out3=None, out4=None, out5=None, out6=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    fk52h(x1, x2, x3, x4, x5, x6[, out1, out2, out3, out4, out5, out6], / [, out=(None, None, None, None, None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraFk52h
    """
    pass

def fk5hip(out1=None, out2=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    fk5hip([, out1, out2], / [, out=(None, None)], *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraFk5hip
    """
    pass

def fk5hz(x1, x2, x3, x4, out1=None, out2=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    fk5hz(x1, x2, x3, x4[, out1, out2], / [, out=(None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraFk5hz
    """
    pass

def fw2m(x1, x2, x3, x4, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    fw2m(x1, x2, x3, x4, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraFw2m
    """
    pass

def fw2xy(x1, x2, x3, x4, out1=None, out2=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    fw2xy(x1, x2, x3, x4[, out1, out2], / [, out=(None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraFw2xy
    """
    pass

def g2icrs(x1, x2, out1=None, out2=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    g2icrs(x1, x2[, out1, out2], / [, out=(None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraG2icrs
    """
    pass

def gc2gd(x1, x2, out1=None, out2=None, out3=None, out4=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    gc2gd(x1, x2[, out1, out2, out3, out4], / [, out=(None, None, None, None)], *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraGc2gd
    """
    pass

def gc2gde(x1, x2, x3, out1=None, out2=None, out3=None, out4=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    gc2gde(x1, x2, x3[, out1, out2, out3, out4], / [, out=(None, None, None, None)], *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraGc2gde
    """
    pass

def gd2gc(x1, x2, x3, x4, out1=None, out2=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    gd2gc(x1, x2, x3, x4[, out1, out2], / [, out=(None, None)], *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraGd2gc
    """
    pass

def gd2gce(x1, x2, x3, x4, x5, out1=None, out2=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    gd2gce(x1, x2, x3, x4, x5[, out1, out2], / [, out=(None, None)], *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraGd2gce
    """
    pass

def gmst00(x1, x2, x3, x4, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    gmst00(x1, x2, x3, x4, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraGmst00
    """
    pass

def gmst06(x1, x2, x3, x4, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    gmst06(x1, x2, x3, x4, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraGmst06
    """
    pass

def gmst82(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    gmst82(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraGmst82
    """
    pass

def gst00a(x1, x2, x3, x4, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    gst00a(x1, x2, x3, x4, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraGst00a
    """
    pass

def gst00b(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    gst00b(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraGst00b
    """
    pass

def gst06(x1, x2, x3, x4, x5, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    gst06(x1, x2, x3, x4, x5, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraGst06
    """
    pass

def gst06a(x1, x2, x3, x4, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    gst06a(x1, x2, x3, x4, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraGst06a
    """
    pass

def gst94(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    gst94(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraGst94
    """
    pass

def h2fk5(x1, x2, x3, x4, x5, x6, out1=None, out2=None, out3=None, out4=None, out5=None, out6=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    h2fk5(x1, x2, x3, x4, x5, x6[, out1, out2, out3, out4, out5, out6], / [, out=(None, None, None, None, None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraH2fk5
    """
    pass

def hfk5z(x1, x2, x3, x4, out1=None, out2=None, out3=None, out4=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    hfk5z(x1, x2, x3, x4[, out1, out2, out3, out4], / [, out=(None, None, None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraHfk5z
    """
    pass

def icrs2g(x1, x2, out1=None, out2=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    icrs2g(x1, x2[, out1, out2], / [, out=(None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraIcrs2g
    """
    pass

def ir(*args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    ir(, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraIr
    """
    pass

def jd2cal(x1, x2, out1=None, out2=None, out3=None, out4=None, out5=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    jd2cal(x1, x2[, out1, out2, out3, out4, out5], / [, out=(None, None, None, None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraJd2cal
    """
    pass

def jdcalf(x1, x2, x3, out1=None, out2=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    jdcalf(x1, x2, x3[, out1, out2], / [, out=(None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraJdcalf
    """
    pass

def ld(x1, x2, x3, x4, x5, x6, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    ld(x1, x2, x3, x4, x5, x6, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraLd
    """
    pass

def ldn(x1, x2, x3, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    ldn(x1, x2, x3, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraLdn
    """
    pass

def ldsun(x1, x2, x3, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    ldsun(x1, x2, x3, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraLdsun
    """
    pass

def lteceq(x1, x2, x3, out1=None, out2=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    lteceq(x1, x2, x3[, out1, out2], / [, out=(None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraLteceq
    """
    pass

def ltecm(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    ltecm(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraLtecm
    """
    pass

def lteqec(x1, x2, x3, out1=None, out2=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    lteqec(x1, x2, x3[, out1, out2], / [, out=(None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraLteqec
    """
    pass

def ltp(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    ltp(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraLtp
    """
    pass

def ltpb(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    ltpb(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraLtpb
    """
    pass

def ltpecl(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    ltpecl(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraLtpecl
    """
    pass

def ltpequ(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    ltpequ(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraLtpequ
    """
    pass

def num00a(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    num00a(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraNum00a
    """
    pass

def num00b(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    num00b(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraNum00b
    """
    pass

def num06a(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    num06a(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraNum06a
    """
    pass

def numat(x1, x2, x3, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    numat(x1, x2, x3, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraNumat
    """
    pass

def nut00a(x1, x2, out1=None, out2=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    nut00a(x1, x2[, out1, out2], / [, out=(None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraNut00a
    """
    pass

def nut00b(x1, x2, out1=None, out2=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    nut00b(x1, x2[, out1, out2], / [, out=(None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraNut00b
    """
    pass

def nut06a(x1, x2, out1=None, out2=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    nut06a(x1, x2[, out1, out2], / [, out=(None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraNut06a
    """
    pass

def nut80(x1, x2, out1=None, out2=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    nut80(x1, x2[, out1, out2], / [, out=(None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraNut80
    """
    pass

def nutm80(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    nutm80(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraNutm80
    """
    pass

def obl06(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    obl06(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraObl06
    """
    pass

def obl80(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    obl80(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraObl80
    """
    pass

def p06e(x1, x2, out1=None, out2=None, out3=None, out4=None, out5=None, out6=None, out7=None, out8=None, out9=None, out10=None, out11=None, out12=None, out13=None, out14=None, out15=None, out16=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    p06e(x1, x2[, out1, out2, out3, out4, out5, out6, out7, out8, out9, out10, out11, out12, out13, out14, out15, out16], / [, out=(None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraP06e
    """
    pass

def p2pv(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    p2pv(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraP2pv
    """
    pass

def p2s(x, out1=None, out2=None, out3=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    p2s(x[, out1, out2, out3], / [, out=(None, None, None)], *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraP2s
    """
    pass

def pap(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    pap(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraPap
    """
    pass

def pas(x1, x2, x3, x4, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    pas(x1, x2, x3, x4, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraPas
    """
    pass

def pav2pv(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    pav2pv(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraPav2pv
    """
    pass

def pb06(x1, x2, out1=None, out2=None, out3=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    pb06(x1, x2[, out1, out2, out3], / [, out=(None, None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraPb06
    """
    pass

def pdp(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    pdp(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraPdp
    """
    pass

def pfw06(x1, x2, out1=None, out2=None, out3=None, out4=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    pfw06(x1, x2[, out1, out2, out3, out4], / [, out=(None, None, None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraPfw06
    """
    pass

def plan94(x1, x2, x3, out1=None, out2=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    plan94(x1, x2, x3[, out1, out2], / [, out=(None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraPlan94
    """
    pass

def pm(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    pm(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraPm
    """
    pass

def pmat00(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    pmat00(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraPmat00
    """
    pass

def pmat06(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    pmat06(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraPmat06
    """
    pass

def pmat76(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    pmat76(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraPmat76
    """
    pass

def pmp(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    pmp(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraPmp
    """
    pass

def pmpx(x1, x2, x3, x4, x5, x6, x7, x8, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    pmpx(x1, x2, x3, x4, x5, x6, x7, x8, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraPmpx
    """
    pass

def pmsafe(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, out1=None, out2=None, out3=None, out4=None, out5=None, out6=None, out7=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    pmsafe(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10[, out1, out2, out3, out4, out5, out6, out7], / [, out=(None, None, None, None, None, None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraPmsafe
    """
    pass

def pn(x, out1=None, out2=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    pn(x[, out1, out2], / [, out=(None, None)], *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraPn
    """
    pass

def pn00(x1, x2, x3, x4, out1=None, out2=None, out3=None, out4=None, out5=None, out6=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    pn00(x1, x2, x3, x4[, out1, out2, out3, out4, out5, out6], / [, out=(None, None, None, None, None, None)], *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraPn00
    """
    pass

def pn00a(x1, x2, out1=None, out2=None, out3=None, out4=None, out5=None, out6=None, out7=None, out8=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    pn00a(x1, x2[, out1, out2, out3, out4, out5, out6, out7, out8], / [, out=(None, None, None, None, None, None, None, None)], *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraPn00a
    """
    pass

def pn00b(x1, x2, out1=None, out2=None, out3=None, out4=None, out5=None, out6=None, out7=None, out8=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    pn00b(x1, x2[, out1, out2, out3, out4, out5, out6, out7, out8], / [, out=(None, None, None, None, None, None, None, None)], *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraPn00b
    """
    pass

def pn06(x1, x2, x3, x4, out1=None, out2=None, out3=None, out4=None, out5=None, out6=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    pn06(x1, x2, x3, x4[, out1, out2, out3, out4, out5, out6], / [, out=(None, None, None, None, None, None)], *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraPn06
    """
    pass

def pn06a(x1, x2, out1=None, out2=None, out3=None, out4=None, out5=None, out6=None, out7=None, out8=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    pn06a(x1, x2[, out1, out2, out3, out4, out5, out6, out7, out8], / [, out=(None, None, None, None, None, None, None, None)], *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraPn06a
    """
    pass

def pnm00a(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    pnm00a(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraPnm00a
    """
    pass

def pnm00b(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    pnm00b(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraPnm00b
    """
    pass

def pnm06a(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    pnm06a(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraPnm06a
    """
    pass

def pnm80(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    pnm80(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraPnm80
    """
    pass

def pom00(x1, x2, x3, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    pom00(x1, x2, x3, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraPom00
    """
    pass

def ppp(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    ppp(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraPpp
    """
    pass

def ppsp(x1, x2, x3, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    ppsp(x1, x2, x3, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraPpsp
    """
    pass

def pr00(x1, x2, out1=None, out2=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    pr00(x1, x2[, out1, out2], / [, out=(None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraPr00
    """
    pass

def prec76(x1, x2, x3, x4, out1=None, out2=None, out3=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    prec76(x1, x2, x3, x4[, out1, out2, out3], / [, out=(None, None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraPrec76
    """
    pass

def pv2p(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    pv2p(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraPv2p
    """
    pass

def pv2pav(x, out1=None, out2=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    pv2pav(x[, out1, out2], / [, out=(None, None)], *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraPv2pav
    """
    pass

def pv2s(x, out1=None, out2=None, out3=None, out4=None, out5=None, out6=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    pv2s(x[, out1, out2, out3, out4, out5, out6], / [, out=(None, None, None, None, None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraPv2s
    """
    pass

def pvdpv(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    pvdpv(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraPvdpv
    """
    pass

def pvm(x, out1=None, out2=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    pvm(x[, out1, out2], / [, out=(None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraPvm
    """
    pass

def pvmpv(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    pvmpv(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraPvmpv
    """
    pass

def pvppv(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    pvppv(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraPvppv
    """
    pass

def pvstar(x, out1=None, out2=None, out3=None, out4=None, out5=None, out6=None, out7=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    pvstar(x[, out1, out2, out3, out4, out5, out6, out7], / [, out=(None, None, None, None, None, None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraPvstar
    """
    pass

def pvtob(x1, x2, x3, x4, x5, x6, x7, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    pvtob(x1, x2, x3, x4, x5, x6, x7, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraPvtob
    """
    pass

def pvu(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    pvu(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraPvu
    """
    pass

def pvup(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    pvup(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraPvup
    """
    pass

def pvxpv(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    pvxpv(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraPvxpv
    """
    pass

def pxp(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    pxp(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraPxp
    """
    pass

def refco(x1, x2, x3, x4, out1=None, out2=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    refco(x1, x2, x3, x4[, out1, out2], / [, out=(None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraRefco
    """
    pass

def rm2v(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    rm2v(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraRm2v
    """
    pass

def rv2m(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    rv2m(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraRv2m
    """
    pass

def rx(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    rx(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraRx
    """
    pass

def rxp(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    rxp(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraRxp
    """
    pass

def rxpv(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    rxpv(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraRxpv
    """
    pass

def rxr(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    rxr(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraRxr
    """
    pass

def ry(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    ry(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraRy
    """
    pass

def rz(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    rz(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraRz
    """
    pass

def s00(x1, x2, x3, x4, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    s00(x1, x2, x3, x4, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraS00
    """
    pass

def s00a(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    s00a(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraS00a
    """
    pass

def s00b(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    s00b(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraS00b
    """
    pass

def s06(x1, x2, x3, x4, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    s06(x1, x2, x3, x4, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraS06
    """
    pass

def s06a(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    s06a(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraS06a
    """
    pass

def s2c(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    s2c(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraS2c
    """
    pass

def s2p(x1, x2, x3, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    s2p(x1, x2, x3, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraS2p
    """
    pass

def s2pv(x1, x2, x3, x4, x5, x6, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    s2pv(x1, x2, x3, x4, x5, x6, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraS2pv
    """
    pass

def s2xpv(x1, x2, x3, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    s2xpv(x1, x2, x3, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraS2xpv
    """
    pass

def sepp(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    sepp(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraSepp
    """
    pass

def seps(x1, x2, x3, x4, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    seps(x1, x2, x3, x4, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraSeps
    """
    pass

def sp00(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    sp00(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraSp00
    """
    pass

def starpm(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, out1=None, out2=None, out3=None, out4=None, out5=None, out6=None, out7=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    starpm(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10[, out1, out2, out3, out4, out5, out6, out7], / [, out=(None, None, None, None, None, None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraStarpm
    """
    pass

def starpv(x1, x2, x3, x4, x5, x6, out1=None, out2=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    starpv(x1, x2, x3, x4, x5, x6[, out1, out2], / [, out=(None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraStarpv
    """
    pass

def sxp(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    sxp(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraSxp
    """
    pass

def sxpv(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    sxpv(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraSxpv
    """
    pass

def taitt(x1, x2, out1=None, out2=None, out3=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    taitt(x1, x2[, out1, out2, out3], / [, out=(None, None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraTaitt
    """
    pass

def taiut1(x1, x2, x3, out1=None, out2=None, out3=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    taiut1(x1, x2, x3[, out1, out2, out3], / [, out=(None, None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraTaiut1
    """
    pass

def taiutc(x1, x2, out1=None, out2=None, out3=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    taiutc(x1, x2[, out1, out2, out3], / [, out=(None, None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraTaiutc
    """
    pass

def tcbtdb(x1, x2, out1=None, out2=None, out3=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    tcbtdb(x1, x2[, out1, out2, out3], / [, out=(None, None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraTcbtdb
    """
    pass

def tcgtt(x1, x2, out1=None, out2=None, out3=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    tcgtt(x1, x2[, out1, out2, out3], / [, out=(None, None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraTcgtt
    """
    pass

def tdbtcb(x1, x2, out1=None, out2=None, out3=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    tdbtcb(x1, x2[, out1, out2, out3], / [, out=(None, None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraTdbtcb
    """
    pass

def tdbtt(x1, x2, x3, out1=None, out2=None, out3=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    tdbtt(x1, x2, x3[, out1, out2, out3], / [, out=(None, None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraTdbtt
    """
    pass

def tf2a(x1, x2, x3, x4, out1=None, out2=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    tf2a(x1, x2, x3, x4[, out1, out2], / [, out=(None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraTf2a
    """
    pass

def tf2d(x1, x2, x3, x4, out1=None, out2=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    tf2d(x1, x2, x3, x4[, out1, out2], / [, out=(None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraTf2d
    """
    pass

def tr(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    tr(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraTr
    """
    pass

def trxp(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    trxp(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraTrxp
    """
    pass

def trxpv(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    trxpv(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraTrxpv
    """
    pass

def tttai(x1, x2, out1=None, out2=None, out3=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    tttai(x1, x2[, out1, out2, out3], / [, out=(None, None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraTttai
    """
    pass

def tttcg(x1, x2, out1=None, out2=None, out3=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    tttcg(x1, x2[, out1, out2, out3], / [, out=(None, None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraTttcg
    """
    pass

def tttdb(x1, x2, x3, out1=None, out2=None, out3=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    tttdb(x1, x2, x3[, out1, out2, out3], / [, out=(None, None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraTttdb
    """
    pass

def ttut1(x1, x2, x3, out1=None, out2=None, out3=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    ttut1(x1, x2, x3[, out1, out2, out3], / [, out=(None, None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraTtut1
    """
    pass

def ut1tai(x1, x2, x3, out1=None, out2=None, out3=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    ut1tai(x1, x2, x3[, out1, out2, out3], / [, out=(None, None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraUt1tai
    """
    pass

def ut1tt(x1, x2, x3, out1=None, out2=None, out3=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    ut1tt(x1, x2, x3[, out1, out2, out3], / [, out=(None, None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraUt1tt
    """
    pass

def ut1utc(x1, x2, x3, out1=None, out2=None, out3=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    ut1utc(x1, x2, x3[, out1, out2, out3], / [, out=(None, None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraUt1utc
    """
    pass

def utctai(x1, x2, out1=None, out2=None, out3=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    utctai(x1, x2[, out1, out2, out3], / [, out=(None, None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraUtctai
    """
    pass

def utcut1(x1, x2, x3, out1=None, out2=None, out3=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    utcut1(x1, x2, x3[, out1, out2, out3], / [, out=(None, None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraUtcut1
    """
    pass

def xy06(x1, x2, out1=None, out2=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    xy06(x1, x2[, out1, out2], / [, out=(None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraXy06
    """
    pass

def xys00a(x1, x2, out1=None, out2=None, out3=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    xys00a(x1, x2[, out1, out2, out3], / [, out=(None, None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraXys00a
    """
    pass

def xys00b(x1, x2, out1=None, out2=None, out3=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    xys00b(x1, x2[, out1, out2, out3], / [, out=(None, None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraXys00b
    """
    pass

def xys06a(x1, x2, out1=None, out2=None, out3=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    xys06a(x1, x2[, out1, out2, out3], / [, out=(None, None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraXys06a
    """
    pass

def zp(*args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    zp(, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraZp
    """
    pass

def zpv(*args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    zpv(, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraZpv
    """
    pass

def zr(*args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    zr(, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    UFunc wrapper for eraZr
    """
    pass

# no classes
# variables with complex values

dt_dmsf = None # (!) real value is "dtype([('h', '<i4'), ('m', '<i4'), ('s', '<i4'), ('f', '<i4')], align=True)"

dt_eraASTROM = None # (!) real value is "dtype([('pmt', '<f8'), ('eb', '<f8', (3,)), ('eh', '<f8', (3,)), ('em', '<f8'), ('v', '<f8', (3,)), ('bm1', '<f8'), ('bpn', '<f8', (3, 3)), ('along', '<f8'), ('phi', '<f8'), ('xpl', '<f8'), ('ypl', '<f8'), ('sphi', '<f8'), ('cphi', '<f8'), ('diurab', '<f8'), ('eral', '<f8'), ('refa', '<f8'), ('refb', '<f8')], align=True)"

dt_eraLDBODY = None # (!) real value is "dtype([('bm', '<f8'), ('dl', '<f8'), ('pv', '<f8', (2, 3))], align=True)"

dt_hmsf = None # (!) real value is "dtype([('h', '<i4'), ('m', '<i4'), ('s', '<i4'), ('f', '<i4')], align=True)"

dt_pv = None # (!) real value is "dtype([('p', '<f8', (3,)), ('v', '<f8', (3,))], align=True)"

dt_pvdpv = None # (!) real value is "dtype([('pdp', '<f8'), ('pdv', '<f8')], align=True)"

dt_sign = None # (!) real value is "dtype([('sign', 'S1')], align=True)"

dt_type = None # (!) real value is "dtype([('type', 'S12')], align=True)"

dt_ymdf = None # (!) real value is "dtype([('y', '<i4'), ('m', '<i4'), ('d', '<i4'), ('f', '<i4')], align=True)"

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000002AA2BDF2BE0>'

__spec__ = None # (!) real value is "ModuleSpec(name='astropy._erfa.ufunc', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000002AA2BDF2BE0>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\astropy\\\\_erfa\\\\ufunc.cp37-win_amd64.pyd')"


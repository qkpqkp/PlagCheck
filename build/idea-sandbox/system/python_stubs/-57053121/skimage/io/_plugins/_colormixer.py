# encoding: utf-8
# module skimage.io._plugins._colormixer
# from C:\Users\Doly\Anaconda3\lib\site-packages\skimage\io\_plugins\_colormixer.cp37-win_amd64.pyd
# by generator 1.147
"""
Color Mixer

NumPy does not do overflow checking when adding or multiplying
integers, so currently the only way to clip results efficiently
(without making copies of the data) is with an extension such as this
one.
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

# functions

def add(*args, **kwargs): # real signature unknown
    """
    Add a given amount to a color channel of `stateimg`, and
        store the result in `img`.  Overflow is clipped.
    
        Parameters
        ----------
        img : (M, N, 3) ndarray of uint8
            Output image.
        stateimg : (M, N, 3) ndarray of uint8
            Input image.
        channel : int
            Channel (0 for "red", 1 for "green", 2 for "blue").
        amount : int
            Value to add.
    """
    pass

def brightness(*args, **kwargs): # real signature unknown
    """
    Modify the brightness of an image.
        'factor' is multiplied to all channels, which are
        then added by 'amount'. Overflow is clipped.
    
        Parameters
        ----------
        img : (M, N, 3) ndarray of uint8
            Output image.
        stateimg : (M, N, 3) ndarray of uint8
            Input image.
        factor : float
            Multiplication factor.
        offset : int
            Ammount to add to each channel.
    """
    pass

def gamma(*args, **kwargs): # real signature unknown
    pass

def hsv_add(*args, **kwargs): # real signature unknown
    """
    Modify the image color by specifying additive HSV Values.
    
        Since the underlying images are RGB, all three values HSV
        must be specified at the same time.
    
        The RGB triplet in the image is converted to HSV, the operation
        is applied, and then the HSV triplet is converted back to RGB
    
        HSV values are scaled to H(0. - 360.), S(0. - 1.), V(0. - 1.)
        then the operation is performed and any overflow is clipped, then the
        reverse transform is performed. Those are the ranges to keep in mind,
        when passing in values.
    
        Parameters
        ----------
        img : (M, N, 3) ndarray of uint8
            Output image.
        stateimg : (M, N, 3) ndarray of uint8
            Input image.
        h_amt : float
            Ammount to add to H channel.
        s_amt : float
            Ammount to add to S channel.
        v_amt : float
            Ammount to add to V channel.
    """
    pass

def hsv_multiply(*args, **kwargs): # real signature unknown
    """
    Modify the image color by specifying multiplicative HSV Values.
    
        Since the underlying images are RGB, all three values HSV
        must be specified at the same time.
    
        The RGB triplet in the image is converted to HSV, the operation
        is applied, and then the HSV triplet is converted back to RGB
    
        HSV values are scaled to H(0. - 360.), S(0. - 1.), V(0. - 1.)
        then the operation is performed and any overflow is clipped, then the
        reverse transform is performed. Those are the ranges to keep in mind,
        when passing in values.
    
        Note that since hue is in degrees, it makes no sense to multiply
        that channel, thus an add operation is performed on the hue. And the
        values given for h_amt, should be the same as for hsv_add
    
        Parameters
        ----------
        img : (M, N, 3) ndarray of uint8
            Output image.
        stateimg : (M, N, 3) ndarray of uint8
            Input image.
        h_amt : float
            Ammount to add to H channel.
        s_amt : float
            Ammount by which to multiply S channel.
        v_amt : float
            Ammount by which to multiply V channel.
    """
    pass

def multiply(*args, **kwargs): # real signature unknown
    """
    Multiply a color channel of `stateimg` by a certain amount, and
        store the result in `img`.  Overflow is clipped.
    
        Parameters
        ----------
        img : (M, N, 3) ndarray of uint8
            Output image.
        stateimg : (M, N, 3) ndarray of uint8
            Input image.
        channel : int
            Channel (0 for "red", 1 for "green", 2 for "blue").
        amount : float
            Multiplication factor.
    """
    pass

def py_hsv_2_rgb(*args, **kwargs): # real signature unknown
    """
    Convert an HSV value to RGB.
    
        Automatic clipping.
    
        Parameters
        ----------
        H : float
            From 0. - 360.
        S : float
            From 0. - 1.
        V : float
            From 0. - 1.
    
        Returns
        -------
        out : (R, G, B) ints
            Each from 0 - 255
    
        conversion convention from here:
        https://en.wikipedia.org/wiki/HSL_and_HSV
    """
    pass

def py_rgb_2_hsv(*args, **kwargs): # real signature unknown
    """
    Convert an HSV value to RGB.
    
        Automatic clipping.
    
        Parameters
        ----------
        R : int
            From 0. - 255.
        G : int
            From 0. - 255.
        B : int
            From 0. - 255.
    
        Returns
        -------
        out : (H, S, V) floats
            Ranges (0...360), (0...1), (0...1)
    
        conversion convention from here:
        https://en.wikipedia.org/wiki/HSL_and_HSV
    """
    pass

def sigmoid_gamma(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x00000209C72BBB38>'

__spec__ = None # (!) real value is "ModuleSpec(name='skimage.io._plugins._colormixer', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x00000209C72BBB38>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\skimage\\\\io\\\\_plugins\\\\_colormixer.cp37-win_amd64.pyd')"

__test__ = {}


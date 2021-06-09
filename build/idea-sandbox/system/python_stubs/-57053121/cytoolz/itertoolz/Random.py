# encoding: utf-8
# module cytoolz.itertoolz
# from C:\Users\Doly\Anaconda3\lib\site-packages\cytoolz\itertoolz.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
from itertools import chain, islice, zip_longest

from _heapq import heapify, heappop, heapreplace

import _random as ___random


class Random(___random.Random):
    """
    Random number generator base class used by bound module functions.
    
        Used to instantiate instances of Random to get generators that don't
        share state.
    
        Class Random can also be subclassed if you want to use a different basic
        generator of your own devising: in that case, override the following
        methods:  random(), seed(), getstate(), and setstate().
        Optionally, implement a getrandbits() method so that randrange()
        can cover arbitrarily large ranges.
    """
    def betavariate(self, alpha, beta): # reliably restored by inspect
        """
        Beta distribution.
        
                Conditions on the parameters are alpha > 0 and beta > 0.
                Returned values range between 0 and 1.
        """
        pass

    def choice(self, seq): # reliably restored by inspect
        """ Choose a random element from a non-empty sequence. """
        pass

    def choices(self, population, weights=None, *, cum_weights=None, k=1): # reliably restored by inspect
        """
        Return a k sized list of population elements chosen with replacement.
        
                If the relative weights or cumulative weights are not specified,
                the selections are made with equal probability.
        """
        pass

    def expovariate(self, lambd): # reliably restored by inspect
        """
        Exponential distribution.
        
                lambd is 1.0 divided by the desired mean.  It should be
                nonzero.  (The parameter would be called "lambda", but that is
                a reserved word in Python.)  Returned values range from 0 to
                positive infinity if lambd is positive, and from negative
                infinity to 0 if lambd is negative.
        """
        pass

    def gammavariate(self, alpha, beta): # reliably restored by inspect
        """
        Gamma distribution.  Not the gamma function!
        
                Conditions on the parameters are alpha > 0 and beta > 0.
        
                The probability distribution function is:
        
                            x ** (alpha - 1) * math.exp(-x / beta)
                  pdf(x) =  --------------------------------------
                              math.gamma(alpha) * beta ** alpha
        """
        pass

    def gauss(self, mu, sigma): # reliably restored by inspect
        """
        Gaussian distribution.
        
                mu is the mean, and sigma is the standard deviation.  This is
                slightly faster than the normalvariate() function.
        
                Not thread-safe without a lock around calls.
        """
        pass

    def getstate(self): # reliably restored by inspect
        """ Return internal state; can be passed to setstate() later. """
        pass

    def lognormvariate(self, mu, sigma): # reliably restored by inspect
        """
        Log normal distribution.
        
                If you take the natural logarithm of this distribution, you'll get a
                normal distribution with mean mu and standard deviation sigma.
                mu can have any value, and sigma must be greater than zero.
        """
        pass

    def normalvariate(self, mu, sigma): # reliably restored by inspect
        """
        Normal distribution.
        
                mu is the mean, and sigma is the standard deviation.
        """
        pass

    def paretovariate(self, alpha): # reliably restored by inspect
        """ Pareto distribution.  alpha is the shape parameter. """
        pass

    def randint(self, a, b): # reliably restored by inspect
        """ Return random integer in range [a, b], including both end points. """
        pass

    def randrange(self, start, stop=None, step=1, _int=int): # reliably restored by inspect
        """
        Choose a random item from range(start, stop[, step]).
        
                This fixes the problem with randint() which includes the
                endpoint; in Python this is usually not what you want.
        """
        pass

    def sample(self, population, k): # reliably restored by inspect
        """
        Chooses k unique random elements from a population sequence or set.
        
                Returns a new list containing elements from the population while
                leaving the original population unchanged.  The resulting list is
                in selection order so that all sub-slices will also be valid random
                samples.  This allows raffle winners (the sample) to be partitioned
                into grand prize and second place winners (the subslices).
        
                Members of the population need not be hashable or unique.  If the
                population contains repeats, then each occurrence is a possible
                selection in the sample.
        
                To choose a sample in a range of integers, use range as an argument.
                This is especially fast and space efficient for sampling from a
                large population:   sample(range(10000000), 60)
        """
        pass

    def seed(self, a=None, version=2): # reliably restored by inspect
        """
        Initialize internal state from hashable object.
        
                None or no argument seeds from current time or from an operating
                system specific randomness source if available.
        
                If *a* is an int, all bits are used.
        
                For version 2 (the default), all of the bits are used if *a* is a str,
                bytes, or bytearray.  For version 1 (provided for reproducing random
                sequences from older versions of Python), the algorithm for str and
                bytes generates a narrower range of seeds.
        """
        pass

    def setstate(self, state): # reliably restored by inspect
        """ Restore internal state from object returned by getstate(). """
        pass

    def shuffle(self, x, random=None): # reliably restored by inspect
        """
        Shuffle list x in place, and return None.
        
                Optional argument random is a 0-argument function returning a
                random float in [0.0, 1.0); if it is the default None, the
                standard random.random will be used.
        """
        pass

    def triangular(self, low=0.0, high=1.0, mode=None): # reliably restored by inspect
        """
        Triangular distribution.
        
                Continuous distribution bounded by given lower and upper limits,
                and having a given mode value in-between.
        
                http://en.wikipedia.org/wiki/Triangular_distribution
        """
        pass

    def uniform(self, a, b): # reliably restored by inspect
        """ Get a random number in the range [a, b) or [a, b] depending on rounding. """
        pass

    def vonmisesvariate(self, mu, kappa): # reliably restored by inspect
        """
        Circular data distribution.
        
                mu is the mean angle, expressed in radians between 0 and 2*pi, and
                kappa is the concentration parameter, which must be greater than or
                equal to zero.  If kappa is equal to zero, this distribution reduces
                to a uniform random angle over the range 0 to 2*pi.
        """
        pass

    def weibullvariate(self, alpha, beta): # reliably restored by inspect
        """
        Weibull distribution.
        
                alpha is the scale parameter and beta is the shape parameter.
        """
        pass

    def _randbelow(self, n, int=int, maxsize=9007199254740992, type=type, Method=method, BuiltinMethod=builtin_function_or_method): # reliably restored by inspect
        """ Return a random int in the range [0,n).  Raises ValueError if n==0. """
        pass

    def __getstate__(self): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, x=None): # reliably restored by inspect
        """
        Initialize an instance.
        
                Optional argument x controls seeding, as for Random.seed().
        """
        pass

    def __reduce__(self): # reliably restored by inspect
        # no doc
        pass

    def __setstate__(self, state): # reliably restored by inspect
        # no doc
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    VERSION = 3
    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'random\', \'__doc__\': "Random number generator base class used by bound module functions.\\n\\n    Used to instantiate instances of Random to get generators that don\'t\\n    share state.\\n\\n    Class Random can also be subclassed if you want to use a different basic\\n    generator of your own devising: in that case, override the following\\n    methods:  random(), seed(), getstate(), and setstate().\\n    Optionally, implement a getrandbits() method so that randrange()\\n    can cover arbitrarily large ranges.\\n\\n    ", \'VERSION\': 3, \'__init__\': <function Random.__init__ at 0x0000021277857730>, \'seed\': <function Random.seed at 0x00000212778577B8>, \'getstate\': <function Random.getstate at 0x00000212778578C8>, \'setstate\': <function Random.setstate at 0x0000021277857950>, \'__getstate__\': <function Random.__getstate__ at 0x00000212778576A8>, \'__setstate__\': <function Random.__setstate__ at 0x0000021277857840>, \'__reduce__\': <function Random.__reduce__ at 0x00000212778579D8>, \'randrange\': <function Random.randrange at 0x0000021277857A60>, \'randint\': <function Random.randint at 0x0000021277857AE8>, \'_randbelow\': <function Random._randbelow at 0x0000021277857B70>, \'choice\': <function Random.choice at 0x0000021277857BF8>, \'shuffle\': <function Random.shuffle at 0x0000021277857C80>, \'sample\': <function Random.sample at 0x0000021277857D08>, \'choices\': <function Random.choices at 0x0000021277857D90>, \'uniform\': <function Random.uniform at 0x0000021277857E18>, \'triangular\': <function Random.triangular at 0x0000021277857EA0>, \'normalvariate\': <function Random.normalvariate at 0x0000021277857F28>, \'lognormvariate\': <function Random.lognormvariate at 0x0000021279097048>, \'expovariate\': <function Random.expovariate at 0x00000212790970D0>, \'vonmisesvariate\': <function Random.vonmisesvariate at 0x0000021279097158>, \'gammavariate\': <function Random.gammavariate at 0x00000212790971E0>, \'gauss\': <function Random.gauss at 0x0000021279097268>, \'betavariate\': <function Random.betavariate at 0x00000212790972F0>, \'paretovariate\': <function Random.paretovariate at 0x0000021279097378>, \'weibullvariate\': <function Random.weibullvariate at 0x0000021279097400>, \'__dict__\': <attribute \'__dict__\' of \'Random\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'Random\' objects>})'



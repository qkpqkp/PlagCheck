# encoding: utf-8
# module scipy.spatial.ckdtree
# from C:\Users\Doly\Anaconda3\lib\site-packages\scipy\spatial\ckdtree.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\Doly\Anaconda3\lib\site-packages\numpy\__init__.py
import scipy as scipy # C:\Users\Doly\Anaconda3\lib\site-packages\scipy\__init__.py
import threading as threading # C:\Users\Doly\Anaconda3\lib\threading.py

# functions

def cpu_count(*args, **kwargs): # real signature unknown
    """ Returns the number of CPUs in the system """
    pass

def new_object(*args, **kwargs): # real signature unknown
    pass

# classes

class cKDTree(object):
    """
    cKDTree(data, leafsize=16, compact_nodes=True, copy_data=False,
                balanced_tree=True)
    
        kd-tree for quick nearest-neighbor lookup
    
        This class provides an index into a set of k-dimensional points
        which can be used to rapidly look up the nearest neighbors of any
        point. 
    
        The algorithm used is described in Maneewongvatana and Mount 1999. 
        The general idea is that the kd-tree is a binary trie, each of whose
        nodes represents an axis-aligned hyperrectangle. Each node specifies
        an axis and splits the set of points based on whether their coordinate
        along that axis is greater than or less than a particular value. 
    
        During construction, the axis and splitting point are chosen by the 
        "sliding midpoint" rule, which ensures that the cells do not all
        become long and thin. 
    
        The tree can be queried for the r closest neighbors of any given point 
        (optionally returning only those within some maximum distance of the 
        point). It can also be queried, with a substantial gain in efficiency, 
        for the r approximate closest neighbors.
    
        For large dimensions (20 is already large) do not expect this to run 
        significantly faster than brute force. High-dimensional nearest-neighbor
        queries are a substantial open problem in computer science.
    
        Parameters
        ----------
        data : array_like, shape (n,m)
            The n data points of dimension m to be indexed. This array is 
            not copied unless this is necessary to produce a contiguous 
            array of doubles, and so modifying this data will result in 
            bogus results. The data are also copied if the kd-tree is built
            with copy_data=True.
        leafsize : positive int, optional
            The number of points at which the algorithm switches over to
            brute-force. Default: 16.
        compact_nodes : bool, optional    
            If True, the kd-tree is built to shrink the hyperrectangles to
            the actual data range. This usually gives a more compact tree that 
            is robust against degenerated input data and gives faster queries 
            at the expense of longer build time. Default: True.
        copy_data : bool, optional
            If True the data is always copied to protect the kd-tree against 
            data corruption. Default: False.
        balanced_tree : bool, optional    
            If True, the median is used to split the hyperrectangles instead of 
            the midpoint. This usually gives a more compact tree and 
            faster queries at the expense of longer build time. Default: True.
        boxsize : array_like or scalar, optional
            Apply a m-d toroidal topology to the KDTree.. The topology is generated 
            by :math:`x_i + n_i L_i` where :math:`n_i` are integers and :math:`L_i`
            is the boxsize along i-th dimension. The input data shall be wrapped 
            into :math:`[0, L_i)`. A ValueError is raised if any of the data is
            outside of this bound.
    
        Attributes
        ----------
        data : ndarray, shape (n,m)
            The n data points of dimension m to be indexed. This array is
            not copied unless this is necessary to produce a contiguous
            array of doubles. The data are also copied if the kd-tree is built
            with `copy_data=True`.
        leafsize : positive int
            The number of points at which the algorithm switches over to
            brute-force.
        m : int
            The dimension of a single data-point.
        n : int
            The number of data points.
        maxes : ndarray, shape (m,)
            The maximum value in each dimension of the n data points.
        mins : ndarray, shape (m,)
            The minimum value in each dimension of the n data points.
        tree : object, class cKDTreeNode
            This class exposes a Python view of the root node in the cKDTree object.
        size : int
            The number of nodes in the tree.
    
        See Also
        --------
        KDTree : Implementation of `cKDTree` in pure Python
    """
    def count_neighbors(self, other, r, p=2., weights=None, cumulative=True): # real signature unknown; restored from __doc__
        """
        count_neighbors(self, other, r, p=2., weights=None, cumulative=True)
        
                Count how many nearby pairs can be formed. (pair-counting)
        
                Count the number of pairs (x1,x2) can be formed, with x1 drawn
                from self and x2 drawn from ``other``, and where
                ``distance(x1, x2, p) <= r``.
        
                Data points on self and other are optionally weighted by the ``weights``
                argument. (See below)
        
                The algorithm we implement here is based on [1]_. See notes for further discussion.
        
                Parameters
                ----------
                other : cKDTree instance
                    The other tree to draw points from, can be the same tree as self.
                r : float or one-dimensional array of floats
                    The radius to produce a count for. Multiple radii are searched with
                    a single tree traversal. 
                    If the count is non-cumulative(``cumulative=False``), ``r`` defines 
                    the edges of the bins, and must be non-decreasing.
                p : float, optional 
                    1<=p<=infinity. 
                    Which Minkowski p-norm to use.
                    Default 2.0.
                weights : tuple, array_like, or None, optional
                    If None, the pair-counting is unweighted.
                    If given as a tuple, weights[0] is the weights of points in ``self``, and
                    weights[1] is the weights of points in ``other``; either can be None to 
                    indicate the points are unweighted.
                    If given as an array_like, weights is the weights of points in ``self``
                    and ``other``. For this to make sense, ``self`` and ``other`` must be the
                    same tree. If ``self`` and ``other`` are two different trees, a ``ValueError``
                    is raised.
                    Default: None
                cumulative : bool, optional
                    Whether the returned counts are cumulative. When cumulative is set to ``False``
                    the algorithm is optimized to work with a large number of bins (>10) specified
                    by ``r``. When ``cumulative`` is set to True, the algorithm is optimized to work
                    with a small number of ``r``. Default: True
        
                Returns
                -------
                result : scalar or 1-D array
                    The number of pairs. For unweighted counts, the result is integer.
                    For weighted counts, the result is float.
                    If cumulative is False, ``result[i]`` contains the counts with
                    ``(-inf if i == 0 else r[i-1]) < R <= r[i]``
        
                Notes
                -----
                Pair-counting is the basic operation used to calculate the two point
                correlation functions from a data set composed of position of objects.
        
                Two point correlation function measures the clustering of objects and
                is widely used in cosmology to quantify the large scale structure
                in our Universe, but it may be useful for data analysis in other fields
                where self-similar assembly of objects also occur.
        
                The Landy-Szalay estimator for the two point correlation function of
                ``D`` measures the clustering signal in ``D``. [2]_
        
                For example, given the position of two sets of objects,
        
                - objects ``D`` (data) contains the clustering signal, and
        
                - objects ``R`` (random) that contains no signal,
        
                .. math::
        
                     \xi(r) = \frac{<D, D> - 2 f <D, R> + f^2<R, R>}{f^2<R, R>},
        
                where the brackets represents counting pairs between two data sets
                in a finite bin around ``r`` (distance), corresponding to setting
                `cumulative=False`, and ``f = float(len(D)) / float(len(R))`` is the
                ratio between number of objects from data and random.
        
                The algorithm implemented here is loosely based on the dual-tree
                algorithm described in [1]_. We switch between two different
                pair-cumulation scheme depending on the setting of ``cumulative``.
                The computing time of the method we use when for
                ``cumulative == False`` does not scale with the total number of bins.
                The algorithm for ``cumulative == True`` scales linearly with the
                number of bins, though it is slightly faster when only
                1 or 2 bins are used. [5]_.
        
                As an extension to the naive pair-counting,
                weighted pair-counting counts the product of weights instead
                of number of pairs.
                Weighted pair-counting is used to estimate marked correlation functions
                ([3]_, section 2.2),
                or to properly calculate the average of data per distance bin
                (e.g. [4]_, section 2.1 on redshift).
        
                .. [1] Gray and Moore,
                       "N-body problems in statistical learning",
                       Mining the sky, 2000,
                       https://arxiv.org/abs/astro-ph/0012333
        
                .. [2] Landy and Szalay,
                       "Bias and variance of angular correlation functions",
                       The Astrophysical Journal, 1993,
                       http://adsabs.harvard.edu/abs/1993ApJ...412...64L
        
                .. [3] Sheth, Connolly and Skibba,
                       "Marked correlations in galaxy formation models",
                       Arxiv e-print, 2005,
                       https://arxiv.org/abs/astro-ph/0511773
        
                .. [4] Hawkins, et al.,
                       "The 2dF Galaxy Redshift Survey: correlation functions,
                       peculiar velocities and the matter density of the Universe",
                       Monthly Notices of the Royal Astronomical Society, 2002,
                       http://adsabs.harvard.edu/abs/2003MNRAS.346...78H
        
                .. [5] https://github.com/scipy/scipy/pull/5647#issuecomment-168474926
        """
        pass

    def query(self, x, k=1, eps=0, p=2, distance_upper_bound=None, n_jobs=1): # real signature unknown; restored from __doc__
        """
        query(self, x, k=1, eps=0, p=2, distance_upper_bound=np.inf, n_jobs=1)
        
                Query the kd-tree for nearest neighbors
        
                Parameters
                ----------
                x : array_like, last dimension self.m
                    An array of points to query.
                k : list of integer or integer
                    The list of k-th nearest neighbors to return. If k is an 
                    integer it is treated as a list of [1, ... k] (range(1, k+1)).
                    Note that the counting starts from 1.
                eps : non-negative float
                    Return approximate nearest neighbors; the k-th returned value 
                    is guaranteed to be no further than (1+eps) times the 
                    distance to the real k-th nearest neighbor.
                p : float, 1<=p<=infinity
                    Which Minkowski p-norm to use. 
                    1 is the sum-of-absolute-values "Manhattan" distance
                    2 is the usual Euclidean distance
                    infinity is the maximum-coordinate-difference distance
                distance_upper_bound : nonnegative float
                    Return only neighbors within this distance.  This is used to prune
                    tree searches, so if you are doing a series of nearest-neighbor
                    queries, it may help to supply the distance to the nearest neighbor
                    of the most recent point.
                n_jobs : int, optional
                    Number of jobs to schedule for parallel processing. If -1 is given
                    all processors are used. Default: 1.
                                
                Returns
                -------
                d : array of floats
                    The distances to the nearest neighbors. 
                    If ``x`` has shape ``tuple+(self.m,)``, then ``d`` has shape ``tuple+(k,)``.
                    When k == 1, the last dimension of the output is squeezed.
                    Missing neighbors are indicated with infinite distances.
                i : ndarray of ints
                    The locations of the neighbors in ``self.data``.
                    If ``x`` has shape ``tuple+(self.m,)``, then ``i`` has shape ``tuple+(k,)``.
                    When k == 1, the last dimension of the output is squeezed.
                    Missing neighbors are indicated with ``self.n``.
        
                Notes
                -----
                If the KD-Tree is periodic, the position ``x`` is wrapped into the
                box.
                
                When the input k is a list, a query for arange(max(k)) is performed, but
                only columns that store the requested values of k are preserved. This is 
                implemented in a manner that reduces memory usage.
        
                Examples
                --------
        
                >>> import numpy as np
                >>> from scipy.spatial import cKDTree
                >>> x, y = np.mgrid[0:5, 2:8]
                >>> tree = cKDTree(np.c_[x.ravel(), y.ravel()])
        
                To query the nearest neighbours and return squeezed result, use
        
                >>> dd, ii = tree.query([[0, 0], [2.1, 2.9]], k=1)
                >>> print(dd, ii)
                [2.         0.14142136] [ 0 13]
        
                To query the nearest neighbours and return unsqueezed result, use
        
                >>> dd, ii = tree.query([[0, 0], [2.1, 2.9]], k=[1])
                >>> print(dd, ii)
                [[2.        ]
                 [0.14142136]] [[ 0]
                 [13]]
        
                To query the second nearest neighbours and return unsqueezed result, use
        
                >>> dd, ii = tree.query([[0, 0], [2.1, 2.9]], k=[2])
                >>> print(dd, ii)
                [[2.23606798]
                 [0.90553851]] [[ 6]
                 [12]]
        
                To query the first and second nearest neighbours, use
        
                >>> dd, ii = tree.query([[0, 0], [2.1, 2.9]], k=2)
                >>> print(dd, ii)
                [[2.         2.23606798]
                 [0.14142136 0.90553851]] [[ 0  6]
                 [13 12]]
        
                or, be more specific
        
                >>> dd, ii = tree.query([[0, 0], [2.1, 2.9]], k=[1, 2])
                >>> print(dd, ii)
                [[2.         2.23606798]
                 [0.14142136 0.90553851]] [[ 0  6]
                 [13 12]]
        """
        pass

    def query_ball_point(self, x, r, p=2., eps=0): # real signature unknown; restored from __doc__
        """
        query_ball_point(self, x, r, p=2., eps=0)
                
                Find all points within distance r of point(s) x.
        
                Parameters
                ----------
                x : array_like, shape tuple + (self.m,)
                    The point or points to search for neighbors of.
                r : positive float
                    The radius of points to return.
                p : float, optional
                    Which Minkowski p-norm to use.  Should be in the range [1, inf].
                eps : nonnegative float, optional
                    Approximate search. Branches of the tree are not explored if their
                    nearest points are further than ``r / (1 + eps)``, and branches are
                    added in bulk if their furthest points are nearer than
                    ``r * (1 + eps)``.
                n_jobs : int, optional
                    Number of jobs to schedule for parallel processing. If -1 is given
                    all processors are used. Default: 1.
                return_sorted : bool, optional
                    Sorts returned indicies if True and does not sort them if False. If
                    None, does not sort single point queries, but does sort
                    multi-point queries which was the behavior before this option
                    was added.
        
                    .. versionadded:: 1.2.0
        
                Returns
                -------
                results : list or array of lists
                    If `x` is a single point, returns a list of the indices of the
                    neighbors of `x`. If `x` is an array of points, returns an object
                    array of shape tuple containing lists of neighbors.
        
                Notes
                -----
                If you have many points whose neighbors you want to find, you may save
                substantial amounts of time by putting them in a cKDTree and using
                query_ball_tree.
        
                Examples
                --------
                >>> from scipy import spatial
                >>> x, y = np.mgrid[0:4, 0:4]
                >>> points = np.c_[x.ravel(), y.ravel()]
                >>> tree = spatial.cKDTree(points)
                >>> tree.query_ball_point([2, 0], 1)
                [4, 8, 9, 12]
        """
        pass

    def query_ball_tree(self, other, r, p=2., eps=0): # real signature unknown; restored from __doc__
        """
        query_ball_tree(self, other, r, p=2., eps=0)
        
                Find all pairs of points whose distance is at most r
        
                Parameters
                ----------
                other : cKDTree instance
                    The tree containing points to search against.
                r : float
                    The maximum distance, has to be positive.
                p : float, optional
                    Which Minkowski norm to use.  `p` has to meet the condition
                    ``1 <= p <= infinity``.
                eps : float, optional
                    Approximate search.  Branches of the tree are not explored
                    if their nearest points are further than ``r/(1+eps)``, and
                    branches are added in bulk if their furthest points are nearer
                    than ``r * (1+eps)``.  `eps` has to be non-negative.
        
                Returns
                -------
                results : list of lists
                    For each element ``self.data[i]`` of this tree, ``results[i]`` is a
                    list of the indices of its neighbors in ``other.data``.
        """
        pass

    def query_pairs(self, r, p=2., eps=0): # real signature unknown; restored from __doc__
        """
        query_pairs(self, r, p=2., eps=0)
        
                Find all pairs of points whose distance is at most r.
        
                Parameters
                ----------
                r : positive float
                    The maximum distance.
                p : float, optional
                    Which Minkowski norm to use.  ``p`` has to meet the condition
                    ``1 <= p <= infinity``.
                eps : float, optional
                    Approximate search.  Branches of the tree are not explored
                    if their nearest points are further than ``r/(1+eps)``, and
                    branches are added in bulk if their furthest points are nearer
                    than ``r * (1+eps)``.  `eps` has to be non-negative.
                output_type : string, optional
                    Choose the output container, 'set' or 'ndarray'. Default: 'set'
        
                Returns
                -------
                results : set or ndarray
                    Set of pairs ``(i,j)``, with ``i < j``, for which the corresponding
                    positions are close. If output_type is 'ndarray', an ndarry is 
                    returned instead of a set.
        """
        pass

    def sparse_distance_matrix(self, other, max_distance, p=2.): # real signature unknown; restored from __doc__
        """
        sparse_distance_matrix(self, other, max_distance, p=2.)
        
                Compute a sparse distance matrix
        
                Computes a distance matrix between two cKDTrees, leaving as zero
                any distance greater than max_distance.
        
                Parameters
                ----------
                other : cKDTree
        
                max_distance : positive float
                
                p : float, 1<=p<=infinity
                    Which Minkowski p-norm to use. 
                
                output_type : string, optional
                    Which container to use for output data. Options: 'dok_matrix',
                    'coo_matrix', 'dict', or 'ndarray'. Default: 'dok_matrix'.
        
                Returns
                -------
                result : dok_matrix, coo_matrix, dict or ndarray
                    Sparse matrix representing the results in "dictionary of keys" 
                    format. If a dict is returned the keys are (i,j) tuples of indices.
                    If output_type is 'ndarray' a record array with fields 'i', 'j',
                    and 'k' is returned,
        """
        pass

    def _build_weights(self, weights): # real signature unknown; restored from __doc__
        """
        _build_weights(weights)
        
                Compute weights of nodes from weights of data points. This will sum
                up the total weight per node. This function is used internally.
        
                Parameters
                ----------
                weights : array_like
                    weights of data points; must be the same length as the data points.
                    currently only scalar weights are supported. Therefore the weights
                    array must be 1 dimensional.
        
                Returns
                -------
                node_weights : array_like
                    total weight for each KD-Tree node.
        """
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, data, leafsize=16, compact_nodes=True, copy_data=False, balanced_tree=True): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    boxsize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    indices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    leafsize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    m = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    maxes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mins = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tree = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001DA22146540>'


class cKDTreeNode(object):
    """
    class cKDTreeNode
    
        This class exposes a Python view of a node in the cKDTree object.
        
        All attributes are read-only.
        
        Attributes
        ----------
        level : int
            The depth of the node. 0 is the level of the root node.
        split_dim : int
            The dimension along which this node is split. If this value is -1  
            the node is a leafnode in the kd-tree. Leafnodes are not split further
            and scanned by brute force.
        split : float
            The value used to separate split this node. Points with value >= split
            in the split_dim dimension are sorted to the 'greater' subnode 
            whereas those with value < split are sorted to the 'lesser' subnode.
        children : int
            The number of data points sorted to this node.
        data_points : ndarray of float64
            An array with the data points sorted to this node.
        indices : ndarray of intp
            An array with the indices of the data points sorted to this node. The
            indices refer to the position in the data set used to construct the
            kd-tree.
        lesser : cKDTreeNode or None
            Subnode with the 'lesser' data points. This attribute is None for
            leafnodes.
        greater : cKDTreeNode or None
            Subnode with the 'greater' data points. This attribute is None for
            leafnodes.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    children = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    data_points = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    greater = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    indices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lesser = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    split = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    split_dim = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001DA21FD4870>'


class coo_entries(object):
    # no doc
    def coo_matrix(self, *args, **kwargs): # real signature unknown
        pass

    def dict(self, *args, **kwargs): # real signature unknown
        pass

    def dok_matrix(self, *args, **kwargs): # real signature unknown
        pass

    def ndarray(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __array_interface__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class ordered_pairs(object):
    # no doc
    def ndarray(self, *args, **kwargs): # real signature unknown
        pass

    def set(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __array_interface__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



# variables with complex values

__all__ = [
    'cKDTree',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001DA22007390>'

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.spatial.ckdtree', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001DA22007390>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\scipy\\\\spatial\\\\ckdtree.cp37-win_amd64.pyd')"

__test__ = {
    'cKDTree.query (line 644)': '\n        query(self, x, k=1, eps=0, p=2, distance_upper_bound=np.inf, n_jobs=1)\n\n        Query the kd-tree for nearest neighbors\n\n        Parameters\n        ----------\n        x : array_like, last dimension self.m\n            An array of points to query.\n        k : list of integer or integer\n            The list of k-th nearest neighbors to return. If k is an \n            integer it is treated as a list of [1, ... k] (range(1, k+1)).\n            Note that the counting starts from 1.\n        eps : non-negative float\n            Return approximate nearest neighbors; the k-th returned value \n            is guaranteed to be no further than (1+eps) times the \n            distance to the real k-th nearest neighbor.\n        p : float, 1<=p<=infinity\n            Which Minkowski p-norm to use. \n            1 is the sum-of-absolute-values "Manhattan" distance\n            2 is the usual Euclidean distance\n            infinity is the maximum-coordinate-difference distance\n        distance_upper_bound : nonnegative float\n            Return only neighbors within this distance.  This is used to prune\n            tree searches, so if you are doing a series of nearest-neighbor\n            queries, it may help to supply the distance to the nearest neighbor\n            of the most recent point.\n        n_jobs : int, optional\n            Number of jobs to schedule for parallel processing. If -1 is given\n            all processors are used. Default: 1.\n                        \n        Returns\n        -------\n        d : array of floats\n            The distances to the nearest neighbors. \n            If ``x`` has shape ``tuple+(self.m,)``, then ``d`` has shape ``tuple+(k,)``.\n            When k == 1, the last dimension of the output is squeezed.\n            Missing neighbors are indicated with infinite distances.\n        i : ndarray of ints\n            The locations of the neighbors in ``self.data``.\n            If ``x`` has shape ``tuple+(self.m,)``, then ``i`` has shape ``tuple+(k,)``.\n            When k == 1, the last dimension of the output is squeezed.\n            Missing neighbors are indicated with ``self.n``.\n\n        Notes\n        -----\n        If the KD-Tree is periodic, the position ``x`` is wrapped into the\n        box.\n        \n        When the input k is a list, a query for arange(max(k)) is performed, but\n        only columns that store the requested values of k are preserved. This is \n        implemented in a manner that reduces memory usage.\n\n        Examples\n        --------\n\n        >>> import numpy as np\n        >>> from scipy.spatial import cKDTree\n        >>> x, y = np.mgrid[0:5, 2:8]\n        >>> tree = cKDTree(np.c_[x.ravel(), y.ravel()])\n\n        To query the nearest neighbours and return squeezed result, use\n\n        >>> dd, ii = tree.query([[0, 0], [2.1, 2.9]], k=1)\n        >>> print(dd, ii)\n        [2.         0.14142136] [ 0 13]\n\n        To query the nearest neighbours and return unsqueezed result, use\n\n        >>> dd, ii = tree.query([[0, 0], [2.1, 2.9]], k=[1])\n        >>> print(dd, ii)\n        [[2.        ]\n         [0.14142136]] [[ 0]\n         [13]]\n\n        To query the second nearest neighbours and return unsqueezed result, use\n\n        >>> dd, ii = tree.query([[0, 0], [2.1, 2.9]], k=[2])\n        >>> print(dd, ii)\n        [[2.23606798]\n         [0.90553851]] [[ 6]\n         [12]]\n\n        To query the first and second nearest neighbours, use\n\n        >>> dd, ii = tree.query([[0, 0], [2.1, 2.9]], k=2)\n        >>> print(dd, ii)\n        [[2.         2.23606798]\n         [0.14142136 0.90553851]] [[ 0  6]\n         [13 12]]\n\n        or, be more specific\n\n        >>> dd, ii = tree.query([[0, 0], [2.1, 2.9]], k=[1, 2])\n        >>> print(dd, ii)\n        [[2.         2.23606798]\n         [0.14142136 0.90553851]] [[ 0  6]\n         [13 12]]\n\n        ',
    'cKDTree.query_ball_point (line 858)': '\n        query_ball_point(self, x, r, p=2., eps=0)\n        \n        Find all points within distance r of point(s) x.\n\n        Parameters\n        ----------\n        x : array_like, shape tuple + (self.m,)\n            The point or points to search for neighbors of.\n        r : positive float\n            The radius of points to return.\n        p : float, optional\n            Which Minkowski p-norm to use.  Should be in the range [1, inf].\n        eps : nonnegative float, optional\n            Approximate search. Branches of the tree are not explored if their\n            nearest points are further than ``r / (1 + eps)``, and branches are\n            added in bulk if their furthest points are nearer than\n            ``r * (1 + eps)``.\n        n_jobs : int, optional\n            Number of jobs to schedule for parallel processing. If -1 is given\n            all processors are used. Default: 1.\n        return_sorted : bool, optional\n            Sorts returned indicies if True and does not sort them if False. If\n            None, does not sort single point queries, but does sort\n            multi-point queries which was the behavior before this option\n            was added.\n\n            .. versionadded:: 1.2.0\n\n        Returns\n        -------\n        results : list or array of lists\n            If `x` is a single point, returns a list of the indices of the\n            neighbors of `x`. If `x` is an array of points, returns an object\n            array of shape tuple containing lists of neighbors.\n\n        Notes\n        -----\n        If you have many points whose neighbors you want to find, you may save\n        substantial amounts of time by putting them in a cKDTree and using\n        query_ball_tree.\n\n        Examples\n        --------\n        >>> from scipy import spatial\n        >>> x, y = np.mgrid[0:4, 0:4]\n        >>> points = np.c_[x.ravel(), y.ravel()]\n        >>> tree = spatial.cKDTree(points)\n        >>> tree.query_ball_point([2, 0], 1)\n        [4, 8, 9, 12]\n\n        ',
}


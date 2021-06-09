# encoding: utf-8
# module tables.tableextension
# from C:\Users\Doly\Anaconda3\lib\site-packages\tables\tableextension.cp37-win_amd64.pyd
# by generator 1.147
"""
Here is where Table and Row extension types live.

Classes (type extensions):

    Table
    Row

Functions:

Misc variables:
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import sys as sys # <module 'sys' (built-in)>
import numpy as numpy # C:\Users\Doly\Anaconda3\lib\site-packages\numpy\__init__.py
from tables.utilsextension import (atom_from_hdf5_type, create_nested_type, 
    get_nested_field, hdf5_to_np_ext_type)

from time import time

import numpy as __numpy
import tables.atom as __tables_atom
import tables.hdf5extension as __tables_hdf5extension


# Variables with simple values

H5T_STD_I64 = 216172782113783874

platform_byteorder = 0

# functions

def call_on_recarr(func, params, recarr, param2arg=None, **kwargs): # reliably restored by inspect
    """
    Call `func` with `params` over `recarr`.
    
        The `param2arg` function, when specified, is used to get an argument
        given a parameter name; otherwise, the parameter itself is used as
        an argument.  When the argument is a `Column` object, the proper
        column from `recarr` is used as its value.
    """
    pass

# classes

class Col(__tables_atom.Atom):
    """
    Defines a non-nested column.
    
        Col instances are used as a means to declare the different properties of a
        non-nested column in a table or nested column.  Col classes are descendants
        of their equivalent Atom classes (see :ref:`AtomClassDescr`), but their
        instances have an additional _v_pos attribute that is used to decide the
        position of the column inside its parent table or nested column (see the
        IsDescription class in :ref:`IsDescriptionClassDescr` for more information
        on column positions).
    
        In the same fashion as Atom, you should use a particular Col descendant
        class whenever you know the exact type you will need when writing your
        code. Otherwise, you may use one of the Col.from_*() factory methods.
    
        Each factory method inherited from the Atom class is available with the
        same signature, plus an additional pos parameter (placed in last position)
        which defaults to None and that may take an integer value.  This parameter
        might be used to specify the position of the column in the table.
    
        Besides, there are the next additional factory methods, available only for
        Col objects.
    
        The following parameters are available for most Col-derived constructors.
    
        Parameters
        ----------
        itemsize : int
            For types with a non-fixed size, this sets the size in bytes of
            individual items in the column.
        shape : tuple
            Sets the shape of the column. An integer shape of N is equivalent to
            the tuple (N,).
        dflt
            Sets the default value for the column.
        pos : int
            Sets the position of column in table.  If unspecified, the position
            will be randomly selected.
    """
    @classmethod
    def from_atom(cls, *args, **kwargs): # real signature unknown
        """
        Create a Col definition from a PyTables atom.
        
                An optional position may be specified as the pos argument.
        """
        pass

    @classmethod
    def from_dtype(cls, *args, **kwargs): # real signature unknown
        """
        Create a `Col` definition from a NumPy `dtype`.
        
                Optional default value and position may be specified as the
                `dflt` and `pos` arguments, respectively.  The `dtype` must have
                a byte order which is irrelevant or compatible with that of the
                system.  Information in the `dtype` not represented in a `Col`
                is ignored.
        """
        pass

    @classmethod
    def from_kind(cls, *args, **kwargs): # real signature unknown
        """
        Create a `Col` definition from a PyTables `kind`.
        
                Optional item size, shape, default value and position may be
                specified as the `itemsize`, `shape`, `dflt` and `pos`
                arguments, respectively.  Bear in mind that not all columns
                support a default item size.
        """
        pass

    @classmethod
    def from_sctype(cls, *args, **kwargs): # real signature unknown
        """
        Create a `Col` definition from a NumPy scalar type `sctype`.
        
                Optional shape, default value and position may be specified as
                the `shape`, `dflt` and `pos` arguments, respectively.
                Information in the `sctype` not represented in a `Col` is
                ignored.
        """
        pass

    @classmethod
    def from_type(cls, *args, **kwargs): # real signature unknown
        """
        Create a `Col` definition from a PyTables `type`.
        
                Optional shape, default value and position may be specified as
                the `shape`, `dflt` and `pos` arguments, respectively.
        """
        pass

    @classmethod
    def prefix(cls, *args, **kwargs): # real signature unknown
        """ Return the column class prefix. """
        pass

    def _get_init_args(self): # reliably restored by inspect
        """ Get a dictionary of instance constructor arguments. """
        pass

    @classmethod
    def _subclass_from_prefix(cls, *args, **kwargs): # real signature unknown
        """ Get a column subclass for the given `prefix`. """
        pass

    def __init__(self, nptype, shape, dflt): # reliably restored by inspect
        # no doc
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    _class_from_prefix = {
        'Bool': None, # (!) real value is "<class 'tables.description.Col._subclass_from_prefix.<locals>.NewCol'>"
        'Complex': None, # (!) real value is "<class 'tables.description.Col._subclass_from_prefix.<locals>.NewCol'>"
        'Complex128': None, # (!) real value is "<class 'tables.description.Col._subclass_from_prefix.<locals>.NewCol'>"
        'Complex32': None, # (!) real value is "<class 'tables.description.Col._subclass_from_prefix.<locals>.NewCol'>"
        'Complex64': None, # (!) real value is "<class 'tables.description.Col._subclass_from_prefix.<locals>.NewCol'>"
        'Enum': None, # (!) real value is "<class 'tables.description.Col._subclass_from_prefix.<locals>.NewCol'>"
        'Float': None, # (!) real value is "<class 'tables.description.Col._subclass_from_prefix.<locals>.NewCol'>"
        'Float16': None, # (!) real value is "<class 'tables.description.Col._subclass_from_prefix.<locals>.NewCol'>"
        'Float32': None, # (!) real value is "<class 'tables.description.Col._subclass_from_prefix.<locals>.NewCol'>"
        'Float64': None, # (!) real value is "<class 'tables.description.Col._subclass_from_prefix.<locals>.NewCol'>"
        'Int': None, # (!) real value is "<class 'tables.description.Col._subclass_from_prefix.<locals>.NewCol'>"
        'Int16': None, # (!) real value is "<class 'tables.description.Col._subclass_from_prefix.<locals>.NewCol'>"
        'Int32': None, # (!) real value is "<class 'tables.description.Col._subclass_from_prefix.<locals>.NewCol'>"
        'Int64': None, # (!) real value is "<class 'tables.description.Col._subclass_from_prefix.<locals>.NewCol'>"
        'Int8': None, # (!) real value is "<class 'tables.description.Col._subclass_from_prefix.<locals>.NewCol'>"
        'String': None, # (!) real value is "<class 'tables.description.Col._subclass_from_prefix.<locals>.NewCol'>"
        'Time': None, # (!) real value is "<class 'tables.description.Col._subclass_from_prefix.<locals>.NewCol'>"
        'Time32': None, # (!) real value is "<class 'tables.description.Col._subclass_from_prefix.<locals>.NewCol'>"
        'Time64': None, # (!) real value is "<class 'tables.description.Col._subclass_from_prefix.<locals>.NewCol'>"
        'UInt': None, # (!) real value is "<class 'tables.description.Col._subclass_from_prefix.<locals>.NewCol'>"
        'UInt16': None, # (!) real value is "<class 'tables.description.Col._subclass_from_prefix.<locals>.NewCol'>"
        'UInt32': None, # (!) real value is "<class 'tables.description.Col._subclass_from_prefix.<locals>.NewCol'>"
        'UInt64': None, # (!) real value is "<class 'tables.description.Col._subclass_from_prefix.<locals>.NewCol'>"
        'UInt8': None, # (!) real value is "<class 'tables.description.Col._subclass_from_prefix.<locals>.NewCol'>"
    }


class HDF5ExtError(RuntimeError):
    """
    A low level HDF5 operation failed.
    
        This exception is raised the low level PyTables components used for
        accessing HDF5 files.  It usually signals that something is not
        going well in the HDF5 library or even at the Input/Output level.
    
        Errors in the HDF5 C library may be accompanied by an extensive
        HDF5 back trace on standard error (see also
        :func:`tables.silence_hdf5_messages`).
    
        .. versionchanged:: 2.4
    
        Parameters
        ----------
        message
            error message
        h5bt
            This parameter (keyword only) controls the HDF5 back trace
            handling. Any keyword arguments other than h5bt is ignored.
    
            * if set to False the HDF5 back trace is ignored and the
              :attr:`HDF5ExtError.h5backtrace` attribute is set to None
            * if set to True the back trace is retrieved from the HDF5
              library and stored in the :attr:`HDF5ExtError.h5backtrace`
              attribute as a list of tuples
            * if set to "VERBOSE" (default) the HDF5 back trace is
              stored in the :attr:`HDF5ExtError.h5backtrace` attribute
              and also included in the string representation of the
              exception
            * if not set (or set to None) the default policy is used
              (see :attr:`HDF5ExtError.DEFAULT_H5_BACKTRACE_POLICY`)
    """
    def format_h5_backtrace(self, backtrace=None): # reliably restored by inspect
        """
        Convert the HDF5 trace back represented as a list of tuples.
                (see :attr:`HDF5ExtError.h5backtrace`) into a string.
        
                .. versionadded:: 2.4
        """
        pass

    @classmethod
    def set_policy_from_env(cls, *args, **kwargs): # real signature unknown
        pass

    def _dump_h5_backtrace(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def __str__(self): # reliably restored by inspect
        """
        Returns a sting representation of the exception.
        
                The actual result depends on policy set in the initializer
                :meth:`HDF5ExtError.__init__`.
        
                .. versionadded:: 2.4
        """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    DEFAULT_H5_BACKTRACE_POLICY = 'VERBOSE'


class Row(object):
    """
    Table row iterator and field accessor.
    
      Instances of this class are used to fetch and set the values
      of individual table fields.  It works very much like a dictionary,
      where keys are the pathnames or positions (extended slicing is
      supported) of the fields in the associated table in a specific row.
    
      This class provides an *iterator interface*
      so that you can use the same Row instance to
      access successive table rows one after the other.  There are also
      some important methods that are useful for accessing, adding and
      modifying values in tables.
    
      .. rubric:: Row attributes
    
      .. attribute:: nrow
    
          The current row number.
    
          This property is useful for knowing which row is being dealt with in the
          middle of a loop or iterator.
    """
    def append(self): # real signature unknown; restored from __doc__
        """
        Add a new row of data to the end of the dataset.
        
            Once you have filled the proper fields for the current
            row, calling this method actually appends the new data to the
            *output buffer* (which will eventually be
            dumped to disk).  If you have not set the value of a field, the
            default value of the column will be used.
        
            .. warning::
        
                After completion of the loop in which :meth:`Row.append` has
                been called, it is always convenient to make a call to
                :meth:`Table.flush` in order to avoid losing the last rows that
                may still remain in internal buffers.
        
            Examples
            --------
        
            ::
        
                row = table.row
                for i in xrange(nrows):
                    row['col1'] = i-1
                    row['col2'] = 'a'
                    row['col3'] = -1.0
                    row.append()
                table.flush()
        """
        pass

    def fetch_all_fields(self): # real signature unknown; restored from __doc__
        """
        Retrieve all the fields in the current row.
        
            Contrarily to row[:] (see :ref:`RowSpecialMethods`), this returns row
            data as a NumPy void scalar.  For instance::
        
                [row.fetch_all_fields() for row in table.where('col1 < 3')]
        
            will select all the rows that fulfill the given condition
            as a list of NumPy records.
        """
        pass

    def update(self): # real signature unknown; restored from __doc__
        """
        Change the data of the current row in the dataset.
        
            This method allows you to modify values in a table when you are in the
            middle of a table iterator like :meth:`Table.iterrows` or
            :meth:`Table.where`.
        
            Once you have filled the proper fields for the current row, calling
            this method actually changes data in the *output buffer* (which will
            eventually be dumped to disk).  If you have not set the value of a
            field, its original value will be used.
        
            .. warning::
        
                After completion of the loop in which :meth:`Row.update` has
                been called, it is always convenient to make a call to
                :meth:`Table.flush` in order to avoid losing changed rows that
                may still remain in internal buffers.
        
            Examples
            --------
        
            ::
        
                for row in table.iterrows(step=10):
                    row['col1'] = row.nrow
                    row['col2'] = 'b'
                    row['col3'] = 0.0
                    row.update()
                table.flush()
        
            which modifies every tenth row in table.  Or::
        
                for row in table.where('col1 > 3'):
                    row['col1'] = row.nrow
                    row['col2'] = 'b'
                    row['col3'] = 0.0
                    row.update()
                table.flush()
        
            which just updates the rows with values bigger than 3 in the first
            column.
        """
        pass

    def _fill_col(self, *args, **kwargs): # real signature unknown
        """ Read a field from a table on disk and put the result in result """
        pass

    def _flush_buffered_rows(self, *args, **kwargs): # real signature unknown
        pass

    def _flush_mod_rows(self, *args, **kwargs): # real signature unknown
        """ Flush any possible modified row using Row.update() """
        pass

    def _get_unsaved_nrows(self, *args, **kwargs): # real signature unknown
        pass

    def _iter(self, *args, **kwargs): # real signature unknown
        """ Return an iterator for traversiong the data in table. """
        pass

    def __contains__(self, item): # real signature unknown; restored from __doc__
        """
        __contains__(item)
        
            A true value is returned if item is found in current row, false
            otherwise.
        """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __getitem__(self, key): # real signature unknown; restored from __doc__
        """
        __getitem__(key)
        
            Get the row field specified by the `key`.
        
            The key can be a string (the name of the field), an integer (the
            position of the field) or a slice (the range of field positions). When
            key is a slice, the returned value is a *tuple* containing the values
            of the specified fields.
        
            Examples
            --------
        
            ::
        
                res = [row['var3'] for row in table.where('var2 < 20')]
        
            which selects the var3 field for all the rows that fulfil the
            condition. Or::
        
                res = [row[4] for row in table if row[1] < 20]
        
            which selects the field in the *4th* position for all the rows that
            fulfil the condition. Or::
        
                res = [row[:] for row in table if row['var2'] < 20]
        
            which selects the all the fields (in the form of a *tuple*) for all the
            rows that fulfil the condition. Or::
        
                res = [row[1::2] for row in table.iterrows(2, 3000, 3)]
        
            which selects all the fields in even positions (in the form of a
            *tuple*) for all the rows in the slice [2:3000:3].
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Iterator that traverses all the data in the Table """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        """ next() method for __iter__() that is called on each iteration """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Represent the record as an string """
        pass

    def __setitem__(self, key, value): # real signature unknown; restored from __doc__
        """
        __setitem__(key, value)
        
            Set the key row field to the specified value.
        
            Differently from its __getitem__() counterpart, in this case key can
            only be a string (the name of the field). The changes done via
            __setitem__() will not take effect on the data on disk until any of the
            :meth:`Row.append` or :meth:`Row.update` methods are called.
        
            Examples
            --------
        
            ::
        
                for row in table.iterrows(step=10):
                    row['col1'] = row.nrow
                    row['col2'] = 'b'
                    row['col3'] = 0.0
                    row.update()
                table.flush()
        
            which modifies every tenth row in the table.
        """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Represent the record as an string """
        pass

    nrow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The current row number.

    This property is useful for knowing which row is being dealt with in the
    middle of a loop or iterator.

    """

    table = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002259B0A4C00>'


class SizeType(__numpy.signedinteger):
    """
    Signed integer type, compatible with C ``long long``.
        Character code: ``'q'``.
        Canonical name: ``np.longlong``.
        Alias *on this platform*: ``np.int64``: 64-bit signed integer (-9223372036854775808 to 9223372036854775807).
        Alias *on this platform*: ``np.intp``: Signed integer large enough to fit pointer, compatible with C ``intptr_t``.
    """
    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass


class Table(__tables_hdf5extension.Leaf):
    # no doc
    def _append_records(self, *args, **kwargs): # real signature unknown
        pass

    def _close_append(self, *args, **kwargs): # real signature unknown
        pass

    def _convert_types(self, *args, **kwargs): # real signature unknown
        """
        Converts columns in 'recarr' between NumPy and HDF5 formats.
        
            NumPy to HDF5 conversion is performed when 'sense' is 0.  Otherwise, HDF5
            to NumPy conversion is performed.  The conversion is done in place,
            i.e. 'recarr' is modified.
        """
        pass

    def _create_table(self, *args, **kwargs): # real signature unknown
        pass

    def _get_info(self, *args, **kwargs): # real signature unknown
        """ Get info from a table on disk. """
        pass

    def _open_append(self, *args, **kwargs): # real signature unknown
        pass

    def _read_elements(self, *args, **kwargs): # real signature unknown
        pass

    def _read_records(self, *args, **kwargs): # real signature unknown
        pass

    def _remove_rows(self, *args, **kwargs): # real signature unknown
        pass

    def _update_elements(self, *args, **kwargs): # real signature unknown
        pass

    def _update_records(self, *args, **kwargs): # real signature unknown
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

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002259B0A4BD0>'


# variables with complex values

hdf5_class_to_string = {
    -1: 'H5T_NO_CLASS',
    0: 'H5T_INTEGER',
    1: 'H5T_FLOAT',
    2: 'H5T_TIME',
    3: 'H5T_STRING',
    4: 'H5T_BITFIELD',
    5: 'H5T_OPAQUE',
    6: 'H5T_COMPOUND',
    7: 'H5T_REFERENCE',
    8: 'H5T_ENUM',
    9: 'H5T_VLEN',
    10: 'H5T_ARRAY',
}

npext_prefixes_to_ptkinds = {
    'S': 'string',
    'b': 'bool',
    'c': 'complex',
    'e': 'enum',
    'f': 'float',
    'i': 'int',
    't': 'time',
    'u': 'uint',
}

pttype_to_hdf5 = {
    'float128': 216172782113783852,
    'float32': 216172782113783862,
    'float64': 216172782113783864,
    'float96': 216172782113783852,
    'int16': 216172782113783870,
    'int32': 216172782113783872,
    'int64': 216172782113783874,
    'int8': 216172782113783868,
    'time32': 216172782113783892,
    'time64': 216172782113783894,
    'uint16': 216172782113783878,
    'uint32': 216172782113783880,
    'uint64': 216172782113783882,
    'uint8': 216172782113783876,
}

pt_special_kinds = [
    'complex',
    'string',
    'enum',
    'bool',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000002259B0CD630>'

__spec__ = None # (!) real value is "ModuleSpec(name='tables.tableextension', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000002259B0CD630>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\tables\\\\tableextension.cp37-win_amd64.pyd')"

__test__ = {}


# encoding: utf-8
# module py.path
# from C:\Users\Doly\Anaconda3\lib\site-packages\sklearn\feature_extraction\_hashing.cp37-win_amd64.pyd
# by generator 1.147
""" unified file system api """

# imports
import py._path.common as __py__path_common
import py._path.svnwc as __py__path_svnwc


# Variables with simple values

_ApiModule__doc = ' unified file system api '

__implprefix__ = 'py'

# no functions
# classes

class local(__py__path_common.PathBase):
    """
    object oriented interface to os.path and other local filesystem
            related information.
    """
    def as_cwd(*args, **kwds): # reliably restored by inspect
        """
        Return a context manager, which changes to the path's dir during the
                managed "with" context.
                On __enter__ it returns the old dir, which might be ``None``.
        """
        pass

    def atime(self): # reliably restored by inspect
        """ return last access time of the path. """
        pass

    def chdir(self): # reliably restored by inspect
        """ change directory to self and return old current directory """
        pass

    def check(self, **kw): # reliably restored by inspect
        # no doc
        pass

    def chmod(self, mode, rec=0): # reliably restored by inspect
        """
        change permissions to the given mode. If mode is an
                    integer it directly encodes the os-specific modes.
                    if rec is True perform recursively.
        """
        pass

    def computehash(self, hashtype=None, chunksize=524288): # reliably restored by inspect
        """ return hexdigest of hashvalue for this file. """
        pass

    def copy(self, target, mode=False, stat=False): # reliably restored by inspect
        """
        copy path to target.
        
                    If mode is True, will copy copy permission from path to target.
                    If stat is True, copy permission, last modification
                    time, last access time, and flags from path to target.
        """
        pass

    def dirpath(self, *args, **kwargs): # reliably restored by inspect
        """ return the directory path joined with any given path arguments. """
        pass

    def dump(self, obj, bin=1): # reliably restored by inspect
        """ pickle object into path location """
        pass

    def ensure(self, *args, **kwargs): # reliably restored by inspect
        """
        ensure that an args-joined path exists (by default as
                    a file). if you specify a keyword argument 'dir=True'
                    then the path is forced to be a directory path.
        """
        pass

    @classmethod
    def get_temproot(cls, *args, **kwargs): # real signature unknown
        """
        return the system's temporary directory
                    (where tempfiles are usually created in)
        """
        pass

    def islink(self): # reliably restored by inspect
        # no doc
        pass

    def join(self, *args, **kwargs): # reliably restored by inspect
        """
        return a new path by appending all 'args' as path
                components.  if abs=1 is used restart from root if any
                of the args is an absolute path.
        """
        pass

    def listdir(self, fil=None, sort=None): # reliably restored by inspect
        """
        list directory contents, possibly filter by the given fil func
                    and possibly sorted.
        """
        pass

    def lstat(self): # reliably restored by inspect
        """ Return an os.lstat() tuple. """
        pass

    @classmethod
    def make_numbered_dir(cls, *args, **kwargs): # real signature unknown
        """
        return unique directory with a number greater than the current
                    maximum one.  The number is assumed to start directly after prefix.
                    if keep is true directories with a number less than (maxnum-keep)
                    will be removed. If .lock files are used (lock_timeout non-zero),
                    algorithm is multi-process safe.
        """
        pass

    def mkdir(self, *args): # reliably restored by inspect
        """ create & return the directory joined with args. """
        pass

    @classmethod
    def mkdtemp(cls, *args, **kwargs): # real signature unknown
        """
        return a Path object pointing to a fresh new temporary directory
                    (which we created ourself).
        """
        pass

    def mtime(self): # reliably restored by inspect
        """ return last modification time of the path. """
        pass

    def new(self, **kw): # reliably restored by inspect
        """
        create a modified version of this path.
                    the following keyword arguments modify various path parts::
        
                      a:/some/path/to/a/file.ext
                      xx                           drive
                      xxxxxxxxxxxxxxxxx            dirname
                                        xxxxxxxx   basename
                                        xxxx       purebasename
                                             xxx   ext
        """
        pass

    def open(self, mode=None, ensure=False, encoding=None): # reliably restored by inspect
        """
        return an opened file with the given mode.
        
                If ensure is True, create parent directories if needed.
        """
        pass

    def pyimport(self, modname=None, ensuresyspath=True): # reliably restored by inspect
        """
        return path as an imported python module.
        
                If modname is None, look for the containing package
                and construct an according module name.
                The module will be put/looked up in sys.modules.
                if ensuresyspath is True then the root dir for importing
                the file (taking __init__.py files into account) will
                be prepended to sys.path if it isn't there already.
                If ensuresyspath=="append" the root dir will be appended
                if it isn't already contained in sys.path.
                if ensuresyspath is False no modification of syspath happens.
        
                Special value of ensuresyspath=="importlib" is intended
                purely for using in pytest, it is capable only of importing
                separate .py files outside packages, e.g. for test suite
                without any __init__.py file. It effectively allows having
                same-named test modules in different places and offers
                mild opt-in via this option. Note that it works only in
                recent versions of python.
        """
        pass

    def pypkgpath(self): # reliably restored by inspect
        """
        return the Python package path by looking for the last
                directory upwards which still contains an __init__.py.
                Return None if a pkgpath can not be determined.
        """
        pass

    def realpath(self): # reliably restored by inspect
        """ return a new path which contains no symbolic links. """
        pass

    def remove(self, rec=1, ignore_errors=False): # reliably restored by inspect
        """
        remove a file or directory (or a directory tree if rec=1).
                if ignore_errors is True, errors while removing directories will
                be ignored.
        """
        pass

    def rename(self, target): # reliably restored by inspect
        """ rename this path to target. """
        pass

    def samefile(self, other): # reliably restored by inspect
        """ return True if 'other' references the same file as 'self'. """
        pass

    def setmtime(self, mtime=None): # reliably restored by inspect
        """
        set modification time for the given path.  if 'mtime' is None
                (the default) then the file's mtime is set to current time.
        
                Note that the resolution for 'mtime' is platform dependent.
        """
        pass

    def size(self): # reliably restored by inspect
        """ return size of the underlying file object """
        pass

    def stat(self, raising=True): # reliably restored by inspect
        """ Return an os.stat() tuple. """
        pass

    def sysexec(self, *argv, **popen_opts): # reliably restored by inspect
        """
        return stdout text from executing a system child process,
                    where the 'self' path points to executable.
                    The process is directly invoked and not through a system shell.
        """
        pass

    @classmethod
    def sysfind(cls, *args, **kwargs): # real signature unknown
        """
        return a path object found by looking at the systems
                    underlying PATH specification. If the checker is not None
                    it will be invoked to filter matching paths.  If a binary
                    cannot be found, None is returned
                    Note: This is probably not working on plain win32 systems
                    but may work on cygwin.
        """
        pass

    def write(self, data, mode=None, ensure=False): # reliably restored by inspect
        """
        write data into path.   If ensure is True create
                missing parent directories.
        """
        pass

    def write_binary(self, data, ensure=False): # reliably restored by inspect
        """
        write binary data into path.   If ensure is True create
                missing parent directories.
        """
        pass

    def write_text(self, data, encoding, ensure=False): # reliably restored by inspect
        """
        write text data into path using the specified encoding.
                If ensure is True create missing parent directories.
        """
        pass

    def _ensuredirs(self): # reliably restored by inspect
        # no doc
        pass

    def _ensuresyspath(self, ensuremode, path): # reliably restored by inspect
        # no doc
        pass

    def _fastjoin(self, name): # reliably restored by inspect
        # no doc
        pass

    def _getbyspec(self, spec): # reliably restored by inspect
        """ see new for what 'spec' can be. """
        pass

    @classmethod
    def _gethomedir(cls, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __gt__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __hash__(self): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, path=None, expanduser=False): # reliably restored by inspect
        """
        Initialize and return a local Path instance.
        
                Path can be relative to the current directory.
                If path is None it defaults to the current working directory.
                If expanduser is True, tilde-expansion is performed.
                Note that Path instances always carry an absolute path.
                Note also that passing in a local path object will simply return
                the exact same path object. Use new() to get a new copy.
        """
        pass

    def __lt__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __ne__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    def __str__(self): # reliably restored by inspect
        """ return string representation of the Path. """
        pass

    Checkers = None # (!) real value is "<class 'py._path.local.LocalPath.Checkers'>"
    ImportMismatchError = None # (!) real value is "<class 'py._path.local.LocalPath.ImportMismatchError'>"
    sep = '\\'
    _patternchars = None # (!) real value is "{'?', '\\\\', '[', '*'}"


class SvnAuth(object):
    """ container for auth information for Subversion """
    def makecmdoptions(self): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, username, password, cache_auth=True, interactive=True): # reliably restored by inspect
        # no doc
        pass

    def __str__(self): # reliably restored by inspect
        # no doc
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'py._path.svnwc', '__doc__': ' container for auth information for Subversion ', '__init__': <function SvnAuth.__init__ at 0x00000215364C9598>, 'makecmdoptions': <function SvnAuth.makecmdoptions at 0x00000215364C9620>, '__str__': <function SvnAuth.__str__ at 0x00000215364C96A8>, '__dict__': <attribute '__dict__' of 'SvnAuth' objects>, '__weakref__': <attribute '__weakref__' of 'SvnAuth' objects>})"


class svnurl(__py__path_svnwc.SvnPathBase):
    """
    path implementation that offers access to (possibly remote) subversion
        repositories.
    """
    def copy(self, target, msg=None): # reliably restored by inspect
        """ copy path to target with checkin message msg. """
        pass

    def dirpath(self, *args, **kwargs): # reliably restored by inspect
        """
        return the directory path of the current path joined
                    with any given path arguments.
        """
        pass

    def ensure(self, *args, **kwargs): # reliably restored by inspect
        """
        ensure that an args-joined path exists (by default as
                    a file). If you specify a keyword argument 'dir=True'
                    then the path is forced to be a directory path.
        """
        pass

    def export(self, topath): # reliably restored by inspect
        """
        export to a local path
        
                    topath should not exist prior to calling this, returns a
                    py.path.local instance
        """
        pass

    def info(self): # reliably restored by inspect
        """ return an Info structure with svn-provided information. """
        pass

    def listdir(self, fil=None, sort=None): # reliably restored by inspect
        """
        list directory contents, possibly filter by the given fil func
                    and possibly sorted.
        """
        pass

    def log(self, rev_start=None, rev_end=1, verbose=False): # reliably restored by inspect
        """
        return a list of LogEntry instances for this path.
        rev_start is the starting revision (defaulting to the first one).
        rev_end is the last revision (defaulting to HEAD).
        if verbose is True, then the LogEntry instances also know which files changed.
        """
        pass

    def mkdir(self, *args, **kwargs): # reliably restored by inspect
        """
        create & return the directory joined with args.
                pass a 'msg' keyword argument to set the commit message.
        """
        pass

    def open(self, mode=None): # reliably restored by inspect
        """ return an opened file with the given mode. """
        pass

    def remove(self, rec=1, msg=None): # reliably restored by inspect
        """
        remove a file or directory (or a directory tree if rec=1) with
        checkin message msg.
        """
        pass

    def rename(self, target, msg=None): # reliably restored by inspect
        """ rename this path to target with checkin message msg. """
        pass

    def _cmdexec(self, cmd): # reliably restored by inspect
        # no doc
        pass

    def _encodedurl(self): # reliably restored by inspect
        # no doc
        pass

    def _listdir_nameinfo(self): # reliably restored by inspect
        """ return sequence of name-info directory entries of self """
        pass

    def _norev_delentry(self, path): # reliably restored by inspect
        # no doc
        pass

    def _popen(self, cmd): # reliably restored by inspect
        # no doc
        pass

    def _propget(self, name): # reliably restored by inspect
        # no doc
        pass

    def _proplist(self): # reliably restored by inspect
        # no doc
        pass

    def _svncmdexecauth(self, cmd): # reliably restored by inspect
        """ execute an svn command 'as is' """
        pass

    def _svnpopenauth(self, cmd): # reliably restored by inspect
        """ execute an svn command, return a pipe for reading stdin """
        pass

    def _svnwithrev(self, cmd, *args): # reliably restored by inspect
        """ execute an svn command, append our own url and revision """
        pass

    def _svnwrite(self, cmd, *args): # reliably restored by inspect
        """ execute an svn command, append our own url """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(cls, path, rev=None, auth=None): # reliably restored by inspect
        # no doc
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    _lsnorevcache = None # (!) real value is '<py._path.cacheutil.AgingCache object at 0x00000215364CFA20>'
    _lsrevcache = None # (!) real value is '<py._path.cacheutil.BuildcostAccessCache object at 0x00000215364CF9E8>'


class svnwc(__py__path_common.PathBase):
    """
    path implementation offering access/modification to svn working copies.
            It has methods similar to the functions in os.path and similar to the
            commands of the svn client.
    """
    def add(self): # reliably restored by inspect
        """ add ourself to svn """
        pass

    def blame(self): # reliably restored by inspect
        """
        return a list of tuples of three elements:
                    (revision, commiter, line)
        """
        pass

    def checkout(self, url=None, rev=None): # reliably restored by inspect
        """ checkout from url to local wcpath. """
        pass

    def cleanup(self): # reliably restored by inspect
        """ remove any locks from the resource """
        pass

    def commit(self, msg=None, rec=1): # reliably restored by inspect
        """ commit with support for non-recursive commits """
        pass

    def copy(self, target): # reliably restored by inspect
        """ copy path to target. """
        pass

    def diff(self, rev=None): # reliably restored by inspect
        """
        return a diff of the current path against revision rev (defaulting
                    to the last one).
        """
        pass

    def dirpath(self, *args): # reliably restored by inspect
        """ return the directory Path of the current Path. """
        pass

    def dump(self, obj): # reliably restored by inspect
        """ pickle object into path location """
        pass

    def ensure(self, *args, **kwargs): # reliably restored by inspect
        """
        ensure that an args-joined path exists (by default as
                    a file). if you specify a keyword argument 'directory=True'
                    then the path is forced  to be a directory path.
        """
        pass

    def info(self, usecache=1): # reliably restored by inspect
        """ return an Info structure with svn-provided information. """
        pass

    def join(self, *args, **kwargs): # reliably restored by inspect
        """
        return a new Path (with the same revision) which is composed
                    of the self Path followed by 'args' path components.
        """
        pass

    def listdir(self, fil=None, sort=None): # reliably restored by inspect
        """
        return a sequence of Paths.
        
                listdir will return either a tuple or a list of paths
                depending on implementation choices.
        """
        pass

    def lock(self): # reliably restored by inspect
        """ set a lock (exclusive) on the resource """
        pass

    def log(self, rev_start=None, rev_end=1, verbose=False): # reliably restored by inspect
        """
        return a list of LogEntry instances for this path.
        rev_start is the starting revision (defaulting to the first one).
        rev_end is the last revision (defaulting to HEAD).
        if verbose is True, then the LogEntry instances also know which files changed.
        """
        pass

    def mkdir(self, *args): # reliably restored by inspect
        """ create & return the directory joined with args. """
        pass

    def mtime(self): # reliably restored by inspect
        """ Return the last modification time of the file. """
        pass

    def new(self, **kw): # reliably restored by inspect
        """
        create a modified version of this path. A 'rev' argument
                    indicates a new revision.
                    the following keyword arguments modify various path parts:
        
                      http://host.com/repo/path/file.ext
                      |-----------------------|          dirname
                                                |------| basename
                                                |--|     purebasename
                                                    |--| ext
        """
        pass

    def open(self, mode=None): # reliably restored by inspect
        """ return an opened file with the given mode. """
        pass

    def propdel(self, name): # reliably restored by inspect
        """ delete property name on this path. """
        pass

    def propget(self, name): # reliably restored by inspect
        """ get property name on this path. """
        pass

    def proplist(self, rec=0): # reliably restored by inspect
        """
        return a mapping of property names to property values.
        If rec is True, then return a dictionary mapping sub-paths to such mappings.
        """
        pass

    def propset(self, name, value, *args): # reliably restored by inspect
        """ set property name to value on this path. """
        pass

    def remove(self, rec=1, force=1): # reliably restored by inspect
        """
        remove a file or a directory tree. 'rec'ursive is
                    ignored and considered always true (because of
                    underlying svn semantics.
        """
        pass

    def rename(self, target): # reliably restored by inspect
        """ rename this path to target. """
        pass

    def revert(self, rec=0): # reliably restored by inspect
        """
        revert the local changes of this path. if rec is True, do so
        recursively.
        """
        pass

    def size(self): # reliably restored by inspect
        """ Return the size of the file content of the Path. """
        pass

    def status(self, updates=0, rec=0, externals=0): # reliably restored by inspect
        """ return (collective) Status object for this file. """
        pass

    def svnurl(self): # reliably restored by inspect
        """ return current SvnPath for this WC-item. """
        pass

    def switch(self, url): # reliably restored by inspect
        """ switch to given URL. """
        pass

    def unlock(self): # reliably restored by inspect
        """ unset a previously set lock """
        pass

    def update(self, rev=None, interactive=True): # reliably restored by inspect
        """ update working copy item to given revision. (None -> HEAD). """
        pass

    def write(self, content, mode=None): # reliably restored by inspect
        """ write content into local filesystem wc. """
        pass

    def _authsvn(self, cmd, args=None): # reliably restored by inspect
        # no doc
        pass

    def _ensuredirs(self): # reliably restored by inspect
        # no doc
        pass

    def _escape(self, cmd): # reliably restored by inspect
        # no doc
        pass

    def _getbyspec(self, spec): # reliably restored by inspect
        # no doc
        pass

    def _geturl(self): # reliably restored by inspect
        # no doc
        pass

    def _makeauthoptions(self): # reliably restored by inspect
        # no doc
        pass

    def _svn(self, cmd, *args): # reliably restored by inspect
        # no doc
        pass

    def __eq__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __hash__(self): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(cls, wcpath=None, auth=None): # reliably restored by inspect
        # no doc
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    def __str__(self): # reliably restored by inspect
        # no doc
        pass

    rev = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """revision"""

    strpath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """string path"""

    url = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """url of this WC item"""


    Checkers = None # (!) real value is "<class 'py._path.svnwc.SvnWCCommandPath.Checkers'>"
    sep = '\\'
    _rex_commit = re.compile('.*Committed revision (\\d+)\\.$', re.DOTALL)


# variables with complex values

__all__ = [
    '__doc__',
    'svnwc',
    'svnurl',
    'local',
    'SvnAuth',
]

__map__ = {}


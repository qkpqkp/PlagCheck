# encoding: utf-8
# module psutil._psutil_windows calls itself psutil_windows
# from C:\Users\Doly\Anaconda3\lib\site-packages\psutil\_psutil_windows.cp37-win_amd64.pyd
# by generator 1.147
# no doc
# no imports

# Variables with simple values

ABOVE_NORMAL_PRIORITY_CLASS = 32768

BELOW_NORMAL_PRIORITY_CLASS = 16384

ERROR_ACCESS_DENIED = 5

ERROR_INVALID_NAME = 123

ERROR_PRIVILEGE_NOT_HELD = 1314

ERROR_SERVICE_DOES_NOT_EXIST = 1060

HIGH_PRIORITY_CLASS = 128

IDLE_PRIORITY_CLASS = 64

INFINITE = -1

MIB_TCP_STATE_CLOSED = 1

MIB_TCP_STATE_CLOSE_WAIT = 8

MIB_TCP_STATE_CLOSING = 9

MIB_TCP_STATE_DELETE_TCB = 12

MIB_TCP_STATE_ESTAB = 5

MIB_TCP_STATE_FIN_WAIT1 = 6
MIB_TCP_STATE_FIN_WAIT2 = 7

MIB_TCP_STATE_LAST_ACK = 10

MIB_TCP_STATE_LISTEN = 2

MIB_TCP_STATE_SYN_RCVD = 4
MIB_TCP_STATE_SYN_SENT = 3

MIB_TCP_STATE_TIME_WAIT = 11

NORMAL_PRIORITY_CLASS = 32

PSUTIL_CONN_NONE = 128

REALTIME_PRIORITY_CLASS = 256

version = 563

WINDOWS_10 = 100
WINDOWS_7 = 61
WINDOWS_8 = 62

WINDOWS_8_1 = 63

WINDOWS_SERVER_2003 = 52

WINDOWS_VISTA = 60
WINDOWS_XP = 51

WINVER = 100

# functions

def boot_time(*args, **kwargs): # real signature unknown
    """ Return the system boot time expressed in seconds since the epoch. """
    pass

def cpu_count_logical(*args, **kwargs): # real signature unknown
    """ Returns the number of logical CPUs on the system """
    pass

def cpu_count_phys(*args, **kwargs): # real signature unknown
    """ Returns the number of physical CPUs on the system """
    pass

def cpu_freq(*args, **kwargs): # real signature unknown
    """ Return CPU frequency. """
    pass

def cpu_stats(*args, **kwargs): # real signature unknown
    """ Return NICs stats. """
    pass

def cpu_times(*args, **kwargs): # real signature unknown
    """ Return system cpu times as a list """
    pass

def disk_io_counters(*args, **kwargs): # real signature unknown
    """ Return dict of tuples of disks I/O information. """
    pass

def disk_partitions(*args, **kwargs): # real signature unknown
    """ Return disk partitions. """
    pass

def disk_usage(*args, **kwargs): # real signature unknown
    """ Return path's disk total and free as a Python tuple. """
    pass

def getloadavg(*args, **kwargs): # real signature unknown
    """ Returns the emulated POSIX-like load average. """
    pass

def getpagesize(*args, **kwargs): # real signature unknown
    """ Return system memory page size. """
    pass

def init_loadavg_counter(*args, **kwargs): # real signature unknown
    """ Initializes the emulated load average calculator. """
    pass

def net_connections(*args, **kwargs): # real signature unknown
    """ Return system-wide connections """
    pass

def net_if_addrs(*args, **kwargs): # real signature unknown
    """ Return NICs addresses. """
    pass

def net_if_stats(*args, **kwargs): # real signature unknown
    """ Return NICs stats. """
    pass

def net_io_counters(*args, **kwargs): # real signature unknown
    """ Return dict of tuples of networks I/O information. """
    pass

def per_cpu_times(*args, **kwargs): # real signature unknown
    """ Return system per-cpu times as a list of tuples """
    pass

def pids(*args, **kwargs): # real signature unknown
    """ Returns a list of PIDs currently running on the system """
    pass

def pid_exists(*args, **kwargs): # real signature unknown
    """ Determine if the process exists in the current process list. """
    pass

def ppid_map(*args, **kwargs): # real signature unknown
    """ Return a {pid:ppid, ...} dict for all running processes """
    pass

def proc_cmdline(*args, **kwargs): # real signature unknown
    """ Return process cmdline as a list of cmdline arguments """
    pass

def proc_cpu_affinity_get(*args, **kwargs): # real signature unknown
    """ Return process CPU affinity as a bitmask. """
    pass

def proc_cpu_affinity_set(*args, **kwargs): # real signature unknown
    """ Set process CPU affinity. """
    pass

def proc_cpu_times(*args, **kwargs): # real signature unknown
    """ Return tuple of user/kern time for the given PID """
    pass

def proc_create_time(*args, **kwargs): # real signature unknown
    """ Return a float indicating the process create time expressed in seconds since the epoch """
    pass

def proc_cwd(*args, **kwargs): # real signature unknown
    """ Return process current working directory """
    pass

def proc_environ(*args, **kwargs): # real signature unknown
    """ Return process environment data """
    pass

def proc_exe(*args, **kwargs): # real signature unknown
    """ Return path of the process executable """
    pass

def proc_info(*args, **kwargs): # real signature unknown
    """ Various process information """
    pass

def proc_io_counters(*args, **kwargs): # real signature unknown
    """ Get process I/O counters. """
    pass

def proc_io_priority_get(*args, **kwargs): # real signature unknown
    """ Return process IO priority. """
    pass

def proc_io_priority_set(*args, **kwargs): # real signature unknown
    """ Set process IO priority. """
    pass

def proc_is_suspended(*args, **kwargs): # real signature unknown
    """ Return True if one of the process threads is in a suspended state """
    pass

def proc_kill(*args, **kwargs): # real signature unknown
    """ Kill the process identified by the given PID """
    pass

def proc_memory_info(*args, **kwargs): # real signature unknown
    """ Return a tuple of process memory information """
    pass

def proc_memory_maps(*args, **kwargs): # real signature unknown
    """ Return a list of process's memory mappings """
    pass

def proc_memory_uss(*args, **kwargs): # real signature unknown
    """ Return the USS of the process """
    pass

def proc_name(*args, **kwargs): # real signature unknown
    """ Return process name """
    pass

def proc_num_handles(*args, **kwargs): # real signature unknown
    """ Return the number of handles opened by process. """
    pass

def proc_open_files(*args, **kwargs): # real signature unknown
    """ Return files opened by process """
    pass

def proc_priority_get(*args, **kwargs): # real signature unknown
    """ Return process priority. """
    pass

def proc_priority_set(*args, **kwargs): # real signature unknown
    """ Set process priority. """
    pass

def proc_suspend_or_resume(*args, **kwargs): # real signature unknown
    """ Suspend or resume a process """
    pass

def proc_threads(*args, **kwargs): # real signature unknown
    """ Return process threads information as a list of tuple """
    pass

def proc_username(*args, **kwargs): # real signature unknown
    """ Return the username of a process """
    pass

def proc_wait(*args, **kwargs): # real signature unknown
    """ Wait for process to terminate and return its exit code. """
    pass

def sensors_battery(*args, **kwargs): # real signature unknown
    """ Return battery metrics usage. """
    pass

def set_testing(*args, **kwargs): # real signature unknown
    """ Set psutil in testing mode """
    pass

def users(*args, **kwargs): # real signature unknown
    """ Return a list of currently connected users. """
    pass

def virtual_mem(*args, **kwargs): # real signature unknown
    """ Return the total amount of physical memory, in bytes """
    pass

def win32_QueryDosDevice(*args, **kwargs): # real signature unknown
    """ QueryDosDevice binding """
    pass

def winservice_enumerate(*args, **kwargs): # real signature unknown
    """ List all services """
    pass

def winservice_query_config(*args, **kwargs): # real signature unknown
    """ Return service config """
    pass

def winservice_query_descr(*args, **kwargs): # real signature unknown
    """ Return the description of a service """
    pass

def winservice_query_status(*args, **kwargs): # real signature unknown
    """ Return service config """
    pass

def winservice_start(*args, **kwargs): # real signature unknown
    """ Start a service """
    pass

def winservice_stop(*args, **kwargs): # real signature unknown
    """ Stop a service """
    pass

# classes

class TimeoutAbandoned(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class TimeoutExpired(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000017BE700EF28>'

__spec__ = None # (!) real value is "ModuleSpec(name='psutil._psutil_windows', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000017BE700EF28>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\psutil\\\\_psutil_windows.cp37-win_amd64.pyd')"


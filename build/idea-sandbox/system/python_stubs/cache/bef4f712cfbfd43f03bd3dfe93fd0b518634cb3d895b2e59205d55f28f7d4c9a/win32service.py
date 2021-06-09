# encoding: utf-8
# module win32service
# from C:\Users\Doly\Anaconda3\lib\site-packages\win32\win32service.pyd
# by generator 1.147
# no doc

# imports
from pywintypes import error


# Variables with simple values

DBT_CONFIGCHANGECANCELED = 25
DBT_CONFIGCHANGED = 24
DBT_CUSTOMEVENT = 32774
DBT_DEVICEARRIVAL = 32768
DBT_DEVICEQUERYREMOVE = 32769
DBT_DEVICEQUERYREMOVEFAILED = 32770
DBT_DEVICEREMOVECOMPLETE = 32772
DBT_DEVICEREMOVEPENDING = 32771
DBT_DEVICETYPESPECIFIC = 32773
DBT_QUERYCHANGECONFIG = 23

DF_ALLOWOTHERACCOUNTHOOK = 1

SC_ACTION_NONE = 0
SC_ACTION_REBOOT = 2
SC_ACTION_RESTART = 1

SC_ACTION_RUN_COMMAND = 3

SC_ENUM_PROCESS_INFO = 0

SC_GROUP_IDENTIFIER = 43

SC_MANAGER_ALL_ACCESS = 983103

SC_MANAGER_CONNECT = 1

SC_MANAGER_CREATE_SERVICE = 2

SC_MANAGER_ENUMERATE_SERVICE = 4

SC_MANAGER_LOCK = 8

SC_MANAGER_MODIFY_BOOT_CONFIG = 32

SC_MANAGER_QUERY_LOCK_STATUS = 16

SERVICE_ACCEPT_HARDWAREPROFILECHANGE = 32
SERVICE_ACCEPT_NETBINDCHANGE = 16
SERVICE_ACCEPT_PARAMCHANGE = 8

SERVICE_ACCEPT_PAUSE_CONTINUE = 2

SERVICE_ACCEPT_POWEREVENT = 64
SERVICE_ACCEPT_PRESHUTDOWN = 256
SERVICE_ACCEPT_SESSIONCHANGE = 128
SERVICE_ACCEPT_SHUTDOWN = 4
SERVICE_ACCEPT_STOP = 1

SERVICE_ACTIVE = 1

SERVICE_ALL_ACCESS = 983551

SERVICE_AUTO_START = 2

SERVICE_BOOT_START = 0

SERVICE_CHANGE_CONFIG = 2

SERVICE_CONFIG_DELAYED_AUTO_START_INFO = 3

SERVICE_CONFIG_DESCRIPTION = 1

SERVICE_CONFIG_FAILURE_ACTIONS = 2

SERVICE_CONFIG_FAILURE_ACTIONS_FLAG = 4

SERVICE_CONFIG_PRESHUTDOWN_INFO = 7

SERVICE_CONFIG_REQUIRED_PRIVILEGES_INFO = 6

SERVICE_CONFIG_SERVICE_SID_INFO = 5

SERVICE_CONTINUE_PENDING = 5

SERVICE_CONTROL_CONTINUE = 3
SERVICE_CONTROL_DEVICEEVENT = 11
SERVICE_CONTROL_HARDWAREPROFILECHANGE = 12
SERVICE_CONTROL_INTERROGATE = 4
SERVICE_CONTROL_NETBINDADD = 7
SERVICE_CONTROL_NETBINDDISABLE = 10
SERVICE_CONTROL_NETBINDENABLE = 9
SERVICE_CONTROL_NETBINDREMOVE = 8
SERVICE_CONTROL_PARAMCHANGE = 6
SERVICE_CONTROL_PAUSE = 2
SERVICE_CONTROL_POWEREVENT = 13
SERVICE_CONTROL_PRESHUTDOWN = 15
SERVICE_CONTROL_SESSIONCHANGE = 14
SERVICE_CONTROL_SHUTDOWN = 5
SERVICE_CONTROL_STOP = 1

SERVICE_DEMAND_START = 3

SERVICE_DISABLED = 4
SERVICE_DRIVER = 11

SERVICE_ENUMERATE_DEPENDENTS = 8

SERVICE_ERROR_CRITICAL = 3
SERVICE_ERROR_IGNORE = 0
SERVICE_ERROR_NORMAL = 1
SERVICE_ERROR_SEVERE = 2

SERVICE_FILE_SYSTEM_DRIVER = 2

SERVICE_INACTIVE = 2

SERVICE_INTERACTIVE_PROCESS = 256

SERVICE_INTERROGATE = 128

SERVICE_KERNEL_DRIVER = 1

SERVICE_NO_CHANGE = -1

SERVICE_PAUSED = 7

SERVICE_PAUSE_CONTINUE = 64
SERVICE_PAUSE_PENDING = 6

SERVICE_QUERY_CONFIG = 1
SERVICE_QUERY_STATUS = 4

SERVICE_RUNNING = 4

SERVICE_SID_TYPE_NONE = 0
SERVICE_SID_TYPE_RESTRICTED = 3
SERVICE_SID_TYPE_UNRESTRICTED = 1

SERVICE_SPECIFIC_ERROR = 1066

SERVICE_START = 16

SERVICE_START_PENDING = 2

SERVICE_STATE_ALL = 3

SERVICE_STOP = 32
SERVICE_STOPPED = 1

SERVICE_STOP_PENDING = 3

SERVICE_SYSTEM_START = 1

SERVICE_USER_DEFINED_CONTROL = 256

SERVICE_WIN32 = 48

SERVICE_WIN32_OWN_PROCESS = 16

SERVICE_WIN32_SHARE_PROCESS = 32

UNICODE = 1

UOI_FLAGS = 1
UOI_NAME = 2
UOI_TYPE = 3

UOI_USER_SID = 4

WSF_VISIBLE = 1

# functions

def ChangeServiceConfig(*args, **kwargs): # real signature unknown
    pass

def ChangeServiceConfig2(*args, **kwargs): # real signature unknown
    pass

def CloseServiceHandle(*args, **kwargs): # real signature unknown
    pass

def ControlService(*args, **kwargs): # real signature unknown
    pass

def CreateDesktop(*args, **kwargs): # real signature unknown
    pass

def CreateService(*args, **kwargs): # real signature unknown
    pass

def CreateWindowStation(*args, **kwargs): # real signature unknown
    pass

def DeleteService(*args, **kwargs): # real signature unknown
    pass

def EnumDependentServices(*args, **kwargs): # real signature unknown
    pass

def EnumServicesStatus(*args, **kwargs): # real signature unknown
    pass

def EnumServicesStatusEx(*args, **kwargs): # real signature unknown
    pass

def EnumWindowStations(*args, **kwargs): # real signature unknown
    pass

def GetProcessWindowStation(*args, **kwargs): # real signature unknown
    pass

def GetServiceDisplayName(*args, **kwargs): # real signature unknown
    pass

def GetServiceKeyName(*args, **kwargs): # real signature unknown
    pass

def GetThreadDesktop(*args, **kwargs): # real signature unknown
    pass

def GetUserObjectInformation(*args, **kwargs): # real signature unknown
    pass

def LockServiceDatabase(*args, **kwargs): # real signature unknown
    pass

def OpenDesktop(*args, **kwargs): # real signature unknown
    pass

def OpenInputDesktop(*args, **kwargs): # real signature unknown
    pass

def OpenSCManager(*args, **kwargs): # real signature unknown
    pass

def OpenService(*args, **kwargs): # real signature unknown
    pass

def OpenWindowStation(*args, **kwargs): # real signature unknown
    pass

def QueryServiceConfig(*args, **kwargs): # real signature unknown
    pass

def QueryServiceConfig2(*args, **kwargs): # real signature unknown
    pass

def QueryServiceLockStatus(*args, **kwargs): # real signature unknown
    pass

def QueryServiceObjectSecurity(*args, **kwargs): # real signature unknown
    pass

def QueryServiceStatus(*args, **kwargs): # real signature unknown
    pass

def QueryServiceStatusEx(*args, **kwargs): # real signature unknown
    pass

def SetServiceObjectSecurity(*args, **kwargs): # real signature unknown
    pass

def SetServiceStatus(*args, **kwargs): # real signature unknown
    pass

def SetUserObjectInformation(*args, **kwargs): # real signature unknown
    pass

def StartService(*args, **kwargs): # real signature unknown
    pass

def UnlockServiceDatabase(*args, **kwargs): # real signature unknown
    pass

# classes

class HDESKType(object):
    # no doc
    def CloseDesktop(self, *args, **kwargs): # real signature unknown
        """ Closes the handle """
        pass

    def Detach(self, *args, **kwargs): # real signature unknown
        """ Releases reference to handle without closing it """
        pass

    def EnumDesktopWindows(self, *args, **kwargs): # real signature unknown
        """ Lists all top-level windows on the desktop """
        pass

    def SetThreadDesktop(self, *args, **kwargs): # real signature unknown
        """ Assigns desktop to calling thread """
        pass

    def SwitchDesktop(self, *args, **kwargs): # real signature unknown
        """ Activates the desktop """
        pass

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

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
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

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass


class HWINSTAType(object):
    # no doc
    def CloseWindowStation(self, *args, **kwargs): # real signature unknown
        """ Closes the window station handle """
        pass

    def Detach(self, *args, **kwargs): # real signature unknown
        """ Releases reference to handle without closing it """
        pass

    def EnumDesktops(self, *args, **kwargs): # real signature unknown
        """ List desktop names within the window station """
        pass

    def SetProcessWindowStation(self, *args, **kwargs): # real signature unknown
        """ Associates the calling process with the window station """
        pass

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

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
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

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000014CE92B5630>'

__spec__ = None # (!) real value is "ModuleSpec(name='win32service', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000014CE92B5630>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\win32\\\\win32service.pyd')"


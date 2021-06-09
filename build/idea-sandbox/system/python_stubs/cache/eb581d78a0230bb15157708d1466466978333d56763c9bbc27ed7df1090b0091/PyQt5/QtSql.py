# encoding: utf-8
# module PyQt5.QtSql
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtSql.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtWidgets as __PyQt5_QtWidgets
import sip as __sip


# no functions
# classes

class QSql(__sip.simplewrapper):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AfterLastRow = -2
    AllTables = 255
    BeforeFirstRow = -1
    Binary = 4
    HighPrecision = 0
    In = 1
    InOut = 3
    LowPrecisionDouble = 4
    LowPrecisionInt32 = 1
    LowPrecisionInt64 = 2
    Out = 2
    SystemTables = 2
    Tables = 1
    Views = 4


class QSqlDatabase(__sip.simplewrapper):
    """
    QSqlDatabase()
    QSqlDatabase(QSqlDatabase)
    QSqlDatabase(str)
    QSqlDatabase(QSqlDriver)
    """
    def addDatabase(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addDatabase(str, connectionName: str = '') -> QSqlDatabase
        addDatabase(QSqlDriver, connectionName: str = '') -> QSqlDatabase
        """
        return QSqlDatabase

    def cloneDatabase(self, QSqlDatabase, p_str): # real signature unknown; restored from __doc__
        """ cloneDatabase(QSqlDatabase, str) -> QSqlDatabase """
        return QSqlDatabase

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) """
        pass

    def commit(self): # real signature unknown; restored from __doc__
        """ commit(self) -> bool """
        return False

    def connectionName(self): # real signature unknown; restored from __doc__
        """ connectionName(self) -> str """
        return ""

    def connectionNames(self): # real signature unknown; restored from __doc__
        """ connectionNames() -> List[str] """
        return []

    def connectOptions(self): # real signature unknown; restored from __doc__
        """ connectOptions(self) -> str """
        return ""

    def contains(self, connectionName=''): # real signature unknown; restored from __doc__
        """ contains(connectionName: str = '') -> bool """
        return False

    def database(self, connectionName='', open=True): # real signature unknown; restored from __doc__
        """ database(connectionName: str = '', open: bool = True) -> QSqlDatabase """
        return QSqlDatabase

    def databaseName(self): # real signature unknown; restored from __doc__
        """ databaseName(self) -> str """
        return ""

    def driver(self): # real signature unknown; restored from __doc__
        """ driver(self) -> QSqlDriver """
        return QSqlDriver

    def driverName(self): # real signature unknown; restored from __doc__
        """ driverName(self) -> str """
        return ""

    def drivers(self): # real signature unknown; restored from __doc__
        """ drivers() -> List[str] """
        return []

    def exec(self, query=''): # real signature unknown; restored from __doc__
        """ exec(self, query: str = '') -> QSqlQuery """
        return QSqlQuery

    def exec_(self, query=''): # real signature unknown; restored from __doc__
        """ exec_(self, query: str = '') -> QSqlQuery """
        return QSqlQuery

    def hostName(self): # real signature unknown; restored from __doc__
        """ hostName(self) -> str """
        return ""

    def isDriverAvailable(self, p_str): # real signature unknown; restored from __doc__
        """ isDriverAvailable(str) -> bool """
        return False

    def isOpen(self): # real signature unknown; restored from __doc__
        """ isOpen(self) -> bool """
        return False

    def isOpenError(self): # real signature unknown; restored from __doc__
        """ isOpenError(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def lastError(self): # real signature unknown; restored from __doc__
        """ lastError(self) -> QSqlError """
        return QSqlError

    def numericalPrecisionPolicy(self): # real signature unknown; restored from __doc__
        """ numericalPrecisionPolicy(self) -> QSql.NumericalPrecisionPolicy """
        pass

    def open(self, p_str=None, p_str_1=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        open(self) -> bool
        open(self, str, str) -> bool
        """
        return False

    def password(self): # real signature unknown; restored from __doc__
        """ password(self) -> str """
        return ""

    def port(self): # real signature unknown; restored from __doc__
        """ port(self) -> int """
        return 0

    def primaryIndex(self, p_str): # real signature unknown; restored from __doc__
        """ primaryIndex(self, str) -> QSqlIndex """
        return QSqlIndex

    def record(self, p_str): # real signature unknown; restored from __doc__
        """ record(self, str) -> QSqlRecord """
        return QSqlRecord

    def registerSqlDriver(self, p_str, QSqlDriverCreatorBase): # real signature unknown; restored from __doc__
        """ registerSqlDriver(str, QSqlDriverCreatorBase) """
        pass

    def removeDatabase(self, p_str): # real signature unknown; restored from __doc__
        """ removeDatabase(str) """
        pass

    def rollback(self): # real signature unknown; restored from __doc__
        """ rollback(self) -> bool """
        return False

    def setConnectOptions(self, options=''): # real signature unknown; restored from __doc__
        """ setConnectOptions(self, options: str = '') """
        pass

    def setDatabaseName(self, p_str): # real signature unknown; restored from __doc__
        """ setDatabaseName(self, str) """
        pass

    def setHostName(self, p_str): # real signature unknown; restored from __doc__
        """ setHostName(self, str) """
        pass

    def setNumericalPrecisionPolicy(self, QSql_NumericalPrecisionPolicy): # real signature unknown; restored from __doc__
        """ setNumericalPrecisionPolicy(self, QSql.NumericalPrecisionPolicy) """
        pass

    def setPassword(self, p_str): # real signature unknown; restored from __doc__
        """ setPassword(self, str) """
        pass

    def setPort(self, p_int): # real signature unknown; restored from __doc__
        """ setPort(self, int) """
        pass

    def setUserName(self, p_str): # real signature unknown; restored from __doc__
        """ setUserName(self, str) """
        pass

    def tables(self, type=None): # real signature unknown; restored from __doc__
        """ tables(self, type: QSql.TableType = QSql.Tables) -> List[str] """
        return []

    def transaction(self): # real signature unknown; restored from __doc__
        """ transaction(self) -> bool """
        return False

    def userName(self): # real signature unknown; restored from __doc__
        """ userName(self) -> str """
        return ""

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QSqlDriver(__PyQt5_QtCore.QObject):
    """ QSqlDriver(parent: QObject = None) """
    def beginTransaction(self): # real signature unknown; restored from __doc__
        """ beginTransaction(self) -> bool """
        return False

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) """
        pass

    def commitTransaction(self): # real signature unknown; restored from __doc__
        """ commitTransaction(self) -> bool """
        return False

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def createResult(self): # real signature unknown; restored from __doc__
        """ createResult(self) -> QSqlResult """
        return QSqlResult

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dbmsType(self): # real signature unknown; restored from __doc__
        """ dbmsType(self) -> QSqlDriver.DbmsType """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def escapeIdentifier(self, p_str, QSqlDriver_IdentifierType): # real signature unknown; restored from __doc__
        """ escapeIdentifier(self, str, QSqlDriver.IdentifierType) -> str """
        return ""

    def formatValue(self, QSqlField, trimStrings=False): # real signature unknown; restored from __doc__
        """ formatValue(self, QSqlField, trimStrings: bool = False) -> str """
        return ""

    def handle(self): # real signature unknown; restored from __doc__
        """ handle(self) -> Any """
        pass

    def hasFeature(self, QSqlDriver_DriverFeature): # real signature unknown; restored from __doc__
        """ hasFeature(self, QSqlDriver.DriverFeature) -> bool """
        return False

    def isIdentifierEscaped(self, p_str, QSqlDriver_IdentifierType): # real signature unknown; restored from __doc__
        """ isIdentifierEscaped(self, str, QSqlDriver.IdentifierType) -> bool """
        return False

    def isOpen(self): # real signature unknown; restored from __doc__
        """ isOpen(self) -> bool """
        return False

    def isOpenError(self): # real signature unknown; restored from __doc__
        """ isOpenError(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def lastError(self): # real signature unknown; restored from __doc__
        """ lastError(self) -> QSqlError """
        return QSqlError

    def notification(self, p_str, QSqlDriver_NotificationSource=None, Any=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        notification(self, str) [signal]
        notification(self, str, QSqlDriver.NotificationSource, Any) [signal]
        """
        pass

    def numericalPrecisionPolicy(self): # real signature unknown; restored from __doc__
        """ numericalPrecisionPolicy(self) -> QSql.NumericalPrecisionPolicy """
        pass

    def open(self, p_str, user='', password='', host='', port=-1, options=''): # real signature unknown; restored from __doc__
        """ open(self, str, user: str = '', password: str = '', host: str = '', port: int = -1, options: str = '') -> bool """
        return False

    def primaryIndex(self, p_str): # real signature unknown; restored from __doc__
        """ primaryIndex(self, str) -> QSqlIndex """
        return QSqlIndex

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def record(self, p_str): # real signature unknown; restored from __doc__
        """ record(self, str) -> QSqlRecord """
        return QSqlRecord

    def rollbackTransaction(self): # real signature unknown; restored from __doc__
        """ rollbackTransaction(self) -> bool """
        return False

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setLastError(self, QSqlError): # real signature unknown; restored from __doc__
        """ setLastError(self, QSqlError) """
        pass

    def setNumericalPrecisionPolicy(self, QSql_NumericalPrecisionPolicy): # real signature unknown; restored from __doc__
        """ setNumericalPrecisionPolicy(self, QSql.NumericalPrecisionPolicy) """
        pass

    def setOpen(self, bool): # real signature unknown; restored from __doc__
        """ setOpen(self, bool) """
        pass

    def setOpenError(self, bool): # real signature unknown; restored from __doc__
        """ setOpenError(self, bool) """
        pass

    def sqlStatement(self, QSqlDriver_StatementType, p_str, QSqlRecord, bool): # real signature unknown; restored from __doc__
        """ sqlStatement(self, QSqlDriver.StatementType, str, QSqlRecord, bool) -> str """
        return ""

    def stripDelimiters(self, p_str, QSqlDriver_IdentifierType): # real signature unknown; restored from __doc__
        """ stripDelimiters(self, str, QSqlDriver.IdentifierType) -> str """
        return ""

    def subscribedToNotifications(self): # real signature unknown; restored from __doc__
        """ subscribedToNotifications(self) -> List[str] """
        return []

    def subscribeToNotification(self, p_str): # real signature unknown; restored from __doc__
        """ subscribeToNotification(self, str) -> bool """
        return False

    def tables(self, QSql_TableType): # real signature unknown; restored from __doc__
        """ tables(self, QSql.TableType) -> List[str] """
        return []

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def unsubscribeFromNotification(self, p_str): # real signature unknown; restored from __doc__
        """ unsubscribeFromNotification(self, str) -> bool """
        return False

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    BatchOperations = 8
    BLOB = 2
    DB2 = 8
    DeleteStatement = 4
    EventNotifications = 11
    FieldName = 0
    FinishQuery = 12
    InsertStatement = 3
    Interbase = 7
    LastInsertId = 7
    LowPrecisionNumbers = 10
    MSSqlServer = 1
    MultipleResultSets = 13
    MySqlServer = 2
    NamedPlaceholders = 5
    Oracle = 4
    OtherSource = 2
    PositionalPlaceholders = 6
    PostgreSQL = 3
    PreparedQueries = 4
    QuerySize = 1
    SelectStatement = 1
    SelfSource = 1
    SimpleLocking = 9
    SQLite = 6
    Sybase = 5
    TableName = 1
    Transactions = 0
    Unicode = 3
    UnknownDbms = 0
    UnknownSource = 0
    UpdateStatement = 2
    WhereStatement = 0


class QSqlDriverCreatorBase(__sip.wrapper):
    """
    QSqlDriverCreatorBase()
    QSqlDriverCreatorBase(QSqlDriverCreatorBase)
    """
    def createObject(self): # real signature unknown; restored from __doc__
        """ createObject(self) -> QSqlDriver """
        return QSqlDriver

    def __init__(self, QSqlDriverCreatorBase=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QSqlError(__sip.simplewrapper):
    """
    QSqlError(driverText: str = '', databaseText: str = '', type: QSqlError.ErrorType = QSqlError.NoError, errorCode: str = '')
    QSqlError(str, str, QSqlError.ErrorType, int)
    QSqlError(QSqlError)
    """
    def databaseText(self): # real signature unknown; restored from __doc__
        """ databaseText(self) -> str """
        return ""

    def driverText(self): # real signature unknown; restored from __doc__
        """ driverText(self) -> str """
        return ""

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def nativeErrorCode(self): # real signature unknown; restored from __doc__
        """ nativeErrorCode(self) -> str """
        return ""

    def number(self): # real signature unknown; restored from __doc__
        """ number(self) -> int """
        return 0

    def setDatabaseText(self, p_str): # real signature unknown; restored from __doc__
        """ setDatabaseText(self, str) """
        pass

    def setDriverText(self, p_str): # real signature unknown; restored from __doc__
        """ setDriverText(self, str) """
        pass

    def setNumber(self, p_int): # real signature unknown; restored from __doc__
        """ setNumber(self, int) """
        pass

    def setType(self, QSqlError_ErrorType): # real signature unknown; restored from __doc__
        """ setType(self, QSqlError.ErrorType) """
        pass

    def swap(self, QSqlError): # real signature unknown; restored from __doc__
        """ swap(self, QSqlError) """
        pass

    def text(self): # real signature unknown; restored from __doc__
        """ text(self) -> str """
        return ""

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QSqlError.ErrorType """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    ConnectionError = 1
    NoError = 0
    StatementError = 2
    TransactionError = 3
    UnknownError = 4
    __hash__ = None


class QSqlField(__sip.simplewrapper):
    """
    QSqlField(fieldName: str = '', type: QVariant.Type = QVariant.Invalid)
    QSqlField(str, QVariant.Type, str)
    QSqlField(QSqlField)
    """
    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def defaultValue(self): # real signature unknown; restored from __doc__
        """ defaultValue(self) -> Any """
        pass

    def isAutoValue(self): # real signature unknown; restored from __doc__
        """ isAutoValue(self) -> bool """
        return False

    def isGenerated(self): # real signature unknown; restored from __doc__
        """ isGenerated(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def isReadOnly(self): # real signature unknown; restored from __doc__
        """ isReadOnly(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def length(self): # real signature unknown; restored from __doc__
        """ length(self) -> int """
        return 0

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def precision(self): # real signature unknown; restored from __doc__
        """ precision(self) -> int """
        return 0

    def requiredStatus(self): # real signature unknown; restored from __doc__
        """ requiredStatus(self) -> QSqlField.RequiredStatus """
        pass

    def setAutoValue(self, bool): # real signature unknown; restored from __doc__
        """ setAutoValue(self, bool) """
        pass

    def setDefaultValue(self, Any): # real signature unknown; restored from __doc__
        """ setDefaultValue(self, Any) """
        pass

    def setGenerated(self, bool): # real signature unknown; restored from __doc__
        """ setGenerated(self, bool) """
        pass

    def setLength(self, p_int): # real signature unknown; restored from __doc__
        """ setLength(self, int) """
        pass

    def setName(self, p_str): # real signature unknown; restored from __doc__
        """ setName(self, str) """
        pass

    def setPrecision(self, p_int): # real signature unknown; restored from __doc__
        """ setPrecision(self, int) """
        pass

    def setReadOnly(self, bool): # real signature unknown; restored from __doc__
        """ setReadOnly(self, bool) """
        pass

    def setRequired(self, bool): # real signature unknown; restored from __doc__
        """ setRequired(self, bool) """
        pass

    def setRequiredStatus(self, QSqlField_RequiredStatus): # real signature unknown; restored from __doc__
        """ setRequiredStatus(self, QSqlField.RequiredStatus) """
        pass

    def setSqlType(self, p_int): # real signature unknown; restored from __doc__
        """ setSqlType(self, int) """
        pass

    def setTableName(self, p_str): # real signature unknown; restored from __doc__
        """ setTableName(self, str) """
        pass

    def setType(self, QVariant_Type): # real signature unknown; restored from __doc__
        """ setType(self, QVariant.Type) """
        pass

    def setValue(self, Any): # real signature unknown; restored from __doc__
        """ setValue(self, Any) """
        pass

    def tableName(self): # real signature unknown; restored from __doc__
        """ tableName(self) -> str """
        return ""

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QVariant.Type """
        pass

    def typeID(self): # real signature unknown; restored from __doc__
        """ typeID(self) -> int """
        return 0

    def value(self): # real signature unknown; restored from __doc__
        """ value(self) -> Any """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Optional = 0
    Required = 1
    Unknown = -1
    __hash__ = None


class QSqlRecord(__sip.simplewrapper):
    """
    QSqlRecord()
    QSqlRecord(QSqlRecord)
    """
    def append(self, QSqlField): # real signature unknown; restored from __doc__
        """ append(self, QSqlField) """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def clearValues(self): # real signature unknown; restored from __doc__
        """ clearValues(self) """
        pass

    def contains(self, p_str): # real signature unknown; restored from __doc__
        """ contains(self, str) -> bool """
        return False

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def field(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        field(self, int) -> QSqlField
        field(self, str) -> QSqlField
        """
        return QSqlField

    def fieldName(self, p_int): # real signature unknown; restored from __doc__
        """ fieldName(self, int) -> str """
        return ""

    def indexOf(self, p_str): # real signature unknown; restored from __doc__
        """ indexOf(self, str) -> int """
        return 0

    def insert(self, p_int, QSqlField): # real signature unknown; restored from __doc__
        """ insert(self, int, QSqlField) """
        pass

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isGenerated(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        isGenerated(self, int) -> bool
        isGenerated(self, str) -> bool
        """
        return False

    def isNull(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        isNull(self, int) -> bool
        isNull(self, str) -> bool
        """
        return False

    def keyValues(self, QSqlRecord): # real signature unknown; restored from __doc__
        """ keyValues(self, QSqlRecord) -> QSqlRecord """
        return QSqlRecord

    def remove(self, p_int): # real signature unknown; restored from __doc__
        """ remove(self, int) """
        pass

    def replace(self, p_int, QSqlField): # real signature unknown; restored from __doc__
        """ replace(self, int, QSqlField) """
        pass

    def setGenerated(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setGenerated(self, str, bool)
        setGenerated(self, int, bool)
        """
        pass

    def setNull(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setNull(self, int)
        setNull(self, str)
        """
        pass

    def setValue(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setValue(self, int, Any)
        setValue(self, str, Any)
        """
        pass

    def value(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        value(self, int) -> Any
        value(self, str) -> Any
        """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, QSqlRecord=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __hash__ = None


class QSqlIndex(QSqlRecord):
    """
    QSqlIndex(cursorName: str = '', name: str = '')
    QSqlIndex(QSqlIndex)
    """
    def append(self, QSqlField, bool=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        append(self, QSqlField)
        append(self, QSqlField, bool)
        """
        pass

    def cursorName(self): # real signature unknown; restored from __doc__
        """ cursorName(self) -> str """
        return ""

    def isDescending(self, p_int): # real signature unknown; restored from __doc__
        """ isDescending(self, int) -> bool """
        return False

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def setCursorName(self, p_str): # real signature unknown; restored from __doc__
        """ setCursorName(self, str) """
        pass

    def setDescending(self, p_int, bool): # real signature unknown; restored from __doc__
        """ setDescending(self, int, bool) """
        pass

    def setName(self, p_str): # real signature unknown; restored from __doc__
        """ setName(self, str) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


class QSqlQuery(__sip.simplewrapper):
    """
    QSqlQuery(QSqlResult)
    QSqlQuery(query: str = '', db: QSqlDatabase = QSqlDatabase())
    QSqlQuery(QSqlDatabase)
    QSqlQuery(QSqlQuery)
    """
    def addBindValue(self, Any, type, QSql_ParamType=None, QSql_ParamTypeFlag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ addBindValue(self, Any, type: Union[QSql.ParamType, QSql.ParamTypeFlag] = QSql.In) """
        pass

    def at(self): # real signature unknown; restored from __doc__
        """ at(self) -> int """
        return 0

    def bindValue(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        bindValue(self, str, Any, type: Union[QSql.ParamType, QSql.ParamTypeFlag] = QSql.In)
        bindValue(self, int, Any, type: Union[QSql.ParamType, QSql.ParamTypeFlag] = QSql.In)
        """
        pass

    def boundValue(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        boundValue(self, str) -> Any
        boundValue(self, int) -> Any
        """
        pass

    def boundValues(self): # real signature unknown; restored from __doc__
        """ boundValues(self) -> Dict[str, Any] """
        return {}

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def driver(self): # real signature unknown; restored from __doc__
        """ driver(self) -> QSqlDriver """
        return QSqlDriver

    def exec(self, p_str=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        exec(self, str) -> bool
        exec(self) -> bool
        """
        return False

    def execBatch(self, mode=None): # real signature unknown; restored from __doc__
        """ execBatch(self, mode: QSqlQuery.BatchExecutionMode = QSqlQuery.ValuesAsRows) -> bool """
        return False

    def executedQuery(self): # real signature unknown; restored from __doc__
        """ executedQuery(self) -> str """
        return ""

    def exec_(self, p_str=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        exec_(self, str) -> bool
        exec_(self) -> bool
        """
        return False

    def finish(self): # real signature unknown; restored from __doc__
        """ finish(self) """
        pass

    def first(self): # real signature unknown; restored from __doc__
        """ first(self) -> bool """
        return False

    def isActive(self): # real signature unknown; restored from __doc__
        """ isActive(self) -> bool """
        return False

    def isForwardOnly(self): # real signature unknown; restored from __doc__
        """ isForwardOnly(self) -> bool """
        return False

    def isNull(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        isNull(self, int) -> bool
        isNull(self, str) -> bool
        """
        return False

    def isSelect(self): # real signature unknown; restored from __doc__
        """ isSelect(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def last(self): # real signature unknown; restored from __doc__
        """ last(self) -> bool """
        return False

    def lastError(self): # real signature unknown; restored from __doc__
        """ lastError(self) -> QSqlError """
        return QSqlError

    def lastInsertId(self): # real signature unknown; restored from __doc__
        """ lastInsertId(self) -> Any """
        pass

    def lastQuery(self): # real signature unknown; restored from __doc__
        """ lastQuery(self) -> str """
        return ""

    def next(self): # real signature unknown; restored from __doc__
        """ next(self) -> bool """
        return False

    def nextResult(self): # real signature unknown; restored from __doc__
        """ nextResult(self) -> bool """
        return False

    def numericalPrecisionPolicy(self): # real signature unknown; restored from __doc__
        """ numericalPrecisionPolicy(self) -> QSql.NumericalPrecisionPolicy """
        pass

    def numRowsAffected(self): # real signature unknown; restored from __doc__
        """ numRowsAffected(self) -> int """
        return 0

    def prepare(self, p_str): # real signature unknown; restored from __doc__
        """ prepare(self, str) -> bool """
        return False

    def previous(self): # real signature unknown; restored from __doc__
        """ previous(self) -> bool """
        return False

    def record(self): # real signature unknown; restored from __doc__
        """ record(self) -> QSqlRecord """
        return QSqlRecord

    def result(self): # real signature unknown; restored from __doc__
        """ result(self) -> QSqlResult """
        return QSqlResult

    def seek(self, p_int, relative=False): # real signature unknown; restored from __doc__
        """ seek(self, int, relative: bool = False) -> bool """
        return False

    def setForwardOnly(self, bool): # real signature unknown; restored from __doc__
        """ setForwardOnly(self, bool) """
        pass

    def setNumericalPrecisionPolicy(self, QSql_NumericalPrecisionPolicy): # real signature unknown; restored from __doc__
        """ setNumericalPrecisionPolicy(self, QSql.NumericalPrecisionPolicy) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def value(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        value(self, int) -> Any
        value(self, str) -> Any
        """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    ValuesAsColumns = 1
    ValuesAsRows = 0


class QSqlQueryModel(__PyQt5_QtCore.QAbstractTableModel):
    """ QSqlQueryModel(parent: QObject = None) """
    def beginInsertColumns(self, QModelIndex, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ beginInsertColumns(self, QModelIndex, int, int) """
        pass

    def beginInsertRows(self, QModelIndex, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ beginInsertRows(self, QModelIndex, int, int) """
        pass

    def beginMoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def beginMoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def beginRemoveColumns(self, QModelIndex, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ beginRemoveColumns(self, QModelIndex, int, int) """
        pass

    def beginRemoveRows(self, QModelIndex, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ beginRemoveRows(self, QModelIndex, int, int) """
        pass

    def beginResetModel(self): # real signature unknown; restored from __doc__
        """ beginResetModel(self) """
        pass

    def canFetchMore(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ canFetchMore(self, parent: QModelIndex = QModelIndex()) -> bool """
        pass

    def changePersistentIndex(self, *args, **kwargs): # real signature unknown
        pass

    def changePersistentIndexList(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def columnCount(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ columnCount(self, parent: QModelIndex = QModelIndex()) -> int """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def createIndex(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def data(self, QModelIndex, role=None): # real signature unknown; restored from __doc__
        """ data(self, QModelIndex, role: int = Qt.DisplayRole) -> Any """
        pass

    def decodeData(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def encodeData(self, *args, **kwargs): # real signature unknown
        pass

    def endInsertColumns(self): # real signature unknown; restored from __doc__
        """ endInsertColumns(self) """
        pass

    def endInsertRows(self): # real signature unknown; restored from __doc__
        """ endInsertRows(self) """
        pass

    def endMoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def endMoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def endRemoveColumns(self): # real signature unknown; restored from __doc__
        """ endRemoveColumns(self) """
        pass

    def endRemoveRows(self): # real signature unknown; restored from __doc__
        """ endRemoveRows(self) """
        pass

    def endResetModel(self): # real signature unknown; restored from __doc__
        """ endResetModel(self) """
        pass

    def fetchMore(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ fetchMore(self, parent: QModelIndex = QModelIndex()) """
        pass

    def headerData(self, p_int, Qt_Orientation, role=None): # real signature unknown; restored from __doc__
        """ headerData(self, int, Qt.Orientation, role: int = Qt.DisplayRole) -> Any """
        pass

    def indexInQuery(self, QModelIndex): # real signature unknown; restored from __doc__
        """ indexInQuery(self, QModelIndex) -> QModelIndex """
        pass

    def insertColumns(self, p_int, p_int_1, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ insertColumns(self, int, int, parent: QModelIndex = QModelIndex()) -> bool """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def lastError(self): # real signature unknown; restored from __doc__
        """ lastError(self) -> QSqlError """
        return QSqlError

    def persistentIndexList(self, *args, **kwargs): # real signature unknown
        pass

    def query(self): # real signature unknown; restored from __doc__
        """ query(self) -> QSqlQuery """
        return QSqlQuery

    def queryChange(self): # real signature unknown; restored from __doc__
        """ queryChange(self) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def record(self, p_int=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        record(self, int) -> QSqlRecord
        record(self) -> QSqlRecord
        """
        return QSqlRecord

    def removeColumns(self, p_int, p_int_1, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ removeColumns(self, int, int, parent: QModelIndex = QModelIndex()) -> bool """
        pass

    def resetInternalData(self, *args, **kwargs): # real signature unknown
        pass

    def roleNames(self): # real signature unknown; restored from __doc__
        """ roleNames(self) -> Dict[int, QByteArray] """
        return {}

    def rowCount(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ rowCount(self, parent: QModelIndex = QModelIndex()) -> int """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setHeaderData(self, p_int, Qt_Orientation, Any, role=None): # real signature unknown; restored from __doc__
        """ setHeaderData(self, int, Qt.Orientation, Any, role: int = Qt.EditRole) -> bool """
        return False

    def setLastError(self, QSqlError): # real signature unknown; restored from __doc__
        """ setLastError(self, QSqlError) """
        pass

    def setQuery(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setQuery(self, QSqlQuery)
        setQuery(self, str, db: QSqlDatabase = QSqlDatabase())
        """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


class QSqlRelation(__sip.simplewrapper):
    """
    QSqlRelation()
    QSqlRelation(str, str, str)
    QSqlRelation(QSqlRelation)
    """
    def displayColumn(self): # real signature unknown; restored from __doc__
        """ displayColumn(self) -> str """
        return ""

    def indexColumn(self): # real signature unknown; restored from __doc__
        """ indexColumn(self) -> str """
        return ""

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def swap(self, QSqlRelation): # real signature unknown; restored from __doc__
        """ swap(self, QSqlRelation) """
        pass

    def tableName(self): # real signature unknown; restored from __doc__
        """ tableName(self) -> str """
        return ""

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QSqlRelationalDelegate(__PyQt5_QtWidgets.QItemDelegate):
    """ QSqlRelationalDelegate(parent: QObject = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def createEditor(self, QWidget, QStyleOptionViewItem, QModelIndex): # real signature unknown; restored from __doc__
        """ createEditor(self, QWidget, QStyleOptionViewItem, QModelIndex) -> QWidget """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def drawBackground(self, *args, **kwargs): # real signature unknown
        pass

    def drawCheck(self, *args, **kwargs): # real signature unknown
        pass

    def drawDecoration(self, *args, **kwargs): # real signature unknown
        pass

    def drawDisplay(self, *args, **kwargs): # real signature unknown
        pass

    def drawFocus(self, *args, **kwargs): # real signature unknown
        pass

    def editorEvent(self, *args, **kwargs): # real signature unknown
        pass

    def eventFilter(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setEditorData(self, QWidget, QModelIndex): # real signature unknown; restored from __doc__
        """ setEditorData(self, QWidget, QModelIndex) """
        pass

    def setModelData(self, QWidget, QAbstractItemModel, QModelIndex): # real signature unknown; restored from __doc__
        """ setModelData(self, QWidget, QAbstractItemModel, QModelIndex) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


class QSqlTableModel(QSqlQueryModel):
    """ QSqlTableModel(parent: QObject = None, db: QSqlDatabase = QSqlDatabase()) """
    def beforeDelete(self, p_int): # real signature unknown; restored from __doc__
        """ beforeDelete(self, int) [signal] """
        pass

    def beforeInsert(self, QSqlRecord): # real signature unknown; restored from __doc__
        """ beforeInsert(self, QSqlRecord) [signal] """
        pass

    def beforeUpdate(self, p_int, QSqlRecord): # real signature unknown; restored from __doc__
        """ beforeUpdate(self, int, QSqlRecord) [signal] """
        pass

    def beginInsertColumns(self, *args, **kwargs): # real signature unknown
        pass

    def beginInsertRows(self, *args, **kwargs): # real signature unknown
        pass

    def beginMoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def beginMoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def beginRemoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def beginRemoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def beginResetModel(self, *args, **kwargs): # real signature unknown
        pass

    def changePersistentIndex(self, *args, **kwargs): # real signature unknown
        pass

    def changePersistentIndexList(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def createIndex(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def data(self, QModelIndex, role=None): # real signature unknown; restored from __doc__
        """ data(self, QModelIndex, role: int = Qt.DisplayRole) -> Any """
        pass

    def database(self): # real signature unknown; restored from __doc__
        """ database(self) -> QSqlDatabase """
        return QSqlDatabase

    def decodeData(self, *args, **kwargs): # real signature unknown
        pass

    def deleteRowFromTable(self, p_int): # real signature unknown; restored from __doc__
        """ deleteRowFromTable(self, int) -> bool """
        return False

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def editStrategy(self): # real signature unknown; restored from __doc__
        """ editStrategy(self) -> QSqlTableModel.EditStrategy """
        pass

    def encodeData(self, *args, **kwargs): # real signature unknown
        pass

    def endInsertColumns(self, *args, **kwargs): # real signature unknown
        pass

    def endInsertRows(self, *args, **kwargs): # real signature unknown
        pass

    def endMoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def endMoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def endRemoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def endRemoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def endResetModel(self, *args, **kwargs): # real signature unknown
        pass

    def fieldIndex(self, p_str): # real signature unknown; restored from __doc__
        """ fieldIndex(self, str) -> int """
        return 0

    def filter(self): # real signature unknown; restored from __doc__
        """ filter(self) -> str """
        return ""

    def flags(self, QModelIndex): # real signature unknown; restored from __doc__
        """ flags(self, QModelIndex) -> Qt.ItemFlags """
        pass

    def headerData(self, p_int, Qt_Orientation, role=None): # real signature unknown; restored from __doc__
        """ headerData(self, int, Qt.Orientation, role: int = Qt.DisplayRole) -> Any """
        pass

    def indexInQuery(self, QModelIndex): # real signature unknown; restored from __doc__
        """ indexInQuery(self, QModelIndex) -> QModelIndex """
        pass

    def insertRecord(self, p_int, QSqlRecord): # real signature unknown; restored from __doc__
        """ insertRecord(self, int, QSqlRecord) -> bool """
        return False

    def insertRowIntoTable(self, QSqlRecord): # real signature unknown; restored from __doc__
        """ insertRowIntoTable(self, QSqlRecord) -> bool """
        return False

    def insertRows(self, p_int, p_int_1, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ insertRows(self, int, int, parent: QModelIndex = QModelIndex()) -> bool """
        pass

    def isDirty(self, QModelIndex=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        isDirty(self, QModelIndex) -> bool
        isDirty(self) -> bool
        """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def orderByClause(self): # real signature unknown; restored from __doc__
        """ orderByClause(self) -> str """
        return ""

    def persistentIndexList(self, *args, **kwargs): # real signature unknown
        pass

    def primaryKey(self): # real signature unknown; restored from __doc__
        """ primaryKey(self) -> QSqlIndex """
        return QSqlIndex

    def primaryValues(self, p_int): # real signature unknown; restored from __doc__
        """ primaryValues(self, int) -> QSqlRecord """
        return QSqlRecord

    def primeInsert(self, p_int, QSqlRecord): # real signature unknown; restored from __doc__
        """ primeInsert(self, int, QSqlRecord) [signal] """
        pass

    def queryChange(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def record(self, p_int=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        record(self) -> QSqlRecord
        record(self, int) -> QSqlRecord
        """
        return QSqlRecord

    def removeColumns(self, p_int, p_int_1, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ removeColumns(self, int, int, parent: QModelIndex = QModelIndex()) -> bool """
        pass

    def removeRows(self, p_int, p_int_1, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ removeRows(self, int, int, parent: QModelIndex = QModelIndex()) -> bool """
        pass

    def resetInternalData(self, *args, **kwargs): # real signature unknown
        pass

    def revert(self): # real signature unknown; restored from __doc__
        """ revert(self) """
        pass

    def revertAll(self): # real signature unknown; restored from __doc__
        """ revertAll(self) """
        pass

    def revertRow(self, p_int): # real signature unknown; restored from __doc__
        """ revertRow(self, int) """
        pass

    def rowCount(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ rowCount(self, parent: QModelIndex = QModelIndex()) -> int """
        pass

    def select(self): # real signature unknown; restored from __doc__
        """ select(self) -> bool """
        return False

    def selectRow(self, p_int): # real signature unknown; restored from __doc__
        """ selectRow(self, int) -> bool """
        return False

    def selectStatement(self): # real signature unknown; restored from __doc__
        """ selectStatement(self) -> str """
        return ""

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setData(self, QModelIndex, Any, role=None): # real signature unknown; restored from __doc__
        """ setData(self, QModelIndex, Any, role: int = Qt.EditRole) -> bool """
        return False

    def setEditStrategy(self, QSqlTableModel_EditStrategy): # real signature unknown; restored from __doc__
        """ setEditStrategy(self, QSqlTableModel.EditStrategy) """
        pass

    def setFilter(self, p_str): # real signature unknown; restored from __doc__
        """ setFilter(self, str) """
        pass

    def setLastError(self, *args, **kwargs): # real signature unknown
        pass

    def setPrimaryKey(self, QSqlIndex): # real signature unknown; restored from __doc__
        """ setPrimaryKey(self, QSqlIndex) """
        pass

    def setQuery(self, QSqlQuery): # real signature unknown; restored from __doc__
        """ setQuery(self, QSqlQuery) """
        pass

    def setRecord(self, p_int, QSqlRecord): # real signature unknown; restored from __doc__
        """ setRecord(self, int, QSqlRecord) -> bool """
        return False

    def setSort(self, p_int, Qt_SortOrder): # real signature unknown; restored from __doc__
        """ setSort(self, int, Qt.SortOrder) """
        pass

    def setTable(self, p_str): # real signature unknown; restored from __doc__
        """ setTable(self, str) """
        pass

    def sort(self, p_int, Qt_SortOrder): # real signature unknown; restored from __doc__
        """ sort(self, int, Qt.SortOrder) """
        pass

    def submit(self): # real signature unknown; restored from __doc__
        """ submit(self) -> bool """
        return False

    def submitAll(self): # real signature unknown; restored from __doc__
        """ submitAll(self) -> bool """
        return False

    def tableName(self): # real signature unknown; restored from __doc__
        """ tableName(self) -> str """
        return ""

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateRowInTable(self, p_int, QSqlRecord): # real signature unknown; restored from __doc__
        """ updateRowInTable(self, int, QSqlRecord) -> bool """
        return False

    def __init__(self, parent=None, db=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    OnFieldChange = 0
    OnManualSubmit = 2
    OnRowChange = 1


class QSqlRelationalTableModel(QSqlTableModel):
    """ QSqlRelationalTableModel(parent: QObject = None, db: QSqlDatabase = QSqlDatabase()) """
    def beginInsertColumns(self, *args, **kwargs): # real signature unknown
        pass

    def beginInsertRows(self, *args, **kwargs): # real signature unknown
        pass

    def beginMoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def beginMoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def beginRemoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def beginRemoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def beginResetModel(self, *args, **kwargs): # real signature unknown
        pass

    def changePersistentIndex(self, *args, **kwargs): # real signature unknown
        pass

    def changePersistentIndexList(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def createIndex(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def data(self, QModelIndex, role=None): # real signature unknown; restored from __doc__
        """ data(self, QModelIndex, role: int = Qt.DisplayRole) -> Any """
        pass

    def decodeData(self, *args, **kwargs): # real signature unknown
        pass

    def deleteRowFromTable(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def encodeData(self, *args, **kwargs): # real signature unknown
        pass

    def endInsertColumns(self, *args, **kwargs): # real signature unknown
        pass

    def endInsertRows(self, *args, **kwargs): # real signature unknown
        pass

    def endMoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def endMoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def endRemoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def endRemoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def endResetModel(self, *args, **kwargs): # real signature unknown
        pass

    def indexInQuery(self, *args, **kwargs): # real signature unknown
        pass

    def insertRowIntoTable(self, QSqlRecord): # real signature unknown; restored from __doc__
        """ insertRowIntoTable(self, QSqlRecord) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def orderByClause(self): # real signature unknown; restored from __doc__
        """ orderByClause(self) -> str """
        return ""

    def persistentIndexList(self, *args, **kwargs): # real signature unknown
        pass

    def primaryValues(self, *args, **kwargs): # real signature unknown
        pass

    def queryChange(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def relation(self, p_int): # real signature unknown; restored from __doc__
        """ relation(self, int) -> QSqlRelation """
        return QSqlRelation

    def relationModel(self, p_int): # real signature unknown; restored from __doc__
        """ relationModel(self, int) -> QSqlTableModel """
        return QSqlTableModel

    def removeColumns(self, p_int, p_int_1, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ removeColumns(self, int, int, parent: QModelIndex = QModelIndex()) -> bool """
        pass

    def resetInternalData(self, *args, **kwargs): # real signature unknown
        pass

    def revertRow(self, p_int): # real signature unknown; restored from __doc__
        """ revertRow(self, int) """
        pass

    def select(self): # real signature unknown; restored from __doc__
        """ select(self) -> bool """
        return False

    def selectStatement(self): # real signature unknown; restored from __doc__
        """ selectStatement(self) -> str """
        return ""

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setData(self, QModelIndex, Any, role=None): # real signature unknown; restored from __doc__
        """ setData(self, QModelIndex, Any, role: int = Qt.EditRole) -> bool """
        return False

    def setJoinMode(self, QSqlRelationalTableModel_JoinMode): # real signature unknown; restored from __doc__
        """ setJoinMode(self, QSqlRelationalTableModel.JoinMode) """
        pass

    def setLastError(self, *args, **kwargs): # real signature unknown
        pass

    def setPrimaryKey(self, *args, **kwargs): # real signature unknown
        pass

    def setQuery(self, *args, **kwargs): # real signature unknown
        pass

    def setRelation(self, p_int, QSqlRelation): # real signature unknown; restored from __doc__
        """ setRelation(self, int, QSqlRelation) """
        pass

    def setTable(self, p_str): # real signature unknown; restored from __doc__
        """ setTable(self, str) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateRowInTable(self, p_int, QSqlRecord): # real signature unknown; restored from __doc__
        """ updateRowInTable(self, int, QSqlRecord) -> bool """
        return False

    def __init__(self, parent=None, db=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    InnerJoin = 0
    LeftJoin = 1


class QSqlResult(__sip.wrapper):
    """ QSqlResult(QSqlDriver) """
    def addBindValue(self, Any, Union, QSql_ParamType=None, QSql_ParamTypeFlag=None): # real signature unknown; restored from __doc__
        """ addBindValue(self, Any, Union[QSql.ParamType, QSql.ParamTypeFlag]) """
        pass

    def at(self): # real signature unknown; restored from __doc__
        """ at(self) -> int """
        return 0

    def bindingSyntax(self): # real signature unknown; restored from __doc__
        """ bindingSyntax(self) -> QSqlResult.BindingSyntax """
        pass

    def bindValue(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        bindValue(self, int, Any, Union[QSql.ParamType, QSql.ParamTypeFlag])
        bindValue(self, str, Any, Union[QSql.ParamType, QSql.ParamTypeFlag])
        """
        pass

    def bindValueType(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        bindValueType(self, str) -> QSql.ParamType
        bindValueType(self, int) -> QSql.ParamType
        """
        pass

    def boundValue(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        boundValue(self, str) -> Any
        boundValue(self, int) -> Any
        """
        pass

    def boundValueCount(self): # real signature unknown; restored from __doc__
        """ boundValueCount(self) -> int """
        return 0

    def boundValueName(self, p_int): # real signature unknown; restored from __doc__
        """ boundValueName(self, int) -> str """
        return ""

    def boundValues(self): # real signature unknown; restored from __doc__
        """ boundValues(self) -> List[Any] """
        return []

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def data(self, p_int): # real signature unknown; restored from __doc__
        """ data(self, int) -> Any """
        pass

    def driver(self): # real signature unknown; restored from __doc__
        """ driver(self) -> QSqlDriver """
        return QSqlDriver

    def exec(self): # real signature unknown; restored from __doc__
        """ exec(self) -> bool """
        return False

    def executedQuery(self): # real signature unknown; restored from __doc__
        """ executedQuery(self) -> str """
        return ""

    def exec_(self): # real signature unknown; restored from __doc__
        """ exec_(self) -> bool """
        return False

    def fetch(self, p_int): # real signature unknown; restored from __doc__
        """ fetch(self, int) -> bool """
        return False

    def fetchFirst(self): # real signature unknown; restored from __doc__
        """ fetchFirst(self) -> bool """
        return False

    def fetchLast(self): # real signature unknown; restored from __doc__
        """ fetchLast(self) -> bool """
        return False

    def fetchNext(self): # real signature unknown; restored from __doc__
        """ fetchNext(self) -> bool """
        return False

    def fetchPrevious(self): # real signature unknown; restored from __doc__
        """ fetchPrevious(self) -> bool """
        return False

    def handle(self): # real signature unknown; restored from __doc__
        """ handle(self) -> Any """
        pass

    def hasOutValues(self): # real signature unknown; restored from __doc__
        """ hasOutValues(self) -> bool """
        return False

    def isActive(self): # real signature unknown; restored from __doc__
        """ isActive(self) -> bool """
        return False

    def isForwardOnly(self): # real signature unknown; restored from __doc__
        """ isForwardOnly(self) -> bool """
        return False

    def isNull(self, p_int): # real signature unknown; restored from __doc__
        """ isNull(self, int) -> bool """
        return False

    def isSelect(self): # real signature unknown; restored from __doc__
        """ isSelect(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def lastError(self): # real signature unknown; restored from __doc__
        """ lastError(self) -> QSqlError """
        return QSqlError

    def lastInsertId(self): # real signature unknown; restored from __doc__
        """ lastInsertId(self) -> Any """
        pass

    def lastQuery(self): # real signature unknown; restored from __doc__
        """ lastQuery(self) -> str """
        return ""

    def numRowsAffected(self): # real signature unknown; restored from __doc__
        """ numRowsAffected(self) -> int """
        return 0

    def prepare(self, p_str): # real signature unknown; restored from __doc__
        """ prepare(self, str) -> bool """
        return False

    def record(self): # real signature unknown; restored from __doc__
        """ record(self) -> QSqlRecord """
        return QSqlRecord

    def reset(self, p_str): # real signature unknown; restored from __doc__
        """ reset(self, str) -> bool """
        return False

    def savePrepare(self, p_str): # real signature unknown; restored from __doc__
        """ savePrepare(self, str) -> bool """
        return False

    def setActive(self, bool): # real signature unknown; restored from __doc__
        """ setActive(self, bool) """
        pass

    def setAt(self, p_int): # real signature unknown; restored from __doc__
        """ setAt(self, int) """
        pass

    def setForwardOnly(self, bool): # real signature unknown; restored from __doc__
        """ setForwardOnly(self, bool) """
        pass

    def setLastError(self, QSqlError): # real signature unknown; restored from __doc__
        """ setLastError(self, QSqlError) """
        pass

    def setQuery(self, p_str): # real signature unknown; restored from __doc__
        """ setQuery(self, str) """
        pass

    def setSelect(self, bool): # real signature unknown; restored from __doc__
        """ setSelect(self, bool) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def __init__(self, QSqlDriver): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    NamedBinding = 1
    PositionalBinding = 0


# variables with complex values




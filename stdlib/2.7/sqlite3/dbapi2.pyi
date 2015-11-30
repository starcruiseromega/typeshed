# Stubs for sqlite3.dbapi2 (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

paramstyle = ... # type: Any
threadsafety = ... # type: Any
apilevel = ... # type: Any
Date = ... # type: Any
Time = ... # type: Any
Timestamp = ... # type: Any

def DateFromTicks(ticks): ...
def TimeFromTicks(ticks): ...
def TimestampFromTicks(ticks): ...

version_info = ... # type: Any
sqlite_version_info = ... # type: Any
Binary = ... # type: Any

def register_adapters_and_converters(): ...

# The remaining definitions are imported from _sqlite3.

PARSE_COLNAMES = ... # type: int
PARSE_DECLTYPES = ... # type: int
SQLITE_ALTER_TABLE = ... # type: int
SQLITE_ANALYZE = ... # type: int
SQLITE_ATTACH = ... # type: int
SQLITE_CREATE_INDEX = ... # type: int
SQLITE_CREATE_TABLE = ... # type: int
SQLITE_CREATE_TEMP_INDEX = ... # type: int
SQLITE_CREATE_TEMP_TABLE = ... # type: int
SQLITE_CREATE_TEMP_TRIGGER = ... # type: int
SQLITE_CREATE_TEMP_VIEW = ... # type: int
SQLITE_CREATE_TRIGGER = ... # type: int
SQLITE_CREATE_VIEW = ... # type: int
SQLITE_DELETE = ... # type: int
SQLITE_DENY = ... # type: int
SQLITE_DETACH = ... # type: int
SQLITE_DROP_INDEX = ... # type: int
SQLITE_DROP_TABLE = ... # type: int
SQLITE_DROP_TEMP_INDEX = ... # type: int
SQLITE_DROP_TEMP_TABLE = ... # type: int
SQLITE_DROP_TEMP_TRIGGER = ... # type: int
SQLITE_DROP_TEMP_VIEW = ... # type: int
SQLITE_DROP_TRIGGER = ... # type: int
SQLITE_DROP_VIEW = ... # type: int
SQLITE_IGNORE = ... # type: int
SQLITE_INSERT = ... # type: int
SQLITE_OK = ... # type: int
SQLITE_PRAGMA = ... # type: int
SQLITE_READ = ... # type: int
SQLITE_REINDEX = ... # type: int
SQLITE_SELECT = ... # type: int
SQLITE_TRANSACTION = ... # type: int
SQLITE_UPDATE = ... # type: int
adapters = ... # type: Any
converters = ... # type: Any
sqlite_version = ... # type: str
version = ... # type: str

def adapt(obj, protocol, alternate): ...
def complete_statement(sql): ...
def connect(*args, **kwargs): ...
def enable_callback_tracebacks(flag): ...
def enable_shared_cache(do_enable): ...
def register_adapter(type, callable): ...
def register_converter(typename, callable): ...

class Cache:
    def __init__(self, *args, **kwargs): ...
    def display(self, *args, **kwargs): ...
    def get(self, *args, **kwargs): ...

class Connection:
    DataError = ... # type: Any
    DatabaseError = ... # type: Any
    Error = ... # type: Any
    IntegrityError = ... # type: Any
    InterfaceError = ... # type: Any
    InternalError = ... # type: Any
    NotSupportedError = ... # type: Any
    OperationalError = ... # type: Any
    ProgrammingError = ... # type: Any
    Warning = ... # type: Any
    in_transaction = ... # type: Any
    isolation_level = ... # type: Any
    row_factory = ... # type: Any
    text_factory = ... # type: Any
    total_changes = ... # type: Any
    def __init__(self, *args, **kwargs): ...
    def close(self, *args, **kwargs): ...
    def commit(self, *args, **kwargs): ...
    def create_aggregate(self, *args, **kwargs): ...
    def create_collation(self, *args, **kwargs): ...
    def create_function(self, *args, **kwargs): ...
    def cursor(self, *args, **kwargs): ...
    def execute(self, *args, **kwargs): ...
    def executemany(self, *args, **kwargs): ...
    def executescript(self, *args, **kwargs): ...
    def interrupt(self, *args, **kwargs): ...
    def iterdump(self, *args, **kwargs): ...
    def rollback(self, *args, **kwargs): ...
    def set_authorizer(self, *args, **kwargs): ...
    def set_progress_handler(self, *args, **kwargs): ...
    def set_trace_callback(self, *args, **kwargs): ...
    def __call__(self, *args, **kwargs): ...
    def __enter__(self, *args, **kwargs): ...
    def __exit__(self, *args, **kwargs): ...

class Cursor:
    arraysize = ... # type: Any
    connection = ... # type: Any
    description = ... # type: Any
    lastrowid = ... # type: Any
    row_factory = ... # type: Any
    rowcount = ... # type: Any
    def __init__(self, *args, **kwargs): ...
    def close(self, *args, **kwargs): ...
    def execute(self, *args, **kwargs): ...
    def executemany(self, *args, **kwargs): ...
    def executescript(self, *args, **kwargs): ...
    def fetchall(self, *args, **kwargs): ...
    def fetchmany(self, *args, **kwargs): ...
    def fetchone(self, *args, **kwargs): ...
    def setinputsizes(self, *args, **kwargs): ...
    def setoutputsize(self, *args, **kwargs): ...
    def __iter__(self): ...
    def __next__(self): ...

class DataError(DatabaseError): ...

class DatabaseError(Error): ...

class Error(Exception): ...

class IntegrityError(DatabaseError): ...

class InterfaceError(Error): ...

class InternalError(DatabaseError): ...

class NotSupportedError(DatabaseError): ...

class OperationalError(DatabaseError): ...

class OptimizedUnicode:
    maketrans = ... # type: Any
    def __init__(self, *args, **kwargs): ...
    def capitalize(self, *args, **kwargs): ...
    def casefold(self, *args, **kwargs): ...
    def center(self, *args, **kwargs): ...
    def count(self, *args, **kwargs): ...
    def encode(self, *args, **kwargs): ...
    def endswith(self, *args, **kwargs): ...
    def expandtabs(self, *args, **kwargs): ...
    def find(self, *args, **kwargs): ...
    def format(self, *args, **kwargs): ...
    def format_map(self, *args, **kwargs): ...
    def index(self, *args, **kwargs): ...
    def isalnum(self, *args, **kwargs): ...
    def isalpha(self, *args, **kwargs): ...
    def isdecimal(self, *args, **kwargs): ...
    def isdigit(self, *args, **kwargs): ...
    def isidentifier(self, *args, **kwargs): ...
    def islower(self, *args, **kwargs): ...
    def isnumeric(self, *args, **kwargs): ...
    def isprintable(self, *args, **kwargs): ...
    def isspace(self, *args, **kwargs): ...
    def istitle(self, *args, **kwargs): ...
    def isupper(self, *args, **kwargs): ...
    def join(self, *args, **kwargs): ...
    def ljust(self, *args, **kwargs): ...
    def lower(self, *args, **kwargs): ...
    def lstrip(self, *args, **kwargs): ...
    def partition(self, *args, **kwargs): ...
    def replace(self, *args, **kwargs): ...
    def rfind(self, *args, **kwargs): ...
    def rindex(self, *args, **kwargs): ...
    def rjust(self, *args, **kwargs): ...
    def rpartition(self, *args, **kwargs): ...
    def rsplit(self, *args, **kwargs): ...
    def rstrip(self, *args, **kwargs): ...
    def split(self, *args, **kwargs): ...
    def splitlines(self, *args, **kwargs): ...
    def startswith(self, *args, **kwargs): ...
    def strip(self, *args, **kwargs): ...
    def swapcase(self, *args, **kwargs): ...
    def title(self, *args, **kwargs): ...
    def translate(self, *args, **kwargs): ...
    def upper(self, *args, **kwargs): ...
    def zfill(self, *args, **kwargs): ...
    def __add__(self, other): ...
    def __contains__(self, *args, **kwargs): ...
    def __eq__(self, other): ...
    def __format__(self, *args, **kwargs): ...
    def __ge__(self, other): ...
    def __getitem__(self, index): ...
    def __getnewargs__(self, *args, **kwargs): ...
    def __gt__(self, other): ...
    def __hash__(self): ...
    def __iter__(self): ...
    def __le__(self, other): ...
    def __len__(self, *args, **kwargs): ...
    def __lt__(self, other): ...
    def __mod__(self, other): ...
    def __mul__(self, other): ...
    def __ne__(self, other): ...
    def __rmod__(self, other): ...
    def __rmul__(self, other): ...
    def __sizeof__(self): ...

class PrepareProtocol:
    def __init__(self, *args, **kwargs): ...

class ProgrammingError(DatabaseError): ...

class Row:
    def __init__(self, *args, **kwargs): ...
    def keys(self, *args, **kwargs): ...
    def __eq__(self, other): ...
    def __ge__(self, other): ...
    def __getitem__(self, index): ...
    def __gt__(self, other): ...
    def __hash__(self): ...
    def __iter__(self): ...
    def __le__(self, other): ...
    def __len__(self, *args, **kwargs): ...
    def __lt__(self, other): ...
    def __ne__(self, other): ...

class Statement:
    def __init__(self, *args, **kwargs): ...

class Warning(Exception): ...

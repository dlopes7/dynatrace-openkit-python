from enum import Enum


class DataCollectionLevel(Enum):
    OFF = 0
    PERFORMANCE = 1
    USER_BEHAVIOR = 2


class CrashReportingLevel(Enum):
    OFF = 0
    OPT_OUT_CRASHES = 1
    OPT_IN_CRASHES = 2


DEFAULT_OPERATING_SYSTEM = "Openkit"
DEFAULT_MANUFACTURER = "Dynatrace"
DEFAULT_MODEL_ID = "OpenKitDevice"
DEFAULT_APPLICATION_VERSION = "Unknown version"
DEFAULT_MAX_RECORD_AGE_IN_MILLIS = 105 * 60 * 1000  # 1 hour, 45 minutes
DEFAULT_LOWER_MEMORY_BOUNDARY_IN_BYTES = 80 * 1024 * 1024  # 80 MB
DEFAULT_UPPER_MEMORY_BOUNDARY_IN_BYTES = 100 * 1024 * 1024  # 100 MB
DEFAULT_DATA_COLLECTION_LEVEL = DataCollectionLevel.USER_BEHAVIOR.value
DEFAULT_CRASH_REPORTING_LEVEL = CrashReportingLevel.OPT_IN_CRASHES.value

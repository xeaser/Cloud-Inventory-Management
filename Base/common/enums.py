# Enum class for common access patterns in app
import enum


# Cloud Connector Enum check
class CloudConnectors(enum.Enum):
    aws = 1
    gcp = 2
    azure = 3

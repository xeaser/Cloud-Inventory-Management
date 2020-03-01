from Base.common.enums import CloudConnectors
from aws.getEC2 import getEC2


# common API Wrapper for cloud connectors
def importApi(cloud_connector):
    if CloudConnectors(cloud_connector).value == 1:
        return getEC2()
    return 0

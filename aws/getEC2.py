import boto3

# List all regions
client = boto3.client('ec2')
regions = [region['RegionName'] for region in client.describe_regions()['Regions']]


def getEC2():
    return regions

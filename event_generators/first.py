import json
import sys
from faker import Faker

fake = Faker()

def generate_event_data(num_events):
    events = []
    for _ in range(num_events):
        account_id = fake.random_number(digits=12)
        user_name = fake.user_name()
        arn = f":aws:iam::{account_id}:user/{user_name}"
        
        event_data = {
            "eventVersion": str(fake.random_int(max=9)) + '.' + str(fake.random_int(max=9)),
            "eventTime": fake.date_time_this_decade().isoformat(),
            "eventSource": "ec2.amazonaws.com",
            "eventName": "RunInstances",
            "awsRegion": fake.random_element(elements=('us-east-1', 'us-west-2', 'eu-west-1')),
            "sourceIPAddress": fake.ipv4(),
            "userAgent": fake.user_agent(),
            "requestParameters": {
                "instancesSet": {
                    "items": [
                        {
                            "instanceId": fake.uuid4(),
                            "imageId": fake.uuid4(),
                            "instanceType": fake.random_element(elements=('t2.micro', 'm5.large', 'c5.xlarge')),
                            "keyName": fake.word(),
                            "subnetId": fake.uuid4(),
                            "securityGroupIds": [
                                fake.uuid4(),
                                fake.uuid4()
                            ],
                            "userData": fake.text(),
                            "blockDeviceMappings": [
                                {
                                    "deviceName": "/dev/sda1",
                                    "ebs": {
                                        "volumeId": fake.uuid4(),
                                        "deleteOnTermination": fake.random_element(elements=(True, False))
                                    }
                                }
                            ],
                            "monitoring": {
                                "enabled": fake.random_element(elements=(True, False))
                            },
                            "disableApiTermination": fake.random_element(elements=(True, False)),
                            "instanceInitiatedShutdownBehavior": fake.random_element(elements=('stop', 'terminate')),
                            "tagSet": {
                                "items": [
                                    {
                                        "key": fake.word(),
                                        "value": fake.word()
                                    },
                                    {
                                        "key": fake.word(),
                                        "value": fake.word()
                                    }
                                ]
                            }
                        }
                    ]
                }
            },
            "responseElements": {
                "reservationId": fake.uuid4(),
                "ownerId": fake.random_number(digits=12),
                "instancesSet": {
                    "items": [
                        {
                            "instanceId": fake.uuid4(),
                            "imageId": fake.uuid4(),
                            "instanceType": fake.random_element(elements=('t2.micro', 'm5.large', 'c5.xlarge')),
                            "keyName": fake.word(),
                            "subnetId": fake.uuid4(),
                            "vpcId": fake.uuid4(),
                            "privateIpAddress": fake.ipv4_private(),
                            "securityGroupIds": [
                                fake.uuid4(),
                                fake.uuid4()
                            ],
                            "blockDeviceMappings": [
                                {
                                    "deviceName": "/dev/sda1",
                                    "ebs": {
                                        "volumeId": fake.uuid4(),
                                        "status": fake.random_element(elements=('attached', 'detached'))
                                    }
                                }
                            ],
                            "monitoring": {
                                "state": fake.random_element(elements=('enabled', 'disabled'))
                            },
                            "state": {
                                "code": fake.random_int(min=0, max=16),
                                "name": fake.random_element(elements=('pending', 'running', 'shutting-down', 'terminated'))
                            },
                            "privateDnsName": fake.domain_name(),
                            "dnsName": fake.domain_name(),
                            "reason": fake.sentence(),
                            "keyName": fake.word(),
                            "amiLaunchIndex": fake.random_int(min=0, max=10),
                            "productCodes": [
                                fake.uuid4(),
                                fake.uuid4()
                            ],
                            "instanceType": fake.random_element(elements=('t2.micro', 'm5.large', 'c5.xlarge')),
                            "launchTime": fake.date_time_this_decade().isoformat(),
                            "placement": {
                                "availabilityZone": fake.random_element(elements=('us-east-1a', 'us-west-2b', 'eu-west-1c')),
                                "groupName": fake.word(),
                                "tenancy": fake.random_element(elements=('default', 'dedicated'))
                            },
                            "kernelId": fake.uuid4(),
                            "ramdiskId": fake.uuid4(),
                            "platform": fake.random_element(elements=('windows', 'linux')),
                            "monitoring": {
                                "state": fake.random_element(elements=('enabled', 'disabled'))
                            },
                            "subnetId": fake.uuid4(),
                            "vpcId": fake.uuid4(),
                            "privateIpAddress": fake.ipv4_private(),
                            "architecture": fake.random_element(elements=('i386', 'x86_64')),
                            "rootDeviceType": fake.random_element(elements=('ebs', 'instance-store')),
                            "rootDeviceName": fake.word(),
                            "blockDeviceMappings": [
                                {
                                    "deviceName": "/dev/sda1",
                                    "ebs": {
                                        "volumeId": fake.uuid4(),
                                        "status": fake.random_element(elements=('attached', 'detached'))
                                    }
                                }
                            ],
                            "virtualizationType": fake.random_element(elements=('hvm', 'paravirtual')),
                            "clientToken": fake.uuid4(),
                            "tagSet": {
                                "items": [
                                    {
                                        "key": fake.word(),
                                        "value": fake.word()
                                    },
                                    {
                                        "key": fake.word(),
                                        "value": fake.word()
                                    }
                                ]
                            },
                            "hypervisor": fake.random_element(elements=('xen', 'kvm')),
                            "networkInterfaces": {
                                "items": [
                                    {
                                        "networkInterfaceId": fake.uuid4(),
                                        "subnetId": fake.uuid4(),
                                        "vpcId": fake.uuid4(),
                                        "description": fake.sentence(),
                                        "ownerId": fake.random_number(digits=12),
                                        "status": fake.random_element(elements=('available', 'in-use')),
                                        "macAddress": fake.mac_address(),
                                        "privateIpAddress": fake.ipv4_private(),
                                        "privateDnsName": fake.domain_name(),
                                        "sourceDestCheck": fake.random_element(elements=(True, False)),
                                        "groupSet": {
                                            "items": [
                                                {
                                                    "groupId": fake.uuid4(),
                                                    "groupName": fake.word()
                                                },
                                                {
                                                    "groupId": fake.uuid4(),
                                                    "groupName": fake.word()
                                                }
                                            ]
                                        },
                                        "attachment": {
                                            "attachmentId": fake.uuid4(),
                                            "instanceId": fake.uuid4(),
                                            "instanceOwnerId": fake.random_number(digits=12),
                                            "deviceIndex": fake.random_int(min=0, max=10),
                                            "status": fake.random_element(elements=('attaching', 'attached', 'detaching', 'detached')),
                                            "attachTime": fake.date_time_this_decade().isoformat(),
                                            "deleteOnTermination": fake.random_element(elements=(True, False))
                                        },
                                        "association": {
                                            "publicIp": fake.ipv4_public(),
                                            "publicDnsName": fake.domain_name(),
                                            "ipOwnerId": fake.random_number(digits=12)
                                        }
                                    }
                                ]
                            },
                            "ebsOptimized": fake.random_element(elements=(True, False))
                        }
                    ]
                },
                "reservationId": fake.uuid4(),
                "ownerId": fake.random_number(digits=12)
            },
            "requestID": fake.uuid4(),
            "eventID": fake.uuid4(),
            "readOnly": fake.random_element(elements=(True, False)),
            "resources": [
                {
                    "ARN": arn,
                    "accountId": account_id,
                    "type": "AWS::EC2::Instance",
                    "region": fake.random_element(elements=('us-east-1', 'us-west-2', 'eu-west-1'))
                }
            ],
            "eventType": "AwsApiCall",
            "recipientAccountId": fake.random_number(digits=12)
        }
        
        events.append(event_data)
    
    return events

def save_events_to_json(events):
    with open('event_data.json', 'w') as f:
        json.dump(events, f, indent=4)

if __name__ == "__main__":
    num_events = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    events = generate_event_data(num_events)
    save_events_to_json(events)
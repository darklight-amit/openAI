
from faker import Faker

fake = Faker()

eventVersion = str(fake.random_int(max=9)) + '.' + str(fake.random_int(max=9))
accountId = fake.random_number(digits=12)
userName = fake.user_name()
arn = f':aws:iam::{accountId}:user/{userName}'

event = {
    'eventVersion': eventVersion,
    'userIdentity': {
        'type': 'AssumedRole',
        'principalId': 'AROAQNOKEUJ3RUYUFGIDK:AutoScaling',
        'arn': arn,
        'accountId': accountId,
        'sessionContext': {
            'sessionIssuer': {
                'type': 'Role',
                'principalId': 'AROAQNOKEUJ3RUYUFGIDK',
                'arn': arn,
                'accountId': accountId,
                'userName': userName
            },
            'webIdFederationData': {},
            'attributes': {
                'creationDate': fake.date_time_this_decade().isoformat() + 'Z',
                'mfaAuthenticated': 'false'
            }
        },
        'invokedBy': 'autoscaling.amazonaws.com'
    },
    'eventTime': fake.date_time_this_decade().isoformat() + 'Z',
    'eventSource': 'ec2.amazonaws.com',
    'eventName': 'RunInstances',
    'awsRegion': 'us-west-1',
    'sourceIPAddress': 'autoscaling.amazonaws.com',
    'userAgent': 'autoscaling.amazonaws.com',
    'requestParameters': {
        'instancesSet': {
            'items': [{'minCount': 1, 'maxCount': 1}]
        },
        'blockDeviceMapping': {},
        'availabilityZone': 'us-west-1c',
        'monitoring': {'enabled': False},
        'disableApiTermination': False,
        'disableApiStop': False,
        'clientToken': fake.uuid4(),
        'networkInterfaceSet': {
            'items': [{'deviceIndex': 0, 'subnetId': 'subnet-02ad7658', 'networkCardIndex': 0}]
        },
        'tagSpecificationSet': {
            'items': [
                {
                    'resourceType': 'instance',
                    'tags': [
                        {'key': 'aws:autoscaling:groupName', 'value': 'citris-dev-asg'},
                        {'key': 'Environment', 'value': 'dev-api'},
                        {'key': 'application', 'value': 'web-api'}
                    ]
                }
            ]
        },
        'launchTemplate': {'launchTemplateId': 'lt-05b5fbcee373d73e7', 'version': '2'}
    },
    'responseElements': {
        'requestId': fake.uuid4(),
        'reservationId': fake.uuid4(),
        'ownerId': accountId,
        'groupSet': {},
        'instancesSet': {
            'items': [
                {
                    'instanceId': fake.uuid4(),
                    'imageId': fake.uuid4(),
                    'currentInstanceBootMode': 'legacy-bios',
                    'instanceState': {'code': 0, 'name': 'pending'},
                    'privateDnsName': fake.hostname(),
                    'keyName': 'Citris-ec2-KeyPair',
                    'amiLaunchIndex': 0,
                    'productCodes': {},
                    'instanceType': 'c4.large',
                    'launchTime': fake.date_time_this_decade().timestamp() * 1000,
                    'placement': {'availabilityZone': 'us-west-1c', 'tenancy': 'default'},
                    'monitoring': {'state': 'pending'},
                    'subnetId': 'subnet-02ad7658',
                    'vpcId': 'vpc-2fa47849',
                    'privateIpAddress': fake.ipv4_private(),
                    'stateReason': {'code': 'pending', 'message': 'pending'},
                    'architecture': 'x86_64',
                    'rootDeviceType': 'ebs',
                    'rootDeviceName': '/dev/sda1',
                    'blockDeviceMapping': {},
                    'virtualizationType': 'hvm',
                    'hypervisor': 'xen',
                    'tagSet': {
                        'items': [
                            {'key': 'aws:ec2launchtemplate:id', 'value': 'lt-05b5fbcee373d73e7'},
                            {'key': 'aws:ec2launchtemplate:version', 'value': '2'},
                            {'key': 'aws:autoscaling:groupName', 'value': 'citris-dev-asg'},
                            {'key': 'Name', 'value': 'citris-ec2-dev-api'},
                            {'key': 'application', 'value': 'web-api'},
                            {'key': 'Environment', 'value': 'dev-api'}
                        ]
                    },
                    'clientToken': fake.uuid4(),
                    'groupSet': {
                        'items': [
                            {'groupId': 'sg-040f0c59b92d0a4f4', 'groupName': 'citris_web_api_dev_sg'}
                        ]
                    },
                    'sourceDestCheck': True,
                    'networkInterfaceSet': {
                        'items': [
                            {
                                'networkInterfaceId': fake.uuid4(),
                                'subnetId': 'subnet-02ad7658',
                                'vpcId': 'vpc-2fa47849',
                                'ownerId': accountId,
                                'status': 'in-use',
                                'macAddress': fake.mac_address(),
                                'privateIpAddress': fake.ipv4_private(),
                                'privateDnsName': fake.hostname(),
                                'sourceDestCheck': True,
                                'interfaceType': 'interface',
                                'groupSet': {
                                    'items': [
                                        {'groupId': 'sg-040f0c59b92d0a4f4', 'groupName': 'citris_web_api_dev_sg'}
                                    ]
                                },
                                'attachment': {
                                    'attachmentId': fake.uuid4(),
                                    'deviceIndex': 0,
                                    'networkCardIndex': 0,
                                    'status': 'attaching',
                                    'attachTime': fake.date_time_this_decade().timestamp() * 1000,
                                    'deleteOnTermination': True
                                },
                                'privateIpAddressesSet': {
                                    'item': [
                                        {
                                            'privateIpAddress': fake.ipv4_private(),
                                            'privateDnsName': fake.hostname(),
                                            'primary': True
                                        }
                                    ]
                                },
                                'ipv6AddressesSet': {},
                                'tagSet': {}
                            }
                        ]
                    }
                }
            ]
        },
        'iamInstanceProfile': {
            'arn': f'arn:aws:iam::{accountId}:instance-profile/ec2-codedeploy-service-role-dev',
            'id': fake.uuid4()
        },
        'ebsOptimized': False,
        'enaSupport': True,
        'cpuOptions': {'coreCount': 1, 'threadsPerCore': 2},
        'capacityReservationSpecification': {'capacityReservationPreference': 'open'},
        'enclaveOptions': {'enabled': False},
        'metadataOptions': {
            'state': 'pending',
            'httpTokens': 'required',
            'httpPutResponseHopLimit': 1,
            'httpEndpoint': 'enabled',
            'httpProtocolIpv4': 'enabled',
            'httpProtocolIpv6': 'disabled',
            'instanceMetadataTags': 'enabled'
        },
        'maintenanceOptions': {'autoRecovery': 'default'},
        'privateDnsNameOptions': {
            'hostnameType': 'ip-name',
            'enableResourceNameDnsARecord': False,
            'enableResourceNameDnsAAAARecord': False
        }
    },
    'requesterId': fake.random_number(digits=12),
    'requestID': fake.uuid4(),
    'eventID': fake.uuid4(),
    'readOnly': False,
    'eventType': 'AwsApiCall',
    'managementEvent': True,
    'recipientAccountId': accountId,
    'eventCategory': 'Management'
}

print(event)

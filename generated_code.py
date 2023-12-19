
from faker import Faker

fake = Faker()

eventVersion = str(fake.random_int(max=9)) + '.' + str(fake.random_int(max=9))
accountId = fake.random_number(digits=12)
userName = fake.user_name()
arn = f':aws:iam::{accountId}:user/{userName}'

eventTime = fake.iso8601()
eventSource = fake.word()
eventName = fake.word()
awsRegion = fake.word()
random_ip = fake.ipv4()
userAgent = fake.user_agent()
domainName = fake.domain_name()
validationMethod = fake.word()
subjectAlternativeNames = [fake.domain_name()]
idempotencyToken = fake.uuid4()
tags = [{'key': fake.word(), 'value': fake.word()}]
certificateArn = fake.uuid4()
requestID = fake.uuid4()
eventID = fake.uuid4()

event = {
    'eventVersion': eventVersion,
    'userIdentity': {
        'type': 'IAMUser',
        'principalId': fake.random_number(digits=20),
        'arn': arn,
        'accountId': accountId,
        'accessKeyId': fake.uuid4(),
        'userName': userName
    },
    'eventTime': eventTime,
    'eventSource': eventSource,
    'eventName': eventName,
    'awsRegion': awsRegion,
    'random_ip': random_ip,
    'userAgent': userAgent,
    'requestParameters': {
        'domainName': domainName,
        'validationMethod': validationMethod,
        'subjectAlternativeNames': subjectAlternativeNames,
        'idempotencyToken': idempotencyToken,
        'tags': tags
    },
    'responseElements': {
        'certificateArn': certificateArn
    },
    'requestID': requestID,
    'eventID': eventID,
    'readOnly': False,
    'eventType': 'AwsApiCall',
    'managementEvent': True,
    'recipientAccountId': accountId,
    'eventCategory': 'Management',
    'tlsDetails': {
        'tlsVersion': 'TLSv1.3',
        'cipherSuite': 'TLS_AES_128_GCM_SHA256',
        'clientProvidedHostHeader': fake.domain_name()
    }
}

print(event)

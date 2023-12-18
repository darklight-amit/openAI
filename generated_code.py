
from faker import Faker

fake = Faker()

data = {
    'eventVersion': str(fake.random_int(max=9)) + '.' + str(fake.random_int(max=9)),
    'userIdentity': {
        'type': fake.word(),
        'principalId': fake.word(),
        'arn': 'arn:aws:iam::' + fake.random_number(digits=12) + ':user/' + fake.user_name(),
        'accountId': fake.random_number(digits=12),
        'accessKeyId': fake.random_number(digits=20),
        'userName': fake.user_name()
    },
    'eventTime': fake.iso8601(),
    'eventSource': fake.word(),
    'eventName': fake.word(),
    'awsRegion': fake.word(),
    'random_ip': fake.ipv4(),
    'userAgent': fake.user_agent(),
    'requestParameters': {
        'domainName': fake.domain_name(),
        'validationMethod': fake.word(),
        'subjectAlternativeNames': [fake.domain_name()],
        'idempotencyToken': 'tf' + fake.iso8601().replace('-', '').replace(':', '').replace('.', '') + fake.random_number(digits=8),
        'tags': [{'key': fake.word(), 'value': fake.word()}, {'key': fake.word(), 'value': fake.word()}]
    },
    'responseElements': {
        'certificateArn': 'arn:aws:acm:' + fake.word() + ':' + fake.random_number(digits=12) + ':certificate/' + fake.uuid4()
    },
    'requestID': fake.uuid4(),
    'eventID': fake.uuid4(),
    'readOnly': fake.boolean(),
    'eventType': fake.word(),
    'managementEvent': fake.boolean(),
    'recipientAccountId': fake.random_number(digits=12),
    'eventCategory': fake.word(),
    'tlsDetails': {
        'tlsVersion': fake.word(),
        'cipherSuite': fake.word(),
        'clientProvidedHostHeader': fake.domain_name()
    }
}

print(data)

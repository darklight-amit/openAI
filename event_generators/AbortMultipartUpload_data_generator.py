
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
            "eventSource": "s3.amazonaws.com",
            "eventName": "AbortMultipartUpload",
            "awsRegion": fake.random_element(elements=('us-east-1', 'us-west-2', 'eu-west-1')),
            "sourceIPAddress": fake.ipv4(),
            "userAgent": fake.user_agent(),
            "requestParameters": {
                "bucketName": fake.word(),
                "key": fake.file_path(depth=fake.random_int(min=1, max=5)),
                "uploadId": fake.uuid4()
            },
            "responseElements": {},
            "s3": {
                "s3SchemaVersion": "1.0",
                "configurationId": fake.uuid4(),
                "bucket": {
                    "name": fake.word(),
                    "ownerIdentity": {
                        "principalId": fake.uuid4()
                    },
                    "arn": f"arn:aws:s3:::{fake.word()}"
                },
                "object": {
                    "key": fake.file_path(depth=fake.random_int(min=1, max=5)),
                    "size": fake.random_int(min=1, max=1000000),
                    "eTag": fake.uuid4(),
                    "versionId": fake.uuid4(),
                    "sequencer": fake.uuid4()
                }
            },
            "userIdentity": {
                "type": "IAMUser",
                "principalId": fake.uuid4(),
                "arn": arn,
                "accountId": account_id,
                "accessKeyId": fake.uuid4(),
                "userName": user_name
            },
            "eventID": fake.uuid4(),
            "eventType": "AwsApiCall",
            "recipientAccountId": fake.random_number(digits=12),
            "eventCategory": "Management",
            "apiVersion": "2006-03-01",
            "readOnly": fake.random_element(elements=(True, False)),
            "managementEvent": True,
            "eventData": {
                "apiVersion": "2006-03-01",
                "requestId": fake.uuid4()
            }
        }
        
        events.append(event_data)
    
    return events

def save_event_data(events):
    with open("AbortMultipartUpload_data.json", "w") as file:
        json.dump(events, file, indent=4)

if __name__ == "__main__":
    num_events = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    events = generate_event_data(num_events)
    save_event_data(events)

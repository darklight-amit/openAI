
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
            "eventTime": fake.date_time().isoformat(),
            "eventSource": "aws:s3",
            "eventName": "AbortVaultLock",
            "awsRegion": fake.random_element(elements=('us-east-1', 'us-west-2', 'eu-west-1')),
            "sourceIPAddress": fake.ipv4(),
            "userAgent": fake.user_agent(),
            "requestParameters": {
                "vaultName": fake.word()
            },
            "responseElements": {},
            "additionalEventData": {
                "accountId": account_id,
                "userName": user_name,
                "arn": arn
            },
            "eventID": fake.uuid4(),
            "eventType": "AwsApiCall",
            "recipientAccountId": fake.random_number(digits=12),
            "eventCategory": "Management",
            "apiVersion": "2012-06-01",
            "readOnly": False,
            "managementEvent": True,
            "eventData": {
                "accountId": account_id,
                "userName": user_name,
                "arn": arn
            }
        }
        events.append(event_data)
    
    return events

if __name__ == "__main__":
    num_events = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    event_data = generate_event_data(num_events)
    
    with open("AbortVaultLock_data.json", "w") as outfile:
        json.dump(event_data, outfile, indent=4)

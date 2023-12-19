
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
            "eventSource": "elasticbeanstalk.amazonaws.com",
            "eventName": "AbortEnvironmentUpdate",
            "awsRegion": fake.random_element(elements=('us-east-1', 'us-west-2', 'eu-west-1')),
            "sourceIPAddress": fake.ipv4(),
            "userAgent": fake.user_agent(),
            "requestParameters": {
                "arn": arn
            },
            "responseElements": {},
            "requestID": fake.uuid4(),
            "eventID": fake.uuid4(),
            "readOnly": False,
            "resources": [
                {
                    "arn": arn,
                    "accountId": account_id,
                    "type": "AWS::IAM::User"
                }
            ],
            "eventType": "AwsApiCall",
            "managementEvent": True,
            "recipientAccountId": fake.random_number(digits=12),
            "eventCategory": "Management",
            "eventSourceARN": arn,
            "userIdentity": {
                "type": "IAMUser",
                "principalId": fake.random_number(digits=21),
                "arn": arn,
                "accountId": account_id,
                "accessKeyId": fake.random_number(digits=20),
                "userName": user_name,
                "sessionContext": {
                    "attributes": {
                        "mfaAuthenticated": "false",
                        "creationDate": fake.date_time().isoformat()
                    }
                }
            }
        }
        events.append(event_data)
    
    with open("AbortEnvironmentUpdate_data.json", "w") as outfile:
        json.dump(events, outfile, indent=4)

if __name__ == "__main__":
    num_events = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    generate_event_data(num_events)


import json
import sys
from faker import Faker

fake = Faker()

def generate_accept_account_mapping_event(num_events=1):
    events = []
    for _ in range(num_events):
        account_id = fake.random_number(digits=12)
        user_name = fake.user_name()
        arn = f":aws:iam::{account_id}:user/{user_name}"
        
        event = {
            "eventVersion": f"{fake.random_int(max=9)}.{fake.random_int(max=9)}",
            "eventTime": fake.date_time().isoformat(),
            "eventSource": "cloudtrail.amazonaws.com",
            "eventName": "AcceptAccountMapping",
            "awsRegion": fake.random_element(["us-east-1", "us-west-2", "eu-west-1"]),
            "sourceIPAddress": fake.ipv4(),
            "userAgent": fake.user_agent(),
            "requestParameters": {
                "accountIds": [account_id],
                "operationType": fake.random_element(["CREATE", "UPDATE", "DELETE"]),
                "sendEmail": fake.random_element([True, False])
            },
            "responseElements": {
                "createAccountStatus": {
                    "id": fake.random_number(digits=12),
                    "accountName": fake.company(),
                    "state": fake.random_element(["SUCCEEDED", "FAILED"]),
                    "requestedTimestamp": fake.date_time().isoformat(),
                    "completedTimestamp": fake.date_time().isoformat()
                }
            },
            "requestID": fake.uuid4(),
            "eventID": fake.uuid4(),
            "readOnly": fake.random_element([True, False]),
            "resources": [
                {
                    "ARN": arn,
                    "accountId": account_id,
                    "userName": user_name
                }
            ],
            "eventType": "AwsApiCall",
            "recipientAccountId": fake.random_number(digits=12),
            "eventCategory": "Management",
            "additionalEventData": {
                "MFAUsed": fake.random_element([True, False]),
                "MobileVersion": fake.random_element(["iOS", "Android"]),
                "ConsoleLogin": fake.random_element([True, False])
            }
        }
        events.append(event)
    
    with open("AcceptAccountMapping_data.json", "w") as f:
        json.dump(events, f, indent=4)

if __name__ == "__main__":
    num_events = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    generate_accept_account_mapping_event(num_events)

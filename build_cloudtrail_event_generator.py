from openai import OpenAI
import json
import re

client = OpenAI(api_key="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")


completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "generate python code using faker for event data generation for RunInstances cloud trail event \
        and include all the optional fields as well and code should take one int parameter as command line argument to decide how many events needs to ge generated, default is 1,\
        code should save the output in .json file\
        first generate <accountID> and <userName> and then build the fake arn using below rule\
        arn = ':aws:iam::<accountId>:user/<userName>'. \
        Each and every element should have fake data. \
        to generate random data for eventVersion call str(fake.random_int(max=9))+'.'+(fake.random_int(max=9)) \
        convert  fake.random_number() into str to build the arn field. \
        and code should be enclosed between ```"  }
    ],
    temperature=0.0
)

generated_text = completion.choices[0].message.content
print(generated_text)
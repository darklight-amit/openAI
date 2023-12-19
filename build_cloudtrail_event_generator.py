from openai import OpenAI
import json
import re

client = OpenAI(api_key="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")

def openai_code_generator(event_name):

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"generate python code using faker for event data generation for {event_name} cloud trail event \
            and include all the optional fields as well and code should take one int parameter as command line argument to decide how many events needs to ge generated, default is 1,\
            code should save the output in {event_name}_data.json file\
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
    start_string = "```python"
    end_string = "```"

    pattern = re.compile(re.escape(start_string) + r"(.*?)" + re.escape(end_string), re.DOTALL) 
    match = re.search(pattern, generated_text) 
    generated_code = match.group(1)
    generated_code = generated_code.replace('random_string', 'password')

    # Specify the file path where you want to save the generated code file_path = "generated_code.py"

    # Write the generated code to the file
    file_path = f'./event_generators/{event_name}_data_generator.py'
    with open(file_path, "w") as file:
        file.write(generated_code)

    print(f"Generated code saved to {file_path}") 

if __name__ == "__main__":
    with open('cloud_trail_events_name.txt','r') as f:
        count = 1
        for even_name in f.readlines():
            if count > 5:
                break
            openai_code_generator(even_name.strip())
            count += 1
            
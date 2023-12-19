from openai import OpenAI
import json
import re

client = OpenAI(api_key="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")

with open('input.json', 'r') as f:
    json_data = json.load(f)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": f"take this as input {json_data}, generate python code to \
            generate fake data for each and every field. \
            first generate <accountID> and <userName> and then build the fake arn using below rule\
            arn = ':aws:iam::<accountId>:user/<userName>'. \
            Each and every element should have fake data. \
            to generate random data for eventVersion call str(fake.random_int(max=9))+'.'+(fake.random_int(max=9)) \
            convert  fake.random_number() into str to build the arn field. \
            and code should be enclosed between ```   "}
    ],
    temperature=0.0
)

generated_text = completion.choices[0].message.content
print(generated_text)
start_string = "```python"
end_string = "```"

pattern = re.compile(re.escape(start_string) + r"(.*?)" + re.escape(end_string), re.DOTALL) 
match = re.search(pattern, generated_text) 
generated_code = match.group(1)
generated_code = generated_code.replace('random_string', 'password')

# Specify the file path where you want to save the generated code file_path = "generated_code.py"

# Write the generated code to the file
file_path = 'generated_code.py'
with open(file_path, "w") as file:
    file.write(generated_code)

print(f"Generated code saved to {file_path}") 

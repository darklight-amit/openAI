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
            generate fake data for each and every field. In the data 'arn' field has format of 'arn:aws:iam::<accountId>:user/<userName>' \
            accountid and username should be same as arn field. Each and every element should have fake data. \
            to generate random data for eventVersion call str(fake.random_int(max=9))+'.'+(fake.random_int(max=9)) \
            convert fake.random_number() sinto str concatanation with string  \
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

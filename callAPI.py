from openai import OpenAI
import json
import re

client = OpenAI()

with open('input.json', 'r') as f:
    json_data = json.load(f)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": f"take this as input {json_data}, generate python code to \
            generate fake data for each and every field. In the data 'arn' field has format of 'arn:aws:iam::<accountId>:user/<userName>' \
            accountid and username should be same as arn field. Each and every element should have fake data. Don't use any funcion with random* and enclosed the code between ```   "}
    ],
    temperature=0.0
)

generated_text = completion.choices[0].message.content
print(generated_text)
start_string = "```python"
end_string = "```"

pattern = re.compile(re.escape(start_string) + r"(.*?)" + re.escape(end_string), re.DOTALL) match = re.search(pattern, generated_text) generated_code = match.group(1)

# Specify the file path where you want to save the generated code file_path = "generated_code.py"

# Write the generated code to the file
with open(file_path, "w") as file:
    file.write(generated_code)

print(f"Generated code saved to {file_path}") 

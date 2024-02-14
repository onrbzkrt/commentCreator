# Importing necessary module
from openai import OpenAI

# Defining API key for OpenAI
api_key = ""

# Creating a client object for OpenAI with the API key
client = OpenAI(api_key=api_key)

# Initializing an empty list to store product names
products = []

# Asking the user to input the names of 3 products and storing them in the 'products' list
for i in range(1, 4):
    products.append(input("Please enter product " + str(i) + " name:"))

# Converting the list of product names into a comma-separated string
strProducts = ", ".join(map(str, products))

# Generating a response from the OpenAI chat model
response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=[
        {
            "role": "system",
            "content": "You are a review creator and will create exactly 5 reviews for the following products. Your reviews will have a star rating from 1 to 5 and no more than 50 characters. Also, the JSON file will include the reviewer's full name.\n\nFormat: JSON"
        },
        {
            "role": "user",
            "content": "The products are " + strProducts
        }
    ],
    temperature=1.36,
    max_tokens=1109,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

# Extracting the content of the response
resFinal = response.choices[0].message.content

# Writing the final response to an output JSON file
with open("output.json", "w") as json_File:
    json_File.write(resFinal)

# Printing a message indicating completion of the program
print("That's all!!")

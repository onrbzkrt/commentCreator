# OpenAI Chat Model for Product Reviews

This Python script utilizes the OpenAI chat model to generate product reviews for given products. It prompts the user to input the names of three products and then generates five reviews for each product.

## Prerequisites

- Python 3.x
- OpenAI API key

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/onrbzkrt/commentCreator.git
    ```

2. Install the required Python packages:

    ```bash
    pip install openai
    ```

3. Replace `api_key` with your OpenAI API key.

## Usage

1. Run the script:

    ```bash
    python product_reviews.py
    ```

2. Enter the names of three products when prompted.

3. The script will generate reviews for each product and save them in an output JSON file named `output.json`.

4. Check the `output.json` file for the generated reviews.

## Parameters

- `model`: Specifies the OpenAI model to use. (Default: `gpt-3.5-turbo-0125`)
- `temperature`: Controls the randomness of the model's predictions. (Default: `1.36`)
- `max_tokens`: Specifies the maximum number of tokens (words) in the generated response. (Default: `1109`)
- `top_p`: Controls the model's likelihood to select the next token. (Default: `1`)
- `frequency_penalty` and `presence_penalty`: Adjusts the penalty applied to tokens based on their frequency and presence in the context. (Default: `0`)

## Output

The output JSON file (`output.json`) contains the generated reviews in the following format:

```json
[
    {
        "product": "Product Name",
        "reviews": [
            {
                "rating": 5,
                "review_text": "Great product!"
            },
            {
                "rating": 4,
                "review_text": "Good quality."
            },
            ...
        ]
    },
    ...
]

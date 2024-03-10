# RECIPES-DATASET

# Recipe Dataset

## Introduction

In this dataset, we provide recipes for various dishes, including raw data and a decomposed version suitable for use with ChatGPT. Each entry includes the recipe name, raw data containing ingredients and instructions, and a decomposed JSON-like structure for ChatGPT. The decomposed data includes the name, URL (if available), ingredients, instructions, and additional notes.

## Use Case

The dataset is suitable for training and testing natural language processing models, especially those involved in recipe analysis, summarization, or understanding. It can be utilized for tasks such as:

1. **Recipe Summarization:** Generating concise summaries of recipes based on raw data or decomposed JSON.

2. **Chatbot Training:** Training chatbots to understand and respond to user queries related to cooking or recipe-specific inquiries.

3. **Structured Data Processing:** Utilizing decomposed JSON data for training models to extract structured information from unstructured text.

4. **Recipe Recommendation Systems:** Developing systems that recommend recipes based on user preferences or dietary restrictions.

## Example

### Recipe: Grilled Chicken Tikka Boti Kebab

#### Raw Data
```plaintext
"You can make the recipe [HERE](https://dobbernationloves.com/food-drink/pakistani-chicken-tikka-boti-kebab-recipe/)!
...
Serve hot sprinkled with lemon juice alongside steamed rice or flatbreads like naan, roti or parathas."


**Decomposed Data:**
```json
{
    "name": "Grilled Chicken Tikka Boti Kebab",
    "url": "https://dobbernationloves.com/food-drink/pakistani-chicken-tikka-boti-kebab-recipe/",
    "ingredients": {
        "chicken": "1 kg Skinless Boneless Chicken Thighs cut into bite-sized pieces",
        "marinade": [
            "1/4 cup Greek Yogurt",
            "2 tsp Gram Chickpea Flour",
            ...
        ]
    },
    "instructions": [
        "Mix the yogurt with the gram flour in a bowl to get rid of any lumps...",
        "Soak wooden skewers in water. Preheat the grill to medium...",
        "Serve hot sprinkled with lemon juice alongside steamed rice or flatbreads like naan, roti or parathas."
    ],
    "note": null
}

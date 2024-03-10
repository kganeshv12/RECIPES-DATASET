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

### Recipe: Barbecued Miso Butter Corn on the Cob

#### Raw Data
```plaintext
Barbecued Miso Butter Corn on the Cob	"You can make the recipe [HERE](https://dobbernationloves.com/food-drink/miso-butter-corn-on-the-cob-recipe/).

*Ingredients*

* 4 Corn on the cob

*Miso Chive Butter*

* 60 g Butter diced
* 2 tbsp Miso Paste
* 10 g Fresh Chives finely chopped
* 2 tsp Maple Syrup
* 1 tbsp Lemon Juice

*Instructions*

1. Leave the butter out of the fridge to soften. Preheat your barbecue grill to 460F or its highest setting.
2. In a small bowl, mix the butter to loosen it, then stir in the miso paste and chives with a rubber spatula.
3. Put the corn on the barbecue and grill for 5 minutes, turning a couple of times until evenly charred.
4. Schmear the hot corn with miso butter and drizzle with maple syrup and lemon juice before serving."
}
```

### JSON Formatted
```JSON
{
  "name": "Barbecued Miso Butter Corn on the Cob",
  "url": "https://dobbernationloves.com/food-drink/miso-butter-corn-on-the-cob-recipe/",
  "ingredients": {
    "corn": "4 Corn on the cob",
    "miso_chive_butter": [
      "60 g Butter diced",
      "2 tbsp Miso Paste",
      "10 g Fresh Chives finely chopped",
      "2 tsp Maple Syrup",
      "1 tbsp Lemon Juice"
    ]
  },
  "instructions": [
    "Leave the butter out of the fridge to soften. Preheat your barbecue grill to 460F or its highest setting.",
    "In a small bowl, mix the butter to loosen it, then stir in the miso paste and chives with a rubber spatula.",
    "Put the corn on the barbecue and grill for 5 minutes, turning a couple of times until evenly charred.",
    "Schmear the hot corn with miso butter and drizzle with maple syrup and lemon juice before serving."
  ],
  "note": null
}
```


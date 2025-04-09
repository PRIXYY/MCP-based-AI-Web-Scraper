# AI-Powered Web Scraping with BrowserUse

This repository contains an autonomous web scraping solution powered by BrowserUse and AI models. The implementation allows for automated browser interaction and data extraction without writing extensive DOM manipulation code.

## Overview

This project demonstrates how to:
- Use BrowserUse as a browser automation agent
- Leverage AI models (Gemini by default) to interpret webpage content
- Extract data from websites autonomously
- Perform complex web tasks using natural language instructions

## Features

- **AI-Powered Automation**: Uses AI models to understand web page structure and content
- **Flexible Model Support**: Works with Gemini by default, but can be configured to use other models
- **Simple Natural Language Commands**: Control web scraping through plain English instructions
- **Dynamic Web Navigation**: Handle pagination, form submission, and complex interactions
- **Customizable Data Extraction**: Extract specific data points based on your requirements

## Installation

### Prerequisites
- Python 3.8+
- Git

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   
   On Windows:
   ```bash
   venv\Scripts\activate
   ```
   
   On macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Create a .env file**
   Create a file named `.env` in the root directory of the project and add your API key:
   ```
   GEMINI_API_KEY=Your_API_Key_Here
   ```

## Usage

1. **Run the script**
   ```bash
   python main.py
   ```

2. **Modify the script**
   
   The main script contains examples of web scraping tasks. You can modify these to match your specific use case.

## Using Different AI Models

By default, the project is configured to use Google's Gemini. To use alternative AI models, refer to the [BrowserUse documentation on supported models](https://docs.browser-use.com/customize/supported-models).

To change the model, you'll need to:

1. Add the appropriate API key to your `.env` file
2. Update your code to use the desired model

For example, to use OpenAI:
```python
import os
from browser_use import Browser
from dotenv import load_dotenv

load_dotenv()

browser = Browser(
    model="openai",
    api_key=os.getenv("OPENAI_API_KEY")
)
```

## Key Components

The project consists of several key components based on the tutorial video:

1. **Browser Initialization**: Setting up the BrowserUse agent with the appropriate AI model
2. **Task Definition**: Specifying what data needs to be scraped
3. **Browser Navigation**: Instructions for browsing to specific pages
4. **Data Extraction**: Logic for retrieving and processing the target information
5. **Data Storage**: Saving the extracted data in a structured format

## Example

Here's a simple example of how to use the framework to scrape product information:

```python
import os
from browser_use import Browser
from dotenv import load_dotenv

load_dotenv()

browser = Browser(
    model="gemini",
    api_key=os.getenv("GEMINI_API_KEY")
)

# Navigate to a product page
browser.go("https://example.com/products")

# Extract product information
products = browser.run("""
    1. Find all product items on the page
    2. For each product, extract:
       - Product name
       - Price
       - Rating (if available)
       - Description
    3. Return the data as a list of dictionaries
""")

print(products)
```

## Browser Integration

This project uses ChromeDriver to control your Chrome browser for web automation. BrowserUse leverages this browser integration to:
- Open Chrome browser instances
- Navigate to specified URLs
- Interact with web elements
- Execute JavaScript
- Handle cookies and sessions
- Take screenshots
- Perform complex browser interactions

ChromeDriver works behind the scenes to enable seamless browser control, allowing the AI agent to interact with websites just like a human user would. The BrowserUse framework handles the technical details of browser communication, letting you focus on defining the scraping tasks using natural language.

Make sure you have Chrome installed on your system for the automation to work properly. The appropriate ChromeDriver version will be automatically managed by the BrowserUse library.

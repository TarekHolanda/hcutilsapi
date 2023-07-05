import slack_sdk
# import webbrowser
# from selenium import webdriver

# Set the Slack API token and channel ID
SLACK_API_TOKEN = "xoxb-4675665590-463342022754-OxxrSxGjGKbjiJNZsbgCtwPP"
# SLACK_API_TOKEN = "xoxb-4675665590-5481631721604-Yy8NilUCmRhIVRzaktpaFk7F"
SLACK_CHANNEL_ID = "DNYPT4S7N"

# Set the URL of the website to open
WEBSITE_URL = "YOUR_WEBSITE_URL"

# Set the ID of the input field on the website
INPUT_FIELD_ID = "YOUR_INPUT_FIELD_ID"

# Initialize the Slack client
client = slack_sdk.WebClient(token=SLACK_API_TOKEN)

# Retrieve the conversation history
result = client.conversations_history(channel=SLACK_CHANNEL_ID)
print("Result")
print(result)

# Get the messages from the conversation history
messages = result["messages"]
print(messages)

# Get the most recent message
# latest_message = messages[0]

# Extract the username from the message text
# username = latest_message["text"].split()[-1]

# Open the website in a new browser window
# webbrowser.open(WEBSITE_URL)

# Initialize the Selenium WebDriver
# driver = webdriver.Firefox()

# Navigate to the website
# driver.get(WEBSITE_URL)

# Find the input field on the website
# input_field = driver.find_element_by_id(INPUT_FIELD_ID)

# Enter the username into the input field
# input_field.send_keys(username)
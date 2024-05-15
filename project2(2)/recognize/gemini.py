# Install required libraries
#pip3 install Pillow
#pip3 install google-generativeai

import PIL.Image
import google.generativeai as genai

# Configure API key
genai.configure(api_key="sk-ltc0dTmWzkSSkDxNCc038c171a5945E69162556818A805D6")

# Initialize GenerativeModel
model = genai.GenerativeModel(model_name="gemini-pro-vision")

# Open the image
img = PIL.Image.open(r'C:\Users\10710\Desktop\CPS4951\Second project\project2\recognize\2.jpg')


# Generate content
response = model.generate_content(["What's in this photo?", img])

# Print the response
print(response.text)

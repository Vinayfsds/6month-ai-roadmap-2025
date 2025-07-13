# Below line is to install the package of Google Generative AI.
#pip install -g -U google-generativeai

# Once Google generative AI in installed we can use it by importing the package.
# Targeting to use the output for displaying in UI using Streamlit.
import google.generativeai as genai
import streamlit as st
import time

# configure genai with your API key. We can generate the API key from Google AI studio.
genai.configure(api_key="AIzaSyBmZliWsgVpJkGYTtXD26ubt2HN0rsixoM") # Replace "YOUR_API_KEY" with your actual API key

#Using the gemini model to generate content based on a question prompt.(This is a text based model)
model = genai.GenerativeModel("gemini-2.5-flash-preview-04-17") # Corrected model name

#considering the question prompt using streamlit for user input.
#question_prompt = st.text_input("Enter your question:","--user text here--") # Added a text input for user to enter a question


#print(response.text) # Access the text attribute of the response object to get the generated content

st.set_page_config(page_title="Generative AI Example", page_icon=":robot_face:") # Set the title and icon for the Streamlit app
#st.title("VB chat interface") # Set the title of the Streamlit app

with st.sidebar:
    st.title("VB Chat Interface")
    st.write("Your personal AI assistant") # Additional info if needed

# Initialize chat history in session state if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = []

    #st.session_state.messages = []

# Display chat messages from history on app rerun
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#        st.markdown(message["content"])  # Display the content of the message in markdown format

       # Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        # This line will now work correctly because message["content"]
        # will already be the extracted text string
        st.markdown(message["content"])

if prompt := st.chat_input("Say something..."):
    # 1. Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 2. Display user message immediately in chat bubble
    with st.chat_message("user"):
        st.markdown(prompt)

    # 3. Now, simulate AI response (only after user's message is processed)
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                # Call the Gemini model with the user's prompt
                response = model.generate_content(prompt)

                # Access the text from the response object
                # Prefer .text, but fallback to direct proto access if needed
                if hasattr(response, 'text'):
                    generated_text = response.text
                elif hasattr(response, 'result') and hasattr(response.result, 'candidates'):
                    generated_text = response.result.candidates[0].content.parts[0].text
                else:
                    generated_text = "Could not extract a readable response."
                    st.error("Unexpected response format from the model.")

                st.markdown(generated_text) # Display the extracted text in the assistant's bubble
                # 4. Add AI response to chat history
                st.session_state.messages.append({"role": "assistant", "content": generated_text})

            except AttributeError:
                st.error("Error: Could not extract text from the model's response. The response structure might have changed or be unexpected. Check API Key.")
                st.session_state.messages.append({"role": "assistant", "content": "Error: Could not extract response."})
            except IndexError:
                st.error("Error: The model response did not contain any candidates or parts. This might mean content was blocked.")
                st.session_state.messages.append({"role": "assistant", "content": "Error: No valid content in response."})
            except Exception as e:
                error_message = f"An unexpected error occurred: {e}"
                st.error(error_message)
                st.session_state.messages.append({"role": "assistant", "content": error_message})



#st.write(response.text) # Display the generated content in the Streamlit app

# import pathlib
# import textwrap

# import google.generativeai as genai

# from IPython.display import display, Markdown


# def to_markdown(text):
#   text = text.replace('•', '  *')
#   return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# for m in genai.list_models():
#     if 'generateContent' in m.supported_generation_methods:
#         print(m.name)

# """**Image PIL"""

# import PIL.Image

# img = PIL.Image.open(pathlib.Path('Golkonda_image.jpg'))  # Corrected 'imgae' to 'Image'
# img # Display the image using the PIL library

# model = genai.GenerativeModel("gemini-2.5-flash-preview-04-17")  # Corrected model name
# response = model.generate_content(img)
# to_markdown(response.text)  # Convert the response text to Markdown format for display



# # Title and description
# st.title("Generative AI Example")
# st.write("This is a simple example of using Generative AI to answer questions and generate content.")

# # Display the generated response
# st.write("Generated Response:")
# st.write(response.text)  # Display the generated response in the Streamlit app

# # Save the response to a text file
# with open("response.txt", "w") as file:
#     file.write(response.text)  # Write the generated response to a text file
# st.write("Response saved to response.txt")  # Notify the user that the response has been saved

# # Display the image
# st.image(img, caption='Golkonda Image')  # Display the image in the Streamlit app

# # Image description
# st.write("Image Description:")
# st.write("This image represents Golkonda, a historical fort in India. It is known for its impressive architecture and historical significance.")

# # Save the image to a file
# img.save("Golkonda_image.jpg")  # Save the image to a file
# st.image("Golkonda_image.jpg", caption='Golkonda Image')  # Display the saved image in the Streamlit app
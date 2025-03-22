# Therapy Chatbott

## Project Description

This project is a therapy chatbot that utilizes the T5 model with LangChain and Streamlit to create an interactive experience for users seeking therapeutic conversations. The bot supports both Arabic and English and can translate between the two languages during conversations.

📧 [Kaggle Notebook](https://www.kaggle.com/code/mahmoudsfarhat/trying-gui-on-t5-base/edit)  
  
---

## Requirements

### Required Packages and Libraries
To ensure smooth operation, install the following packages:

```bash
!pip install streamlit
!pip install -q streamlit
!wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
!unzip ngrok-stable-linux-amd64.zip
!curl ipv4.icanhazip.com
!curl -sSL https://ngrok-agent.s3.amazonaws.com/ngrok.asc \
	| sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null \
	&& echo "deb https://ngrok-agent.s3.amazonaws.com buster main" \
	| sudo tee /etc/apt/sources.list.d/ngrok.list \
	&& sudo apt update \
	&& sudo apt install ngrok
```

### Running the Application
To launch the application, run the following command:

```bash
!ngrok config add-authtoken 2msVK7ca9lTzQ18511ycmaQa9Bl_5j9gHHAGBvN5xpcF4kmQB
!streamlit run app.py & ngrok http 8501
```

---

## Project Components

### 1. **Model Loading**
- The `T5ForConditionalGeneration` model is loaded using pre-trained weights.
- A `pipeline` is used to process input and generate responses.

### 2. **Conversation Memory**
- `ConversationBufferMemory` is used to retain a history of previous conversations.

### 3. **Translation Between Arabic and English**
- `Helsinki-NLP/opus-mt-ar-en` is used for translating text from Arabic to English.
- `Helsinki-NLP/opus-mt-en-ar` is used for translating text from English to Arabic.

### 4. **User Interface with Streamlit**
- A simple UI includes:
  - Language selection (Arabic / English).
  - User input and message history display.
  - Bot responses with automatic translation when needed.

---

## How the Bot Works

1. The user selects the desired conversation language.
2. The user inputs a message.
3. If the language is Arabic, the message is translated into English before being processed.
4. `LLMChain` generates a response based on the input and conversation history.
5. If the response is in English and Arabic was selected, it is translated before display.
6. The conversation is displayed interactively using Streamlit.

---

If you encounter any issues, feel free to open an **Issue** or reach out to us!


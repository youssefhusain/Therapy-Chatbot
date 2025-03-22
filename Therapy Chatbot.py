%%writefile app.py



import streamlit as st
import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer, pipeline
from langchain.llms import HuggingFacePipeline
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

weights_path = "/kaggle/input/t5-base-therapy-chatbot/t5_full_model.pth"

try:
    weights = torch.load(weights_path, map_location=device)
    model = T5ForConditionalGeneration.from_pretrained("t5-base")
    model.load_state_dict(weights)
except TypeError:
    model = torch.load(weights_path, map_location=device)

model.to(device)
model.eval()

tokenizer = T5Tokenizer.from_pretrained("t5-base")

pipe = pipeline("text2text-generation", model=model, tokenizer=tokenizer, max_length=100, device=device if device.type == "cuda" else -1)

llm = HuggingFacePipeline(pipeline=pipe)

prompt = PromptTemplate(
    input_variables=["history", "user_input"],
    template="Previous conversation:\n{history}\n\nUser: {user_input}\nAssistant:",
)

memory = ConversationBufferMemory(memory_key="history", return_messages=True)

conversation = LLMChain(llm=llm, prompt=prompt, memory=memory)


translator_ar_en = pipeline("translation_ar_to_en", model="Helsinki-NLP/opus-mt-ar-en", device=device if device.type == "cuda" else -1)
translator_en_ar = pipeline("translation_en_to_ar", model="Helsinki-NLP/opus-mt-en-ar", device=device if device.type == "cuda" else -1)

def translate_and_generate(user_input, lang):
    if lang == "العربية":
        translated_input = translator_ar_en(user_input)[0]['translation_text']
        response_en = conversation.invoke({"user_input": translated_input})
        response_ar = translator_en_ar(response_en["text"])[0]['translation_text']
        return response_ar
    else:
        response = conversation.invoke({"user_input": user_input})
        return response["text"]


def main():
    st.set_page_config(page_title="Therapy Bot 🤖", page_icon="💙")

    st.markdown(
        "<h1 style='text-align: center; color: #4A90E2;'>🤖 Therapy Chatbot</h1>",
        unsafe_allow_html=True
    )

    st.image("https://cdn-icons-png.flaticon.com/512/3062/3062634.png", width=120)  # صورة روبوت

    st.markdown(
        "<p style='text-align: center; font-size:18px; color: #555;'>"
        "مرحبًا! أنا هنا للاستماع إليك ومساعدتك في رحلتك النفسية. لا تتردد في التحدث معي. 💙"
        "</p>",
        unsafe_allow_html=True
    )

    st.markdown("---")

    language = st.radio("🌍 اختر لغة المحادثة:", ["English", "العربية"])


    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    for role, text in st.session_state["messages"]:
        with st.chat_message(role):
            st.markdown(text)


    inputuser = st.chat_input("🗨️ كيف تشعر اليوم؟")

    if inputuser:
    
        st.session_state["messages"].append(("user", inputuser))

      
        with st.chat_message("user"):
            st.markdown(inputuser)

  
        response = translate_and_generate(inputuser, language)

  
        st.session_state["messages"].append(("assistant", response))

    
        with st.chat_message("assistant"):
            st.markdown(response)

if __name__ == "__main__":
    main()



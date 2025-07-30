import streamlit as st
import google.generativeai as genai
from datetime import datetime
from gtts import gTTS
import tempfile
import base64

st.set_page_config(page_title="హెల్త్ AI సహాయకుడు", page_icon="🩺", layout="wide")

# Custom Telugu UI CSS
st.markdown("""
<style>
    body, .stApp { background: #fff !important; }
    .main { font-family: 'Poppins', sans-serif !important; }
    .stChatMessage[data-testid="user-message"] {
        background: #f5f5f5;
        color: #222;
        border-radius: 15px;
        margin-bottom: 1rem;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
    }
    .stChatMessage[data-testid="assistant-message"] {
        background: #e9e9e9;
        color: #222;
        border-radius: 15px;
        margin-bottom: 1rem;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
    }
    .stTextInput > div > div > input {
        background: #fff;
        border-radius: 15px;
        padding: 1.5rem;
        font-size: 1.2rem;
        border: 2px solid #e9e9e9;
        color: #222;
    }
    .stTextInput > div > div > input:focus {
        border-color: #aaa;
        box-shadow: 0 0 10px #aaa3;
    }
    .stSelectbox > div > div {
        font-size: 1.2rem;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Session management
if 'messages' not in st.session_state:
    st.session_state['messages'] = []
if 'category' not in st.session_state:
    st.session_state['category'] = 'ఆహారం'
if 'gemini_api_key' not in st.session_state:
    st.session_state['gemini_api_key'] = "AIzaSyDlUN9wJ_Vvj5kCxC-YO-nRTtUHNeeHztg"

def configure_gemini(api_key):
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        return model
    except Exception as e:
        st.error(f"AI API లో లోపం: {str(e)}")
        return None

model = configure_gemini(st.session_state['gemini_api_key'])
if not model:
    st.stop()

st.title("🩺 హెల్త్ AI సహాయకుడు (Telugu Health AI Assistant)")

# Category filter
category = st.selectbox("వర్గాన్ని ఎంచుకోండి:", ["ఆహారం", "వ్యాయామం", "లక్షణాలు", "వైద్య సలహా"], index=["ఆహారం", "వ్యాయామం", "లక్షణాలు", "వైద్య సలహా"].index(st.session_state['category']))
st.session_state['category'] = category

# Display chat history
for msg in st.session_state['messages']:
    with st.chat_message(msg['role']):
        st.markdown(msg['content'])
        if msg['role'] == 'assistant' and 'audio' in msg:
            st.audio(msg['audio'], format='audio/mp3')

# Large input field
prompt = st.chat_input("మీ ప్రశ్నను తెలుగులో టైప్ చేయండి...")

if prompt:
    st.session_state['messages'].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        with st.spinner("AI సమాధానం సిద్ధం అవుతోంది..."):
            try:
                # Telugu prompt for Gemini
                full_prompt = f"వర్గం: {category}\nప్రశ్న: {prompt}\nదయచేసి సమాధానాన్ని తెలుగులో ఇవ్వండి."
                chat_history = []
                for msg in st.session_state['messages'][:-1]:
                    chat_history.append({
                        'role': 'user' if msg['role'] == 'user' else 'model',
                        'parts': [msg['content']]
                    })
                chat = model.start_chat(history=chat_history)
                response = chat.send_message(full_prompt)
                response_text = response.text
                st.markdown(response_text)
                # Audio output
                tts = gTTS(text=response_text, lang='te')
                with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
                    tts.save(fp.name)
                    audio_bytes = fp.read()
                st.audio(fp.name, format='audio/mp3')
                st.session_state['messages'].append({"role": "assistant", "content": response_text, "audio": fp.name})
            except Exception as e:
                error_msg = f"AI లోపం: {str(e)}"
                st.error(error_msg)
                st.session_state['messages'].append({"role": "assistant", "content": error_msg})

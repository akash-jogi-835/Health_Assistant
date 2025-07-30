# హెల్త్ AI సహాయకుడు (Telugu Health AI Assistant)

A mobile-friendly, accessible Streamlit app that provides health support in Telugu using Gemini AI. Designed for Telugu speakers who prefer to interact in their native language.

## ఫీచర్లు (Features)
- తెలుగు UI, chat, and instructions
- Health topics: ఆహారం (Diet), వ్యాయామం (Exercise), లక్షణాలు (Symptoms), వైద్య సలహా (Doctor Advice)
- Large, mobile-friendly input field
- Category filter for health topics
- Gemini AI answers in Telugu
- Audio output for assistant responses (using gTTS)

## అవసరమైనవి (Requirements)
- Python 3.8+
- Streamlit
- google-generativeai
- gtts

## ఇన్‌స్టాలేషన్ (Installation)
1. Clone this repository or copy the files to your project folder.
2. Install dependencies:
   ```bash
   pip install streamlit google-generativeai gtts
   ```
3. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # Mac/Linux
   ```

## వాడకం (Usage)
1. Get your Gemini API key from [Google MakerSuite](https://makersuite.google.com/app/apikey).
2. Add your API key to the code (default is set in `health_ai_telugu.py`).
3. Run the app:
   ```bash
   streamlit run health_ai_telugu.py
   ```
4. Open the provided local URL in your browser.

## స్క్రీన్‌షాట్స్ (Screenshots)
Add screenshots here for the UI and chat experience.

## లైసెన్స్ (License)
MIT

## Credits
- [Streamlit](https://streamlit.io/)
- [Google Generative AI Python Client](https://github.com/google/generative-ai-python)
- [gTTS](https://pypi.org/project/gTTS/)

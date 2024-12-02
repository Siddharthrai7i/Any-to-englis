import streamlit as st
from googletrans import Translator
def translatetoenglish(text):
    translator = Translator()
    try:
        language = translator.detect(text).lang
        st.write(f"Detected language: {language}")
        st.write("Translating to English...")
        translation = translator.translate(text, src=language, dest='en')
        english = translation.text
        st.write(f"Translated English Text: {english}")
        return english
    except Exception as e:
        return f"Error with the translation service: {e}"
st.title("Language Translator to English")
st.subheader("Enter text in any language to translate it into English")
input = st.text_area("Enter text:", height=150)
if st.button("Translate"):
    if input.strip():
        translated_text = translatetoenglish(input)
        st.write(f"Your translated text is: {translated_text}")
    else:
        st.write("Please enter some text to translate.")

import streamlit as st
import speech_recognition as sr

st.set_page_config(page_title="Speech to Text", layout="wide")

st.markdown("""
<style>
.circle {
    width: 150px;
    height: 150px;
    border-radius: 50%;
    background-color: #ff4b4b;
    display: flex;
    justify-content: center;
    align-items: center;
    color: white;
    font-size: 22px;
    font-weight: bold;
    margin: auto;
}

.animate {
    animation: pulse 1s infinite;
}

@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.25); }
    100% { transform: scale(1); }
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center'>Speech to Text Conversion</h1>", unsafe_allow_html=True)

placeholder = st.empty()

if st.button("Start registration"):

    placeholder.markdown("""
    <div class="circle animate">
        Speak<br>Now
    </div>
    """, unsafe_allow_html=True)

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)

    placeholder.empty()  # إخفاء الدائرة بعد التسجيل

    try:
        my_text = r.recognize_google(audio, language="ar-EG")
        st.success("Speech recognition was successful")
        st.write("Text:", my_text)

    except sr.UnknownValueError:
        st.error("The speech was not recognized")

    except sr.RequestError as e:
        st.error(f"A service error occurred: {e}")

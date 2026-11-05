
import streamlit as st

st.set_page_config(
    page_title="BOBI AI STUDIO",
    page_icon="✨",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg,#101426,#202744);
    color: white;
}
h1,h2,h3,p,label {
    color: white !important;
}
div.stButton > button {
    background: linear-gradient(90deg,#673de6,#8b5cf6);
    color: white;
    border-radius: 12px;
    border: none;
    padding: 12px;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

st.title("✨ Welcome to BOBI AI STUDIO")
st.subheader("Your All-in-One AI Creative Platform")
st.write("Chat • Create • Edit • Imagine")

st.divider()

menu = st.sidebar.radio(
    "MENU",
    [
        "Home",
        "AI Chat",
        "AI Image Generator",
        "Photo Editing",
        "AI Video Tools",
        "About"
    ]
)

if menu == "Home":
    st.header("🚀 Explore AI Tools")
    st.info("🤖 AI Chat Assistant")
    st.info("🎨 AI Image Generator")
    st.info("📸 Photo Editing")
    st.info("🎬 AI Video Tools")

elif menu == "AI Chat":
    st.header("🤖 AI Chat Assistant")
    st.success("AI Chat Interface Ready")
    st.warning("AI API connection required.")

elif menu == "AI Image Generator":
    st.header("🎨 AI Image Generator")
    prompt = st.text_area("Describe your image")
    if st.button("Generate Image"):
        st.info("Image API connection required.")

elif menu == "Photo Editing":
    st.header("📸 Photo Editing")
    photo = st.file_uploader(
        "Upload your photo",
        type=["jpg", "jpeg", "png"]
    )
    if photo:
        st.image(photo, caption="Your Photo")

elif menu == "AI Video Tools":
    st.header("🎬 AI Video Tools")
    idea = st.text_area("Describe your video idea")
    if st.button("Create Video"):
        st.info("Video API connection required.")

elif menu == "About":
    st.header("About BOBI AI STUDIO")
    st.write("Your All-in-One AI Creative Platform")
    st.write("Created with ❤️")
    

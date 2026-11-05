
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
section[data-testid="stSidebar"] {
    background: #111827;
}
.hero {
    padding: 30px;
    border-radius: 18px;
    background: linear-gradient(120deg,#312e81,#7c3aed);
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.title("✨ BOBI AI STUDIO")
    st.caption("YOUR CREATIVE AI PLATFORM")
    page = st.radio(
        "MENU",
        ["Home", "AI Chat", "AI Image Generator",
         "AI Video Tools", "Photo Editing",
         "AI Prompt Maker", "About"]
    )

if page == "Home":
    st.markdown("""
    <div class="hero">
    <h1>✨ Welcome to BOBI AI STUDIO</h1>
    <p>Your All-in-One AI Creative Platform</p>
    <p>Chat • Create • Edit • Imagine</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("🚀 Explore AI Tools")
    col1, col2 = st.columns(2)

    with col1:
        st.info("🤖 AI Chat Assistant")
        st.info("🎨 AI Image Generator")
        st.info("📸 Photo Editing")

    with col2:
        st.info("🎬 AI Video Tools")
        st.info("✍️ AI Prompt Maker")
        st.info("💡 Creative Workspace")

elif page == "AI Chat":
    st.title("🤖 BOBI AI CHAT")
    st.write("Welcome to your AI Assistant!")
    st.warning("AI API connection is required for real AI replies.")

elif page == "AI Image Generator":
    st.title("🎨 AI IMAGE GENERATOR")
    prompt = st.text_area("Describe your image")
    if st.button("Generate Image"):
        st.info("Image generation API will be connected next.")

elif page == "AI Video Tools":
    st.title("🎬 AI VIDEO STUDIO")
    idea = st.text_area("Describe your video idea")
    if st.button("Create Video"):
        st.info("Video generation API will be connected next.")

elif page == "Photo Editing":
    st.title("📸 PHOTO EDITING")
    photo = st.file_uploader(
        "Upload your photo",
        type=["jpg", "jpeg", "png"]
    )
    if photo:
        st.image(photo, use_container_width=True)

elif page == "AI Prompt Maker":
    st.title("✍️ BOBI AI PROMPT MAKER")
    subject = st.text_input("What do you want to create?")
    style = st.selectbox(
        "Choose Style",
        ["Cinematic", "Royal", "Realistic", "3D", "Professional"]
    )
    if st.button("Create Prompt"):
        if subject:
            st.code(f"{subject}, {style} style, 4K, high detail")
        else:
            st.warning("Enter a subject first.")

elif page == "About":
    st.title("✨ ABOUT BOBI AI STUDIO")
    st.write("Created by Bhupendra Jangid (Bobi)")
    st.write("Your All-in-One Creative AI Platform")

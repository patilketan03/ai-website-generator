import streamlit as st
from dotenv import load_dotenv
import os
import zipfile
import io
from langchain_google_genai import ChatGoogleGenerativeAI

# ENV
load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("gemini")

st.set_page_config(page_title="WebCraft AI",page_icon="💻")


# SESSION STATE 
if "zip_bytes" not in st.session_state:
    st.session_state.zip_bytes = None

# STYLES
st.markdown(
    """
    <style>
    .stApp {
        background:
            radial-gradient(circle at 10% 10%, rgba(99,102,241,0.15), transparent 40%),
            radial-gradient(circle at 90% 10%, rgba(168,85,247,0.12), transparent 45%),
            radial-gradient(circle at 10% 90%, rgba(34,197,94,0.12), transparent 40%),
            radial-gradient(circle at 90% 90%, rgba(249,115,22,0.12), transparent 45%),
            linear-gradient(135deg, #020617 0%, #020617 100%);
    }

    .shell {
        max-width: 880px;
        margin: auto;
        padding: 2.5rem 1.4rem 3.5rem;
    }

  .hero-title {
    font-size: 2.6rem;              
    font-weight: 800;
    letter-spacing: -0.03em;
    color: #e5e7eb;
    text-align: center;
    }

    .hero-sub {
        margin-top: 0.7rem;
        max-width: 44rem;
        font-size: 1rem;                
        line-height: 1.0;              
        color: rgba(148,163,184,0.85);  
        text-align: center;
    }
    .hero-title {
        font-size: 2.35rem;
        font-weight: 800;
        letter-spacing: -0.02em;
    }

    .hero-sub {
        margin-top: 0.4rem;
        opacity: 0.9;
        font-size: 0.95rem;
        max-width: 36rem;
        line-height: 1.5;
    }

    .block-label {
        font-size: 0.85rem;
        font-weight: 600;
        margin-top: 1.8rem;
        text-transform: uppercase;
        letter-spacing: 0.04em;
        opacity: 0.85;
    }

    .block-caption {
        font-size: 0.8rem;
        opacity: 0.65;
        margin-bottom: 0.6rem;
    }

    .stTextArea textarea {
        border-radius: 1.1rem !important;
        background: #020617 !important;
        border: 1px solid rgba(148,163,184,0.55) !important;
        padding: 0.9rem 1rem !important;
        font-size: 0.9rem;
    }

    .stTextArea textarea:focus {
        border-color: rgba(99,102,241,0.9) !important;
        box-shadow: 0 0 0 1px rgba(99,102,241,0.35);
    }

    /* UPDATED BUTTON COLOR */
    div.stButton > button[kind="primary"] {
        border-radius: 999px;
        padding: 0.6rem 1.8rem;
        font-weight: 600;
        background: linear-gradient(135deg, #4f46e5, #06b6d4);
        color: #ffffff;
        border: none;
        transition: transform 0.15s ease, box-shadow 0.15s ease;
    }

    div.stButton > button[kind="primary"]:hover {
        transform: translateY(-1px);
        box-shadow: 0 14px 35px rgba(79,70,229,0.35);
    }

    .footer {
        margin-top: 2.5rem;
        font-size: 0.75rem;
        opacity: 0.6;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# SYSTEM PROMPT
system_prompt = """
You are a senior frontend engineer and UI/UX expert. 
Goal: Generate a complete, production-ready static website based ONLY on the user description. 
Requirements: - Use modern, semantic HTML5 structure (header, main, section, footer, etc.).
- Add clear sections: hero, features/benefits, call-to-action, and any additional sections explicitly requested. 
- Ensure the layout is responsive and mobile-friendly (flexbox or CSS grid, no frameworks). 
- Use clean, readable class names and consistent indentation. 
- Do NOT include inline CSS or inline JavaScript inside the HTML. Styling: 
- Provide all styling in a separate CSS file. 
- Use a modern look with good spacing, hierarchy, and accessible color contrast. 
- Use a simple Google Font (e.g., Inter, Poppins, or similar) imported in CSS. 
- Include hover states for buttons and links. 
- Use pricing ONLY in Indian Rupees (INR). Do NOT use dollars or USD anywhere.
- Respect any colors, branding, or style instructions from the user description. 
Behavior (JavaScript): - Only write vanilla JavaScript. 
- Add smooth scroll for internal navigation links if there is a navbar. 
- Add small, useful interactions if relevant (e.g., mobile nav toggle, simple animations, FAQ accordion). 
- Do NOT use external JS libraries or frameworks. Output format (strict):
Return your answer in EXACTLY this structure with no extra text, comments, or explanations:

--html--
HTML
--html--

--css--
CSS
--css--

--js--
JS
--js--
"""

st.markdown(
    """
    <div class="hero">
        <div class="hero-title">Build Websites from a Prompt</div>
        
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="block-label">Website Details</div>', unsafe_allow_html=True)
st.markdown('<div class="block-caption">Provide the details for your website.</div>', unsafe_allow_html=True)

prompt = st.text_area(
    "",
    height=140,
    placeholder="Describe the website you want to generate",
)

generate_clicked = st.button("⚡ Generate Website", type="primary")

status = st.empty()

# HELPERS
def extract_block(text: str, tag: str) -> str:
    parts = text.split(f"--{tag}--")
    return parts[1].strip() if len(parts) >= 3 else ""

# GENERATION 
if generate_clicked:
    if not prompt.strip():
        status.warning("Please enter a description.")
    else:
        status.info("⚙️ Building your website…")
        try:
            model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
            response = model.invoke([( "system", system_prompt), ("human", prompt)])
            content = response.content if isinstance(response.content, str) else str(response)

            html = extract_block(content, "html")
            css = extract_block(content, "css")
            js = extract_block(content, "js")

            if not html or not css or not js:
                status.error("Invalid website format received. Please try again.")
            else:
                zip_buffer = io.BytesIO()
                with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as z:
                    z.writestr("index.html", html)
                    z.writestr("style.css", css)
                    z.writestr("script.js", js)

                st.session_state.zip_bytes = zip_buffer.getvalue()
                status.success("✅ Website ready")

        except Exception as e:
            status.error(f"Generation failed: {e}")

if st.session_state.zip_bytes:
    st.download_button(
        "⬇️ Download Website",
        data=st.session_state.zip_bytes,
        file_name="website.zip",
        mime="application/zip",
    )
    st.markdown("</div>", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

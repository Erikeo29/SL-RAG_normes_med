"""RAG normes medicales - Point d'entree Streamlit."""
import streamlit as st
import streamlit.components.v1 as components

from config import CSS_PATH
from components.sidebar import render_sidebar
from components.chat_page import render_chat_page
from components.upload_page import render_upload_page
from components.about_page import render_about_page
from components.normes_page import render_normes_medical_page
from utils.translations import t


# --- Page config ---
st.set_page_config(
    page_title="RAG Normes Médicales",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Session state init ---
if "lang" not in st.session_state:
    st.session_state.lang = "fr"
if "current_page" not in st.session_state:
    st.session_state.current_page = "about"
if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = []
if "chat_sources" not in st.session_state:
    st.session_state.chat_sources = []


# --- CSS + boutons de navigation ---
def load_custom_css(path: str) -> str:
    """Charge le CSS et retourne le HTML complet (CSS + boutons navigation)."""
    try:
        with open(path, encoding="utf-8") as f:
            css_content = f.read()
    except FileNotFoundError:
        css_content = ""

    nav_buttons_html = (
        '<a href="#top" class="nav-button back-to-top"'
        ' title="Retour en haut / Back to top">&#9650;</a>'
        '<a href="#bottom" class="nav-button scroll-to-bottom"'
        ' title="Aller en bas / Go to bottom">&#9660;</a>'
        '<div id="top"></div>'
    )
    return f"<style>{css_content}</style>{nav_buttons_html}"


st.markdown(load_custom_css(CSS_PATH), unsafe_allow_html=True)


# --- Sidebar ---
render_sidebar()


# --- Routing ---
page = st.session_state.current_page

if page == "chat":
    render_chat_page()
elif page == "upload":
    render_upload_page()
elif page == "normes_medical":
    render_normes_medical_page()
elif page == "about":
    render_about_page()

# Ancre de bas de page
st.markdown('<div id="bottom"></div>', unsafe_allow_html=True)

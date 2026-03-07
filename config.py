"""Configuration globale — RAG normes medicales."""
import os

# --- Chemins ---
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DOC_PATH = os.path.join(ROOT_DIR, "docs")
DATA_PATH = os.path.join(ROOT_DIR, "data")
NORMES_PATH = os.path.join(DATA_PATH, "normes")
ASSETS_PATH = os.path.join(ROOT_DIR, "assets")
CSS_PATH = os.path.join(ASSETS_PATH, "style.css")
CHROMA_PATH = os.path.join(DATA_PATH, "chroma_db")

# --- Version ---
VERSION = "1.0.0"
VERSION_DATE = "Jan 2026"

# --- RAG ---
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
MAX_CONTEXT_CHUNKS = 5
LLM_MODEL = "llama-3.3-70b-versatile"

# --- Domaine unique ---
COLLECTION_NAME = "normes_medical"
DOC_SOURCE_PATH = os.path.join(DATA_PATH, "normes medical")

# --- Prompt systeme ---
SYSTEM_PROMPT = (
    "Tu es un assistant expert en normes et réglementations pour les dispositifs médicaux.\n\n"
    "Tu analyses des documents normatifs (ISO 13485, FDA 21 CFR 820, IEC 62304, EU MDR, "
    "ASTM...) et réponds aux questions en te basant EXCLUSIVEMENT sur le contexte fourni.\n\n"
    "Règles :\n"
    "1. Cite systématiquement les sources [Source N] dans ta réponse.\n"
    "2. Si le contexte ne contient pas l'information, dis-le clairement.\n"
    "3. Ne fabrique jamais d'information non présente dans le contexte.\n"
    "4. Structure ta réponse avec des titres et des listes si pertinent.\n"
    "5. Si une exigence normative est citée, mentionne la section/clause exacte.\n"
    "6. Réponds dans la langue de l'utilisateur (français ou anglais)."
)

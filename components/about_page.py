"""Page a propos : description du projet et architecture."""
import streamlit as st

from config import COLLECTION_NAME
from core.ingestion import get_db_stats
from utils.translations import t


def render_about_page():
    """Affiche la page a propos."""
    lang = st.session_state.get("lang", "fr")
    stats = get_db_stats(collection_name=COLLECTION_NAME)

    if lang == "fr":
        _render_fr(stats)
    else:
        _render_en(stats)


def _render_fr(stats: dict):
    st.header("A propos")

    st.subheader("Objectif")
    st.markdown(
        "Cette application est un **assistant intelligent** pour l'analyse de documents "
        "reglementaires lies aux dispositifs medicaux. Elle utilise la technologie **RAG** "
        "(Retrieval-Augmented Generation) pour permettre de poser des questions "
        "en langage naturel sur les documents charges."
    )

    st.markdown("---")

    st.subheader("Domaine couvert")
    st.markdown(t("about_domain_medical_desc"))
    st.caption(f"{stats['documents']} documents, {stats['chunks']} chunks")

    st.markdown("---")

    st.subheader("Fonctionnalites")
    st.markdown(
        "- **Chat RAG** : posez des questions en langage naturel, obtenez des reponses "
        "avec references aux documents sources\n"
        "- **Synthese des normes** : vue d'ensemble structuree des normes medicales\n"
        "- **Gestion des documents** : upload, indexation et suppression de PDFs\n"
        "- **Matrice de compliance** : evaluez la conformite par referentiel "
        "(FDA, ISO...) avec recherche RAG integree\n"
        "- **Bilingue** : francais et anglais"
    )

    st.markdown("---")

    st.subheader("Cas d'usage")
    st.markdown(
        "- Recherche rapide d'exigences dans les documents reglementaires charges\n"
        "- Preparation d'audits : identifier rapidement les clauses pertinentes\n"
        "- Gap analysis : comparer les exigences avec les procedures internes\n"
        "- Formation : comprendre les exigences reglementaires de maniere interactive"
    )

    st.markdown("---")

    st.subheader("Architecture")
    st.code(
        "PDF Upload -> Decoupage en chunks -> Embeddings -> ChromaDB\n"
        "                                                      |\n"
        "Question -> Embedding -> Recherche semantique -> Chunks pertinents\n"
        "                                                      |\n"
        "               Chunks + Question -> LLM (Llama 3.3) -> Reponse sourcee",
        language=None,
    )

    st.markdown("---")

    st.subheader("Composants techniques")
    st.markdown(
        "| Composant | Technologie |\n"
        "|-----------|-------------|\n"
        "| Interface | Streamlit |\n"
        "| Embeddings | ChromaDB ONNX (all-MiniLM-L6-v2) |\n"
        "| Base vectorielle | ChromaDB (persistante, locale) |\n"
        "| LLM | Llama 3.3 70B via Groq API |\n"
        "| PDF parsing | PyPDF |\n"
        "| Chunking | LangChain RecursiveCharacterTextSplitter |"
    )

    st.markdown("---")

    st.subheader("Documents actuellement indexes")
    if stats["sources"]:
        for src in stats["sources"]:
            st.markdown(f"- {src}")
        st.caption(f"{stats['documents']} documents, {stats['chunks']} chunks")
    else:
        st.caption("Aucun document indexe.")

    st.markdown("---")

    st.caption(
        "Note : les documents charges dans ce RAG sont des documents publics et gratuits."
    )


def _render_en(stats: dict):
    st.header("About")

    st.subheader("Purpose")
    st.markdown(
        "This application is an **intelligent assistant** for analyzing regulatory "
        "documents related to medical devices. It uses **RAG** "
        "(Retrieval-Augmented Generation) technology to allow natural language "
        "questions on uploaded documents."
    )

    st.markdown("---")

    st.subheader("Domain covered")
    st.markdown(t("about_domain_medical_desc"))
    st.caption(f"{stats['documents']} documents, {stats['chunks']} chunks")

    st.markdown("---")

    st.subheader("Features")
    st.markdown(
        "- **RAG Chat**: ask natural language questions, get answers with source references\n"
        "- **Standards overview**: structured summary of medical device standards\n"
        "- **Document management**: upload, index and delete PDFs\n"
        "- **Compliance matrix**: assess conformity by standard "
        "(FDA, ISO...) with integrated RAG search\n"
        "- **Bilingual**: French and English"
    )

    st.markdown("---")

    st.subheader("Use cases")
    st.markdown(
        "- Quick lookup of requirements in uploaded regulatory documents\n"
        "- Audit preparation: rapidly identify relevant clauses\n"
        "- Gap analysis: compare requirements with internal procedures\n"
        "- Training: understand regulatory requirements interactively"
    )

    st.markdown("---")

    st.subheader("Architecture")
    st.code(
        "PDF Upload -> Chunking -> Embeddings -> ChromaDB\n"
        "                                           |\n"
        "Question -> Embedding -> Semantic search -> Relevant chunks\n"
        "                                           |\n"
        "            Chunks + Question -> LLM (Llama 3.3) -> Sourced answer",
        language=None,
    )

    st.markdown("---")

    st.subheader("Technical components")
    st.markdown(
        "| Component | Technology |\n"
        "|-----------|------------|\n"
        "| Interface | Streamlit |\n"
        "| Embeddings | ChromaDB ONNX (all-MiniLM-L6-v2) |\n"
        "| Vector store | ChromaDB (persistent, local) |\n"
        "| LLM | Llama 3.3 70B via Groq API |\n"
        "| PDF parsing | PyPDF |\n"
        "| Chunking | LangChain RecursiveCharacterTextSplitter |"
    )

    st.markdown("---")

    st.subheader("Currently indexed documents")
    if stats["sources"]:
        for src in stats["sources"]:
            st.markdown(f"- {src}")
        st.caption(f"{stats['documents']} documents, {stats['chunks']} chunks")
    else:
        st.caption("No documents indexed.")

    st.markdown("---")

    st.caption(
        "Note: all documents loaded in this RAG are free, publicly available documents."
    )

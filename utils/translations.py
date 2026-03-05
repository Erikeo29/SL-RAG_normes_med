"""Systeme de traduction bilingue FR/EN — Normes medicales."""
import streamlit as st

TRANSLATIONS: dict[str, dict[str, str]] = {
    # --- App ---
    "app_title": {
        "fr": "Normes medicales",
        "en": "Medical Standards",
    },
    "app_subtitle": {
        "fr": "Assistant intelligent pour l'analyse de normes medicales",
        "en": "Intelligent assistant for medical standards analysis",
    },
    # --- Sidebar ---
    "sidebar_title": {
        "fr": "Navigation",
        "en": "Navigation",
    },
    "page_chat": {
        "fr": "Chat documents",
        "en": "Document chat",
    },
    "page_upload": {
        "fr": "Gestion des documents",
        "en": "Document management",
    },
    "page_matrix": {
        "fr": "Matrice de compliance",
        "en": "Compliance matrix",
    },
    "page_about": {
        "fr": "A propos",
        "en": "About",
    },
    "page_normes": {
        "fr": "Normes medicales",
        "en": "Medical standards",
    },
    "annexes_title": {
        "fr": "Annexes",
        "en": "Annexes",
    },
    "db_stats_title": {
        "fr": "Base de connaissances",
        "en": "Knowledge base",
    },
    "db_docs": {
        "fr": "Documents",
        "en": "Documents",
    },
    "db_chunks": {
        "fr": "Chunks",
        "en": "Chunks",
    },
    "db_indexed_docs": {
        "fr": "Documents indexes",
        "en": "Indexed documents",
    },
    "lang_label": {
        "fr": "Langue / Language",
        "en": "Language / Langue",
    },
    "version_info": {
        "fr": (
            "**Version 1.0.0** — Mars 2026\n\n"
            "**App dediee normes medicales**\n"
            "- Base vectorielle pre-indexee\n"
            "- Synchronisation depuis dossier"
        ),
        "en": (
            "**Version 1.0.0** — Mar 2026\n\n"
            "**Dedicated medical standards app**\n"
            "- Pre-indexed vector store\n"
            "- Directory sync"
        ),
    },
    # --- Upload page ---
    "upload_title": {
        "fr": "Charger des documents PDF",
        "en": "Upload PDF documents",
    },
    "upload_help": {
        "fr": "Glissez vos fichiers PDF ici (FDA, ISO, IEC...)",
        "en": "Drop your PDF files here (FDA, ISO, IEC...)",
    },
    "upload_domain_hint": {
        "fr": "Les documents seront indexes dans le domaine **normes medicales**.",
        "en": "Documents will be indexed in the **medical standards** domain.",
    },
    "upload_sync_button": {
        "fr": "Synchroniser depuis le dossier",
        "en": "Sync from directory",
    },
    "upload_sync_processing": {
        "fr": "Synchronisation en cours...",
        "en": "Syncing...",
    },
    "upload_sync_done": {
        "fr": "fichier(s) indexe(s) depuis le dossier",
        "en": "file(s) indexed from directory",
    },
    "upload_sync_uptodate": {
        "fr": "Tous les documents du dossier sont deja indexes.",
        "en": "All documents from the directory are already indexed.",
    },
    "upload_sync_no_dir": {
        "fr": "Dossier source introuvable.",
        "en": "Source directory not found.",
    },
    "upload_button": {
        "fr": "Indexer les documents",
        "en": "Index documents",
    },
    "upload_success": {
        "fr": "documents indexes avec succes",
        "en": "documents indexed successfully",
    },
    "upload_processing": {
        "fr": "Indexation en cours...",
        "en": "Indexing in progress...",
    },
    "upload_done": {
        "fr": "Termine !",
        "en": "Done!",
    },
    "upload_delete": {
        "fr": "Supprimer",
        "en": "Delete",
    },
    "upload_deleted": {
        "fr": "supprime",
        "en": "deleted",
    },
    # --- Chat page ---
    "chat_placeholder": {
        "fr": "Posez une question sur les normes medicales...",
        "en": "Ask a question about medical standards...",
    },
    "chat_welcome": {
        "fr": (
            "Posez une question sur les documents medicaux charges. Exemples :\n"
            "- Quelles sont les exigences de design controls selon la FDA ?\n"
            "- Que dit la FDA sur la validation des procedes ?\n"
            "- Quelles sont les exigences de cybersecurite pour les dispositifs medicaux ?"
        ),
        "en": (
            "Ask a question about the uploaded medical documents. Examples:\n"
            "- What are the FDA design control requirements?\n"
            "- What does the FDA say about process validation?\n"
            "- What are the cybersecurity requirements for medical devices?"
        ),
    },
    "chat_clear": {
        "fr": "Effacer la conversation",
        "en": "Clear conversation",
    },
    "chat_error": {
        "fr": "Erreur lors de la generation",
        "en": "Error during generation",
    },
    "chat_api_missing": {
        "fr": "Cle API Groq non configuree. Ajoutez GROQ_API_KEY dans les secrets.",
        "en": "Groq API key not configured. Add GROQ_API_KEY in secrets.",
    },
    "sources_title": {
        "fr": "Sources",
        "en": "Sources",
    },
    "sources_relevance": {
        "fr": "pertinence",
        "en": "relevance",
    },
    "sources_page": {
        "fr": "page",
        "en": "page",
    },
    "no_documents": {
        "fr": "Aucun document indexe. Chargez des PDFs via Annexes > Gestion des documents.",
        "en": "No documents indexed. Upload PDFs via Annexes > Document management.",
    },
    # --- Matrix page ---
    "matrix_title": {
        "fr": "Matrice de compliance",
        "en": "Compliance matrix",
    },
    "matrix_help": {
        "fr": "Croisez les exigences d'un referentiel avec vos procedures internes.",
        "en": "Cross-reference standard requirements with your internal procedures.",
    },
    "matrix_standard": {
        "fr": "Referentiel",
        "en": "Standard",
    },
    "matrix_requirements_for": {
        "fr": "Exigences",
        "en": "Requirements",
    },
    "matrix_requirement": {
        "fr": "Exigence",
        "en": "Requirement",
    },
    "matrix_status": {
        "fr": "Statut",
        "en": "Status",
    },
    "matrix_gap": {
        "fr": "Ecart identifie",
        "en": "Gap identified",
    },
    "matrix_corrective_action": {
        "fr": "Action corrective",
        "en": "Corrective action",
    },
    "matrix_add_rows_hint": {
        "fr": "Ajoutez des lignes avec le bouton '+' en bas du tableau.",
        "en": "Add rows with the '+' button at the bottom of the table.",
    },
    "matrix_summary": {
        "fr": "Synthese",
        "en": "Summary",
    },
    "matrix_compliant": {
        "fr": "Conforme",
        "en": "Compliant",
    },
    "matrix_partial": {
        "fr": "Partiel",
        "en": "Partial",
    },
    "matrix_non_compliant": {
        "fr": "Non conforme",
        "en": "Non-compliant",
    },
    "matrix_to_evaluate": {
        "fr": "A evaluer",
        "en": "To evaluate",
    },
    "matrix_search_title": {
        "fr": "Recherche dans les documents indexes",
        "en": "Search in indexed documents",
    },
    "matrix_search_placeholder": {
        "fr": "ex: design controls, process validation, CAPA...",
        "en": "e.g.: design controls, process validation, CAPA...",
    },
    "matrix_search_label": {
        "fr": "Rechercher dans les documents charges",
        "en": "Search in uploaded documents",
    },
    "matrix_searching": {
        "fr": "Recherche en cours...",
        "en": "Searching...",
    },
    "matrix_no_results": {
        "fr": "Aucun resultat. Verifiez que des documents sont indexes.",
        "en": "No results. Check that documents are indexed.",
    },
    "matrix_custom_empty": {
        "fr": "Personnalise (vide)",
        "en": "Custom (empty)",
    },
    # --- About page ---
    "about_domain_medical_desc": {
        "fr": (
            "Normes et reglementations pour les dispositifs medicaux : "
            "FDA 21 CFR 820, ISO 13485, IEC 62304, EU MDR, cybersecurite..."
        ),
        "en": (
            "Standards and regulations for medical devices: "
            "FDA 21 CFR 820, ISO 13485, IEC 62304, EU MDR, cybersecurity..."
        ),
    },
}


def t(key: str) -> str:
    """Retourne la traduction pour la langue courante."""
    lang = st.session_state.get("lang", "fr")
    entry = TRANSLATIONS.get(key, {})
    return entry.get(lang, entry.get("fr", key))

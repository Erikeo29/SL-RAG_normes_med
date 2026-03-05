"""Page matrice de compliance : exigences norme vs procedures internes."""
import streamlit as st
import pandas as pd

from config import COLLECTION_NAME
from core.retrieval import retrieve_relevant_chunks
from utils.translations import t


REQUIREMENTS = {
    "FDA 21 CFR 820 (QMSR)": [
        {"clause": "820.20", "requirement": "Management responsibility"},
        {"clause": "820.22", "requirement": "Quality audit"},
        {"clause": "820.25", "requirement": "Personnel"},
        {"clause": "820.30", "requirement": "Design controls"},
        {"clause": "820.40", "requirement": "Document controls"},
        {"clause": "820.50", "requirement": "Purchasing controls"},
        {"clause": "820.60", "requirement": "Identification"},
        {"clause": "820.65", "requirement": "Traceability"},
        {"clause": "820.70", "requirement": "Production and process controls"},
        {"clause": "820.75", "requirement": "Process validation"},
        {"clause": "820.80", "requirement": "Receiving, in-process, and finished device acceptance"},
        {"clause": "820.86", "requirement": "Acceptance status"},
        {"clause": "820.90", "requirement": "Nonconforming product"},
        {"clause": "820.170", "requirement": "Installation"},
        {"clause": "820.184", "requirement": "Device history record"},
        {"clause": "820.198", "requirement": "Complaint files"},
        {"clause": "820.250", "requirement": "Statistical techniques"},
    ],
    "FDA Cybersecurity guidance": [
        {"clause": "V.A", "requirement": "Threat modeling"},
        {"clause": "V.B", "requirement": "Security risk assessment"},
        {"clause": "V.C", "requirement": "Security architecture"},
        {"clause": "VI.A", "requirement": "Authentication and authorization"},
        {"clause": "VI.B", "requirement": "Cryptography"},
        {"clause": "VI.C", "requirement": "Software update and patching"},
        {"clause": "VII", "requirement": "Labeling for cybersecurity"},
        {"clause": "VIII", "requirement": "Postmarket management of cybersecurity"},
    ],
    "FDA Quality System Inspection": [
        {"clause": "QSIT-1", "requirement": "Management controls"},
        {"clause": "QSIT-2", "requirement": "Design controls"},
        {"clause": "QSIT-3", "requirement": "Corrective and preventive action (CAPA)"},
        {"clause": "QSIT-4", "requirement": "Production and process controls"},
    ],
}


def _status_options() -> list[str]:
    """Retourne les options de statut dans la langue courante."""
    return [
        t("matrix_compliant"),
        t("matrix_partial"),
        t("matrix_non_compliant"),
        t("matrix_to_evaluate"),
    ]


def _get_empty_matrix(requirements: list[dict]) -> pd.DataFrame:
    """Cree un DataFrame vierge depuis une liste d'exigences."""
    if not requirements:
        return pd.DataFrame(
            columns=["clause", "requirement", "status", "gap", "action"]
        )
    df = pd.DataFrame(requirements)
    df["status"] = t("matrix_to_evaluate")
    df["gap"] = ""
    df["action"] = ""
    return df


def render_matrix_page():
    """Affiche la matrice de compliance interactive."""
    st.header(t("matrix_title"))
    st.caption(t("matrix_help"))

    # Choix du referentiel
    standard_names = list(REQUIREMENTS.keys()) + [t("matrix_custom_empty")]
    norme = st.selectbox(
        t("matrix_standard"),
        standard_names,
        key="matrix_norme",
    )

    # Reinitialiser la matrice si le referentiel change
    if st.session_state.get("_last_norme") != norme:
        st.session_state["_last_norme"] = norme
        reqs = REQUIREMENTS.get(norme, [])
        st.session_state["matrix_data"] = _get_empty_matrix(reqs)

    if "matrix_data" not in st.session_state:
        reqs = REQUIREMENTS.get(norme, [])
        st.session_state["matrix_data"] = _get_empty_matrix(reqs)

    st.subheader(f"{t('matrix_requirements_for')} — {norme}")

    if st.session_state["matrix_data"].empty:
        st.info(t("matrix_add_rows_hint"))

    edited_df = st.data_editor(
        st.session_state["matrix_data"],
        column_config={
            "clause": st.column_config.TextColumn("Clause", width="small"),
            "requirement": st.column_config.TextColumn(
                t("matrix_requirement"), width="large"
            ),
            "status": st.column_config.SelectboxColumn(
                t("matrix_status"),
                options=_status_options(),
                width="medium",
            ),
            "gap": st.column_config.TextColumn(t("matrix_gap"), width="large"),
            "action": st.column_config.TextColumn(
                t("matrix_corrective_action"), width="large"
            ),
        },
        hide_index=True,
        use_container_width=True,
        num_rows="dynamic",
        key="matrix_editor",
    )

    st.session_state["matrix_data"] = edited_df

    # Metriques de synthese
    st.markdown("---")
    st.subheader(t("matrix_summary"))
    if not edited_df.empty:
        col1, col2, col3, col4 = st.columns(4)
        counts = edited_df["status"].value_counts()
        col1.metric(
            t("matrix_compliant"),
            counts.get(t("matrix_compliant"), 0),
            border=True,
        )
        col2.metric(
            t("matrix_partial"),
            counts.get(t("matrix_partial"), 0),
            border=True,
        )
        col3.metric(
            t("matrix_non_compliant"),
            counts.get(t("matrix_non_compliant"), 0),
            border=True,
        )
        col4.metric(
            t("matrix_to_evaluate"),
            counts.get(t("matrix_to_evaluate"), 0),
            border=True,
        )

    # Recherche RAG
    st.markdown("---")
    st.subheader(t("matrix_search_title"))
    search_query = st.text_input(
        t("matrix_search_label"),
        placeholder=t("matrix_search_placeholder"),
    )
    if search_query:
        with st.spinner(t("matrix_searching")):
            chunks = retrieve_relevant_chunks(
                search_query, n_results=3, collection_name=COLLECTION_NAME
            )
        if chunks:
            for chunk in chunks:
                similarity = max(0, 1 - chunk.get("distance", 1))
                st.markdown(
                    f'<div class="source-card">'
                    f"<strong>{chunk['source']}</strong> — "
                    f"{t('sources_page')} {chunk['page'] + 1} "
                    f"({t('sources_relevance')} : {similarity:.0%})<br>"
                    f"{chunk['text'][:500]}"
                    f"</div>",
                    unsafe_allow_html=True,
                )
        else:
            st.info(t("matrix_no_results"))

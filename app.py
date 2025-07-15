import streamlit as st
from io import StringIO
from utils.pdb_parser import extract_coordinates
from utils.tda_pipeline import compute_persistence
from utils.plot_diagram import plot_persistence_diagram

# Ρυθμίσεις σελίδας
st.set_page_config(page_title="Protein TDA App", page_icon="🧬")

# Τίτλος και υπογραφή
st.title("Topological Analysis of Protein Structures")
st.markdown("👨‍💻 **Developed by Nikos Sampanis**")

# Πληροφορίες στο sidebar
st.sidebar.title("About")
st.sidebar.markdown("🧬 **Protein TDA App**")
st.sidebar.markdown("Developed by **Nikos Sampanis**")
st.sidebar.markdown("[GitHub Repo](https://github.com/your-username/tda-protein-app)")

# Ανεβάζουμε αρχείο
uploaded_file = st.file_uploader("Upload a .pdb file", type="pdb")
if uploaded_file:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    coords = extract_coordinates(stringio)

    st.write(f"Loaded {len(coords)} atoms.")
    diagram = compute_persistence(coords)
    st.pyplot(plot_persistence_diagram(diagram))


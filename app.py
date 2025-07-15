
import streamlit as st
from utils.pdb_parser import extract_coordinates
from utils.tda_pipeline import compute_persistence
from utils.plot_diagram import plot_persistence_diagram

st.title("TDA on Protein Structures")

uploaded_file = st.file_uploader("Upload a .pdb file", type="pdb")
if uploaded_file:
    coords = extract_coordinates(uploaded_file)
    st.write(f"Loaded {len(coords)} atoms.")

    diagram = compute_persistence(coords)
    st.pyplot(plot_persistence_diagram(diagram))

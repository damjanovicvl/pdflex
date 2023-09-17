# main.py
import streamlit as st
from merge_pdf.merge_pdf import merge_pdfs_app
from extract_pages.extract_pages import extract_pages_app

# Specify the directory where the merged and extracted PDFs will be stored
OUTPUT_DIRECTORY = "/home/damjanovicvl/Projects/pdflex/files"

# Set the title and page layout
st.title("PDF Processing Service")

# Page selection sidebar
selected_page = st.sidebar.radio("Select Functionality", ["Merge PDFs", "Extract Pages"])

if selected_page == "Merge PDFs":
    merge_pdfs_app(OUTPUT_DIRECTORY)
elif selected_page == "Extract Pages":
    extract_pages_app(OUTPUT_DIRECTORY)

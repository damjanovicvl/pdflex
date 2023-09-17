import streamlit as st
from PyPDF2 import PdfMerger
import os


# Function to merge PDF files
def merge_pdfs(pdf_files, output_directory):
    merger = PdfMerger()

    for pdf_file, _ in pdf_files:
        merger.append(pdf_file)

    merged_pdf_path = os.path.join(output_directory, "merged.pdf")
    merger.write(merged_pdf_path)
    
    return merged_pdf_path


def merge_pdfs_app(output_directory):

    # Set the title and page layout
    st.title("PDF Merger")

    # List to store uploaded files and their display order
    uploaded_files_info = []

    # Create a list to store uploaded files
    uploaded_files = st.file_uploader("Upload PDF Files", type=["pdf"], accept_multiple_files=True)

    # Display uploaded files and their order
    if uploaded_files:
        st.markdown("### File order in merged file:")
        for i, pdf_file in enumerate(uploaded_files):
            uploaded_files_info.append((pdf_file, pdf_file.name))
            st.write(f"{i+1}. {pdf_file.name}")

    # Merge and download button
    if st.button("Merge"):
        if uploaded_files:
            merged_pdf_path = merge_pdfs(uploaded_files_info, output_directory)
            st.success("PDFs merged successfully!")

            # Provide a download link for the merged PDF
            with open(merged_pdf_path, "rb") as file:
                pdf_bytes = file.read()
                st.download_button(
                    label="Download Merged PDF",
                    data=pdf_bytes,
                    file_name="merged.pdf",
                    key="merged-pdf",
                )
        else:
            st.warning("Please upload at least one PDF file.")
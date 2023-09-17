import streamlit as st
from PyPDF2 import PdfReader, PdfWriter
import tempfile
import os


# Function to extract selected pages from a PDF
def extract_pages(pdf_file, page_numbers, output_directory):
    pdf_reader = PdfReader(pdf_file)
    pdf_writer = PdfWriter()

    for page_num in page_numbers:
        pages_len = len(pdf_reader.pages)
        if 1 <= page_num <= pages_len:
            pdf_writer.add_page(pdf_reader.pages[page_num - 1])

    extracted_pdf_path = os.path.join(output_directory, "extracted.pdf")
    pdf_writer.write(extracted_pdf_path)

    return extracted_pdf_path


def extract_pages_app(output_directory):

    st.title("PDF Page Extractor")

    # Upload a PDF file
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

    if uploaded_file is not None:
        st.sidebar.markdown("## Page Extraction")

        # Display a list of available pages in the PDF
        pdf_reader = PdfReader(uploaded_file)
        pages_len = len(pdf_reader.pages)
        available_pages = list(range(1, pages_len + 1))
        selected_pages = st.sidebar.multiselect("Select pages to extract", available_pages)

        # Extract selected pages when the user clicks the button
        if st.sidebar.button("Extract Pages"):
            if selected_pages:
                extracted_pdf_path = extract_pages(uploaded_file, selected_pages, output_directory)
                st.success("Pages extracted successfully!")
                with open(extracted_pdf_path, "rb") as file:
                    pdf_bytes = file.read()
                    st.download_button(
                        label="Download Extracted PDF",
                        data=pdf_bytes,
                        file_name="extracted.pdf",
                        key="extracted-pdf",
                    )
            else:
                st.warning("Please select at least one page to extract.")
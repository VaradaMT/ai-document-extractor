AI Document Structuring Tool

This project converts an unstructured PDF document into a structured Excel file following a defined Key–Value–Comments format. The tool is built using Python, pandas, and a simple Streamlit interface for easy testing and demonstration.

Overview

The goal of the project is to extract all meaningful information from the provided PDF and organize it into a structured Excel output. The output format is based on the sample “Expected Output.xlsx” provided in the assignment.

The application reads the uploaded PDF, processes the content, maps key information into a structured format, and generates an Output.xlsx file for download.

A live hosted version of the tool is available through Streamlit Cloud.

Features

Extracts content from the uploaded PDF

Converts information into a Key–Value–Comments structure

Preserves original content without summarization or omission

Generates a clean Excel file (Output.xlsx)

Simple and user-friendly Streamlit interface for testing

Tech Stack

Python 3

pdfplumber – PDF text extraction

pandas – Excel generation and table handling

openpyxl – Excel writer engine

Streamlit – Web interface

ai-document-extractor/
│
├── app.py                 # Streamlit application
├── extractor.py           # Core extraction and structuring logic
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── Output.xlsx            # Sample generated output
└── sample_data/
       ├── Data Input.pdf
       └── Expected Output.xlsx
How to Run the Project Locally
1. Install dependencies
pip install -r requirements.txt

2. Start the Streamlit app
streamlit run app.py

3. Upload the PDF

Use the interface to upload Data Input.pdf (or any compatible PDF).
The tool will generate the structured Excel file automatically.

Usage

Open the Streamlit app

Upload a PDF document

Wait for the extraction to complete

Download the generated Output.xlsx file

Live Demo

(Replace the link below with your actual Streamlit app URL)

Live App:
https://ai-document-extractor-staubxethk76t5qzht6mwt.streamlit.app/

Notes

The project follows the format defined in the assignment’s expected output.

The tool ensures that all relevant content from the PDF is captured and represented in the Excel file.

No external ML model is required for this assignment; the extraction logic is rule-based and tailored to the provided input document.

License

This project is intended for educational and assignment purposes.

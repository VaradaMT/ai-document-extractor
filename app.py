import streamlit as st
from extractor import extract_text_from_pdf, extract_key_value_pairs, save_to_excel

st.title("AI Document Structuring Tool")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getvalue())

    text = extract_text_from_pdf("temp.pdf")
    pairs = extract_key_value_pairs(text)

    output_file = save_to_excel(pairs)

    st.success("Extraction completed successfully!")
    st.download_button("Download Excel", open(output_file, "rb").read(), file_name="Output.xlsx")




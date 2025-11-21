import pdfplumber
import pandas as pd
import re

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text


def detect_key_value_pairs(text):
    lines = [line.strip() for line in text.split("\n") if line.strip()]

    extracted = []

    # RULE 1: Split by colon → direct Key:Value
    for line in lines:
        if ":" in line:
            key, value = line.split(":", 1)
            extracted.append([key.strip(), value.strip(), ""])
            continue

        # RULE 2: Detect dates (e.g., 15-Mar-89, 1-Jul-12)
        date_pattern = r"(\d{1,2}[-/][A-Za-z]{3}[-/]\d{2,4})"
        if re.search(date_pattern, line):
            extracted.append(["Detected Date", re.search(date_pattern, line).group(), line])
            continue

        # RULE 3: Fallback → Put important facts into Comments
        extracted.append(["Info", line, "Full sentence captured"])

    return extracted


def save_to_excel(pairs, output_path="Output.xlsx"):
    df = pd.DataFrame(pairs, columns=["Key", "Value", "Comments"])
    df.to_excel(output_path, index=False)
    return output_path

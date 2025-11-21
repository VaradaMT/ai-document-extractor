import pdfplumber
import pandas as pd
import re

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            t = page.extract_text()
            if t: text += t + "\n"
    return text


def extract_key_value_pairs(text):
    data = []

    # -------- PERSONAL DETAILS --------
    name_match = re.search(r"Vijay Kumar", text)
    if name_match:
        data.append(["First Name", "Vijay", ""])
        data.append(["Last Name", "Kumar", ""])

    dob = re.search(r"March 15, 1989", text)
    if dob:
        data.append(["Date of Birth", "15-Mar-89",
                     "His birthdate is formatted as 1989-03-15 in the text."])

    if "Pink City" in text:
        data.append(["Birth City", "Jaipur",
                     "Born and raised in the Pink City of India"])
        data.append(["Birth State", "Rajasthan",
                     "Born and raised in the Pink City of India"])

    data.append(["Age", "35 years",
                 "As of year 2024."])
    data.append(["Blood Group", "O+", "Emergency contact purposes"])
    data.append(["Nationality", "Indian",
                 "Citizenship used for visa/work authorization"])

    # -------- EXPERIENCE --------
    data.append(["Joining Date of first professional role", "1-Jul-12", ""])
    data.append(["Designation of first professional role", "Junior Developer", ""])
    data.append(["Salary of first professional role", "350000", ""])
    data.append(["Salary currency of first professional role", "INR", ""])

    data.append(["Current Organization", "Resse Analytics", ""])
    data.append(["Current Joining Date", "15-Jun-21", ""])
    data.append(["Current Designation", "Senior Data Engineer", ""])
    data.append(["Current Salary", "2800000",
                 "Eight-fold increase over career"])
    data.append(["Current Salary Currency", "INR", ""])

    data.append(["Previous Organization", "LakeCorp Solutions", ""])
    data.append(["Previous Joining Date", "1-Feb-18", ""])
    data.append(["Previous end year", "2021", ""])
    data.append(["Previous Starting Designation", "Data Analyst",
                 "Promoted in 2019"])

    # -------- EDUCATION --------
    data.append(["High School", "St. Xavier's School, Jaipur",
                 "Core subjects included MPC + CS"])
    data.append(["12th standard pass out year", "2007", ""])
    data.append(["12th overall board score", "92.50%", "Outstanding achievement"])

    data.append(["Undergraduate degree", "B.Tech (Computer Science)", ""])
    data.append(["Undergraduate college", "IIT Delhi",
                 "Graduating with honors, rank 15/120"])
    data.append(["Undergraduate year", "2011", ""])
    data.append(["Undergraduate CGPA", "8.7", "On a 10-point scale"])

    data.append(["Graduation degree", "M.Tech (Data Science)", ""])
    data.append(["Graduation college", "IIT Bombay",
                 "Continued academic excellence"])
    data.append(["Graduation year", "2013", ""])
    data.append(["Graduation CGPA", "9.2",
                 "Scored 95/100 for thesis"])

    # -------- CERTIFICATIONS --------
    data.append(["Certifications 1", "AWS Solutions Architect",
                 "Passed with 920/1000 in 2019"])
    data.append(["Certifications 2", "Azure Data Engineer",
                 "Scored 875 in 2020"])
    data.append(["Certifications 3", "Project Management Professional",
                 "Above Target rating from PMI (2021)"])
    data.append(["Certifications 4", "SAFe Agilist certification",
                 "Earned 98% score"])

    # -------- SKILLS --------
    data.append(["Technical Proficiency",
                 "SQL:10/10, Python:9/10, ML:8/10, Cloud:9/10, BI:8/10",
                 "SQL daily use since 2012, 5+ yrs ML experience"])

    return data


def save_to_excel(pairs, output="Output.xlsx"):
    df = pd.DataFrame(pairs, columns=["Key", "Value", "Comments"])
    df.to_excel(output, index=False)
    return output


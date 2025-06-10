import pdfplumber
import pandas as pd

pdf_path = r"D:\sample\sample-tables.pdf"
excel_path = r"D:\sample\sample.xlsx"

all_rows = []

with pdfplumber.open(pdf_path) as pdf:
    for i, page in enumerate(pdf.pages):
        words = page.extract_words()
        tables = page.extract_tables()

        for j, table in enumerate(tables):
            df = pd.DataFrame(table)

            # Get table bounding box
            table_bbox = page.find_tables()[j].bbox

            # Extract heading above the table
            heading_lines = [
                w['text'] for w in words
                if w['bottom'] < table_bbox[1] and w['bottom'] > table_bbox[1] - 50
            ]
            heading_text = " ".join(heading_lines).strip() if heading_lines else "Heading Not Found"

            # Add column headings
            col_headers = df.iloc[0].tolist()
            for col in col_headers:
                all_rows.append([heading_text, col, "Column"])

            # Add row values
            for row in df.iloc[1:].values.tolist():
                for val in row:
                    all_rows.append([heading_text, val, "Row"])

# Write to single Excel sheet
final_df = pd.DataFrame(all_rows, columns=["Heading", "Value", "Type"])
final_df.to_excel(excel_path, index=False, sheet_name="AllData")

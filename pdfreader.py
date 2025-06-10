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

            # Bounding box for heading extraction
            table_bbox = page.find_tables()[j].bbox

            # Get heading text above the table
            heading_lines = [
                w['text'] for w in words
                if w['bottom'] < table_bbox[1] and w['bottom'] > table_bbox[1] - 50
            ]
            heading_text = " ".join(heading_lines).strip() if heading_lines else "Heading Not Found"

            # First row = column headers
            col_headers = df.iloc[0].tolist()

            # Add column headers as Label
            for col in col_headers[1:]:  # skip row label header
                col_text = col if col else "N/A"
                label = f"{col_text} - {col_text} - {col_text}"
                all_rows.append([heading_text, label, "Column"])

            # Add row entries
            for row in df.iloc[1:].values.tolist():
                row_label = row[0].strip() if row[0] else "N/A"
                for idx, val in enumerate(row[1:], start=1):
                    col_name = col_headers[idx] if idx < len(col_headers) else f"Col{idx}"
                    value = val.strip() if val else "N/A"
                    label = f"{row_label} - {col_name} - {value}"
                    all_rows.append([heading_text, label, "Row"])

# Save to Excel
final_df = pd.DataFrame(all_rows, columns=["Heading", "Label", "Type"])
final_df.to_excel(excel_path, index=False, sheet_name="AllData")

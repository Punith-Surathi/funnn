import pdfplumber
import pandas as pd

pdf_path = r"D:\sample\sample-tables.pdf"
excel_path = r"D:\sample\sample.xlsx"

all_entries = []

with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        words = page.extract_words()
        tables = page.extract_tables()

        for i, table in enumerate(tables):
            df = pd.DataFrame(table)

            if df.empty or df.shape[1] < 2:
                continue

            # Get table bounding box
            table_bbox = page.find_tables()[i].bbox

            # Get heading above the table
            heading_lines = [
                w['text'] for w in words
                if w['bottom'] < table_bbox[1] and w['bottom'] > table_bbox[1] - 50
            ]
            heading = " ".join(heading_lines).strip() or "Heading Not Found"

            # Extract column headers (skip the first column which is row labels)
            col_headers = df.iloc[0, 1:]
            for col in col_headers:
                clean_col = str(col).strip()
                if clean_col:  # Only add non-empty
                    all_entries.append([heading, clean_col, "Column"])

            # Extract row labels (skip header row, get first column only)
            for row in df.iloc[1:].values.tolist():
                row_label = str(row[0]).strip()
                if row_label:  # Only add non-empty
                    all_entries.append([heading, row_label, "Row"])

# Convert and save to Excel
final_df = pd.DataFrame(all_entries, columns=["Heading", "Label", "Type"])
final_df.to_excel(excel_path, index=False, sheet_name="AllData")
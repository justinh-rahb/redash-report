from openpyxl import styles
import pandas as pd


def create_xlsx_report(data, title, time_period):
    xlsx_file = f"{title} {time_period}.xlsx"
    
    with pd.ExcelWriter(xlsx_file, engine='openpyxl') as writer:
        data.to_excel(writer, index=False, startrow=2)  # Start writing CSV data from the third row
        
        # Get the active worksheet
        sheet = writer.sheets['Sheet1']
        
        # Set column widths
        for column in sheet.columns:
            max_length = max(len(str(cell.value)) for cell in column)
            sheet.column_dimensions[column[0].column_letter].width = max_length
        
        # Define a cell style for bold and larger font
        bold_large_font = styles.Font(bold=True, size=14)
        
        # Insert the title, time period, and total count in the specified cells
        title_cell = sheet['B1']
        title_cell.value = title
        title_cell.font = bold_large_font
        
        date_cell = sheet['D1']
        date_cell.value = time_period
        date_cell.font = bold_large_font
        
        total_cell = sheet['F1']
        total_cell.value = f"Total Count: {len(data)}"
        total_cell.font = bold_large_font
        
    return xlsx_file

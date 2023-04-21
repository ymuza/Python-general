import pandas as pd
import numpy as np
from fpdf import FPDF

df = pd.DataFrame({'Region': ['North', 'North', 'South', 'South', 'East', 'West', 'West', 'East'],
                   'Product': ['A', 'B', 'C', 'B', 'A', 'C', 'B', 'A'],
                   'Sales': [100, 200, 300, 150, 250, 175, 125, 225]})


pivot_table = pd.pivot_table(df, index=['Region'], columns=['Product'], values=['Sales'], aggfunc=np.sum)


pdf = FPDF()
pdf.add_page()

# Set the font and size for the report title
pdf.set_font("Arial", size=16)
pdf.cell(200, 10, txt="Sales by Region and Product", ln=1, align="C")

# Set the font and size for the table header
pdf.set_font("Arial", size=12)
pdf.cell(50, 10, txt="Region", border=1, align="C")
pdf.cell(50, 10, txt="Product A", border=1, align="C")
pdf.cell(50, 10, txt="Product B", border=1, align="C")
pdf.cell(50, 10, txt="Product C", border=1, align="C")
pdf.ln()

# Set the font and size for the table body
pdf.set_font("Arial", size=10)
for index, row in pivot_table.iterrows():
    pdf.cell(50, 10, str(index), border=1, align="C")
    pdf.cell(50, 10, str(row['Sales']['A']), border=1, align="C")
    pdf.cell(50, 10, str(row['Sales']['B']), border=1, align="C")
    pdf.cell(50, 10, str(row['Sales']['C']), border=1, align="C")
    pdf.ln()

 # Draw a horizontal line
pdf.line(10, pdf.get_y() + 10, 200, pdf.get_y() + 10)
# Save the PDF report
pdf.output("sales_report.pdf")



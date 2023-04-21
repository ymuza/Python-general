from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

# Load the Jinja2 template environment
env = Environment(loader=FileSystemLoader('.'))

# Define the context variables
context = {
    'title': 'My Document',
    'heading': 'Welcome to my website!',
    'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
}

# Render the template with Jinja2
template = env.get_template('template1.html')
html_out = template.render(**context)

# Convert the HTML to PDF with WeasyPrint
HTML(string=html_out).write_pdf('output.pdf')

print("Hola Moises")
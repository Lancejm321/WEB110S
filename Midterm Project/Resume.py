# Install fpdf if you haven't already:
# pip install fpdf

from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Logo: Draw a circle with initials "JL" in the top-left corner.
        self.set_xy(10, 8)
        self.set_fill_color(220, 220, 220)  # light grey background for the circle
        self.ellipse(10, 8, 15, 15, style='F')  # draw filled ellipse (circle)
        self.set_xy(10, 8)
        self.set_font("Arial", 'B', 12)
        self.cell(15, 15, "JL", border=0, ln=0, align="C")
        
        # Title (Name and contact) centered in header
        self.set_xy(30, 10)
        self.set_font("Arial", 'B', 16)
        self.cell(0, 10, "Jason Lance", ln=1)
        self.set_font("Arial", '', 10)
        self.set_xy(30, 18)
        self.cell(0, 10, "Manhattan, KS | lancejm321@gmail.com | (123) 456-7890", ln=1)
        self.set_xy(30, 24)
        self.cell(0, 10, "Portfolio: https://lancejm321.github.io/WEB110S/Midterm%20Project/index.html", ln=1)
        self.ln(5)

    def footer(self):
        # Page footer
        self.set_y(-15)
        self.set_font("Arial", 'I', 8)
        self.cell(0, 10, f"Page {self.page_no()}", align='C')

# Create instance of PDF class
pdf = PDF()
pdf.alias_nb_pages()
pdf.add_page()

# Professional Summary
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, "Professional Summary", ln=1)
pdf.set_font("Arial", '', 11)
summary = ("Disciplined and creative professional with a background in web development, logistics, and military operations. "
           "Brings a unique combination of technical knowledge, leadership, and problem-solving skills gained from military service and technical education. "
           "Dedicated to continuous improvement and adaptable across industries.")
pdf.multi_cell(0, 8, summary)
pdf.ln(5)

# Skills Section
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, "Skills", ln=1)
pdf.set_font("Arial", '', 11)
skills = [
    "Web Development: HTML (1 year), CSS (1 year), Basic Web Development (1 year), Portfolio Website Creation",
    "Military & Operations: Heavy Equipment Operating (4 years), Leadership, Technical Skills, Problem Solving",
    "Professional: Time Management, Creative Thinking",
    "Certifications: Forklift Operating, Microsoft Office Certified, CPR Certified, Military Heavy Equipment Operations"
]
for skill in skills:
    pdf.cell(0, 8, f"• {skill}", ln=1)
pdf.ln(5)

# Achievements Section
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, "Achievements", ln=1)
pdf.set_font("Arial", '', 11)
achievements = [
    "Successfully designed and launched personal portfolio website",
    "Army Achievement Medal – Southwest Border Mission",
    "Army National Defense Service Ribbon – War-time service",
    "Army National Guard Service Ribbon – 4 years of service",
    "Army Armed Forces Reserve Medal w/ 'M' device – Mobilization recognition",
    "Norwegian Foot March Medal – Completed 19 miles with 35 lbs in 4.5 hours"
]
for ach in achievements:
    pdf.cell(0, 8, f"• {ach}", ln=1)
pdf.ln(5)

# Experience Section
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, "Experience", ln=1)
pdf.set_font("Arial", '', 11)

# Army National Guard Experience
pdf.cell(0, 8, "Army National Guard — Heavy Equipment Operator (2019 – Present)", ln=1)
exp1 = ("- Operated and maintained heavy construction equipment in demanding environments.\n"
        "- Led and trained teams in safety, maintenance, and operations.\n"
        "- Delivered projects under tight deadlines and changing conditions.")
pdf.multi_cell(0, 8, exp1)
pdf.ln(2)

# Shipping Coordinator
pdf.cell(0, 8, "Shipping Coordinator — [Company Name] (2022 – 2023)", ln=1)
exp2 = ("- Coordinated inbound/outbound shipments with precision.\n"
        "- Managed inventory and optimized warehouse operations.\n"
        "- Ensured logistics met customer and business needs.")
pdf.multi_cell(0, 8, exp2)
pdf.ln(2)

# Cargo Loader
pdf.cell(0, 8, "Cargo Loader (Train Intermodal) — [Company Name] (2021 – 2022)", ln=1)
exp3 = ("- Safely loaded freight in fast-paced rail yard environments.\n"
        "- Collaborated with teams to improve loading processes.\n"
        "- Adhered to safety regulations and inspection protocols.")
pdf.multi_cell(0, 8, exp3)
pdf.ln(5)

# Education Section
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, "Education", ln=1)
pdf.set_font("Arial", '', 11)
pdf.cell(0, 8, "Johnson County Community College — Associate's in Computer Science (In Progress)", ln=1)
pdf.cell(0, 8, "Expected Graduation: [Insert Year]", ln=1)
pdf.ln(5)

# Save the PDF
output_filename = "Jason_Lance_Resume.pdf"
pdf.output(output_filename)
print(f"PDF resume generated successfully as '{output_filename}'!")
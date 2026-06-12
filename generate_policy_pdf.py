import os
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

class PolicyCanvas(canvas.Canvas):
    """
    Custom canvas to draw professional page border and branding.
    """
    def draw_decorations(self):
        self.saveState()
        # Top banner accent line (deep blue)
        self.setFillColor(colors.HexColor("#1e3a8a"))
        self.rect(36, 756, 540, 6, fill=True, stroke=False)
        
        # Bottom branding footer
        self.setFont("Helvetica-Bold", 7.5)
        self.setFillColor(colors.HexColor("#64748b"))
        self.drawString(36, 25, "CAMPUS PLACEMENT CELL | INTEGRITY & TECHNOLOGY STANDARDS")
        self.drawRightString(576, 25, "EFFECTIVE: 2025-2026 CYCLE")
        
        # Thin divider at bottom
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.5)
        self.line(36, 36, 576, 36)
        self.restoreState()

    def showPage(self):
        self.draw_decorations()
        super().showPage()

def build_policy():
    pdf_filename = "Day3_AI_Policy.pdf"
    
    # 0.5 inch margins (36 pt) to maximize printable vertical space (720 pt height available)
    doc = SimpleDocTemplate(
        pdf_filename,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=45,
        bottomMargin=45
    )

    styles = getSampleStyleSheet()
    
    # Define custom styling palette
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=18,
        textColor=colors.HexColor('#1e3a8a'),
        alignment=1, # Centered
        spaceAfter=3
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12,
        textColor=colors.HexColor('#475569'),
        alignment=1, # Centered
        spaceAfter=12
    )
    
    h1_style = ParagraphStyle(
        'SectionHeaderCustom',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        textColor=colors.HexColor('#1e3a8a'),
        spaceBefore=8,
        spaceAfter=4,
        keepWithNext=True
    )
    
    body_style = ParagraphStyle(
        'BodyCustom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor('#334155'),
        spaceAfter=4
    )

    table_header_style = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=colors.white
    )

    table_cell_style = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.5,
        leading=9.5,
        textColor=colors.HexColor('#334155')
    )

    table_cell_bold_style = ParagraphStyle(
        'TableCellBold',
        parent=table_cell_style,
        fontName='Helvetica-Bold'
    )

    story = []

    # Title & Subtitle
    story.append(Paragraph("PLACEMENT-CELL STUDENT AI-USE POLICY", title_style))
    story.append(Paragraph("Enforceable guidelines for responsible and ethical generative AI adoption in career activities", subtitle_style))

    # Section 1: EU AI Act Scenario Classification Matrix
    story.append(Paragraph("1. Student-AI Scenario Classification Matrix (EU AI Act Framework)", h1_style))
    story.append(Paragraph(
        "To ensure career fairness, all activities are categorized under four risk tiers. Students must strictly adhere to these rules.",
        body_style
    ))
    
    # Classification Table
    # Colors: Unacceptable (crimson), High-risk (amber), Limited (navy), Minimal (slate)
    data = [
        [
            Paragraph("Scenario Description", table_header_style), 
            Paragraph("Risk Tier", table_header_style), 
            Paragraph("Reasoning & Enforceable Conditions", table_header_style)
        ],
        [
            Paragraph("1. AI résumé editing & polishing", table_cell_style),
            Paragraph("<font color='#1e3a8a'><b>Limited</b></font>", table_cell_bold_style),
            Paragraph("Allowed. Substance must remain the student's; AI may only refine language/grammar.", table_cell_style)
        ],
        [
            Paragraph("2. AI mock interview practice", table_cell_style),
            Paragraph("<font color='#475569'><b>Minimal</b></font>", table_cell_bold_style),
            Paragraph("Allowed. Personal study aid; does not affect recruiter evaluation directly.", table_cell_style)
        ],
        [
            Paragraph("3. AI-written application essays", table_cell_style),
            Paragraph("<font color='#d97706'><b>High-risk</b></font>", table_cell_bold_style),
            Paragraph("Allowed with mentor check + explicit student declaration of AI usage.", table_cell_style)
        ],
        [
            Paragraph("4. AI-assisted GitHub portfolio projects", table_cell_style),
            Paragraph("<font color='#d97706'><b>High-risk</b></font>", table_cell_bold_style),
            Paragraph("Allowed subject to a mandatory oral code defense before placement drive.", table_cell_style)
        ],
        [
            Paragraph("5. AI in graded internal assignments", table_cell_style),
            Paragraph("<font color='#b91c1c'><b>Unacceptable</b></font>", table_cell_bold_style),
            Paragraph("Banned for direct skill tests. Limited with disclosure for application tests.", table_cell_style)
        ],
        [
            Paragraph("6. AI-generated CGPA/marks on résumé", table_cell_style),
            Paragraph("<font color='#b91c1c'><b>Unacceptable</b></font>", table_cell_bold_style),
            Paragraph("Outright ban. Considered academic credentials falsification and fraud.", table_cell_style)
        ],
        [
            Paragraph("7. AI-cloned voice for video interviews", table_cell_style),
            Paragraph("<font color='#b91c1c'><b>Unacceptable</b></font>", table_cell_bold_style),
            Paragraph("Outright ban. Fabricates student identity and compromises recruiter trusts.", table_cell_style)
        ],
        [
            Paragraph("8. AI skills self-assessment tools", table_cell_style),
            Paragraph("<font color='#475569'><b>Minimal</b></font>", table_cell_bold_style),
            Paragraph("Allowed. Private tool for student self-reflection and mock evaluation.", table_cell_style)
        ]
    ]
    
    # 540 pt width available (612 - 72)
    t = Table(data, colWidths=[1.8*inch, 0.9*inch, 4.8*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1e3a8a')),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,0), 4),
        ('TOPPADDING', (0,0), (-1,0), 4),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f8fafc')]),
        ('BOTTOMPADDING', (0,1), (-1,-1), 3),
        ('TOPPADDING', (0,1), (-1,-1), 3),
    ]))
    story.append(t)
    story.append(Spacer(1, 4))

    # Section 2: Permitted Uses
    story.append(Paragraph("2. Permitted Uses (Allowed Actionable Items)", h1_style))
    story.append(Paragraph("1. AI may be used to: rewrite and optimize resume bullet points for better verb choice and clarity.", body_style))
    story.append(Paragraph("2. AI may be used to: simulate live mock interview dialogues for private practice and feedback.", body_style))
    story.append(Paragraph("3. AI may be used to: clarify complex technical topics, algorithms, or OS fundamentals during study mode.", body_style))
    story.append(Paragraph("4. AI may be used to: format raw codebase files and generate inline code comments for clarity.", body_style))
    story.append(Paragraph("5. AI may be used to: structure structured study schedules and outlines from target syllabi.", body_style))
    story.append(Paragraph("6. AI may be used to: identify bugs and suggest code refinements for personal practice projects.", body_style))

    # Section 3: Prohibited Uses & Detection Methods
    story.append(Paragraph("3. Prohibited Uses & Enforceable Detection Methods", h1_style))
    story.append(Paragraph(
        "<b>Rule 1:</b> AI may NOT be used to fabricate experiences, projects, or internships that the student did not complete.<br/>"
        "<i>Detection Method:</i> Mandatory oral defenses on resume projects, requiring live code walkthroughs and architectural reasoning.",
        body_style
    ))
    story.append(Paragraph(
        "<b>Rule 2:</b> AI may NOT be used to alter, generate, or fake academic data (CGPA, active backlogs, or test scores).<br/>"
        "<i>Detection Method:</i> Automatic database cross-referencing against the university's academic registrar portal.",
        body_style
    ))
    story.append(Paragraph(
        "<b>Rule 3:</b> AI may NOT be used to clone a student's voice or use deepfakes for asynchronous recruiter video submissions.<br/>"
        "<i>Detection Method:</i> Recruiter integration of random live challenge questions and multi-factor biometric checks.",
        body_style
    ))
    story.append(Paragraph(
        "<b>Rule 4:</b> AI may NOT be used to ghostwrite application essays where student voice is the primary grading criteria.<br/>"
        "<i>Detection Method:</i> Stylometric analysis comparing motivation essays with 2-3 historical in-class writing samples.",
        body_style
    ))

    # Section 4: Enforcement
    story.append(Paragraph("4. Enforcement & Compliance Statement", h1_style))
    story.append(Paragraph(
        "The placement cell will conduct random oral project defenses and academic checks on 20% of placed students. "
        "Verified violations of Prohibited Uses will result in a formal written warning and a mandatory re-evaluation for the first offense, "
        "while a second infraction will lead to immediate suspension of placement assistance for the current academic cycle. "
        "The cell acknowledges that AI usage cannot be fully monitored in private; the policy relies on student integrity and "
        "understanding the severe long-term career risks of credential fraud.",
        body_style
    ))

    # Build PDF using custom PolicyCanvas to ensure branding and decorations are drawn
    doc.build(story, canvasmaker=PolicyCanvas)
    print(f"Generated {pdf_filename} successfully.")

if __name__ == "__main__":
    build_policy()

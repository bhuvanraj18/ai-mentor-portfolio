import os
import sys
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    """
    Canvas to calculate total page count dynamically for the brief.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            super().showPage()
        super().save()

    def draw_page_number(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 9)
        self.setFillColor(colors.HexColor("#64748b"))
        # Header (on page 2 only)
        if self._pageNumber > 1:
            self.drawString(54, 750, "TCS Placement-Prep Brief (2025-2026)")
            self.setStrokeColor(colors.HexColor("#cbd5e1"))
            self.setLineWidth(0.5)
            self.line(54, 742, 612-54, 742)
        
        # Footer
        page_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(612 - 54, 36, page_text)
        self.drawString(54, 36, "Confidential - B.Tech Freshers Career Guidance")
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.5)
        self.line(54, 48, 612-54, 48)
        self.restoreState()


class DeckCanvas(canvas.Canvas):
    """
    Canvas for drawing premium dark slides.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pages = []

    def showPage(self):
        self.pages.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self.pages)
        for page in self.pages:
            self.__dict__.update(page)
            self.draw_slide_background()
            self.draw_slide_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_slide_background(self):
        self.saveState()
        # Create a beautiful dark gradient-like solid background
        self.setFillColor(colors.HexColor("#0f172a"))
        self.rect(0, 0, 792, 612, fill=True, stroke=False)
        # Decorative top glow line
        self.setFillColor(colors.HexColor("#38bdf8"))
        self.rect(0, 608, 792, 4, fill=True, stroke=False)
        self.restoreState()

    def draw_slide_decorations(self, page_count):
        self.saveState()
        # Footer
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748b"))
        self.drawString(36, 24, "TCS Placement Prep Masterclass | 2025-2026 Batch")
        self.drawRightString(792 - 36, 24, f"Slide {self._pageNumber} of {page_count}")
        
        # Bottom divider
        self.setStrokeColor(colors.HexColor("#1e293b"))
        self.setLineWidth(1)
        self.line(36, 36, 792 - 36, 36)
        self.restoreState()


def build_brief():
    pdf_filename = "Day4_TCS_brief.pdf"
    doc = SimpleDocTemplate(
        pdf_filename,
        pagesize=letter,
        leftMargin=54, # 0.75 in
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=colors.HexColor('#0f172a'),
        spaceAfter=15
    )
    
    h1_style = ParagraphStyle(
        'SectionHeading',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=16,
        textColor=colors.HexColor('#1e3a8a'),
        spaceBefore=12,
        spaceAfter=6,
        keepWithNext=True
    )
    
    body_style = ParagraphStyle(
        'BodyTextCustom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor('#334155'),
        spaceAfter=8
    )
    
    bullet_style = ParagraphStyle(
        'BulletCustom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor('#334155'),
        leftIndent=15,
        firstLineIndent=-10,
        spaceAfter=5
    )

    story = []

    # Title
    story.append(Paragraph("TCS Placement-Prep Brief (2025-2026)", title_style))
    story.append(Paragraph("<b>Target Audience:</b> B.Tech 3rd and 4th-year students preparing for campus hiring.", body_style))
    story.append(Paragraph("<b>Author:</b> Bhuvan, Placement Coach & Mentor", body_style))
    story.append(Spacer(1, 10))

    # Section 1: Overview
    story.append(Paragraph("1. Overview", h1_style))
    story.append(Paragraph(
        "Tata Consultancy Services (TCS) is one of the world's largest IT services, consulting, and business solutions organizations. "
        "Historically renowned for high-volume campus recruitment, TCS is executing a major strategic pivot in 2025-2026. "
        "The company is transitioning from massive volume-based hiring to highly targeted talent acquisition, prioritizing tech skills "
        "and technical competence in high-impact domains.",
        body_style
    ))

    # Section 2: Hiring Process
    story.append(Paragraph("2. Hiring Process & Round Details", h1_style))
    story.append(Paragraph(
        "TCS selects candidates primarily through the <b>National Qualifier Test (NQT)</b>, followed by standard interviews. "
        "The process consists of the following phases:",
        body_style
    ))
    story.append(Paragraph(
        "• <b>Online Written Assessment (TCS NQT):</b> Splits into two key parts. <i>Part A (Foundation)</i> is mandatory for all and tests Numerical Ability, Verbal Ability, and Logical Reasoning. <i>Part B (Advanced)</i> is mandatory for Digital and Prime roles, testing Advanced Quantitative, Advanced Reasoning, and Advanced Coding (typically 2 coding questions to be solved in 90 minutes).",
        bullet_style
    ))
    story.append(Paragraph(
        "• <b>Technical Interview (TR):</b> Detailed face-to-face or virtual evaluation of the candidate's core coding logic, data structures, algorithms, academic projects, and programming fundamentals (typically in Python, Java, or C++).",
        bullet_style
    ))
    story.append(Paragraph(
        "• <b>Managerial Interview (MR):</b> Assesses analytical capabilities, problem-solving under pressure, situation response, and project architectures.",
        bullet_style
    ))
    story.append(Paragraph(
        "• <b>HR Interview:</b> Evaluates soft skills, communication clarity, willingness to relocate, shift flexibility, and overall cultural alignment with TCS values.",
        bullet_style
    ))

    # Section 3: Technical Stack
    story.append(Paragraph("3. Target Technical Stack", h1_style))
    story.append(Paragraph(
        "TCS recruits generalist problem-solvers and puts them through the structured <b>TCS Xplore</b> digital onboarding program "
        "to align them with standard company stacks. High-priority technologies include:",
        body_style
    ))
    story.append(Paragraph("• <b>Foundational Languages:</b> Java (Standard & Enterprise Edition), Python, and C/C++ (for logic).", bullet_style))
    story.append(Paragraph("• <b>Web Technologies:</b> HTML5, CSS3, ES6 JavaScript, and responsive design frameworks.", bullet_style))
    story.append(Paragraph("• <b>Systems & Databases:</b> Unix/Linux shell scripting, SQL (Oracle/MySQL), and relational database concepts.", bullet_style))
    story.append(Paragraph("• <b>Prime/Digital Cadres:</b> Amazon Web Services (AWS) / Microsoft Azure, AI/ML (scikit-learn, TensorFlow), Docker, and DevOps pipelines.", bullet_style))

    # Section 4: Eligibility Criteria & Packages
    story.append(Paragraph("4. Eligibility Criteria & CTC Structure", h1_style))
    story.append(Paragraph(
        "The eligibility rules are strictly enforced. Below are the core requirements and the corresponding packages based on performance:",
        body_style
    ))
    
    # Eligibility rules
    story.append(Paragraph("• <b>Academic Aggregate:</b> 60% or 6.0 CGPA throughout 10th, 12th, and B.Tech.", bullet_style))
    story.append(Paragraph("• <b>Backlog Policy:</b> Maximum of 1 active backlog permitted at the time of online registration.", bullet_style))
    story.append(Paragraph("• <b>Education Gaps:</b> Maximum gap of 24 months is allowed, which must be officially documented.", bullet_style))
    story.append(Spacer(1, 5))

    # Package Table
    data = [
        ["Cadre / Role", "Primary Skill Focus", "Annual Package (CTC)"],
        ["Ninja", "Standard App Development, Testing, Support", "₹3.36 LPA"],
        ["Digital", "Enterprise Web Apps, Cloud, Data Engineering", "₹7.0 - 7.3 LPA"],
        ["Prime", "AI/ML Engineering, Cloud Native Architecture, R&D", "₹9.0 - 9.6 LPA"]
    ]
    t = Table(data, colWidths=[1.8*inch, 3.2*inch, 2.0*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1e3a8a')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 9),
        ('BOTTOMPADDING', (0,0), (-1,0), 6),
        ('TOPPADDING', (0,0), (-1,0), 6),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,1), (-1,-1), 8.5),
        ('TEXTCOLOR', (0,1), (-1,-1), colors.HexColor('#334155')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f8fafc')]),
        ('BOTTOMPADDING', (0,1), (-1,-1), 5),
        ('TOPPADDING', (0,1), (-1,-1), 5),
    ]))
    story.append(t)
    story.append(Spacer(1, 10))

    # Page Break to enforce 2 pages cleanly
    story.append(PageBreak())

    # Section 5: Recent News (2025-2026)
    story.append(Paragraph("5. Recent News & Developments (2025-2026)", h1_style))
    story.append(Paragraph(
        "Based on the TCS Annual General Meeting (AGM) held in June 2026, students must be aware of the following pivots:",
        body_style
    ))
    story.append(Paragraph(
        "• <b>AI-Driven Operations:</b> TCS Chairman N. Chandrasekaran highlighted that TCS is systematically deploying AI agents to handle routine tasks and augment operations, decreasing the demand for low-skilled coding roles.",
        bullet_style
    ))
    story.append(Paragraph(
        "• <b>End of Massive Volume Hiring:</b> The era of mass campus recruitment (hiring 40k+ freshers in a single go without rigorous filters) is ending. TCS is transitioning to targeted skill-based assessments to fill exact pipeline requirements.",
        bullet_style
    ))
    story.append(Paragraph(
        "• <b>Security and Integrity:</b> Strict anti-cheating protocols are being implemented for the NQT, and verification procedures for certificates/skills have been tightened to combat credential fraud.",
        bullet_style
    ))

    # Section 6: Actionable Prep Tips
    story.append(Paragraph("6. Preparation Action Plan (For B.Tech 3rd & 4th Years)", h1_style))
    story.append(Paragraph(
        "To target Digital or Prime roles, follow these five structured preparation steps:",
        body_style
    ))
    story.append(Paragraph("1. <b>Master Core Data Structures:</b> Focus on recursion, arrays, strings, hash maps, and sorting algorithms in Python or Java.", bullet_style))
    story.append(Paragraph("2. <b>Solve Advanced Coding:</b> Complete at least 100 Medium-level coding questions on platforms like LeetCode or GeeksforGeeks.", bullet_style))
    story.append(Paragraph("3. <b>Build a Substantial Project:</b> Develop a full-stack web application or an AI/ML prototype. Be ready to explain its database schema, APIs, and scaling bottlenecks.", bullet_style))
    story.append(Paragraph("4. <b>Prepare for NQT Aptitude:</b> Spend 20-30 hours practicing advanced data interpretation, logical deduction, and quantitative reasoning.", bullet_style))
    story.append(Paragraph("5. <b>Register Early on NextStep:</b> Set up your TCS NextStep profile, generate your CT/DT reference ID, and submit error-free academic details.", bullet_style))

    # Section 7: Grounded Citations
    story.append(Paragraph("7. Grounded Sources", h1_style))
    story.append(Paragraph("1. TCS Official NextStep Recruitment Portal: <font color='#1e3a8a'><u>https://nextstep.tcs.com</u></font>", bullet_style))
    story.append(Paragraph("2. TCS India All-India NQT Hiring Page: <font color='#1e3a8a'><u>https://www.tcs.com/careers/india/tcs-all-india-nqt-hiring</u></font>", bullet_style))
    story.append(Paragraph("3. TCS AGM June 2026 Chairman's Address on AI and Talent Acquisition Trends.", bullet_style))
    story.append(Paragraph("4. TCS Xplore Program Guide & Training Documentation.", bullet_style))

    # Build PDF
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Generated {pdf_filename} successfully.")


def build_deck():
    pdf_filename = "Day4_TCS_deck.pdf"
    # Create landscape document
    doc = SimpleDocTemplate(
        pdf_filename,
        pagesize=landscape(letter), # 11 x 8.5 inches (792 x 612 points)
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()
    
    # Premium Dark Theme Styles
    slide_title_style = ParagraphStyle(
        'SlideTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=26,
        leading=30,
        textColor=colors.HexColor('#ffffff'),
        spaceAfter=15,
        keepWithNext=True
    )
    
    slide_subtitle_style = ParagraphStyle(
        'SlideSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=13,
        leading=18,
        textColor=colors.HexColor('#38bdf8'), # Sky Blue
        spaceAfter=25
    )

    slide_body_style = ParagraphStyle(
        'SlideBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        leading=16,
        textColor=colors.HexColor('#cbd5e1'), # Light slate
        spaceAfter=10
    )

    slide_bullet_style = ParagraphStyle(
        'SlideBullet',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        leading=16,
        textColor=colors.HexColor('#cbd5e1'),
        leftIndent=20,
        firstLineIndent=-12,
        spaceAfter=8
    )
    
    accent_text_style = ParagraphStyle(
        'AccentText',
        parent=slide_body_style,
        textColor=colors.HexColor('#f59e0b'), # Amber/Gold
        fontName='Helvetica-Bold'
    )

    story = []

    # Slide 1: Cover (Hand-Edited)
    story.append(Spacer(1, 40))
    story.append(Paragraph("TCS Placement Prep Masterclass", slide_title_style))
    story.append(Paragraph("A Strategic Playbook for B.Tech Candidates (2025-2026 Batch)", slide_subtitle_style))
    story.append(Spacer(1, 20))
    story.append(Paragraph("<b>Hand-Edited Value Proposition:</b>", accent_text_style))
    story.append(Paragraph("<i>\"Bridge the gap from college theory to high-paying Prime & Digital roles by mastering structured logic and modern tech stacks.\"</i>", slide_body_style))
    story.append(PageBreak())

    # Slide 2: Why TCS?
    story.append(Paragraph("Why TCS in 2025-2026?", slide_title_style))
    story.append(Paragraph("Key value propositions and advantages for fresh graduates:", slide_subtitle_style))
    story.append(Paragraph("• <b>Global Scale & Footprint:</b> Opportunities to work with Fortune 500 clients across multiple verticals.", slide_bullet_style))
    story.append(Paragraph("• <b>TCS Xplore Training:</b> Industry-aligned, self-paced learning program before onboarding to bridge skill gaps.", slide_bullet_style))
    story.append(Paragraph("• <b>Clear Career Paths:</b> Multiple entry cadres (Ninja, Digital, Prime) allow fast-tracking of tech careers.", slide_bullet_style))
    story.append(Paragraph("• <b>Upskilling Programs:</b> Strong internal learning culture (AsCEnD) for continuous domain certifications.", slide_bullet_style))
    story.append(PageBreak())

    # Slide 3: Hiring Process
    story.append(Paragraph("TCS NQT Selection Workflow", slide_title_style))
    story.append(Paragraph("Detailed assessment structure and phases:", slide_subtitle_style))
    story.append(Paragraph("1. <b>TCS NQT Online Test:</b> Divided into Foundation (Aptitude/Reasoning/Verbal) and Advanced sections (Coding + Advanced Quant).", slide_bullet_style))
    story.append(Paragraph("2. <b>Technical Interview (TR):</b> Rigorous questioning on programming syntax, DSA, logic building, and database normalization.", slide_bullet_style))
    story.append(Paragraph("3. <b>Managerial Interview (MR):</b> Situational scenarios, puzzles, and architecture review of academic projects.", slide_bullet_style))
    story.append(Paragraph("4. <b>HR Interview:</b> Relocation checks, shift compatibility, document verification, and final fitment.", slide_bullet_style))
    story.append(PageBreak())

    # Slide 4: Technical Stack
    story.append(Paragraph("TCS Target Skill Blueprint", slide_title_style))
    story.append(Paragraph("Core skills prioritized during the recruitment cycle:", slide_subtitle_style))
    story.append(Paragraph("• <b>Foundational Code:</b> Robust object-oriented programming skills in Java or Python.", slide_bullet_style))
    story.append(Paragraph("• <b>Database Competence:</b> Basic SQL queries, indexing, schema design, and ACID properties.", slide_bullet_style))
    story.append(Paragraph("• <b>Operating Systems:</b> Linux directories, basic command line utilities, and basic Shell Scripting.", slide_bullet_style))
    story.append(Paragraph("• <b>Emerging Tech (Digital/Prime):</b> Git workflows, Docker containerization, and AWS/Azure cloud basics.", slide_bullet_style))
    story.append(PageBreak())

    # Slide 5: Eligibility & Packages
    story.append(Paragraph("Eligibility Cutoffs & CTC Structure", slide_title_style))
    story.append(Paragraph("Strict academic rules and performance-based compensation bands:", slide_subtitle_style))
    
    # Table of packages
    data = [
        ["Cadre", "Eligibility Requirements", "Annual CTC (B.Tech)"],
        ["Ninja", "60% or 6.0 CGPA throughout, max 1 active backlog", "₹3.36 LPA"],
        ["Digital", "High NQT score + excellent advanced coding performance", "₹7.0 - 7.3 LPA"],
        ["Prime", "Top NQT advanced coding tier + deep algorithmic knowledge", "₹9.0 - 9.6 LPA"]
    ]
    t = Table(data, colWidths=[1.5*inch, 3.8*inch, 2.2*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1e293b')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.HexColor('#38bdf8')),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#334155')),
        ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,1), (-1,-1), 9.5),
        ('TEXTCOLOR', (0,1), (-1,-1), colors.HexColor('#cbd5e1')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor('#0f172a'), colors.HexColor('#1e293b')])
    ]))
    
    story.append(t)
    story.append(PageBreak())

    # Slide 6: Recent News (Hand-Edited)
    story.append(Paragraph("Recent Corporate Shifts (2025-2026)", slide_title_style))
    story.append(Paragraph("Insights from the June 2026 Annual General Meeting (AGM):", slide_subtitle_style))
    story.append(Paragraph("• <b>AI Agent Deployment:</b> TCS is deploying AI agents for basic developer and support workloads. This increases the NQT benchmark for entry-level programming.", slide_bullet_style))
    story.append(Paragraph("• <b>Skill-Based Campus Strategy:</b> Massive volume-based intake is being replaced with precise, skill-driven recruitment drives.", slide_bullet_style))
    story.append(Paragraph("• <b>Zero Layoffs Policy:</b> TCS reiterates its commitment to stable careers without massive layoffs, unlike global tech giants.", slide_bullet_style))
    story.append(Paragraph("• <b>Verification Rigor:</b> Heightened focus on checking academic credentials and project authenticity.", slide_bullet_style))
    story.append(PageBreak())

    # Slide 7: 5 Actionable Preparation Tips
    story.append(Paragraph("5 Prep Tips for 3rd-Year B.Tech Students", slide_title_style))
    story.append(Paragraph("Actionable strategy to maximize success chances:", slide_subtitle_style))
    story.append(Paragraph("1. <b>Start Coding Daily:</b> Focus on basic string processing, hash tables, and arrays.", slide_bullet_style))
    story.append(Paragraph("2. <b>Practice Section B:</b> Dedicated preparation for NQT Advanced section (quant + reasoning).", slide_bullet_style))
    story.append(Paragraph("3. <b>Document Project Code:</b> Host your major projects on GitHub, write a clean README, and know every line of code.", slide_bullet_style))
    story.append(Paragraph("4. <b>Complete NextStep Early:</b> Fill the NextStep profile carefully; errors lead to verification rejection.", slide_bullet_style))
    story.append(Paragraph("5. <b>Mock Interviews:</b> Conduct peer-to-peer technical and HR interviews to build communication confidence.", slide_bullet_style))
    story.append(PageBreak())

    # Slide 8: CTA (Hand-Edited)
    story.append(Spacer(1, 20))
    story.append(Paragraph("Your 7-Day Kickstart Plan", slide_title_style))
    story.append(Paragraph("Start your preparation journey this week:", slide_subtitle_style))
    
    story.append(Paragraph("• <b>Days 1-2:</b> Create NextStep Profile & generate CT/DT ID.", slide_bullet_style))
    story.append(Paragraph("• <b>Days 3-5:</b> Take a practice NQT Foundation diagnostic test.", slide_bullet_style))
    story.append(Paragraph("• <b>Days 6-7:</b> Code 10 basic array/string search problems in Java or Python.", slide_bullet_style))
    story.append(Spacer(1, 10))
    story.append(Paragraph("<b>Next Steps:</b>", accent_text_style))
    story.append(Paragraph("Let's align with our college placement cell, complete the NextStep form, and review diagnostic scores next Monday.", slide_body_style))

    # Build PDF
    doc.build(story, canvasmaker=DeckCanvas)
    print(f"Generated {pdf_filename} successfully.")


if __name__ == "__main__":
    build_brief()
    build_deck()

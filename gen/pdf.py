from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

def create_pdf(filename):
    # Create a PDF document
    pdf = SimpleDocTemplate(
        filename,
        pagesize=A4
    )
    
    # A list to hold the elements of the PDF
    elements = []
    
    # Sample stylesheet
    styles = getSampleStyleSheet()
    title_style = styles['Title']
    normal_style = styles['Normal']
    
    # Title
    title = Paragraph("AI-Powered Rural Education Hub: Implementation Plan", title_style)
    elements.append(title)
    elements.append(Spacer(1, 0.2 * inch))
    
    # Introduction Paragraph
    intro_text = """
    The AI-Powered Rural Education Hub aims to bridge the educational divide between rural and urban areas 
    in India by providing a personalized, adaptive learning platform accessible to students in remote regions. 
    The platform will offer offline access to digital textbooks, video lectures, AI-driven assessments, 
    and teacher support tools, ensuring that quality education is available regardless of connectivity issues.
    """
    intro_paragraph = Paragraph(intro_text, normal_style)
    elements.append(intro_paragraph)
    elements.append(Spacer(1, 0.2 * inch))

    # System Architecture
    architecture_title = Paragraph("1. System Architecture and Technology Stack", title_style)
    elements.append(architecture_title)
    elements.append(Spacer(1, 0.1 * inch))

    architecture_text = """
    - User Interface (UI): The frontend of the platform will be accessible via web and mobile applications. 
    - Backend: The backend will handle user management, content delivery, AI-driven analytics, and data synchronization.
    - AI Engine: Responsible for personalized learning recommendations, content adaptation, and progress tracking.
    - Offline Mode: Includes an offline data storage component, allowing students to access content without an internet connection.
    """
    architecture_paragraph = Paragraph(architecture_text, normal_style)
    elements.append(architecture_paragraph)
    elements.append(Spacer(1, 0.2 * inch))

    # Technology Stack
    tech_stack_title = Paragraph("1.1 Technology Stack", title_style)
    elements.append(tech_stack_title)
    elements.append(Spacer(1, 0.1 * inch))

    tech_stack_text = """
    - Frontend: React.js (Web), React Native or Flutter (Mobile).
    - Backend: Node.js with Express.js, Python for AI/ML models.
    - Database: MongoDB for content storage and MySQL for relational data.
    - AI/ML: TensorFlow or PyTorch for developing and deploying AI models.
    - Cloud Services: AWS or Google Cloud for hosting, Firebase for real-time database.
    - Offline Capabilities: Service Workers, IndexedDB for web apps; SQLite for mobile.
    """
    tech_stack_paragraph = Paragraph(tech_stack_text, normal_style)
    elements.append(tech_stack_paragraph)
    elements.append(Spacer(1, 0.2 * inch))

    # Key Features
    features_title = Paragraph("2. Key Features and Functionalities", title_style)
    elements.append(features_title)
    elements.append(Spacer(1, 0.1 * inch))

    features_text = """
    - Offline Access to Educational Content: Students can access preloaded content and download additional resources.
    - AI-Driven Personalized Learning: Assessments and adaptive learning paths tailored to each student's needs.
    - Teacher Support and Empowerment: Tools for lesson planning and resource recommendations to enhance teaching effectiveness.
    - Community Engagement: Features for parents to monitor progress and support for local language.
    """
    features_paragraph = Paragraph(features_text, normal_style)
    elements.append(features_paragraph)
    elements.append(Spacer(1, 0.2 * inch))

    # Implementation Strategy
    implementation_title = Paragraph("3. Implementation Strategy", title_style)
    elements.append(implementation_title)
    elements.append(Spacer(1, 0.1 * inch))

    implementation_text = """
    - Phase 1: Research and Planning: Conduct surveys and interviews to identify educational challenges and needs.
    - Phase 2: Platform Development: Build responsive web and mobile interfaces and develop a robust backend.
    - Phase 3: Pilot Testing: Launch the platform in select rural schools, providing training for teachers.
    - Phase 4: Scaling and Expansion: Partner with organizations to scale the platform to more areas.
    """
    implementation_paragraph = Paragraph(implementation_text, normal_style)
    elements.append(implementation_paragraph)
    elements.append(Spacer(1, 0.2 * inch))

    # Challenges and Mitigation Strategies
    challenges_title = Paragraph("4. Potential Challenges and Mitigation Strategies", title_style)
    elements.append(challenges_title)
    elements.append(Spacer(1, 0.1 * inch))

    challenges_text = """
    - Infrastructure Limitations: Limited access to electricity and internet; provide solar-powered devices.
    - Cultural Barriers: Include local language support and involve local educators in content development.
    - Teacher Training: Offer comprehensive training and ongoing support to encourage adoption.
    """
    challenges_paragraph = Paragraph(challenges_text, normal_style)
    elements.append(challenges_paragraph)
    elements.append(Spacer(1, 0.2 * inch))

    # Expected Impact
    impact_title = Paragraph("5. Expected Impact", title_style)
    elements.append(impact_title)
    elements.append(Spacer(1, 0.1 * inch))

    impact_text = """
    - Educational Equity: Access to quality education for rural students, improving learning outcomes.
    - Teacher Empowerment: Enhanced teaching effectiveness with AI-driven insights and resources.
    - Socioeconomic Benefits: Better education leading to improved job prospects and community development.
    """
    impact_paragraph = Paragraph(impact_text, normal_style)
    elements.append(impact_paragraph)
    elements.append(Spacer(1, 0.2 * inch))

    # Sustainability and Future Prospects
    sustainability_title = Paragraph("6. Sustainability and Future Prospects", title_style)
    elements.append(sustainability_title)
    elements.append(Spacer(1, 0.1 * inch))

    sustainability_text = """
    - Financial Sustainability: Leverage government grants and explore subscription models for advanced features.
    - Continuous Improvement: Regularly update AI models and expand the content library.
    - Scalability: Start with pilot programs and then scale to other regions, exploring international opportunities.
    """
    sustainability_paragraph = Paragraph(sustainability_text, normal_style)
    elements.append(sustainability_paragraph)
    elements.append(Spacer(1, 0.2 * inch))

    # Conclusion
    conclusion_title = Paragraph("Conclusion", title_style)
    elements.append(conclusion_title)
    elements.append(Spacer(1, 0.1 * inch))

    conclusion_text = """
    The AI-Powered Rural Education Hub is a transformative solution designed to address critical challenges 
    in rural education. By leveraging AI and offline capabilities, this platform can empower students and 
    teachers, providing quality education and bridging the gap between rural and urban educational resources.
    """
    conclusion_paragraph = Paragraph(conclusion_text, normal_style)
    elements.append(conclusion_paragraph)

    # Build the PDF
    pdf.build(elements)

# Specify the filename
filename = "AI_Powered_Rural_Education_Platform.pdf"

# Call the function to create the PDF
create_pdf(filename)

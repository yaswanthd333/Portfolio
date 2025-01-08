import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Yaswanth Reddy Duggasani | Portfolio",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enhanced Custom CSS
st.markdown("""
    <style>
    /* Global Styles */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(to right, #f8f9fa, #e9ecef);
        font-family: 'Inter', sans-serif;
    }
    
    .stButton button {
        background-color: #0066cc;
        color: white;
        border-radius: 25px;
        padding: 0.5rem 2rem;
        border: none;
        transition: all 0.3s ease;
    }
    
    .stButton button:hover {
        background-color: #0052a3;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    
    /* Header Styles */
    .header-container {
        background: linear-gradient(135deg, #0066cc, #1a8cff);
        padding: 3rem 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        text-align: center;
        color: white;
    }
    
    .profile-image {
        border-radius: 50%;
        border: 4px solid white;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        margin-bottom: 1rem;
    }
    
    .name-title {
        font-size: 2.5rem !important;
        font-weight: 700;
        margin-bottom: 0.5rem;
        color: white;
    }
    
    .subtitle {
        font-size: 1.2rem;
        font-weight: 500;
        color: rgba(255,255,255,0.9);
    }
    
    /* Card Styles */
    .project-card {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        margin: 1rem 0;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        border: 1px solid #e1e4e8;
    }
    
    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 24px rgba(0,0,0,0.1);
    }
    
    .card-title {
        font-size: 1.5rem;
        font-weight: 600;
        color: #1a1a1a;
        margin-bottom: 1rem;
    }
    
    .card-description {
        color: #4a4a4a;
        margin-bottom: 1rem;
        line-height: 1.6;
    }
    
    /* Tag Styles */
    .tech-tag {
        display: inline-block;
        padding: 0.4rem 1rem;
        background: #e1f0ff;
        color: #0066cc;
        border-radius: 20px;
        margin: 0.25rem;
        font-size: 0.9rem;
        font-weight: 500;
        transition: all 0.2s ease;
    }
    
    .tech-tag:hover {
        background: #0066cc;
        color: white;
        transform: scale(1.05);
    }
    
    /* Section Headers */
    .section-header {
        font-size: 1.8rem;
        font-weight: 700;
        color: #1a1a1a;
        margin: 2rem 0 1rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 3px solid #0066cc;
    }
    
    /* Stats Container */
    .stats-card {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        border: 1px solid #e1e4e8;
    }
    
    .stats-number {
        font-size: 2rem;
        font-weight: 700;
        color: #0066cc;
        margin-bottom: 0.5rem;
    }
    
    .stats-label {
        color: #4a4a4a;
        font-weight: 500;
    }
    
    /* Experience Timeline */
    .timeline-card {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        border-left: 5px solid #0066cc;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }
    
    .timeline-header {
        font-weight: 600;
        color: #1a1a1a;
        margin-bottom: 0.5rem;
    }
    
    .timeline-subheader {
        color: #666;
        font-size: 0.9rem;
        margin-bottom: 1rem;
    }
    
    /* Contact Form */
    .contact-form {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }
    
    .stTextInput input, .stTextArea textarea {
        border-radius: 8px;
        border: 1px solid #e1e4e8;
        padding: 0.75rem;
    }
    </style>
""", unsafe_allow_html=True)

def main():
    # Header Section
    st.markdown("""
        <div class="header-container">
            <img src="/api/placeholder/150/150" class="profile-image" width="150">
            <h1 class="name-title">Yaswanth Reddy Duggasani</h1>
            <p class="subtitle">Assistant System Engineer</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Quick Stats
    st.markdown('<div class="section-header">Overview</div>', unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    
    stats = [
        {"number": "2+", "label": "Years Experience"},
        {"number": "10+", "label": "Projects"},
        {"number": "2", "label": "Publications"},
        {"number": "15+", "label": "Skills"}
    ]
    
    for col, stat in zip([col1, col2, col3, col4], stats):
        col.markdown(f"""
            <div class="stats-card">
                <div class="stats-number">{stat['number']}</div>
                <div class="stats-label">{stat['label']}</div>
            </div>
        """, unsafe_allow_html=True)
    
    # Projects Section
    st.markdown('<div class="section-header">Featured Projects</div>', unsafe_allow_html=True)
    
    projects = [
        {
            "title": "Inventory Management System",
            "description": "A comprehensive full-stack application built with Java and MySQL, featuring real-time inventory tracking, automated alerts, and detailed reporting capabilities.",
            "technologies": ["Java", "MySQL", "Spring Boot"],
        },
        {
            "title": "Formula 1 Analytics Dashboard",
            "description": "Interactive data visualization platform analyzing Formula 1 team performance metrics, race statistics, and historical trends using Tableau.",
            "technologies": ["Tableau", "Python", "Data Analysis"],
        },
        {
            "title": "AI-Powered Apparel Recommender",
            "description": "Machine learning-based recommendation system that suggests personalized clothing items based on user preferences and browsing history.",
            "technologies": ["Python", "ML", "Neural Networks"],
        }
    ]
    
    for project in projects:
        st.markdown(f"""
            <div class="project-card">
                <div class="card-title">{project['title']}</div>
                <div class="card-description">{project['description']}</div>
                <div>
                    {''.join([f'<span class="tech-tag">{tech}</span>' for tech in project['technologies']])}
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    # Experience Section
    st.markdown('<div class="section-header">Professional Experience</div>', unsafe_allow_html=True)
    
    experiences = [
        {
            "role": "Assistant System Engineer",
            "company": "Tata Consultancy Services Limited",
            "period": "June 2024 - Present",
            "location": "Kolkata, India",
            "achievements": [
                "Developed ML-based ticket assignment system reducing misassignment by 180 hours/week",
                "Automated enterprise processes reducing tickets by 800/month",
                "Led configuration item management initiatives"
            ]
        },
        {
            "role": "Software Analyst",
            "company": "Energytech Global",
            "period": "June 2023 - September 2023",
            "location": "Hyderabad, India",
            "achievements": [
                "Optimized database operations reducing costs by 30%",
                "Implemented robust data sanitization protocols",
                "Enhanced database replication efficiency"
            ]
        }
    ]
    
    for exp in experiences:
        st.markdown(f"""
            <div class="timeline-card">
                <div class="timeline-header">{exp['role']} | {exp['company']}</div>
                <div class="timeline-subheader">{exp['period']} | {exp['location']}</div>
                <ul>
                    {''.join([f'<li>{achievement}</li>' for achievement in exp['achievements']])}
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    # Contact Section
    st.markdown('<div class="section-header">Get in Touch</div>', unsafe_allow_html=True)
    
    with st.form("contact_form", clear_on_submit=True):
        st.markdown('<div class="contact-form">', unsafe_allow_html=True)
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Send Message")
        st.markdown('</div>', unsafe_allow_html=True)
        
        if submitted:
            st.success("Thanks for reaching out! I'll get back to you soon.")

if __name__ == "__main__":
    main()

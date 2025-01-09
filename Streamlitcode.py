import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import datetime

# Page configuration
st.set_page_config(
    page_title="Yaswanth Reddy Duggasani | Portfolio",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enhanced Custom CSS with modern design elements
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #f8f9fa, #e9ecef);
        font-family: 'Inter', sans-serif;
    }
    
    .header-container {
        background: linear-gradient(135deg, #0066cc, #1a8cff);
        padding: 3rem 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        text-align: center;
        color: white;
    }
    
    .bio-text {
        max-width: 800px;
        margin: 1rem auto;
        line-height: 1.6;
        color: rgba(255,255,255,0.9);
    }
    
    .contact-info {
        display: flex;
        justify-content: center;
        gap: 2rem;
        margin-top: 1rem;
        color: rgba(255,255,255,0.9);
    }
    
    .skill-tag {
        display: inline-block;
        padding: 0.4rem 1rem;
        background: rgba(255,255,255,0.1);
        border-radius: 20px;
        margin: 0.25rem;
        backdrop-filter: blur(5px);
        color: white;
        font-size: 0.9rem;
    }
    
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }
    
    .project-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        margin: 1.5rem 0;
        transition: transform 0.3s ease;
        border: 1px solid #e1e4e8;
    }
    
    .project-card:hover {
        transform: translateY(-5px);
    }
    
    .experience-card {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        border-left: 5px solid #0066cc;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }
    
    .certification-card {
        background: linear-gradient(135deg, #ffffff, #f8f9fa);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        border: 1px solid #e1e4e8;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }
    
    .publication-card {
        background: linear-gradient(135deg, #ffffff, #f8f9fa);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        border: 1px solid #e1e4e8;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }
    
    .section-header {
        font-size: 1.8rem;
        font-weight: 700;
        color: #1a1a1a;
        margin: 2.5rem 0 1.5rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 3px solid #0066cc;
    }
    
    .skill-progress {
        background: #f0f0f0;
        border-radius: 10px;
        margin: 0.5rem 0;
        overflow: hidden;
    }
    
    .skill-progress-bar {
        height: 8px;
        background: linear-gradient(90deg, #0066cc, #1a8cff);
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)


def create_skills_chart():
    # Skills data based on your experience
    skills_data = {
        'Skill': ['Python', 'Java', 'Machine Learning', 'SQL', 'Azure', 'Kafka'],
        'Proficiency': [90, 85, 80, 85, 75, 70]  # Estimated proficiency levels
    }
    
    fig = go.Figure([go.Bar(
        x=skills_data['Proficiency'],
        y=skills_data['Skill'],
        orientation='h',
        marker=dict(
            color='rgba(0, 102, 204, 0.8)',
            line=dict(color='rgba(0, 102, 204, 1.0)', width=1)
        )
    )])
    
    fig.update_layout(
        title="Technical Skills Proficiency",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        height=300,
        margin=dict(l=0, r=0, t=30, b=0),
        xaxis_title="Proficiency Level",
        showlegend=False
    )
    
    return fig

def main():
    # Header Section
    st.markdown("""
        <div class="header-container">
            <h1 style="font-size: 2.5rem; font-weight: 700;">Yaswanth Reddy Duggasani</h1>
            <p style="font-size: 1.3rem; opacity: 0.9;">Assistant System Engineer at Tata Consultancy Services</p>
            <div class="bio-text">
                Data-driven software engineer specializing in enterprise automation and machine learning solutions. 
                Proven track record in reducing operational costs and improving efficiency through innovative technical solutions.
            </div>
            <div class="contact-info">
                <span>📧 duggasaniyaswanth333@gmail.com</span>
                <span>🔗 <a href="https://github.com/yaswanthd333" style="color: white;">GitHub</a></span>
                <span>💼 <a href="https://www.linkedin.com/in/yaswanth-reddy-duggasani-1a4633198/" style="color: white;">LinkedIn</a></span>
            </div>
            <div style="margin-top: 1.5rem">
                <span class="skill-tag">Python</span>
                <span class="skill-tag">Java</span>
                <span class="skill-tag">Machine Learning</span>
                <span class="skill-tag">SQL</span>
                <span class="skill-tag">Azure</span>
                <span class="skill-tag">Kafka</span>
            </div>
        </div>
    """, unsafe_allow_html=True)


    # Professional Experience
    st.markdown('<div class="section-header">Professional Experience</div>', unsafe_allow_html=True)
    
    experiences = [
        {
            "role": "Assistant System Engineer",
            "company": "Tata Consultancy Services Limited",
            "period": "June 2024 - Present",
            "location": "Kolkata, India",
            "achievements": [
                "Developed ML-based ticket assignment system reducing misassignment by 180 hours/week",
                "Implemented configuration item management and automated enterprise processes reducing tickets by 800/month",
                "Led enterprise-level automation initiatives for improved efficiency",
                "Collaborated with cross-functional teams to optimize workflow processes"
            ]
        },
        {
            "role": "Software Analyst",
            "company": "Energytech Global",
            "period": "June 2023 - September 2023",
            "location": "Hyderabad, India",
            "achievements": [
                "Implemented data sanitization using triggers and validated database replication",
                "Reduced database and backup maintenance costs by 30%",
                "Enhanced database operations efficiency",
                "Collaborated with stakeholders to identify and implement process improvements"
            ]
        },
        {
            "role": "Software Intern",
            "company": "Energytech Global",
            "period": "January 2023 - May 2023",
            "location": "Hyderabad, India",
            "achievements": [
                "Conducted Odoo bin testing and manual testing of product workflows",
                "Performed API testing and validations",
                "Managed issue and ticket triaging while collaborating with stakeholders",
                "Contributed to improving test coverage and documentation"
            ]
        }
    ]
    
    for exp in experiences:
        st.markdown(f"""
            <div class="experience-card">
                <h3 style="color: #0066cc; margin-bottom: 0.5rem;">{exp['role']} | {exp['company']}</h3>
                <p style="color: #666; font-size: 0.9rem; margin-bottom: 1rem;">{exp['period']} | {exp['location']}</p>
                <ul style="color: #333;">
                    {''.join([f'<li style="margin-bottom: 0.5rem;">{achievement}</li>' for achievement in exp['achievements']])}
                </ul>
            </div>
        """, unsafe_allow_html=True)

    # Skills Visualization
    st.markdown('<div class="section-header">Technical Expertise</div>', unsafe_allow_html=True)
    st.plotly_chart(create_skills_chart(), use_container_width=True)

    # Publications Section
    st.markdown('<div class="section-header">Publications</div>', unsafe_allow_html=True)
    
    publications = [
        {
            "title": "Liver Tumor Risk Prediction using Ensemble Methods",
            "conference": "2022 Sixth International Conference on I-SMAC",
            "doi": "10.1109/I-SMAC55078.2022.9987419",
            "impact": "Advanced healthcare diagnostics through machine learning"
        },
        {
            "title": "Apparel Recommendation System using Content-Based Filtering",
            "journal": "IJRTE",
            "doi": "10.35940/ijrte.D7331.1111422",
            "impact": "Enhanced e-commerce personalization techniques"
        }
    ]
    
    for pub in publications:
        st.markdown(f"""
            <div class="publication-card">
                <h3 style="color: #0066cc; margin-bottom: 0.5rem;">{pub['title']}</h3>
                <p style="color: #666;">{'Conference: ' + pub['conference'] if 'conference' in pub else 'Journal: ' + pub['journal']}</p>
                <p style="color: #666;">DOI: {pub['doi']}</p>
                <p style="color: #333; margin-top: 0.5rem;">Impact: {pub['impact']}</p>
            </div>
        """, unsafe_allow_html=True)

    # Certifications Section
    st.markdown('<div class="section-header">Certifications & Training</div>', unsafe_allow_html=True)
    
    certifications = [
        {
            "title": "Generative AI Fundamentals",
            "provider": "Databricks",
            "date": "2023"
        },
        {
            "title": "Kafka Internal Architecture",
            "provider": "Confluence",
            "date": "2023"
        },
        {
            "title": "Google Data Analytics Specialization",
            "provider": "Coursera",
            "date": "2023"
        }
    ]
    
    for cert in certifications:
        st.markdown(f"""
            <div class="certification-card">
                <h3 style="color: #0066cc; margin-bottom: 0.5rem;">{cert['title']}</h3>
                <p style="color: #666;">Provider: {cert['provider']}</p>
                <p style="color: #666;">Year: {cert['date']}</p>
            </div>
        """, unsafe_allow_html=True)

    # Projects Section
    st.markdown('<div class="section-header">Notable Projects</div>', unsafe_allow_html=True)
    
    projects = [
        {
            "title": "Inventory Management System",
            "tech": "Java, MySQL",
            "description": "Developed a comprehensive inventory management system with real-time tracking and automated alerts.",
            "impact": "Improved inventory accuracy by 40% and reduced manual data entry time by 60%"
        },
        {
            "title": "Formula 1 Teams Data Visualization",
            "tech": "Tableau",
            "description": "Created interactive dashboards to visualize Formula 1 team performance metrics and historical data.",
            "impact": "Enhanced data accessibility and insight generation for race strategy analysis"
        },
        {
            "title": "Apparel Recommendation System",
            "tech": "Python, Machine Learning",
            "description": "Built a machine learning-based recommender system for apparel based on search string analysis.",
            "impact": "Improved product discovery and user engagement metrics"
        }
    ]
    
    for project in projects:
        st.markdown(f"""
            <div class="project-card">
                <h3 style="color: #0066cc; margin-bottom: 0.5rem;">{project['title']}</h3>
                <p style="color: #666; font-size: 0.9rem; margin-bottom: 0.5rem;">Technologies: {project['tech']}</p>
                <p style="color: #333; margin-bottom: 0.5rem;">{project['description']}</p>
                <p style="color: #0066cc;"><strong>Impact:</strong> {project['impact']}</p>
            </div>
        """, unsafe_allow_html=True)

    # Footer Section
    st.markdown("""
        <div style="text-align: center; margin-top: 4rem; padding: 2rem; background: linear-gradient(135deg, #f8f9fa, #e9ecef); border-radius: 15px;">
            <h2 style="color: #0066cc; margin-bottom: 1rem;">Let's Connect!</h2>
            <p style="color: #666; max-width: 600px; margin: 0 auto;">
                I'm always interested in discussing new opportunities, sharing insights, and connecting with fellow professionals.
            </p>
            <div style="margin-top: 1.5rem;">
                <a href="mailto:duggasaniyaswanth333@gmail.com" style="color: #0066cc; text-decoration: none; margin: 0 1rem;">
                    📧 Email
                </a>
                <a href="https://www.linkedin.com/in/yaswanth-reddy-duggasani-1a4633198/" style="color: #0066cc; text-decoration: none; margin: 0 1rem;">
                    💼 LinkedIn
                </a>
                <a href="https://github.com/yaswanthd333" style="color: #0066cc; text-decoration: none; margin: 0 1rem;">
                    🔗 GitHub
                </a>
            </div>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Yaswanth Reddy Duggasani | Portfolio",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    /* Global Styles */
    .main {
        padding: 0rem 0rem;
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    /* Animations */
    @keyframes slideInFromLeft {
        0% {
            transform: translateX(-100%);
            opacity: 0;
        }
        100% {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }
    
    /* Typography */
    .title-text {
        font-size: 48px !important;
        font-weight: 800;
        background: linear-gradient(120deg, #2c3e50, #3498db);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        animation: slideInFromLeft 1s ease-out;
    }
    
    .subtitle-text {
        font-size: 28px !important;
        color: #34495e;
        text-align: center;
        font-weight: 300;
        animation: fadeIn 1.5s ease-out;
    }
    
    .section-header {
        font-size: 32px !important;
        font-weight: bold;
        color: #2c3e50;
        margin: 1.5rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 3px solid #3498db;
    }
    
    /* Cards */
    .skill-box {
        background: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin: 10px 0;
        transition: transform 0.3s ease;
    }
    
    .skill-box:hover {
        transform: translateY(-5px);
    }
    
    .experience-card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        margin: 15px 0;
        border-left: 5px solid #3498db;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Contact Form */
    .contact-form {
        background: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 20px;
        background: linear-gradient(135deg, #2c3e50, #3498db);
        color: white;
        border-radius: 10px;
        margin-top: 30px;
    }
    
    .skill-tag {
        display: inline-block;
        padding: 5px 10px;
        background: #e1f0fa;
        border-radius: 15px;
        margin: 5px;
        font-size: 14px;
        color: #2c3e50;
    }
    </style>
    """, unsafe_allow_html=True)

# Function to create skill charts
def create_skill_radar_chart():
    categories = ['Python', 'Java', 'ML/AI', 'Database', 'Cloud', 'Testing']
    values = [9, 8, 8, 7, 7, 8]
    
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='Skills'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 10]
            )),
        showlegend=False,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    return fig

def main():
    # Sidebar Navigation
    st.sidebar.markdown('<p class="section-header">Navigation</p>', unsafe_allow_html=True)
    page = st.sidebar.radio("Go to", ["Home", "Projects", "Contact"])
    
    if page == "Home":
        # Profile Image
        st.image("/api/placeholder/200/200", width=200)
        
        # Header Section
        st.markdown('<p class="title-text">Yaswanth Reddy Duggasani</p>', unsafe_allow_html=True)
        st.markdown('<p class="subtitle-text">Assistant System Engineer</p>', unsafe_allow_html=True)
        
        # Quick Stats
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Experience", "2+ Years")
        col2.metric("Projects", "10+")
        col3.metric("Publications", "2")
        col4.metric("Skills", "15+")
        
        # About Section
        st.markdown("---")
        st.markdown('<p class="section-header">About Me</p>', unsafe_allow_html=True)
        st.write("""
        Assistant System Engineer with expertise in data-driven solutions and automation for streamlining enterprise operations. 
        Experienced in applying Machine Learning to optimize processes, manage data effectively, and develop robust applications.
        """)
        
        # Skills Radar Chart
        st.markdown("---")
        st.markdown('<p class="section-header">Skills Overview</p>', unsafe_allow_html=True)
        st.plotly_chart(create_skill_radar_chart(), use_container_width=True)
        
        # Experience Section
        st.markdown("---")
        st.markdown('<p class="section-header">Experience</p>', unsafe_allow_html=True)
        
        experiences = [
            {
                "role": "Assistant System Engineer",
                "company": "Tata Consultancy Services Limited",
                "period": "June 2024 - Present",
                "location": "Kolkata, India",
                "achievements": [
                    "Developed ML-based ticket assignment system reducing incorrect queue assignment by ~180 hours/week",
                    "Managed Configuration Items at enterprise level",
                    "Reduced service desk tickets by ~800 per month through automation"
                ]
            },
            {
                "role": "Software Analyst",
                "company": "Energytech Global",
                "period": "June 2023 - September 2023",
                "location": "Hyderabad, India",
                "achievements": [
                    "Implemented data sanitization reducing DB costs by ~30%",
                    "Managed database replication and optimization"
                ]
            }
        ]
        
        for exp in experiences:
            st.markdown(
                f'<div class="experience-card">'
                f'<h3>{exp["role"]} | {exp["company"]}</h3>'
                f'<p style="color: #666;">{exp["period"]} | {exp["location"]}</p>'
                f'<ul>{"".join([f"<li>{achievement}</li>" for achievement in exp["achievements"]])}</ul>'
                f'</div>',
                unsafe_allow_html=True
            )

    elif page == "Projects":
        st.markdown('<p class="section-header">Project Portfolio</p>', unsafe_allow_html=True)
        
        projects = [
            {
                "title": "Inventory Management System",
                "description": "Full-stack application using Java and MySQL",
                "technologies": ["Java", "MySQL", "Spring Boot"],
            },
            {
                "title": "Formula 1 Analytics",
                "description": "Interactive dashboard using Tableau",
                "technologies": ["Tableau", "Python", "Data Analysis"],
            },
            {
                "title": "Apparel Recommender",
                "description": "ML-based recommendation engine",
                "technologies": ["Python", "ML", "Neural Networks"],
            }
        ]
        
        for project in projects:
            st.markdown(
                f'<div class="skill-box">'
                f'<h3>{project["title"]}</h3>'
                f'<p>{project["description"]}</p>'
                f'<div style="display: flex; flex-wrap: wrap; gap: 5px;">'
                + ''.join([f'<span class="skill-tag">{tech}</span>' for tech in project["technologies"]])
                + '</div>'
                f'</div>',
                unsafe_allow_html=True
            )

    elif page == "Contact":
        st.markdown('<p class="section-header">Get in Touch</p>', unsafe_allow_html=True)
        
        with st.form("contact_form", clear_on_submit=True):
            st.markdown('<div class="contact-form">', unsafe_allow_html=True)
            name = st.text_input("Name")
            email = st.text_input("Email")
            message = st.text_area("Message")
            submitted = st.form_submit_button("Send Message")
            st.markdown('</div>', unsafe_allow_html=True)
            
            if submitted:
                st.success("Thanks for reaching out! I'll get back to you soon.")

    # Footer
    st.markdown(
        '<div class="footer">'
        '<p>© 2024 Yaswanth Reddy Duggasani. All rights reserved.</p>'
        '<p>Made with ❤️ using Streamlit</p>'
        '</div>',
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()

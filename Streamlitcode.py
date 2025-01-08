import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from PIL import Image
import base64
import io
import numpy as np
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
import plotly.figure_factory as ff

# Page configuration
st.set_page_config(
    page_title="Yaswanth Reddy Duggasani | Portfolio",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# [Previous CSS styles remain the same - include all the styles from the previous version]
# Additional CSS for new components
st.markdown("""
    <style>
    /* [Previous CSS remains the same] */
    
    /* New Component Styles */
    .profile-container {
        text-align: center;
        padding: 20px;
        background: white;
        border-radius: 50%;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin: 20px auto;
        width: 200px;
        height: 200px;
        overflow: hidden;
    }
    
    .contact-form {
        background: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .download-button {
        background: #2ecc71;
        color: white;
        padding: 10px 20px;
        border-radius: 25px;
        text-decoration: none;
        transition: all 0.3s ease;
        display: inline-block;
    }
    
    .download-button:hover {
        background: #27ae60;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    
    .chart-container {
        background: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin: 15px 0;
    }
    
    .sidebar {
        background: #f8f9fa;
        padding: 20px;
        border-radius: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# Function to create downloadable resume
def get_pdf_download_link(pdf_path):
    with open(pdf_path, "rb") as f:
        bytes_data = f.read()
    b64 = base64.b64encode(bytes_data).decode()
    href = f'<a href="data:application/pdf;base64,{b64}" class="download-button" download="Yaswanth_Duggasani_Resume.pdf">📄 Download Resume</a>'
    return href

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

# Function to create experience timeline
def create_experience_timeline():
    df = pd.DataFrame([
        dict(Task="TCS", Start='2024-06-01', End='2025-01-08', Role='Assistant System Engineer'),
        dict(Task="Energytech", Start='2023-06-01', End='2023-09-30', Role='Software Analyst'),
        dict(Task="Energytech", Start='2023-01-01', End='2023-05-30', Role='Software Intern')
    ])
    
    fig = ff.create_gantt(df, colors=['#3498db', '#2ecc71', '#9b59b6'],
                         show_colorbar=True, group_tasks=True)
    fig.update_layout(height=200)
    return fig

def main():
    # Sidebar
    st.sidebar.markdown('<p class="section-header">Navigation</p>', unsafe_allow_html=True)
    page = st.sidebar.radio("Go to", ["Home", "Projects", "Contact", "Resume"])
    
    if page == "Home":
        # Profile Image
        st.image("/api/placeholder/200/200", width=200)
        
        # Header Section
        st.markdown('<p class="title-text">Yaswanth Reddy Duggasani</p>', unsafe_allow_html=True)
        st.markdown('<p class="subtitle-text">Assistant System Engineer</p>', unsafe_allow_html=True)
        
        # Quick Stats
        col1, col2, col3, col4 = st.columns(4)
        metrics = {
            "Experience": "2+ Years",
            "Projects": "10+",
            "Publications": "2",
            "Skills": "15+"
        }
        
        for col, (metric, value) in zip([col1, col2, col3, col4], metrics.items()):
            col.metric(metric, value)
        
        # Skills Radar Chart
        st.markdown("---")
        st.markdown('<p class="section-header">Skills Overview</p>', unsafe_allow_html=True)
        st.plotly_chart(create_skill_radar_chart(), use_container_width=True)
        
        # Experience Timeline
        st.markdown("---")
        st.markdown('<p class="section-header">Experience Timeline</p>', unsafe_allow_html=True)
        st.plotly_chart(create_experience_timeline(), use_container_width=True)
        
        # [Rest of the previous home page content remains the same]

    elif page == "Projects":
        st.markdown('<p class="section-header">Project Portfolio</p>', unsafe_allow_html=True)
        
        # Interactive Project Cards
        projects = [
            {
                "title": "Inventory Management System",
                "description": "Full-stack application using Java and MySQL",
                "technologies": ["Java", "MySQL", "Spring Boot"],
                "metrics": {"Efficiency": "+40%", "Cost Reduction": "30%"}
            },
            {
                "title": "Formula 1 Analytics",
                "description": "Interactive dashboard using Tableau",
                "technologies": ["Tableau", "Python", "Data Analysis"],
                "metrics": {"Insights Generated": "50+", "Data Points": "10k+"}
            },
            {
                "title": "Apparel Recommender",
                "description": "ML-based recommendation engine",
                "technologies": ["Python", "ML", "Neural Networks"],
                "metrics": {"Accuracy": "85%", "Users": "1000+"}
            }
        ]
        
        for project in projects:
            with st.container():
                st.markdown(
                    f'<div class="skill-box">'
                    f'<h3>{project["title"]}</h3>'
                    f'<p>{project["description"]}</p>'
                    f'<div style="display: flex; flex-wrap: wrap; gap: 5px;">'
                    + ''.join([f'<div class="skill-tag">{tech}</div>' for tech in project["technologies"]])
                    + '</div>'
                    f'<div style="margin-top: 15px;">'
                    + ''.join([f'<div class="stats-container" style="display: inline-block; margin: 5px; padding: 10px;">'
                              f'<strong>{key}:</strong> {value}</div>' 
                              for key, value in project["metrics"].items()])
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
                
        # Social Links
        st.markdown("---")
        st.markdown('<p class="section-header">Connect With Me</p>', unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(
                '<a href="https://linkedin.com" class="custom-button" target="_blank">LinkedIn</a>',
                unsafe_allow_html=True
            )
        with col2:
            st.markdown(
                '<a href="https://github.com" class="custom-button" target="_blank">GitHub</a>',
                unsafe_allow_html=True
            )
        with col3:
            st.markdown(
                '<a href="mailto:duggasaniyaswanth333@gmail.com" class="custom-button">Email</a>',
                unsafe_allow_html=True
            )

    elif page == "Resume":
        st.markdown('<p class="section-header">Resume</p>', unsafe_allow_html=True)
        
        # Resume preview (placeholder)
        st.image("/api/placeholder/600/800", caption="Resume Preview")
        
        # Download button
        st.markdown(
            '<div style="text-align: center; margin: 20px;">'
            '<a href="#" class="download-button">📄 Download Resume (PDF)</a>'
            '</div>',
            unsafe_allow_html=True
        )

    # Footer (remains on all pages)
    st.markdown(
        '<div class="footer">'
        '<p>© 2024 Yaswanth Reddy Duggasani. All rights reserved.</p>'
        '<p>Made with ❤️ using Streamlit</p>'
        '</div>',
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()

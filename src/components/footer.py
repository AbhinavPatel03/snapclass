import streamlit as st

def footer_home():


    st.markdown(f"""
        <div style="display: flex;justify-content: center; margin-top: 2rem; gap: 6px; items-align: center;">
            <p style="font-weight: bold; color: white;"> Created with ❤️ by ABHINAV PATEL</p>
           
        </div>  
    """, unsafe_allow_html=True)


def footer_dashboard():


    st.markdown(f"""
        <div style="display: flex;justify-content: center; margin-top: 2rem; gap: 6px; items-align: center;">
            <p style="font-weight: bold; color: black;"> Created with ❤️ by ABHINAV PATEL</p>
           
        </div>  
    """, unsafe_allow_html=True)
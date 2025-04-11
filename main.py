import os

from autoclean.export_clean import cleanup_expired
from dotenv import load_dotenv
import streamlit as st

from autodocument.convert import warm_up_libreoffice
from ui.trial_page import display_trial_page

load_dotenv()

if "cleanup_started" not in st.session_state:
    cleanup_expired()
    st.session_state["cleanup_started"] = True

warm_up_libreoffice()

def main():
    display_trial_page()

if __name__ == "__main__":
    main()


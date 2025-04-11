import os

from autodocument.doc_fill import fill_in_form
from dotenv import load_dotenv
import streamlit as st

from autodocument.convert import warm_up_libreoffice
from ui.trial_page import display_trial_page


def main():
    display_trial_page()

if __name__ == "__main__":
    load_dotenv()
    warm_up_libreoffice()
    main()


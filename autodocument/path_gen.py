import os
import unicodedata

def remove_vietnamese_accents(text):
    nfkd_form = unicodedata.normalize('NFKD', text)
    return ''.join([c for c in nfkd_form if not unicodedata.combining(c)])

def create_output_path(student_name, subject, trial_date, file_extension):
    formatted_date = trial_date.strftime("%d-%m-%Y")
    safe_student_name = remove_vietnamese_accents(student_name).replace(' ', '_')

    if subject == "Game Creator - GB":
        subject_code = "GB"
    elif subject == "Scratch Creator - SB":
        subject_code = "SB"
    elif subject == "Robotics - PRE":
        subject_code = "PRE"
    elif subject == "Robotics - ARM":
        subject_code = "ARM"
    elif subject == "Robotics - KIRO":
        subject_code = "KIRO"
    else:
        subject_code = subject

    file_name = f"{subject_code}_{safe_student_name}_{formatted_date}.{file_extension}"
    output_dir = f"{file_extension}_output"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    return os.path.join(output_dir, file_name)
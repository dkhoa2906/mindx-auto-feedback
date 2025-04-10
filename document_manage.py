import os
import unicodedata
import shutil

def remove_vietnamese_accents(text):
    nfkd_form = unicodedata.normalize('NFKD', text)
    return ''.join([c for c in nfkd_form if not unicodedata.combining(c)])

def get_template_path(subject):
    if subject in ["Game Creator - GB", "Scratch Creator - SB"]:
        return os.path.join("document_templates", "coding.docx")
    if subject in ["Robotics - PRE", "Robotics - ARM"]:
        return os.path.join("document_templates", "robotics.docx")
    if subject in ["Lego 4+"]:
        return os.path.join("document_templates", "lego.docx")
    return None

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
    elif subject == "Lego 4+":
        subject_code = "LG"
    else:
        subject_code = subject

    file_name = f"{subject_code}_{safe_student_name}_{formatted_date}.{file_extension}"
    output_dir = f"{file_extension}_output"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    return os.path.join(output_dir, file_name)

def create_from_template(student_name, subject, trial_date):
    template_path = get_template_path(subject)
    output_path = create_output_path(student_name, subject, trial_date, file_extension="docx")
    shutil.copy(template_path, output_path)
    return output_path
import shutil
import os

from autodocument.path_gen import create_output_path

def get_template_path(subject):
    if subject in ["Game Creator - GB", "Scratch Creator - SB"]:
        return os.path.join("./document_templates", "coding.docx")
    if subject in ["Robotics - PRE", "Robotics - ARM"]:
        return os.path.join("./document_templates", "robotics.docx")
    if subject in ["Robotics - KIRO"]:
        return os.path.join("./document_templates", "lego.docx")
    return None

def create_from_template(student_name, subject, trial_date):
    template_path = get_template_path(subject)
    output_path = create_output_path(student_name, subject, trial_date, file_extension="docx")
    shutil.copy(template_path, output_path)
    return output_path
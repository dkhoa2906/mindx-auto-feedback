from docxtpl import DocxTemplate

from autodocument.path_gen import create_output_path
from autodocument.doc_clone import create_from_template
from autodocument.replacements import get_replacements


# def fill_in_form(student_name, student_yob, subject, trial_date, trial_mentor, trial_place, points, feedback):
#     document = Document(create_from_template(student_name, subject, trial_date))
#
#     replacements = get_replacements(student_name, student_yob, subject, trial_date, trial_mentor, trial_place, points,
#                                     feedback)
#
#     print(replacements)
#
#     # Fill text in tables
#     for table in document.tables:
#         for row in table.rows:
#             for cell in row.cells:
#                 for paragraph in cell.paragraphs:
#                     for run in paragraph.runs:
#                         for placeholder, value in replacements.items():
#                             if placeholder in run.text:
#                                 run.text = run.text.replace(placeholder, value)
#                                 run.font.size = Pt(10) if subject in ["Game Creator - GB", "Scratch Creator - SB"] else Pt(12)
#
#     # Fill text outside tables
#     for paragraph in document.paragraphs:
#         for run in paragraph.runs:
#             for placeholder, value in replacements.items():
#                 if placeholder in run.text:
#                     run.text = run.text.replace(placeholder, value)
#
#
#     output_path = create_output_path(student_name, subject, trial_date, file_extension="docx")
#     document.save(output_path)
#
#     return output_path

def fill_in_form(student_name, student_yob, subject, trial_date, trial_mentor, trial_place, points, feedback):
    doc = DocxTemplate(create_from_template(student_name, subject, trial_date))

    replacements = get_replacements(student_name, student_yob, subject, trial_date, trial_mentor, trial_place, points, feedback)

    cleaned_replacements = {k.strip("{}"): v for k, v in replacements.items()}
    doc.render(cleaned_replacements)

    output_path = create_output_path(student_name, subject, trial_date, file_extension="docx")
    doc.save(output_path)

    return output_path

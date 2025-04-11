from datetime import datetime


def get_replacements(student_name, student_yob, subject, trial_date, trial_mentor, trial_place, points, feedback):
    replacements = {
        "student_name": student_name,
        "student_yob": student_yob,
        "student_grade": str(datetime.now().year - int(student_yob) - 6 + (datetime.now().month >= 8)),
        "trial_date": trial_date.strftime("%d/%m/%Y"),
        "trial_mentor": trial_mentor,
        "trial_place": trial_place,
        "subject": subject,
        "trial_city": "Bình Dương" if trial_place == "Dĩ An" else "TP. HCM"
    }

    # Add points to replacements
    for i, point in enumerate(points):
        row = i + 1
        max_points = 5 if subject in ["Game Creator - GB", "Scratch Creator - SB", "Robotics - KIRO"] else 3
        for col in range(1, max_points + 1):
            placeholder = f"p{row}{col}"
            replacements[placeholder] = "✅" if col == point else ""

    # Add feedback paragraphs to replacements
    paragraphs = [p.strip() for p in feedback.strip().split("\n\n") if p.strip()]
    for i in range(1, 9):
        placeholder = f"feedback_{i}"
        replacements[placeholder] = paragraphs[i - 1] if i <= len(paragraphs) else ""


    ############################################################


    # Unique replacements
    if subject in ["Game Creator - GB", "Scratch Creator - SB"]:
        # Calculate average point
        avg_point = (sum(points) / 9)
        replacements["avg_point"] = f"{avg_point:.1f}"

        # Add types to replacements
        if 4 <= avg_point <= 5:
            replacements["type_1"] = "✅"
            replacements["type_2"] = replacements["type_3"] = replacements["type_4"] = replacements[
                "type_5"] = "    "
        elif 3.5 <= avg_point < 4:
            replacements["type_2"] = "✅"
            replacements["type_1"] = replacements["type_3"] = replacements["type_4"] = replacements[
                "type_5"] = "    "
        elif 2.5 <= avg_point < 3.5:
            replacements["type_3"] = "✅"
            replacements["type_1"] = replacements["type_2"] = replacements["type_4"] = replacements[
                "type_5"] = "    "
        elif 1.5 <= avg_point < 2.5:
            replacements["type_4"] = "✅"
            replacements["type_1"] = replacements["type_2"] = replacements["type_3"] = replacements[
                "type_5"] = "    "
        else:
            replacements["type_5"] = "✅"
            replacements["type_1"] = replacements["type_2"] = replacements["type_3"] = replacements[
                "type_4"] = "    "

    elif subject in ["Robotics - PRE", "Robotics - ARM"]:
        # Calculate average point
        avg_point = (sum(points) / 15)
        replacements["avg_point"] = f"{avg_point:.1f}"

        if 2 < avg_point <= 3:
            replacements["p163"] = "✅"
            replacements["p161"] = replacements["p162"] = ""
        elif 1.7 <= avg_point <= 2:
            replacements["p162"] = "✅"
            replacements["p161"] = replacements["p163"] = ""
        else:
            replacements["p161"] = "✅"
            replacements["p162"] = replacements["p163"] = ""


    elif  "Robotics - KIRO":
        # Calculate average point

        avg_point = (sum(points) / 4)
        replacements["avg_point"] = f"{avg_point:.1f}"


    return replacements


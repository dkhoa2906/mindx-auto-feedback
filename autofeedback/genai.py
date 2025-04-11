import os
from google import genai
from google.genai import types

from autofeedback.prompts import PROMPTS_BY_SUBJECT


def generate_feedback(student_name, basic_comment, subject, points, trial_result, suggested_level):
    client = genai.Client(api_key=os.environ.get("AI_STUDIO_API_KEY"))

    instructions = PROMPTS_BY_SUBJECT.get(subject)
    full_prompt = \
    f"""{instructions}
    Tên học viên: {student_name.strip().split()[-1]}
    Môn học: {subject}
    Nhận xét sơ bộ: {basic_comment}
    Điểm đánh giá theo thứ tự các tiêu chí: {points}
    Kết quả sau buổi trial: {trial_result}
    Cấp độ đề xuất (bỏ qua nếu kết quả không đạt): {suggested_level}
    Viết bài nhận xét theo yêu cầu trên.
    """

    form_config = types.GenerateContentConfig(
        response_mime_type="text/plain",
        temperature=0.6,
    )

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=full_prompt,
        config=form_config,
    )

    return response.text

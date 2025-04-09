import json
import os
from google import genai
from google.genai import types

from feedback_instructions import INSTRUCTION_BY_SUBJECT


def generate_feedback(student_name, basic_comment, subject, points):
    client = genai.Client(api_key=os.environ.get("AI_STUDIO_API_KEY"))

    instructions = INSTRUCTION_BY_SUBJECT.get(subject)
    full_prompt = \
    f"""{instructions}
    Tên học viên: {student_name.strip().split()[-1]}
    Môn học: {subject}
    Nhận xét sơ bộ: {basic_comment}
    Điểm đánh giá theo thứ tự các tiêu chí: {points}
    Viết bài nhận xét theo yêu cầu trên.
    """

    form_config = types.GenerateContentConfig(
        response_mime_type="text/plain",
        temperature=0.6,
    )

    # Enable for debugging
    # print(full_prompt)

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=full_prompt,
        config=form_config,
    )

    return response.text

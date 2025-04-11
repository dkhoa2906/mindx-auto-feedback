import urllib.parse

def get_mailto_link():
    email = "khoacao.dev@gmail.com"
    subject = "Feedback & Bug Report for MindX Auto Tool"
    body = f"""Chào Khoa,
    
Mình muốn gửi một vài góp ý/báo lỗi như sau:

Vấn đề gặp phải:
- (Mô tả lỗi tại đây)

Gợi ý tính năng:
- (Gợi ý tại đây)
"""

    return f"https://mail.google.com/mail/?view=cm&fs=1&to={email}&su={urllib.parse.quote(subject)}&body={urllib.parse.quote(body)}"
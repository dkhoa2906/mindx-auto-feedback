import datetime
import os

from document_generate import fill_in_form
from dotenv import load_dotenv
import streamlit as st

from feedback_generate import generate_feedback


def main():
    st.set_page_config(layout="wide")
    st.markdown("""
        <style>
            .block-container {
                padding-left: 10rem;
                padding-right: 10rem;
                margin-bottom: 0.5rem;
            }
        </style>
    """, unsafe_allow_html=True)

    col1, spacer, col2 = st.columns([1.2, 0.1, 0.8])

    with col1:
        st.title("🧠 Tạo Nhận Xét Học Viên")
        if st.button("Refresh now"):
            st.rerun()

        col1l, col1m, col1r = st.columns([1, 0.1, 1])

        with col1l:
            student_name = st.text_input("Tên học viên")
            student_age = st.text_input("Lớp:")
            subject = st.selectbox("Chọn bộ môn", ["Game Creator - GB", "-", "Scratch Creator - SB", "Robotics"])

        with col1r:
            trial_mentor = st.text_input("Giáo viên hướng dẫn")
            trial_place = st.selectbox("Cơ sở", ["-", "99 Lê Văn Việt", "Dĩ An", "Nào rảnh thêm mấy cơ sở khác :D"])
            trial_date = st.date_input("Ngày trải nghiệm", value="today", max_value="today", format="DD/MM/YYYY")

    with col2:
        if subject in ["Game Creator - GB", "Scratch Creator - SB"]:
            points = []
            categories = [
                "Hoàn thành thử thách trong khoảng thời gian quy định",
                "Biết cách ứng dụng công nghệ để hoàn thành thử thách",
                "Có kiến thức nền tảng (về văn hoá, tự nhiên, xã hội...)",

                "Sản phẩm tạo ra trong quá trình trải nghiệm có tính sáng tạo (cốt truyện, xây dựng nhân vật, màu sắc, âm thanh, v.v.)",
                "Khả năng biến tấu từ mẫu có sẵn, tạo ra sản phẩm độc đáo",

                "Biết cách tổ chức suy nghĩ và hành động theo các bước logic và trình tự",
                "Khi gặp lỗi hoặc vấn đề khi lập trình, học viên biết cách xác định và sửa chữa các lỗi",

                "Thuyết trình chia sẻ ý tưởng, sản phẩm",
                "Mạnh dạn, tự tin trong giao tiếp, đặt câu hỏi khi cần"
            ]

            for idx, category in enumerate(categories):
                point = st.slider(f"Mục {idx+1}. \n {category}", 1, 5, 3)
                points.append(point)

    with col1:
        if "docx_path" not in st.session_state:
            st.session_state.docx_path = None

        if "feedback" not in st.session_state:
            st.session_state.feedback = None

        basic_comment = st.text_area("Nhận xét sơ bộ")

        if st.button("Tạo nhận xét"):
            with st.spinner("🧠 Đang tạo nhận xét..."):
                feedback = generate_feedback(student_name, basic_comment, subject, points)
                st.session_state.feedback = feedback
                st.success("✅ Đã tạo nhận xét!")

        if st.session_state.feedback:
            st.text_area("Chỉnh sửa nhận xét", value=st.session_state.feedback, height=300, key="final_feedback")

            if st.button("📄 Xác nhận"):
                feedback = st.session_state.final_feedback

                docx_path = fill_in_form(student_name, student_age, subject, trial_date, trial_mentor, trial_place, points, feedback)
                print(docx_path) # debug

                st.session_state.docx_path = docx_path
                print(st.session_state.docx_path)

                st.success("✅ Đã điền nhận xét!")

            if st.session_state.docx_path:
                with open(st.session_state.docx_path, "rb") as f:
                    st.download_button("⬇️ Tải file Word (.docx)", f, file_name=os.path.basename(st.session_state.docx_path))
                    st.download_button("⬇️ Tải file PDF", f, file_name=os.path.basename(st.session_state.docx_path))

if __name__ == "__main__":
    load_dotenv()
    main()


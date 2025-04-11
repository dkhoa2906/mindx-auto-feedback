import base64
import os

from autodocument.doc_fill import fill_in_form
import streamlit as st

from autodocument.convert import convert_docx_to_pdf
from autofeedback.genai import generate_feedback
from contact.email_direct import get_mailto_link


def display_trial_page():

    ############ CONFIG CHUNG ############
    ############### Begin ################
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

    ################ End #################
    ############ CONFIG CHUNG ############


    col1, spacer, col2 = st.columns([1.2, 0.1, 0.8])


    ######## THÔNG TIN CHUNG SƠ BỘ ########
    ################ Begin ################

    with col1:
        st.title("🧠 MindX Auto Tool")
        st.caption("Developed by Cao Dang Khoa. Vui lòng sử dụng có trách nhiệm.\n"
                   )
        st.caption("Tool này được phát triển nhằm mục đích hỗ trợ viết nhận xét học viên một cách nhanh chóng và thuận tiện. "
                   "Nội dung nhận xét được gợi ý "
                   "dựa trên thông tin người dùng cung cấp và có thể cần được điều chỉnh trước khi sử dụng chính thức.")
        st.caption("Chúng tôi không chịu trách nhiệm về bất kỳ sai sót, thiếu sót hoặc hậu quả nào phát sinh từ việc sử "
                   "dụng trực tiếp nội dung nhận xét mà không kiểm tra lại. Người dùng cần tự chịu trách nhiệm kiểm duyệt "
                   "và điều chỉnh nội dung trước khi gửi cho phụ huynh, học sinh hoặc các bên liên quan.")

        col1l, col1m, col1r = st.columns([0.6, 1, 2])

        with col1l:
            if st.button("🔄 Reset"):
                st.rerun()
        with col1m:
            st.link_button("🐞 Contact", get_mailto_link())

        col1l, col1m, col1r = st.columns([1, 0.1, 1])

        with col1l:
            student_name = st.text_input("Tên học viên")
            student_yob = st.text_input("Năm sinh:")
            subject = st.selectbox("Chọn bộ môn", ["-", "Robotics - KIRO", "Robotics - PRE", "Robotics - ARM",
                                                   "Scratch Creator - SB", "Game Creator - GB"])
            trial_result = st.selectbox("Kết quả trial", ["Phù hợp", "Chưa phù hợp"])

        with col1r:
            trial_mentor = st.text_input("Giáo viên hướng dẫn")
            trial_place = st.selectbox("Cơ sở", ["-", "99 Lê Văn Việt", "Dĩ An", "Nào rảnh thêm mấy cơ sở khác :D"])
            trial_date = st.date_input("Ngày trải nghiệm", value="today", max_value="today", format="DD/MM/YYYY")
            suggested_level = st.selectbox("Cấp độ đề xuất", ["Basic", "Advanced", "Intensive"])

    ################# End #################
    ######## THÔNG TIN CHUNG SƠ BỘ ########



    ############ ĐIỂM ĐÁNH GIÁ ############
    ################ Begin ################

    with col2:
        points = []

        if subject in ["Game Creator - GB", "Scratch Creator - SB"]:
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
                point = st.slider(f"Mục {idx+1}. \n {category}", 1, 5, 1)
                points.append(point)

        elif subject in ["Robotics - PRE", "Robotics - ARM"]:

            categories = [
                "Hiểu cấu trúc và chức năng của motor và servo",
                "Biết cách kết nối và lắp đặt các thành phần cơ bản",
                "Có khả năng sử dụng công cụ và phụ kiện lắp ráp",

                "Lắp ráp một Robot đơn giản",

                "Hiểu cú pháp và cấu trúc cơ bản của ngôn ngữ lập trình",
                "Hiểu và sử dụng các câu lệnh điều khiển cơ bản (di chuyển, quay đầu, nâng hạ)",
                "Lập trình robot để hoàn thành một nhiệm vụ đơn giản",

                "Hiểu và sử dụng các cấu trúc điều khiển phức tạp (vòng lặp, rẽ nhánh)",
                "Lập trình robot để hoàn thành một nhiệm vụ phức tạp",

                "Giao tiếp hiệu quả với bạn và giáo viên hướng dẫn",
                "Trình bày ý kiến và ý tưởng một cách rõ ràng và logic",

                "Sử dụng thuật ngữ và ngôn ngữ chuyên ngành phù hợp trong lĩnh vực Robotics",
                "Mô tả các khái niệm kỹ thuật một cách rõ ràng và dễ hiểu",

                "Nhận biết và phân biệt các màu sắc cơ bản (đỏ, xanh, vàng)",
                "Nhận biết và định vị các vật thể trong không gian"
            ]

            col2l, col2m, col2r = st.columns([1, 0.01, 1])

            for idx, category in enumerate(categories):
                if idx < 8:
                    with col2l:
                        point = st.slider(f"Mục {idx + 1}. \n {category}", 1, 3, 1)
                        points.append(point)
                else:
                    with col2r:
                        point = st.slider(f"Mục {idx + 1}. \n {category}", 1, 3, 1)
                        points.append(point)

        elif subject in ["Robotics - KIRO"]:
            categories = {
                "NĂNG LỰC NHẬN BIẾT VÀ KHÁM PHÁ": """
                1️⃣ Cần giáo viên hỗ trợ phân biệt hình dạng và màu sắc chi tiết lắp ráp.  
                2️⃣ Nhận diện được màu sắc và hình dạng nhưng vẫn nhầm lẫn, cần hỗ trợ.  
                3️⃣ Nhận diện đúng hình dạng và màu sắc.  
                4️⃣ Nhận biết đúng, có thể diễn đạt chức năng các bộ phận.  
                5️⃣ Ghi nhớ mô hình, sáng tạo khi cải tiến mô hình.
                """,

                "NĂNG LỰC LẮP RÁP VÀ TƯ DUY KHÔNG GIAN": """
                1️⃣ Gặp nhiều khó khăn, sai sót nhiều, cần hỗ trợ liên tục.  
                2️⃣ Chọn đúng chi tiết nhưng lắp sai hướng/vị trí, cần hỗ trợ.  
                3️⃣ Đúng chi tiết và vị trí, đôi lúc sai, cần nhắc nhở.  
                4️⃣ Lắp ráp chính xác, biết sửa sai khi được gợi ý.  
                5️⃣ Lắp đúng, tự sửa sai, không cần hỗ trợ.
                """,

                "NĂNG LỰC LẬP TRÌNH": """
                1️⃣ Chưa kéo thả được, gặp khó khăn kể cả khi có hỗ trợ.  
                2️⃣ Kéo thả được nhưng chương trình sai, cần chỉnh sửa.  
                3️⃣ Lập trình để mô hình hoạt động đơn giản, cần gợi ý.  
                4️⃣ Lập trình đúng yêu cầu, ít cần hỗ trợ.  
                5️⃣ Thao tác nhanh, chính xác, chủ động điều chỉnh.
                """,

                "NĂNG LỰC GIAO TIẾP VÀ HỢP TÁC": """
                1️⃣ Chưa phản hồi, chưa hợp tác với giáo viên.  
                2️⃣ Có phản hồi ngắn, chưa tích cực tham gia.  
                3️⃣ Phản hồi và hợp tác, nhưng còn rụt rè.  
                4️⃣ Chủ động giao tiếp, hợp tác tốt trong hoạt động.  
                5️⃣ Giao tiếp tự tin, sẵn sàng chia sẻ mô hình/câu chuyện.
                """
            }

            for idx, (category, description) in enumerate(categories.items(), 1):
                st.markdown(f'<h4 style="font-size: 18px;">{idx}. {category}</h4>', unsafe_allow_html=True)
                st.caption(description)
                point = st.slider("Chọn mức điểm đánh giá", 1, 5, 1, key=f"score{idx}")
                points.append(point)

    ################ End #################
    ############ ĐIỂM ĐÁNH GIÁ ###########



    ############ TẠO NHẬN XÉT #############
    ################ Begin ################

    with col1:
        if "docx_path" not in st.session_state:
            st.session_state.docx_path = None

        if "feedback" not in st.session_state:
            st.session_state.feedback = None

        basic_comment = st.text_area("Nhận xét sơ bộ")

        if st.button("Tạo nhận xét"):
            st.session_state.docx_path = None
            st.session_state.pdf_path = None

            with st.spinner("🧠 Đang tạo nhận xét..."):
                feedback = generate_feedback(student_name, basic_comment, subject, points, trial_result, suggested_level)
                st.session_state.feedback = feedback
                st.success("✅ Đã tạo nhận xét!")

    ################ End #################
    ############# TẠO NHẬN XÉT ###########



    ############## XÁC NHẬN ##############
    ############### Begin ################

    with col1:
        if st.session_state.feedback:
            st.text_area("Chỉnh sửa nhận xét", value=st.session_state.feedback, height=300, key="final_feedback")

            pdf_needed = st.checkbox("Enable PDF exporting")

            if st.button("🫡 Xác nhận"):
                with st.spinner("🔄 Đang nhập thông tin vào file..."):
                    feedback = st.session_state.final_feedback
                    st.success("✅ Đã nhập thông tin")

                with st.spinner("🔄 Đang lưu file..."):
                    docx_path = fill_in_form(student_name, student_yob, subject, trial_date, trial_mentor, trial_place, points, feedback)
                    st.session_state.docx_path = docx_path
                    st.success("✅ Đã lưu file dưới dạng .DOCX")

                if pdf_needed:
                    with st.spinner("🔄 Đang xuất file sang .PDF..."):
                        pdf_path = convert_docx_to_pdf(docx_path, "pdf_output")
                        st.session_state.pdf_path = pdf_path

                st.success("✅ Tự động điền hoàn tất! Bấm nút bên dưới để tải xuống.")

            col1l, col1m, col1r = st.columns([2, 1, 1])

            if st.session_state.docx_path:
                with open(st.session_state.docx_path, "rb") as f:
                    with col1r:
                        st.download_button("📥 Tải file DOCX", f, file_name=os.path.basename(st.session_state.docx_path))

            elif st.session_state.pdf_path:
                with open(st.session_state.docx_path, "rb") as f:
                    with col1m:
                        st.download_button("📥 Tải file DOCX", f, file_name=os.path.basename(st.session_state.docx_path))
                with open(st.session_state.pdf_path, "rb") as f:
                    with col1r:
                        st.download_button("📥 Tải file PDF", f, file_name=os.path.basename(st.session_state.pdf_path))

    ################# End #################
    ############### XÁC NHẬN ##############
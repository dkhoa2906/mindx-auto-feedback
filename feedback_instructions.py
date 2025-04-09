INSTRUCTION_BY_SUBJECT = {
    "Game Creator - GB":
        """
        Hãy viết một bài nhận xét chi tiết cho học viên sau buổi học trải nghiệm theo cấu trúc sau. 
        Dùng ngôn từ tích cực, lịch sự, rõ ràng. Tránh chỉ trích, thay vào đó hãy nêu phương án cải thiện.
        Đánh giá dựa trên các tiêu chí: thái độ học tập, thao tác máy tính, kiến thức, tư duy, khả năng 
        tiếng Anh, và giao tiếp. Chia nội dung thành 4 phần, từng phần viết thành một đoạn:
        
        1. Điểm mạnh: Liệt kê 2–3 ưu điểm nổi bật mà học viên thể hiện trong buổi học, như: thái độ 
        học tập tích cực, thao tác chuột/gõ phím tốt, khả năng ghi nhớ, tư duy logic, vốn từ tiếng Anh 
        tốt, v.v. Nếu kỹ năng chuyên môn còn hạn chế, hãy nhấn mạnh các kỹ năng mềm.
        
        2. Điểm cần cải thiện: Chỉ ra 1–2 khía cạnh học viên còn yếu (như thao tác còn chậm, ít chủ 
        động tương tác, vốn từ hạn chế…) và giải thích nhẹ nhàng, mang tính xây dựng. Tránh nói các
        từ tiêu cực như: tuy nhiên, mặc dù vậy,...; thay vào đó hãy nói nhẹ nhàng hơn hoặc nói theo 
        cách con sẽ còn phát triển hơn nếu mặt này của con tốt hơn.
        
        3. Đề xuất cách cải thiện: Nêu 1–2 giải pháp cụ thể giúp học viên khắc phục những điểm trên 
        (như luyện gõ phím, xem thêm tài liệu tiếng Anh, chơi game giáo dục…). Nếu có thể, nên lồng 
        ghép khéo léo những giải pháp trong lớp học từ phía giáo viên (ví dụ các trường hợp sau đây
        tạo nhiều thử thách nhỏ trong quá trình học; chú ý lồng ghép các cơ hội để con được sáng tạo;
        trau dồi những từ tiếng anh xuất hiện trong quá trình học;...; và môi trường từ MindX để giúp
        con cải thiện/ phát triển).
        
        4. Kết luận: Đưa ra kết luận khách quan: học viên có phù hợp để bắt đầu chương trình học 
        Game Creator không, và đề xuất cấp độ phù hợp nếu có.
            
        Chỉ trong trường hợp nhận xét ban đầu là quá ít và bạn cần thêm ý để viết, hãy tham khảo kết quả
        đánh giá bằng điểm số dưới đây để tìm ra thế mạnh và điểm cần cải thiện của học viên. Các tiêu chí
        dưới đây được đang giá trên thang từ 1 đến 5, tương ứng với từ thấp đến cao:
        
        1. Hoàn thành thử thách trong khoảng thời gian quy định
        2. Biết cách ứng dụng công nghệ để hoàn thành thử thách
        3. Có kiến thức nền tảng (về văn hoá, tự nhiên, xã hội...)
	    4. Sản phẩm tạo ra trong quá trình trải nghiệm có tính sáng tạo 
	    (cốt truyện, xây dựng nhân vật, màu sắc, âm thanh, v.v.)
	    5. Khả năng biến tấu từ mẫu có sẵn, tạo ra sản phẩm độc đáo
	    6. Biết cách tổ chức suy nghĩ và hành động theo các bước logic và trình tự
	    7. Khi gặp lỗi hoặc vấn đề khi lập trình, học viên biết cách xác định và sửa chữa các lỗi
        8. Thuyết trình chia sẻ ý tưởng, sản phẩm
	    9. Mạnh dạn, tự tin trong giao tiếp, đặt câu hỏi khi cần.
	    
	    Dựa vào điểm trung bình của 9 tiêu chí trên, ta có thể đánh giá bé một cách tương đối như sau:
	    Mức xuất sắc (Điểm trung bình từ 4 - 5 điểm)
        Ở mức độ cao nhất, học viên không những tự chủ trong học tập, ứng dụng công nghệ mà còn biết cách sáng tạo để tạo ra những sản phẩm độc đáo. Với khả năng giao tiếp tự tin, tư duy logic và sáng tạo cân bằng, Học viên có nhiều cơ hội để phát triển trong tương lai số, có thể đóng góp tích cực vào việc phát triển và áp dụng công nghệ trong cộng đồng hoặc môi trường học tập của mình.
        
        Mức tiềm năng (Điểm trung bình từ 3,5 - 4 điểm)
        Học viên có năng khiếu thẩm mỹ, sáng tạo và khả năng ứng dụng công nghệ tương đối linh hoạt. Tiếp thu kiến thức nhanh, tương đối chủ động và tự tin khi giao tiếp. Có tiềm năng để phát triển trong tương lai khi có người hướng dẫn và lộ trình phù hợp.
        Mức trung bình (Điểm trung bình từ 2,5 - 3,5 điểm)
        Ở mức độ này, học viên bắt đầu khám phá và thử nghiệm với công nghệ một cách tự giác và có ý thức hơn. Có thể thực hiện các nhiệm vụ đơn giản như sử dụng phần mềm hoặc tìm kiếm thông tin trực tuyến, nhưng còn hạn chế trong việc áp dụng công nghệ để sáng tạo hoặc giải quyết vấn đề. Cần môi trường để kích thích phát triển.
        Mức cơ bản (Điểm trung bình từ 1,5 - 2,5 điểm)
        Học viên mới bắt đầu tiếp xúc với công nghệ. Tư duy thẩm mỹ và sáng tạo ở mức độ cơ bản. Biết cách ứng dụng công nghệ để tạo ra sản phẩm sáng tạo nhưng vẫn cần hướng dẫn và hỗ trợ sát sao. Cần tìm kiếm môi trường học tập phù hợp, lộ trình và người hướng dẫn để truyền cảm hứng, động lực cho trẻ.  
        Mức hạn chế (Điểm trung bình từ 1 - 1,5 điểm)
        Học viên chưa có nhiều trải nghiệm với công nghệ. Biết cách ứng dụng công nghệ để tạo ra sản phẩm sáng tạo, nhưng chưa tự tin và chủ động trong giao tiếp. Cần tìm kiếm môi trường học tập phù hợp, lộ trình và người hướng dẫn để truyền cảm hứng, động lực cho trẻ

	    
	    Không cần chào hỏi và hãy tránh nói quá để không gây sượng. Đối tượng đọc nhận xét này sẽ là cả
	    phụ huynh và người quản lí trung tâm MindX nên hãy xưng hô một cách chuyên nghiệp. Đừng xưng tôi,
	    mà hãy xưng là giáo viên. Đối với tên học viên, tuyệt đối không gọi bằng cả họ tên (tên đầy đủ) 
	    mà thay vào đó có thể linh hoạt gọi tên riêng (từ cuối cùng trong tên) hoặc tên riêng và tên đệm 
	    (2 từ cuối cùng trong tên). Dù vậy hãy chú ý tránh gọi tên nhiều gây sượng. Bạn có thể sử dụng từ
	    con hoặc từ bé để chỉ học viên. Tuy nhiên hãy sử dụng có đồng bộ. Chỉ cần trả về nhận xét của học 
	    viên thôi, không thêm bất kì câu nào khác. Không có phân đoạn rồi kí hiệu từng phần bằng ** **. Chỉ
	    output ra bài nhận xét thôi. Ở các phần ngắt đoạn, không cần thêm một dòng trống giữa hai đoạn mà
	    chỉ cần line break thôi. Không thêm khoảng trống chữa các đoạn.
	    
	    Dưới đây là một nhận xét mẫu, vui lòng chỉ dùng để tham khảo một cách có trách nhiệm:
	    Bé có thái độ học tập tốt, tập trung và lắng nghe nội dung giáo viên hướng dẫn. Khi 
	    được hỏi, bé có thể trả lời và đưa ra cách giải quyết vấn đề, thể hiện khả năng tiếp 
	    thu và tư duy logic khá tốt.\\n

        Bé tiếp thu kiến thức nhanh, hiểu và ghi nhớ tốt nội dung bài học. Đặc biệt, bé có thể 
        nhận diện và hiểu nghĩa một số từ tiếng Anh xuất hiện trong lập trình, đây là nền tảng 
        rất quan trọng trong quá trình học và phát triển sau này, đặc biệt là trong lĩnh vực Công 
        nghệ. Vì vậy giáo viên đề xuất bé nên tiếp tục rèn luyện và mở rộng vốn từ vựng để nâng 
        cao khả năng tiếp cận kiến thức lập trình.\\n
        
        Về thao tác, do bé đã quen thuộc với máy tính từ trước nên sử dụng chuột và bàn phím khá 
        thành thạo, thao tác nhanh và chính xác. Bé biết một số phím tắt trên Windows như Ctrl + C, 
        Ctrl + V, và khi được hướng dẫn thêm Ctrl + A, bé ghi nhớ rất nhanh và có thể áp dụng ngay 
        vào bài học.

        Dựa trên khả năng và biểu hiện của bé, giáo viên nhận thấy bé phù hợp với bộ môn Game Creator - Cấp độ Basic. 
        """,
}

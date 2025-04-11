PROMPTS_BY_SUBJECT = {
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

    "Scratch Creator - SB":
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
        Scratch Creator không, và đề xuất cấp độ phù hợp nếu có.
        
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
        
        Dựa trên khả năng và biểu hiện của bé, giáo viên nhận thấy bé phù hợp với bộ môn Scratch Creator - Cấp độ Basic. 
        """,

    "Robotics - PRE":
        """
        Hãy viết một bài nhận xét chi tiết cho học viên sau buổi học trải nghiệm theo cấu trúc sau. 
        Dùng ngôn từ tích cực, lịch sự, rõ ràng. Tránh chỉ trích, thay vào đó hãy nêu phương án cải thiện.
        Đánh giá dựa trên các tiêu chí: thái độ học tập, thao tác lắp ráp robot, kiến thức, tư duy, khả năng 
        tiếng Anh, và giao tiếp. Lưu ý rằng học viên là các bạn nhỏ tuổi. Chia nội dung thành 4 phần, từng 
        phần viết thành một đoạn:
        
        1. Điểm mạnh: Liệt kê 2–3 ưu điểm nổi bật mà học viên thể hiện trong buổi học, như: thái độ 
        học tập tích cực, khả năng hình học không gian tốt - khả năng lắp ráp robot, khả năng ghi nhớ,
        tư duy logic, vốn từ tiếng Anh tốt, khả năng nhận dạng màu sắc, hiểu biết về các bộ phận robot,
        v.v. Nếu kỹ năng chuyên môn còn hạn chế, hãy nhấn mạnh các kỹ năng mềm.
        
        2. Điểm cần cải thiện: Chỉ ra 1–2 khía cạnh học viên còn yếu (như thao tác còn chậm, ít chủ 
        động tương tác, vốn từ hạn chế…) và giải thích nhẹ nhàng, mang tính xây dựng. Tránh nói các
        từ tiêu cực như: tuy nhiên, mặc dù vậy,...; thay vào đó hãy nói nhẹ nhàng hơn hoặc nói theo 
        cách con sẽ còn phát triển hơn nếu mặt này của con tốt hơn.
        
        3. Đề xuất cách cải thiện: Nêu 1–2 giải pháp cụ thể giúp học viên khắc phục những điểm trên 
        (cho con được tiếp xúc với các loại mô hình lắp ráp nhiều hơn, cho con được thực hành lập trình
        nhiều để con có thể ghi nhớ…). Nếu có thể, nên lồng ghép khéo léo những giải pháp trong lớp học 
        từ phía giáo viên (ví dụ các trường hợp sau đây: tạo nhiều thử thách nhỏ trong quá trình học; 
        chú ý lồng ghép các cơ hội để con được sáng tạo; trau dồi những từ tiếng anh xuất hiện trong 
        quá trình học;...; và môi trường từ MindX để giúp con cải thiện/ phát triển).
        
        4. Kết luận: Đưa ra kết luận khách quan: học viên có phù hợp để bắt đầu chương trình học 
        Robotics - PRE không, và đề xuất cấp độ phù hợp nếu có.
        
        Chỉ trong trường hợp nhận xét ban đầu là quá ít và bạn cần thêm ý để viết, hãy tham khảo kết quả
        đánh giá bằng điểm số dưới đây để tìm ra thế mạnh và điểm cần cải thiện của học viên. Các tiêu chí
        dưới đây được đang giá trên thang từ 1 đến 5, tương ứng với từ thấp đến cao:
        
        1. Hiểu cấu trúc và chức năng của motor và servo
        2. Biết cách kết nối và lắp đặt các thành phần cơ bản
        3. Có khả năng sử dụng công cụ và phụ kiện lắp ráp
        4. Lắp ráp một Robot đơn giản

        5. Hiểu cú pháp và cấu trúc cơ bản của ngôn ngữ lập trình
        6. Hiểu và sử dụng các câu lệnh điều khiển cơ bản (di chuyển, quay đầu, nâng hạ)
        7. Lập trình robot để hoàn thành một nhiệm vụ đơn giản

        8. Hiểu và sử dụng các cấu trúc điều khiển phức tạp (vòng lặp, rẽ nhánh)
        9. Lập trình robot để hoàn thành một nhiệm vụ phức tạp

        10. Giao tiếp hiệu quả với bạn và giáo viên hướng dẫn
        11. Trình bày ý kiến và ý tưởng một cách rõ ràng và logic

        12. Sử dụng thuật ngữ và ngôn ngữ chuyên ngành phù hợp trong lĩnh vực Robotics
        13. Mô tả các khái niệm kỹ thuật một cách rõ ràng và dễ hiểu

        14. Nhận biết và phân biệt các màu sắc cơ bản (đỏ, xanh, vàng)",
        15. Nhận biết và định vị các vật thể trong không gian"    
        
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
        
        Bé có thái độ học tập tốt, tập trung và lắng nghe nội dung giáo viên hướng dẫn. Trong 
        quá trình học, bé khá tò mò với các linh kiện robot và tỏ ra thích thú khi được tự tay
        lắp ráp một robot đơn giản.
        
        Trong quá trình lắp ráp, bé thể hiện khả năng nhận dạng màu sắc, đặc điểm tốt, nhờ đó 
        bé có thể tìm các linh kiện cần thiết nhanh chóng. Tuy nhiên, tốc độ lắp ráp của bé 
        chưa nhanh do chưa được tiếp xúc với bộ kit Vex Go nhiều và điều này có thể dễ dàng khắc
        phục qua quá trình học khi bé được tiếp xúc và thực hành nhiều hơn.
        
        Khi tiếp xúc với các lệnh lập trình cơ bản cho robot, bé tiếp thu kiến thức nhanh, hiểu 
        và ghi nhớ ổn các câu lệnh. Khi được giáo viên đặt ra thử thách, bé biết thử nghiệm các 
        câu lệnh để tìm ra giải pháp cho vấn đề. Mặt khác, vì đây là lần đầu tiếp xúc với lập 
        trình thông qua tiếng Anh nên vẫn còn một số phần bé chưa thể hiểu hết. Nếu rèn luyện
        thêm vốn từ tiếng Anh, bé sẽ có khả năng tiếp xúc với các lệnh phức tạp hơn và mở rộng
        kiến thức của mình.
        
        
        Dựa trên khả năng và biểu hiện của bé, giáo viên nhận thấy bé phù hợp với bộ môn Robotics PRE - Cấp độ Basic. 
        """,

    "Robotics - ARM":
        """
        Hãy viết một bài nhận xét chi tiết cho học viên sau buổi học trải nghiệm theo cấu trúc sau. 
        Dùng ngôn từ tích cực, lịch sự, rõ ràng. Tránh chỉ trích, thay vào đó hãy nêu phương án cải thiện.
        Đánh giá dựa trên các tiêu chí: thái độ học tập, thao tác lắp ráp robot, kiến thức, tư duy, khả năng 
        tiếng Anh, và giao tiếp. Lưu ý rằng học viên là các bạn nhỏ tuổi. Chia nội dung thành 4 phần, từng 
        phần viết thành một đoạn:

        1. Điểm mạnh: Liệt kê 2–3 ưu điểm nổi bật mà học viên thể hiện trong buổi học, như: thái độ 
        học tập tích cực, khả năng hình học không gian tốt - khả năng lắp ráp robot, khả năng ghi nhớ,
        tư duy logic, vốn từ tiếng Anh tốt, khả năng nhận dạng màu sắc, hiểu biết về các bộ phận robot,
        v.v. Nếu kỹ năng chuyên môn còn hạn chế, hãy nhấn mạnh các kỹ năng mềm.

        2. Điểm cần cải thiện: Chỉ ra 1–2 khía cạnh học viên còn yếu (như thao tác còn chậm, ít chủ 
        động tương tác, vốn từ hạn chế…) và giải thích nhẹ nhàng, mang tính xây dựng. Tránh nói các
        từ tiêu cực như: tuy nhiên, mặc dù vậy,...; thay vào đó hãy nói nhẹ nhàng hơn hoặc nói theo 
        cách con sẽ còn phát triển hơn nếu mặt này của con tốt hơn.

        3. Đề xuất cách cải thiện: Nêu 1–2 giải pháp cụ thể giúp học viên khắc phục những điểm trên 
        (cho con được tiếp xúc với các loại mô hình lắp ráp nhiều hơn, cho con được thực hành lập trình
        nhiều để con có thể ghi nhớ…). Nếu có thể, nên lồng ghép khéo léo những giải pháp trong lớp học 
        từ phía giáo viên (ví dụ các trường hợp sau đây: tạo nhiều thử thách nhỏ trong quá trình học; 
        chú ý lồng ghép các cơ hội để con được sáng tạo; trau dồi những từ tiếng anh xuất hiện trong 
        quá trình học;...; và môi trường từ MindX để giúp con cải thiện/ phát triển).

        4. Kết luận: Đưa ra kết luận khách quan: học viên có phù hợp để bắt đầu chương trình học 
        Robotics - ARM không, và đề xuất cấp độ phù hợp nếu có.

        Chỉ trong trường hợp nhận xét ban đầu là quá ít và bạn cần thêm ý để viết, hãy tham khảo kết quả
        đánh giá bằng điểm số dưới đây để tìm ra thế mạnh và điểm cần cải thiện của học viên. Các tiêu chí
        dưới đây được đang giá trên thang từ 1 đến 5, tương ứng với từ thấp đến cao:

        1. Hiểu cấu trúc và chức năng của motor và servo
        2. Biết cách kết nối và lắp đặt các thành phần cơ bản
        3. Có khả năng sử dụng công cụ và phụ kiện lắp ráp
        4. Lắp ráp một Robot đơn giản

        5. Hiểu cú pháp và cấu trúc cơ bản của ngôn ngữ lập trình
        6. Hiểu và sử dụng các câu lệnh điều khiển cơ bản (di chuyển, quay đầu, nâng hạ)
        7. Lập trình robot để hoàn thành một nhiệm vụ đơn giản

        8. Hiểu và sử dụng các cấu trúc điều khiển phức tạp (vòng lặp, rẽ nhánh)
        9. Lập trình robot để hoàn thành một nhiệm vụ phức tạp

        10. Giao tiếp hiệu quả với bạn và giáo viên hướng dẫn
        11. Trình bày ý kiến và ý tưởng một cách rõ ràng và logic

        12. Sử dụng thuật ngữ và ngôn ngữ chuyên ngành phù hợp trong lĩnh vực Robotics
        13. Mô tả các khái niệm kỹ thuật một cách rõ ràng và dễ hiểu

        14. Nhận biết và phân biệt các màu sắc cơ bản (đỏ, xanh, vàng)",
        15. Nhận biết và định vị các vật thể trong không gian"    

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

        Bé có thái độ học tập tốt, tập trung và lắng nghe nội dung giáo viên hướng dẫn. Trong 
        quá trình học, bé khá tò mò với các linh kiện robot và tỏ ra thích thú khi được tự tay
        lắp ráp một robot đơn giản.

        Trong quá trình lắp ráp, bé thể hiện khả năng nhận dạng màu sắc, đặc điểm tốt, nhờ đó 
        bé có thể tìm các linh kiện cần thiết nhanh chóng. Tuy nhiên, tốc độ lắp ráp của bé 
        chưa nhanh do chưa được tiếp xúc với bộ kit Vex Go nhiều và điều này có thể dễ dàng khắc
        phục qua quá trình học khi bé được tiếp xúc và thực hành nhiều hơn.

        Khi tiếp xúc với các lệnh lập trình cơ bản cho robot, bé tiếp thu kiến thức nhanh, hiểu 
        và ghi nhớ ổn các câu lệnh. Khi được giáo viên đặt ra thử thách, bé biết thử nghiệm các 
        câu lệnh để tìm ra giải pháp cho vấn đề. Mặt khác, vì đây là lần đầu tiếp xúc với lập 
        trình thông qua tiếng Anh nên vẫn còn một số phần bé chưa thể hiểu hết. Nếu rèn luyện
        thêm vốn từ tiếng Anh, bé sẽ có khả năng tiếp xúc với các lệnh phức tạp hơn và mở rộng
        kiến thức của mình.


        Dựa trên khả năng và biểu hiện của bé, giáo viên nhận thấy bé phù hợp với bộ môn Robotics ARM - Cấp độ Basic. 
        """,

    "Robotics - KIRO":
        """
        Hãy viết một bài nhận xét chi tiết cho học viên sau buổi học trải nghiệm theo cấu trúc sau. 
        Dùng ngôn từ tích cực, lịch sự, rõ ràng. Tránh chỉ trích, thay vào đó hãy nêu phương án cải thiện.
        Đánh giá dựa trên các tiêu chí: thái độ học tập, thao tác lắp ráp robot, kiến thức, tư duy và 
        giao tiếp. Lưu ý rằng học viên là các bạn trong khoảng 4-6 tuổi. Chia nội dung thành 4 phần, từng 
        phần viết thành một đoạn:
    
        1. Điểm mạnh: Liệt kê 2–3 ưu điểm nổi bật mà học viên thể hiện trong buổi học, như: thái độ 
        học tập tích cực, khả năng hình học không gian tốt - khả năng lắp ráp robot, khả năng ghi nhớ,
        tư duy logic, khả năng nhận dạng màu sắc, hiểu biết về các bộ phận robot,
        v.v. Nếu kỹ năng chuyên môn còn hạn chế, hãy nhấn mạnh các kỹ năng mềm.
    
        2. Điểm cần cải thiện: Chỉ ra 1–2 khía cạnh học viên còn yếu (như thao tác còn chậm, ít chủ 
        động tương tác, vốn từ hạn chế…) và giải thích nhẹ nhàng, mang tính xây dựng. Tránh nói các
        từ tiêu cực như: tuy nhiên, mặc dù vậy,...; thay vào đó hãy nói nhẹ nhàng hơn hoặc nói theo 
        cách con sẽ còn phát triển hơn nếu mặt này của con tốt hơn.
    
        3. Đề xuất cách cải thiện: Nêu 1–2 giải pháp cụ thể giúp học viên khắc phục những điểm trên 
        (cho con được tiếp xúc với các loại mô hình lắp ráp nhiều hơn, cho con được thực hành lập trình
        nhiều để con có thể ghi nhớ…). Nếu có thể, nên lồng ghép khéo léo những giải pháp trong lớp học 
        từ phía giáo viên (ví dụ các trường hợp sau đây: tạo nhiều thử thách nhỏ trong quá trình học; 
        chú ý lồng ghép các cơ hội để con được sáng tạo; trau dồi những từ tiếng anh xuất hiện trong 
        quá trình học;...; và môi trường từ MindX để giúp con cải thiện/ phát triển).
    
        4. Kết luận: Đưa ra kết luận khách quan: học viên có phù hợp để bắt đầu chương trình học 
        Robotics - KIRO không, và đề xuất cấp độ phù hợp nếu có.
    
        Chỉ trong trường hợp nhận xét ban đầu là quá ít và bạn cần thêm ý để viết, hãy tham khảo kết quả
        đánh giá bằng điểm số dưới đây để tìm ra thế mạnh và điểm cần cải thiện của học viên. Các tiêu chí
        dưới đây được đang giá trên thang từ 1 đến 5, tương ứng với từ thấp đến cao:
    
        1. NĂNG LỰC NHẬN BIẾT VÀ KHÁM PHÁ
        Thang 1: Học viên cần giáo viên hỗ trợ phân biệt hình dạng và màu sắc chi tiết lắp ráp.
        Thang 2: Học viên nhận diện được màu sắc và hình dạng của các chi tiết lắp ráp, nhưng vẫn còn một số nhầm lẫn và cần giáo viên hỗ trợ.
        Thang 3: Học viên nhận diện đúng hình dạng và màu sắc của các chi tiết lắp ráp.
        Thang 4: Học viên nhận biết đúng màu sắc, hình dạng chi tiết lắp ráp. Có thể diễn đạt đơn giản chức năng của các bộ phận trong mô hình.	
        Thang 5: Học viên nhận diện đúng hình dạng, màu sắc chi tiết lắp ráp, nhớ tên mô hình và thể hiện sự sáng tạo qua việc cải tiến mô hình.
 
        II. NĂNG LỰC LẮP RÁP VÀ TƯ DUY KHÔNG GIAN
        Thang 1: Học viên gặp nhiều khó khăn trong việc chọn đúng chi tiết và lắp ráp. Sai sót nhiều, cần giáo viên hướng dẫn liên tục.	
        Thang 2: Học viên chọn đúng chi tiết nhưng gặp khó khăn về hướng và vị trí lắp ráp. Cần giáo viên hỗ trợ thường xuyên.
        Thang 3: Học viên chọn đúng chi tiết, xác định đúng hướng và vị trí nhưng đôi khi mắc lỗi. Cần giáo viên nhắc nhở để sửa sai.	
        Thang 4: Học viên lắp ráp chính xác, đôi khi sai nhưng có thể sửa lại khi được gợi ý.
        Thang 5: Học viên chọn đúng chi tiết, lắp ráp chính xác, có thể tự sửa sai mà không cần hỗ trợ.	

        III. NĂNG LỰC LẬP TRÌNH
        Thang 1: Học viên chưa thể kéo thả khối lệnh, gặp nhiều khó khăn ngay cả khi có giáo viên hỗ trợ.
        Thang 2: Học viên có thể kéo thả nhưng chương trình chưa chạy đúng, cần giáo viên chỉnh sửa.	
        Thang 3: Học viên kéo thả và lập trình để mô hình hoạt động đơn giản, nhưng vẫn cần gợi ý.
        Thang 4: Học viên lập trình đúng theo yêu cầu,  mà không cần nhiều sự hỗ trợ.
        Thang 5: Học viên thao tác nhanh, chính xác, chủ động điều chỉnh thông số trong chương trình.

        IV. NĂNG LỰC GIAO TIẾP VÀ HỢP TÁC 		
        Thang 1: Học viên chưa phản hồi hoặc chưa hợp tác với giáo viên trong quá trình học.
        Thang 2: Học viên có phản hồi ngắn nhưng chưa thực sự hợp tác với giáo viên, chưa tham gia vào hoạt động lắp ráp mô hình.
        Thang 3: Học viên có phản hồi và hợp tác với giáo viên, tuy nhiên vẫn còn rụt rè, chưa thực sự tự tin khi tham gia trải nghiệm.
        Thang 4: Học viên chủ động giao tiếp, sẵn sàng trò chuyện và hợp tác với giáo viên trong các hoạt động.
        Thang 5: Học viên giao tiếp tự tin, hợp tác tốt với giáo viên và sẵn sàng chia sẻ về mô hình hoặc câu chuyện của mình.


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
    
        Bé có thái độ học tập tốt, thích thú và lắng nghe nội dung giáo viên hướng dẫn. Trong 
        quá trình học, bé khá tò mò với các linh kiện lego và tỏ ra thích thú khi được tự tay
        lắp ráp một robot đơn giản.
    
        Trong quá trình lắp ráp, bé thể hiện khả năng nhận dạng màu sắc, đặc điểm tốt, nhờ đó 
        bé có thể tìm các linh kiện cần thiết nhanh chóng. Tuy nhiên, tốc độ lắp ráp của bé 
        chưa nhanh do chưa được tiếp xúc với lego nhiều và điều này có thể dễ dàng khắc
        phục qua quá trình học khi bé được tiếp xúc và thực hành nhiều hơn.
    
        Khi tiếp xúc với các lệnh lập trình cơ bản cho robot, bé có khả năng ghi nhớ chức năng
        câu lệnh sau vài lần chạy thử lệnh. Mặt khác, vì đây là lần đầu tiếp xúc với lập 
        trình nên bé còn hơi ham thử nghiệm mà chưa thật sự tập trung vào thử thách giáo viên đề ra.
        Do đó giáo viên sẽ lồng ghép các cơ hội cho bé được thử sáng tạo trong quá trình học
        để bé vừa được tiếp thu kiến thức mà không ngăn cản khả năng sáng tạo của bé.
    
        Dựa trên khả năng và biểu hiện của bé, giáo viên nhận thấy bé phù hợp với bộ môn Robotics KIRO - Cấp độ Basic. 
        """,
}

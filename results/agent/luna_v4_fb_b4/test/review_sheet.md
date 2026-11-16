# Review sheet luna_v4_fb_b4 / test


## t3_ch1 [chart] status=answered retrieval_calls=1
**Q:** Trong biểu đồ 'Color Emotion Guide', dải màu xanh lá thể hiện những cảm xúc nào?
**Expected:** PEACEFUL, GROWTH, HEALTH.
**Gold:** p78 (visual) `GROWTH`
**Context evidence:** {'all': True, 'any': True, 'groups': [True]}
**Answer:** Dải màu xanh lá thể hiện: **PEACEFUL – GROWTH – HEALTH** (yên bình – phát triển – sức khỏe). [B4:colorme3:p078:v00]
- `B4:colorme3:p078:v00` p?: MISSING
**Searches:** search_docs('biểu đồ Color Emotion Guide dải màu xanh lá thể hiện những cảm xúc nào', {'chapter': 'ch3', 'content_type': 'visual'})

## t3_ch2 [chart] status=answered retrieval_calls=1
**Q:** Trong biểu đồ 'Color Emotion Guide', cảm xúc TRUST nằm ở dải màu gì và đi cùng những từ nào?
**Expected:** Dải xanh dương: TRUST, DEPENDABLE, STRENGTH.
**Gold:** p78 (visual) `DEPENDABLE`
**Context evidence:** {'all': True, 'any': True, 'groups': [True]}
**Answer:** Trong biểu đồ “Color Emotion Guide”, **TRUST** nằm ở **dải màu xanh dương**, đi cùng các từ **DEPENDABLE** và **STRENGTH**. [B4:colorme3:p078:v00]
- `B4:colorme3:p078:v00` p?: MISSING
**Searches:** search_docs('biểu đồ Color Emotion Guide TRUST dải màu những từ đi cùng', {'chapter': 'ch3', 'content_type': 'visual'})

## t3_ch3 [chart] status=answered retrieval_calls=1
**Q:** Trong trang 'CV – Charts', thanh tiến trình ngang được tô màu nhiều hơn hay ít hơn một nửa chiều dài?
**Expected:** Nhiều hơn một nửa (khoảng 80%).
**Gold:** p160 (visual) `80`
**Context evidence:** {'all': False, 'any': False, 'groups': [False]}
**Answer:** Thanh tiến trình ngang được tô màu nhiều hơn một nửa chiều dài; phần màu xanh dương chiếm khoảng 85%, còn phần màu xám khoảng 15%. [B4:colorme3:p160:v03]
- `B4:colorme3:p160:v03` p?: MISSING
**Searches:** search_docs('trang CV – Charts thanh tiến trình ngang được tô màu dài bao nhiêu so với một nửa', {'chapter': 'ch7', 'content_type': 'visual'})

## t3_ch4 [chart] status=abstain retrieval_calls=2
**Q:** Trong biểu đồ bong bóng 'Các bài toán thường gặp', bong bóng 'Nhận diện thương hiệu' lớn hơn hay nhỏ hơn bong bóng 'Chỉnh sửa ảnh'?
**Expected:** Lớn hơn (bong bóng xanh dương lớn hơn bong bóng vàng).
**Gold:** p6 (visual) `Nhận diện thương hiệu`
**Context evidence:** {'all': True, 'any': True, 'groups': [True]}
**Answer:** Không đủ bằng chứng trong sách để trả lời câu hỏi này.
**Searches:** search_docs('biểu đồ bong bóng "Các bài toán thường gặp" bong bóng "Nhận diện thương hiệu" "Chỉnh sửa ảnh"', {'content_type': 'visual'}) | read_page('page=6', None)

## t3_ch5 [chart] status=abstain retrieval_calls=2
**Q:** Trong sơ đồ vòng tròn màu minh họa hệ RGB, biểu tượng ở tâm vòng tròn thể hiện trạng thái các đèn led thế nào?
**Expected:** Cả 3 đèn đỏ, xanh lá, xanh dương đều bật (tạo màu trắng).
**Gold:** p17 (visual) `tâm`
**Context evidence:** {'all': True, 'any': True, 'groups': [True]}
**Answer:** Không đủ bằng chứng trong sách để trả lời câu hỏi này.
**Searches:** search_docs('sơ đồ vòng tròn màu hệ RGB biểu tượng ở tâm vòng tròn trạng thái các đèn led', {'chapter': 'ch1', 'content_type': 'visual'}) | search_docs('hệ màu RGB ba đèn LED tâm vòng tròn cùng bật trạng thái tắt bật ánh sáng trắng', {'chapter': 'ch1', 'content_type': 'text'})

## t3_img1 [image] status=answered retrieval_calls=1
**Q:** Chiếc iPod trong ảnh minh họa mục 'Apple với iPod' có màu gì?
**Expected:** Xanh dương (sáng), dây đeo cùng màu.
**Gold:** p64 (visual) `iPod`
**Context evidence:** {'all': True, 'any': True, 'groups': [True]}
**Answer:** Chiếc iPod có màu xanh dương ngả xanh ngọc. [B4:colorme3:p064:v00]
- `B4:colorme3:p064:v00` p?: MISSING
**Searches:** search_docs('mục “Apple với iPod” chiếc iPod trong ảnh minh họa màu gì', {'content_type': 'visual'})

## t3_img2 [image] status=answered retrieval_calls=2
**Q:** Hai poster phim minh họa phối màu tương đồng (Gradient Tool) là những phim nào?
**Expected:** The Little Mermaid và The Lion King (Disney).
**Gold:** p69 (visual) `LION KING`
**Context evidence:** {'all': True, 'any': True, 'groups': [True]}
**Answer:** Hai poster phim là **The Little Mermaid** và **The Lion King**. [B4:colorme3:p069:v00] [B4:colorme3:p069:v01]
- `B4:colorme3:p069:v00` p?: MISSING
- `B4:colorme3:p069:v01` p?: MISSING
**Searches:** search_docs('hai poster phim minh họa phối màu tương đồng Gradient Tool tên phim', {'chapter': 'ch3', 'content_type': 'visual'}) | search_docs('Gradient Tool phối màu tương đồng poster phim', {'chapter': 'ch3', 'content_type': 'text'})

## t3_img3 [image] status=answered retrieval_calls=1
**Q:** Poster sự kiện minh họa nhóm màu neon có tên sự kiện gì và diễn ra vào ngày nào?
**Expected:** SUMMER DANCE PARTY (Cocktail Bar), FRIDAY 18 SEPTEMBER.
**Gold:** p83 (visual) `SUMMER DANCE PARTY`
**Context evidence:** {'all': True, 'any': True, 'groups': [True]}
**Answer:** Poster có tên sự kiện **“SUMMER DANCE PARTY”** và diễn ra vào **Friday, 18 September** (Thứ Sáu, 18 tháng 9). [B4:colorme3:p083:v00]
- `B4:colorme3:p083:v00` p?: MISSING
**Searches:** search_docs('poster sự kiện minh họa nhóm màu neon tên sự kiện ngày diễn ra', {'chapter': 'ch3', 'content_type': 'visual'})

## t3_img4 [image] status=answered retrieval_calls=1
**Q:** Ví dụ 'thay đổi kích thước' với 1 typeface là poster phim nào, và hình chính là gì?
**Expected:** THE GOOD THE BAD AND THE UGLY; bóng một người đàn ông đội mũ chứa phong cảnh bên trong.
**Gold:** p95 (visual) `THE GOOD THE BAD AND THE UGLY`
**Context evidence:** {'all': True, 'any': True, 'groups': [True]}
**Answer:** Đó là poster phim **The Good, the Bad and the Ugly**. Hình chính là một người đội mũ rộng vành, với phần thân được tạo thành từ hình ảnh phong cảnh sa mạc/đồng cỏ. [B4:colorme3:p095:v00]
- `B4:colorme3:p095:v00` p?: MISSING
**Searches:** search_docs('ví dụ “thay đổi kích thước” với một typeface poster phim hình chính là gì', {'chapter': 'ch4', 'content_type': 'visual'})

## t3_img5 [image] status=answered retrieval_calls=1
**Q:** Ba logo ví dụ cho loại logo kết hợp là của những thương hiệu nào?
**Expected:** Starbucks Coffee, BMW, Puma.
**Gold:** p135 (visual) `BMW`
**Context evidence:** {'all': True, 'any': True, 'groups': [True]}
**Answer:** Ba logo ví dụ cho loại logo kết hợp là của Starbucks Coffee, BMW và Puma. [B4:colorme3:p135:v00]
- `B4:colorme3:p135:v00` p?: MISSING
**Searches:** search_docs('ba logo ví dụ cho loại logo kết hợp là của những thương hiệu nào', {'chapter': 'ch6', 'content_type': 'visual'})

## t3_mh1 [multihop] status=answered retrieval_calls=1
**Q:** Hiệu ứng làm mờ mở đầu chương 5 tên là gì, và ở chương xu hướng thiết kế nó được ứng dụng kết hợp với phong cách nào?
**Expected:** Blur; kết hợp với thiết kế phẳng (Flat Design) qua Blur Background.
**Gold:** p124 (text) `Bắt đầu chương 5 với hiệu ứng blur bạn nhé`; p171 (text) `Ứng dụng với Blur BackGround`
**Context evidence:** {'all': True, 'any': True, 'groups': [True, True]}
**Answer:** Hiệu ứng làm mờ mở đầu chương 5 có tên là **Blur – Filter Gallery**. [B4:colorme3:p124:t00]

Ở chương xu hướng thiết kế, hiệu ứng này được ứng dụng kết hợp với phong cách **Flat Design**, dưới dạng **Blur Background**. [B4:colorme3:p171:t00]
- `B4:colorme3:p124:t00` p?: MISSING
- `B4:colorme3:p171:t00` p?: MISSING
**Searches:** search_docs('hiệu ứng làm mờ mở đầu chương 5 tên là gì và trong chương xu hướng thiết kế được ứng dụng kết hợp với phong cách nào', {'content_type': 'text'})

## t3_mh2 [multihop] status=answered retrieval_calls=1
**Q:** Font serif và font sans-serif lần lượt được dùng nhiều trong những lĩnh vực nào?
**Expected:** Serif: nhà hàng, khách sạn, kinh tế, giáo dục; sans-serif: quảng cáo, truyền thông, công nghệ.
**Gold:** p89 (text) `nhà hàng, khách sạn, kinh tế, giáo dục`; p91 (text) `quảng cáo, truyền thông và công nghệ`
**Context evidence:** {'all': True, 'any': True, 'groups': [True, True]}
**Answer:** - **Font serif (chữ có chân):** được ứng dụng nhiều trong **nhà hàng, khách sạn, kinh tế và giáo dục**, đồng thời hoạt động tốt ở những nơi có mật độ chữ dày như **sách hoặc báo**. [B4:colorme3:p089:t00]
- **Font sans-serif (chữ không chân):** được dùng nhiều trong **quảng cáo, truyền thông và công nghệ**. [B4:colorme3:p091:t00]
- `B4:colorme3:p089:t00` p?: MISSING
- `B4:colorme3:p091:t00` p?: MISSING
**Searches:** search_docs('font serif và sans-serif được dùng nhiều trong những lĩnh vực nào', {'chapter': 'ch4', 'content_type': 'text'})

## t3_mh3 [multihop] status=answered retrieval_calls=1
**Q:** Kĩ thuật đóng khung và kĩ thuật line trong typography khác nhau thế nào?
**Expected:** Đóng khung: tạo bo viền quanh chữ để mọi thứ bên trong thành một thể thống nhất; line: dùng đường kẻ để phân tách bố cục.
**Gold:** p102 (text) `tạo ra một bo viền xung quanh chữ`; p106 (text) `Là kĩ thuật dùng những đường kẻ để phân tách bố cục của bản thiết kế.`
**Context evidence:** {'all': True, 'any': True, 'groups': [True, True]}
**Answer:** - **Kĩ thuật đóng khung (Border):** tạo một bo viền xung quanh chữ, khiến tất cả những thứ nằm trong bo viền trở thành một thể thống nhất. Bo viền không bắt buộc phải có hình chữ nhật hoặc phải khép kín. [B4:colorme3:p102:t00] [B4:colorme3:p103:t00]
- **Kĩ thuật line:** dùng những đường kẻ để phân tách bố cục của bản thiết kế. [B4:colorme3:p106:t00]

**Khác nhau:** đóng khung tạo bo viền quanh chữ và thống nhất các thành phần bên trong, còn line dùng đường kẻ để phân tách bố cục.
- `B4:colorme3:p102:t00` p?: MISSING
- `B4:colorme3:p103:t00` p?: MISSING
- `B4:colorme3:p106:t00` p?: MISSING
**Searches:** search_docs('Typography kĩ thuật đóng khung và kĩ thuật line khác nhau như thế nào', {'chapter': 'ch4', 'content_type': 'text'})

## t3_mh4 [multihop] status=answered retrieval_calls=1
**Q:** Logo mô thức (Pattern and Shape) và logo hình khối (Geometric Shape) được định nghĩa khác nhau thế nào?
**Expected:** Logo mô thức nằm trong các hình đa giác đều (tam giác đều, hình vuông, lục giác đều); logo hình khối chỉ tạo thành từ những đường thẳng.
**Gold:** p143 (text) `Là nhóm logo nằm trong các hình đa giác đều`; p144 (text) `Là những logo chỉ được tạo thành từ những đường thẳng`
**Context evidence:** {'all': True, 'any': True, 'groups': [True, True]}
**Answer:** - **Logo mô thức (Pattern And Shape Logo):** là nhóm logo nằm trong các hình đa giác đều như tam giác đều, hình vuông, lục giác đều. [B4:colorme3:p143:t00]
- **Logo hình khối (Geometric Shape Logos):** là những logo chỉ được tạo thành từ những đường thẳng. [B4:colorme3:p144:t00]

Vì vậy, logo mô thức được định nghĩa theo việc nằm trong các hình đa giác đều, còn logo hình khối được định nghĩa theo việc chỉ được tạo thành từ những đường thẳng.
- `B4:colorme3:p143:t00` p?: MISSING
- `B4:colorme3:p144:t00` p?: MISSING
**Searches:** search_docs('logo mô thức Pattern and Shape logo hình khối Geometric Shape định nghĩa khác nhau', {'chapter': 'ch6', 'content_type': 'text'})

## t3_tab1 [table] status=answered retrieval_calls=1
**Q:** Trong bảng phím tắt nhóm FILE, CTRL + W và CTRL + ALT + S dùng để làm gì?
**Expected:** CTRL + W: đóng file; CTRL + ALT + S: lưu thêm 1 bản copy.
**Gold:** p174 (text) `CTRL + ALT + S (Save a Copy): Lưu thêm 1 bản copy`
**Context evidence:** {'all': True, 'any': True, 'groups': [True]}
**Answer:** Trong nhóm FILE:
- **CTRL + W (Close):** Đóng file.
- **CTRL + ALT + S (Save a Copy):** Lưu thêm một bản copy. [B4:colorme3:p174:t00]
- `B4:colorme3:p174:t00` p?: MISSING
**Searches:** search_docs('bảng phím tắt nhóm FILE CTRL + W CTRL + ALT + S dùng để làm gì', {'chapter': 'appendix', 'content_type': 'text'})

## t3_tab2 [table] status=answered retrieval_calls=1
**Q:** Trong nhóm lệnh EDIT của bảng phím tắt, CTRL + ALT + Z và CTRL + SHIFT + C làm gì?
**Expected:** CTRL + ALT + Z: trở lại nhiều bước; CTRL + SHIFT + C: Copy Merged.
**Gold:** p175 (text) `CTRL + ALT + Z: Trở lại nhiều bước`
**Context evidence:** {'all': True, 'any': True, 'groups': [True]}
**Answer:** Trong nhóm lệnh EDIT:
- **CTRL + ALT + Z**: Trở lại nhiều bước.
- **CTRL + SHIFT + C**: Copy Merged (sao chép phần đã hợp nhất). [B4:colorme3:p175:t01]
- `B4:colorme3:p175:t01` p?: MISSING
**Searches:** search_docs('bảng phím tắt nhóm lệnh EDIT CTRL + ALT + Z CTRL + SHIFT + C', {'chapter': 'appendix', 'content_type': 'text'})

## t3_tab3 [table] status=answered retrieval_calls=1
**Q:** Trong bảng phím tắt Toolbar, phím G và phím E tương ứng công cụ gì?
**Expected:** G: đổ màu/đổ màu chuyển; E: tẩy.
**Gold:** p176 (text) `G: Đổ màu/Đổ màu chuyển`
**Context evidence:** {'all': True, 'any': True, 'groups': [True]}
**Answer:** Trong nhóm phím tắt Toolbar:
- **G**: Đổ màu/Đổ màu chuyển. [B4:colorme3:p176:t00]
- **E**: Tẩy. [B4:colorme3:p176:t00]
- `B4:colorme3:p176:t00` p?: MISSING
**Searches:** search_docs('bảng phím tắt Toolbar phím G phím E công cụ', {'chapter': 'appendix', 'content_type': 'text'})

## t3_tab4 [table] status=answered retrieval_calls=1
**Q:** Trong ảnh Adobe Kuler, ô màu đầu tiên (đang được chọn) có giá trị RGB và mã HEX nào?
**Expected:** RGB 255 83 13; HEX FF530D.
**Gold:** p86 (visual) `FF530D`
**Context evidence:** {'all': True, 'any': True, 'groups': [True]}
**Answer:** Ô màu đầu tiên có giá trị RGB **255 83 13** và mã HEX **FF530D**. [B4:colorme3:p086:v01]
- `B4:colorme3:p086:v01` p?: MISSING
**Searches:** search_docs('ảnh Adobe Kuler ô màu đầu tiên đang được chọn giá trị RGB mã HEX', {'content_type': 'visual'})

## t3_tab5 [table] status=answered retrieval_calls=1
**Q:** Trong bảng 8 ô màu kèm từ khóa cảm nhận (tiếng Anh), màu pink gắn với những từ khóa nào?
**Expected:** TENDERNESS, SENSITIVE, CARING, EMOTIONAL, SYMPATHETIC, LOVE, SEXUALITY.
**Gold:** p77 (visual) `TENDERNESS`
**Context evidence:** {'all': True, 'any': True, 'groups': [True]}
**Answer:** Màu **pink** gắn với các từ khóa: **TENDERNESS, SENSITIVE, CARING, EMOTIONAL, SYMPATHETIC, LOVE, SEXUALITY**. [B4:colorme3:p077:v00]
- `B4:colorme3:p077:v00` p?: MISSING
**Searches:** search_docs('bảng 8 ô màu từ khóa cảm nhận tiếng Anh màu pink', {'chapter': 'ch3', 'content_type': 'visual'})

## t3_tab6 [table] status=answered retrieval_calls=1
**Q:** Trong bảng màu dành cho logo, thanh màu hồng gắn với những tính từ nào?
**Expected:** Nữ tính, ngây thơ, dịu dàng, khoẻ mạnh, trẻ trung.
**Gold:** p136 (visual) `hồng`
**Context evidence:** {'all': True, 'any': True, 'groups': [True]}
**Answer:** Thanh màu hồng gắn với các tính từ: **nữ tính, ngây thơ, dịu dàng, khoẻ mạnh, trẻ trung**. [B4:colorme3:p136:v00]
- `B4:colorme3:p136:v00` p?: MISSING
**Searches:** search_docs('bảng màu dành cho logo thanh màu hồng gắn với những tính từ nào', {'chapter': 'ch6', 'content_type': 'visual'})

## t3_tx1 [text] status=answered retrieval_calls=2
**Q:** Theo sách, sai lầm lớn nhất thường gặp của người mới bắt đầu thiết kế là gì?
**Expected:** Dùng quá nhiều màu sắc, biến tác phẩm thành mớ hỗn độn.
**Gold:** p62 (text) `các bạn dùng… quá nhiều màu sắc`
**Context evidence:** {'all': True, 'any': True, 'groups': [True]}
**Answer:** Theo sách, sai lầm lớn nhất thường gặp của người mới bắt đầu thiết kế là dùng quá nhiều màu sắc, khiến thiết kế trở thành một mớ hỗn độn khó cảm nhận. [B4:colorme3:p062:t00]
- `B4:colorme3:p062:t00` p?: MISSING
**Searches:** search_docs('sai lầm lớn nhất thường gặp của người mới bắt đầu thiết kế', {'content_type': 'text'}) | search_docs('người mới bắt đầu thiết kế sai lầm lớn nhất lỗi thường gặp bắt đầu từ đâu', {'content_type': 'text'})

## t3_tx2 [text] status=answered retrieval_calls=1
**Q:** Khi tác giả hỏi lớp học colorME ai cần một CV đẹp, tỉ lệ người giơ tay thế nào?
**Expected:** Chưa lần nào dưới 80%.
**Gold:** p153 (text) `Chưa lần nào số`
**Context evidence:** {'all': True, 'any': True, 'groups': [True]}
**Answer:** Chưa lần nào số người giơ tay thấp hơn 80%.[B4:colorme3:p153:t00]
- `B4:colorme3:p153:t00` p?: MISSING
**Searches:** search_docs('tác giả hỏi lớp học colorME ai cần một CV đẹp bao nhiêu người giơ tay tỉ lệ', {'chapter': 'ch7', 'content_type': 'text'})

## t3_tx3 [text] status=answered retrieval_calls=1
**Q:** Theo sách, kích thước chữ phụ thuộc vào điều gì của nội dung?
**Expected:** Độ phân cấp thông tin.
**Gold:** p39 (text) `Câu trả lời chính là độ phân cấp thông tin.`
**Context evidence:** {'all': True, 'any': True, 'groups': [True]}
**Answer:** Theo sách, kích thước chữ phụ thuộc vào **độ phân cấp thông tin** của nội dung. [B4:colorme3:p039:t00]
- `B4:colorme3:p039:t00` p?: MISSING
**Searches:** search_docs('kích thước chữ phụ thuộc vào điều gì của nội dung', {'chapter': 'ch4', 'content_type': 'text'})

## t3_tx4 [text] status=answered retrieval_calls=1
**Q:** Vì sao cần phân bố độ to nhỏ của từng con chữ cho phù hợp (lỗi 'không có chính phụ')?
**Expected:** Để những phần nội dung có thêm không gian để có thể 'thở'.
**Gold:** p116 (text) `Để những phần nội dung có thêm không gian`
**Context evidence:** {'all': True, 'any': True, 'groups': [True]}
**Answer:** Cần phân bố độ to nhỏ của từng con chữ một cách phù hợp để những phần nội dung có thêm không gian để “thở”. [B4:colorme3:p116:t00]
- `B4:colorme3:p116:t00` p?: MISSING
**Searches:** search_docs('phân bố độ to nhỏ của từng con chữ phù hợp lỗi không có chính phụ vì sao typography', {'chapter': 'ch4', 'content_type': 'text'})

## t3_un1 [unanswerable] status=abstain retrieval_calls=2
**Q:** Theo sách, xây dựng một bộ nhận diện thương hiệu đầy đủ thường tốn bao nhiêu chi phí?
**Expected:** abstain — p149-151 liệt kê thành phần bộ nhận diện, không có chi phí.
**Answer:** Sách không nêu mức chi phí cụ thể cho một bộ nhận diện thương hiệu đầy đủ. Sách chỉ liệt kê bộ nhận diện có thể gồm logo, font chữ, slogan, ấn phẩm văn phòng, đồng phục, ấn phẩm truyền thông, hàng hóa và quà tặng. [B4:colorme3:p150:t00]
**Searches:** search_docs('chi phí xây dựng một bộ nhận diện thương hiệu đầy đủ thường tốn bao nhiêu', {'chapter': 'ch6', 'content_type': 'text'}) | search_docs('giá tiền chi phí thiết kế brand identity bộ nhận diện thương hiệu đầy đủ', {'content_type': 'text'})

## t3_un2 [unanswerable] status=abstain retrieval_calls=2
**Q:** Kích thước file PSD tối đa mà Photoshop hỗ trợ là bao nhiêu?
**Expected:** abstain — Sách không nói về giới hạn kích thước file.
**Answer:** Sách không có thông tin về kích thước file PSD tối đa mà Photoshop hỗ trợ.
**Searches:** search_docs('kích thước file PSD tối đa Photoshop hỗ trợ dung lượng tối đa', {'chapter': 'ch1', 'content_type': 'text'}) | search_docs('PSD file maximum size 2 GB Photoshop hỗ trợ tối đa file PSD', {'content_type': 'text'})

## t3_un3 [unanswerable] status=abstain retrieval_calls=2
**Q:** Sách so sánh Photoshop với phần mềm GIMP như thế nào?
**Expected:** abstain — p8 chỉ so Photoshop với Illustrator, InDesign, Lightroom; không nhắc GIMP.
**Answer:** Sách không có thông tin so sánh Photoshop với phần mềm GIMP.
**Searches:** search_docs('Photoshop GIMP so sánh phần mềm chỉnh sửa ảnh khác nhau', {'content_type': 'text'}) | search_docs('GIMP phần mềm Photoshop các phần mềm thiết kế thường gặp', {'chapter': 'ch1'})

## t3_un4 [unanswerable] status=answered retrieval_calls=2
**Q:** Theo sách, mã HEX của màu đỏ trong logo colorME là gì?
**Expected:** abstain — Sách không ghi mã màu logo colorME (mã HEX duy nhất là của ảnh Kuler p86).
**Answer:** Mã HEX của màu đỏ trong logo colorME là **FF0000**. [B4:colorme3:p086:v01]
- `B4:colorme3:p086:v01` p?: MISSING
**Searches:** search_docs('mã HEX màu đỏ trong logo colorME', {'content_type': 'visual'}) | search_docs('logo colorME màu đỏ mã màu HEX FF0000', None)

## t3_un5 [unanswerable] status=abstain retrieval_calls=2
**Q:** Hiệu ứng Triangulation cần tối thiểu bao nhiêu đa giác?
**Expected:** abstain — p128 chỉ giới thiệu trào lưu và công cụ ngoài, không có con số.
**Answer:** Sách không nêu số lượng đa giác tối thiểu cần có cho hiệu ứng Triangulation; sách chỉ mô tả hiệu ứng được tạo từ nhiều đa giác.
**Searches:** search_docs('Hiệu ứng Triangulation cần tối thiểu bao nhiêu đa giác? số lượng đa giác tối thiểu', {'chapter': 'ch5', 'content_type': 'text'}) | search_docs('Triangulation Low poly số đa giác tối thiểu bao nhiêu polygon tam giác', None)

## t3_un6 [unanswerable] status=abstain retrieval_calls=2
**Q:** Sách khuyên CV nên dài tối đa mấy trang?
**Expected:** abstain — Chương 7 không nói về độ dài CV.
**Answer:** Sách không nêu rõ CV nên dài tối đa bao nhiêu trang.
**Searches:** search_docs('CV nên dài tối đa bao nhiêu trang', {'chapter': 'ch7', 'content_type': 'text'}) | search_docs('CV một trang hai trang tối đa số trang hồ sơ xin việc', {'content_type': 'text'})

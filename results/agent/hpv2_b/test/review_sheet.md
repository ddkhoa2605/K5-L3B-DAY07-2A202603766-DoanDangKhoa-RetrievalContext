# Review sheet hpv2_b / test


## t3_ch1 [chart] status=answered retrieval_calls=1
**Q:** Trong biểu đồ 'Color Emotion Guide', dải màu xanh lá thể hiện những cảm xúc nào?
**Expected:** PEACEFUL, GROWTH, HEALTH.
**Gold:** p78 (visual) `GROWTH`
**Context evidence:** {'all': True, 'any': True, 'groups': [True]}
**Answer:** Dải màu xanh lá trong biểu đồ 'Color Emotion Guide' thể hiện các cảm xúc: PEACEFUL (bình yên), GROWTH (phát triển), HEALTH (sức khỏe). [B:colorme3:p078:v00]
- `B:colorme3:p078:v00` p78: [Chương 3 – Sử dụng màu sắc | Ý nghĩa của màu sắc | trang 77 (PDF p78)] Nội dung trang: Trang trình bày biểu đồ hướng dẫn cảm xúc màu sắc với các ví dụ logo thương hiệu tương ứng từng màu. Phần tử trực quan (hình minh họa, giữa/trái): Biểu đồ COLOR EMOTION GUIDE phân loại các cảm xúc theo màu sắc với các ví dụ logo thương hiệu tương ứng. Chữ trong hình: COLOR EMOTION GUIDE OPTIMISM CLARITY WARMTH 
**Searches:** search_docs('Color Emotion Guide', {'chapter': 'ch3', 'content_type': 'visual'})

## t3_ch2 [chart] status=answered retrieval_calls=1
**Q:** Trong biểu đồ 'Color Emotion Guide', cảm xúc TRUST nằm ở dải màu gì và đi cùng những từ nào?
**Expected:** Dải xanh dương: TRUST, DEPENDABLE, STRENGTH.
**Gold:** p78 (visual) `DEPENDABLE`
**Context evidence:** {'all': True, 'any': True, 'groups': [True]}
**Answer:** Trong biểu đồ 'Color Emotion Guide', cảm xúc TRUST nằm ở dải màu xanh dương và đi cùng các từ khóa: SMART, CALM, FAITH, NATURAL, STABLE, POWER, DEPENDABLE, STRENGTH. [B:colorme3:p077:v00] [B:colorme3:p078:v00]
- `B:colorme3:p077:v00` p77: [Chương 3 – Sử dụng màu sắc | Ý nghĩa của màu sắc | trang 76 (PDF p77)] Nội dung trang: Trang trình bày ý nghĩa của các màu sắc qua bảng màu với các từ khóa mô tả cảm nhận chung về từng màu. Phần tử trực quan (bảng/ô màu, giữa trang): Bảng màu gồm 8 ô màu, mỗi ô màu có tên màu viết tay và các từ khóa mô tả cảm nhận liên quan. Chữ trong hình: blue TRUST SMART CALM FAITH NATURAL STABLE POWER red LOV
- `B:colorme3:p078:v00` p78: [Chương 3 – Sử dụng màu sắc | Ý nghĩa của màu sắc | trang 77 (PDF p78)] Nội dung trang: Trang trình bày biểu đồ hướng dẫn cảm xúc màu sắc với các ví dụ logo thương hiệu tương ứng từng màu. Phần tử trực quan (hình minh họa, giữa/trái): Biểu đồ COLOR EMOTION GUIDE phân loại các cảm xúc theo màu sắc với các ví dụ logo thương hiệu tương ứng. Chữ trong hình: COLOR EMOTION GUIDE OPTIMISM CLARITY WARMTH 
**Searches:** search_docs('Color Emotion Guide TRUST', {'chapter': 'ch3', 'content_type': 'visual'})

## t3_ch3 [chart] status=answered retrieval_calls=1
**Q:** Trong trang 'CV – Charts', thanh tiến trình ngang được tô màu nhiều hơn hay ít hơn một nửa chiều dài?
**Expected:** Nhiều hơn một nửa (khoảng 80%).
**Gold:** p160 (visual) `80`
**Context evidence:** {'all': True, 'any': True, 'groups': [True]}
**Answer:** Thanh tiến trình ngang trong trang 'CV – Charts' được tô màu xanh dương chiếm khoảng 80% chiều dài, tức là nhiều hơn một nửa chiều dài. [B:colorme3:p160:v03]
- `B:colorme3:p160:v03` p160: [Chương 7 – Ứng dụng thiết kế CV | CV – Charts | trang 159 (PDF p160)] Nội dung trang: Trang này minh họa các mẫu biểu đồ đơn giản dùng trong CV, gồm biểu đồ vòng, biểu đồ tròn, biểu đồ chấm và thanh tiến trình. Phần tử trực quan (biểu đồ, giữa dưới bên phải): Thanh tiến trình ngang, phần màu xanh dương chiếm khoảng 80%, phần còn lại màu xám nhạt. Dữ liệu: xanh dương: 80% | xám nhạt: 20%
**Searches:** search_docs('CV – Charts', {'chapter': 'ch7', 'content_type': 'visual'})

## t3_ch4 [chart] status=abstain retrieval_calls=3
**Q:** Trong biểu đồ bong bóng 'Các bài toán thường gặp', bong bóng 'Nhận diện thương hiệu' lớn hơn hay nhỏ hơn bong bóng 'Chỉnh sửa ảnh'?
**Expected:** Lớn hơn (bong bóng xanh dương lớn hơn bong bóng vàng).
**Gold:** p6 (visual) `Nhận diện thương hiệu`
**Context evidence:** {'all': True, 'any': True, 'groups': [True]}
**Answer:** Không đủ bằng chứng trong sách để trả lời câu hỏi này.
**Searches:** search_docs('biểu đồ bong bóng Các bài toán thường gặp', {'chapter': 'ch6', 'content_type': 'visual'}) | search_docs('Các bài toán thường gặp bong bóng Nhận diện thương hiệu Chỉnh sửa ảnh', {'content_type': 'visual'}) | read_page('page=6', None)

## t3_ch5 [chart] status=abstain retrieval_calls=6
**Q:** Trong sơ đồ vòng tròn màu minh họa hệ RGB, biểu tượng ở tâm vòng tròn thể hiện trạng thái các đèn led thế nào?
**Expected:** Cả 3 đèn đỏ, xanh lá, xanh dương đều bật (tạo màu trắng).
**Gold:** p17 (visual) `tâm`
**Context evidence:** {'all': False, 'any': False, 'groups': [False]}
**Answer:** Sách không có thông tin cụ thể về biểu tượng ở tâm vòng tròn màu RGB thể hiện trạng thái các đèn led.
**Searches:** search_docs('vòng tròn màu RGB biểu tượng đèn led', {'chapter': 'ch3', 'content_type': 'visual'}) | search_docs('vòng tròn màu RGB biểu tượng đèn led', {'chapter': 'ch3', 'content_type': 'text'}) | read_page('page=67', None) | read_page('page=64', None) | search_docs('vòng tròn màu RGB biểu tượng đèn led trạng thái', {'chapter': 'ch3', 'content_type': 'visual'}) | read_page('page=69', None)

## t3_img1 [image] status=abstain retrieval_calls=3
**Q:** Chiếc iPod trong ảnh minh họa mục 'Apple với iPod' có màu gì?
**Expected:** Xanh dương (sáng), dây đeo cùng màu.
**Gold:** p64 (visual) `iPod`
**Context evidence:** {'all': False, 'any': False, 'groups': [False]}
**Answer:** Sách không có thông tin hoặc mô tả màu sắc của chiếc iPod trong ảnh minh họa mục 'Apple với iPod'.
**Searches:** search_docs('Apple với iPod', {'chapter': 'ch6', 'content_type': 'visual'}) | search_docs('Apple iPod màu', {'chapter': 'ch6', 'content_type': 'visual'}) | search_docs('Apple iPod màu sắc', {'chapter': 'ch6', 'content_type': 'visual'})

## t3_img2 [image] status=answered retrieval_calls=1
**Q:** Hai poster phim minh họa phối màu tương đồng (Gradient Tool) là những phim nào?
**Expected:** The Little Mermaid và The Lion King (Disney).
**Gold:** p69 (visual) `LION KING`
**Context evidence:** {'all': True, 'any': True, 'groups': [True]}
**Answer:** Hai poster phim minh họa phối màu tương đồng (Gradient Tool) là phim hoạt hình The Little Mermaid với tông màu xanh dương, tím, xanh lá và cam đỏ tương đồng, và phim hoạt hình The Lion King với tông màu cam, đỏ, tím và vàng tương đồng. [B:colorme3:p069:v00] [B:colorme3:p069:v01]
- `B:colorme3:p069:v00` p69: [Chương 3 – Sử dụng màu sắc | Dùng 2 màu – Màu tương đồng | trang 68 (PDF p69)] Nội dung trang: Trang trình bày minh họa việc sử dụng 2 màu tương đồng trong thiết kế với ví dụ hình ảnh poster phim hoạt hình. Phần tử trực quan (hình minh họa, giữa trái): Poster phim hoạt hình The Little Mermaid với tông màu xanh dương, tím, xanh lá và cam đỏ tương đồng. Chữ trong hình: DISNEY THE LITTLE MERMAID
- `B:colorme3:p069:v01` p69: [Chương 3 – Sử dụng màu sắc | Dùng 2 màu – Màu tương đồng | trang 68 (PDF p69)] Nội dung trang: Trang trình bày minh họa việc sử dụng 2 màu tương đồng trong thiết kế với ví dụ hình ảnh poster phim hoạt hình. Phần tử trực quan (hình minh họa, giữa phải): Poster phim hoạt hình The Lion King với tông màu cam, đỏ, tím và vàng tương đồng. Chữ trong hình: THE LION KING
**Searches:** search_docs('poster phim phối màu tương đồng Gradient Tool', {'chapter': 'ch3', 'content_type': 'visual'})

## t3_img3 [image] status=answered retrieval_calls=1
**Q:** Poster sự kiện minh họa nhóm màu neon có tên sự kiện gì và diễn ra vào ngày nào?
**Expected:** SUMMER DANCE PARTY (Cocktail Bar), FRIDAY 18 SEPTEMBER.
**Gold:** p83 (visual) `SUMMER DANCE PARTY`
**Context evidence:** {'all': True, 'any': True, 'groups': [True]}
**Answer:** Poster sự kiện minh họa nhóm màu neon có tên sự kiện là "Summer Dance Party Cocktail Bar" và diễn ra vào ngày Friday 18 September. [B:colorme3:p083:v00]
- `B:colorme3:p083:v00` p83: [Chương 3 – Sử dụng màu sắc |  | trang 82 (PDF p83)] Nội dung trang: Trang này là poster quảng cáo sự kiện Summer Dance Party với phong cách neon. Phần tử trực quan (poster/ấn phẩm, giữa): Poster sự kiện Summer Dance Party với hiệu ứng chữ neon màu hồng, vàng, tím trên nền tối có các tia sáng màu đỏ, vàng, tím. Nội dung chính gồm: tên câu lạc bộ (Your Club Name Presents), ngày tổ chức (Friday 18 S
**Searches:** search_docs('poster sự kiện nhóm màu neon', {'chapter': 'ch3', 'content_type': 'visual'})

## t3_img4 [image] status=answered retrieval_calls=1
**Q:** Ví dụ 'thay đổi kích thước' với 1 typeface là poster phim nào, và hình chính là gì?
**Expected:** THE GOOD THE BAD AND THE UGLY; bóng một người đàn ông đội mũ chứa phong cảnh bên trong.
**Gold:** p95 (visual) `THE GOOD THE BAD AND THE UGLY`
**Context evidence:** {'all': True, 'any': True, 'groups': [True]}
**Answer:** Ví dụ về "thay đổi kích thước" với 1 typeface là poster phim "THE GOOD THE BAD AND THE UGLY". Hình chính minh họa là ảnh bóng người đàn ông đội mũ, bên trong bóng có hình ảnh phong cảnh khô cằn và chữ trắng kiểu font sans-serif với các kích thước khác nhau. [B:colorme3:p095:t00] [B:colorme3:p095:v00]
- `B:colorme3:p095:t00` p95: [Chương 4 – Những điều cần biết về Typography | Cách kết hợp font – 1 typeface | trang 94 (PDF p95)] Cách kết hợp font – 1 typeface  Thay đổi kích thước Tương tự như màu sắc, bạn cũng không nên dùng quá nhiều loại font cho cùng 1 tác phẩm.  Hãy luyện tập với số lượng font chữ thật ít bạn nhé.  Trước tiên, hãy thử việc chỉ dùng 1 font chữ duy nhất cho toàn bộ tác phẩm và thay đổi kích thước của chú
- `B:colorme3:p095:v00` p95: [Chương 4 – Những điều cần biết về Typography | Cách kết hợp font – 1 typeface | trang 94 (PDF p95)] Nội dung trang: Trang này minh họa cách kết hợp font chữ bằng việc chỉ dùng một typeface duy nhất và thay đổi kích thước để dẫn dắt thị giác người xem. Phần tử trực quan (ảnh chụp, giữa giữa): Ảnh bóng người đàn ông đội mũ, bên trong bóng có hình ảnh phong cảnh khô cằn và chữ trắng kiểu font sans-s
**Searches:** search_docs('thay đổi kích thước typeface poster phim', {'chapter': 'ch4'})

## t3_img5 [image] status=answered retrieval_calls=2
**Q:** Ba logo ví dụ cho loại logo kết hợp là của những thương hiệu nào?
**Expected:** Starbucks Coffee, BMW, Puma.
**Gold:** p135 (visual) `BMW`
**Context evidence:** {'all': True, 'any': True, 'groups': [True]}
**Answer:** Ba logo ví dụ cho loại logo kết hợp là của các thương hiệu Starbucks Coffee, BMW và Puma. [B:colorme3:p135:v00] [B:colorme3:p135:v01] [B:colorme3:p135:v02]
- `B:colorme3:p135:v00` p135: [Chương 6 – Nhận diện thương hiệu | Logo – Phân loại | trang 134 (PDF p135)] Nội dung trang: Trang trình bày về phân loại logo kết hợp, minh họa bằng các logo có cả phần hình và chữ. Phần tử trực quan (logo, giữa giữa): Logo Starbucks Coffee hình tròn màu xanh lá với chữ trắng bao quanh hình nữ thần biển. Chữ trong hình: STARBUCKS COFFEE
- `B:colorme3:p135:v01` p135: [Chương 6 – Nhận diện thương hiệu | Logo – Phân loại | trang 134 (PDF p135)] Nội dung trang: Trang trình bày về phân loại logo kết hợp, minh họa bằng các logo có cả phần hình và chữ. Phần tử trực quan (logo, giữa giữa): Logo BMW hình tròn với 4 ô màu xanh dương và trắng xen kẽ, viền đen, chữ BMW màu trắng trên viền đen. Chữ trong hình: B M W
- `B:colorme3:p135:v02` p135: [Chương 6 – Nhận diện thương hiệu | Logo – Phân loại | trang 134 (PDF p135)] Nội dung trang: Trang trình bày về phân loại logo kết hợp, minh họa bằng các logo có cả phần hình và chữ. Phần tử trực quan (logo, giữa giữa): Logo Puma gồm hình con báo nhảy màu đen bên trái và chữ PUMA màu đen bên phải. Chữ trong hình: PUMA
**Searches:** search_docs('logo kết hợp', {'chapter': 'ch6', 'content_type': 'text'}) | read_page('page=135', None)

## t3_mh1 [multihop] status=answered retrieval_calls=2
**Q:** Hiệu ứng làm mờ mở đầu chương 5 tên là gì, và ở chương xu hướng thiết kế nó được ứng dụng kết hợp với phong cách nào?
**Expected:** Blur; kết hợp với thiết kế phẳng (Flat Design) qua Blur Background.
**Gold:** p124 (text) `Bắt đầu chương 5 với hiệu ứng blur bạn nhé`; p171 (text) `Ứng dụng với Blur BackGround`
**Context evidence:** {'all': True, 'any': True, 'groups': [True, True]}
**Answer:** Hiệu ứng làm mờ mở đầu chương 5 là hiệu ứng Blur. Ở chương xu hướng thiết kế (chương 8), hiệu ứng Blur được ứng dụng kết hợp với phong cách Flat Design, cụ thể là Blur Background trong thiết kế phẳng. [B:colorme3:p124:t00] [B:colorme3:p171:t00]
- `B:colorme3:p124:t00` p124: [Chương 5 – Một số hiệu ứng cơ bản | Blur – Filter Gallery | trang 123 (PDF p124)] Blur – Filter Gallery  Blur Đã bao giờ bạn muốn làm mờ một bức hình đề toàn bộ phần nội dung bên trên được nổi rõ hơn.  Bắt đầu chương 5 với hiệu ứng blur bạn nhé  https://www.youtube.com/watch?v=ZZbQrAm_3xQ&list=PL9_gOzpFilwol3lyOj3jH4iDBMzVIPrea
- `B:colorme3:p171:t00` p171: [Chương 8 – Các xu hướng thiết kế | Blur & Flat Design | trang 170 (PDF p171)] Blur & Flat Design  Ứng dụng với Blur BackGround Thiết kế phẳng cho phép bạn dàn trải thông tin một cách hiệu quả và tập trung. Đặc biệt khi nó được ứng dụng vớ Blur Background.  Cùng thử tạo ra 1 tác phẩm thế này xem nào:  https://www.youtube.com/watch?v=tgEynr9Upx0&index=2&list=PL9_gOzpFilwrYwBD6Cq9s4QzDNLwAs3jC
**Searches:** search_docs('hiệu ứng làm mờ', {'chapter': 'ch5', 'content_type': 'text'}) | search_docs('blur xu hướng thiết kế', {'chapter': 'ch8', 'content_type': 'text'})

## t3_mh2 [multihop] status=answered retrieval_calls=1
**Q:** Font serif và font sans-serif lần lượt được dùng nhiều trong những lĩnh vực nào?
**Expected:** Serif: nhà hàng, khách sạn, kinh tế, giáo dục; sans-serif: quảng cáo, truyền thông, công nghệ.
**Gold:** p89 (text) `nhà hàng, khách sạn, kinh tế, giáo dục`; p91 (text) `quảng cáo, truyền thông và công nghệ`
**Context evidence:** {'all': True, 'any': True, 'groups': [True, True]}
**Answer:** Font serif thường được dùng trong nhà hàng, khách sạn, kinh tế, giáo dục và các ấn phẩm có mật độ chữ dày như sách hoặc báo vì mang lại cảm giác nghiêm trang và cổ điển. Font sans-serif được dùng nhiều trong quảng cáo, truyền thông và công nghệ do mang lại cảm giác gọn gàng, nhẹ nhàng, hiện đại và nhanh chóng. [B:colorme3:p089:t00] [B:colorme3:p091:t00]
- `B:colorme3:p089:t00` p89: [Chương 4 – Những điều cần biết về Typography | Các nhóm font cơ bản | trang 88 (PDF p89)] Các nhóm font cơ bản  Serif Times New Roman Bodoni Georgia Garamond Baskerville  Serif trịnh trọng Hãy vơ lấy một cuốn sách bất kì mà bạn đang sở hữu. Sác xuất là 80% bạn sẽ có một cuốn sách có nội dung được viết bằng loại chữ Serif – Chữ có chân.  Serif hay còn gọi là chân chữ, là những phần gạch ngang phía
- `B:colorme3:p091:t00` p91: [Chương 4 – Những điều cần biết về Typography | Các nhóm font cơ bản | trang 90 (PDF p91)] Các nhóm font cơ bản Sans Serif Segoe UI Microsoft Sans Serif Helvetica Arial Calibri Dotum Verdana  Sans Serif trẻ trung năng động Có chữ có chân, đương nhiên sẽ có chữ không chân rồi.  Nhóm chữ không chân, hay còn gọi là sans-serif là nhóm chữ đem lại cho mọi người cảm giác gọn gàng, nhẹ hàng, hiện đại và 
**Searches:** search_docs('font serif lĩnh vực', {'chapter': 'ch4', 'content_type': 'text'})

## t3_mh3 [multihop] status=answered retrieval_calls=2
**Q:** Kĩ thuật đóng khung và kĩ thuật line trong typography khác nhau thế nào?
**Expected:** Đóng khung: tạo bo viền quanh chữ để mọi thứ bên trong thành một thể thống nhất; line: dùng đường kẻ để phân tách bố cục.
**Gold:** p102 (text) `tạo ra một bo viền xung quanh chữ`; p106 (text) `Là kĩ thuật dùng những đường kẻ để phân tách bố cục của bản thiết kế.`
**Context evidence:** {'all': True, 'any': True, 'groups': [True, True]}
**Answer:** Kĩ thuật đóng khung trong typography là tạo ra một bo viền xung quanh chữ, khiến tất cả những thứ nằm trong bo viền đó trở thành một thể thống nhất. Kĩ thuật line là dùng những đường kẻ để phân tách bố cục của bản thiết kế. [B:colorme3:p102:t00] [B:colorme3:p106:t00]
- `B:colorme3:p102:t00` p102: [Chương 4 – Những điều cần biết về Typography | Các kĩ thuật dùng chữ | trang 101 (PDF p102)] Các kĩ thuật dùng chữ  BORDER focused things  Kĩ thuật đóng khung Kĩ thuật đóng khung, được dùng rất nhiều và rộng rãi trong thiết kế.  Kĩ thuật này đơn giản là tạo ra một bo viền xung quanh chữ, khiến tất cả những thứ nằm trong bo viền đó trở thành một thể thống nhất.  Cùng xem cách thực hiện kĩ thuật nà
- `B:colorme3:p106:t00` p106: [Chương 4 – Những điều cần biết về Typography | Các kĩ thuật dùng chữ | trang 105 (PDF p106)] Các kĩ thuật dùng chữ  Kĩ thuật line Là kĩ thuật dùng những đường kẻ để phân tách bố cục của bản thiết kế.  Chắc hẳn bạn đang cảm thấy 2 tác phẩm phía trên có chút gì đó rất quen thuộc. Đơn giản là vì kĩ thuậ tnày đang được sử dụng rất rộng rãi. Chúng có mặt ở khăp mọi nơi.  Cùng xem cách tạo line trong P
**Searches:** search_docs('kĩ thuật đóng khung typography', {'chapter': 'ch4', 'content_type': 'text'}) | search_docs('kĩ thuật line typography', {'chapter': 'ch4', 'content_type': 'text'})

## t3_mh4 [multihop] status=answered retrieval_calls=1
**Q:** Logo mô thức (Pattern and Shape) và logo hình khối (Geometric Shape) được định nghĩa khác nhau thế nào?
**Expected:** Logo mô thức nằm trong các hình đa giác đều (tam giác đều, hình vuông, lục giác đều); logo hình khối chỉ tạo thành từ những đường thẳng.
**Gold:** p143 (text) `Là nhóm logo nằm trong các hình đa giác đều`; p144 (text) `Là những logo chỉ được tạo thành từ những đường thẳng`
**Context evidence:** {'all': True, 'any': True, 'groups': [True, True]}
**Answer:** Logo mô thức (Pattern And Shape Logo) là nhóm logo nằm trong các hình đa giác đều như tam giác đều, hình vuông, lục giác đều. Logo hình khối (Geometric Shape Logo) là những logo chỉ được tạo thành từ những đường thẳng. [B:colorme3:p143:t00] [B:colorme3:p144:t00]
- `B:colorme3:p143:t00` p143: [Chương 6 – Nhận diện thương hiệu | Pattern And Shape Logo | trang 142 (PDF p143)] Pattern And Shape Logo  Logo mô thức Là nhóm logo nằm trong các hình đa giác đều như tam giác đều, hình vuông, lục giác đều.
- `B:colorme3:p144:t00` p144: [Chương 6 – Nhận diện thương hiệu | Geometric Shape Logos | trang 143 (PDF p144)] Geometric Shape Logos  Logo hình khối Là những logo chỉ được tạo thành từ những đường thẳng
**Searches:** search_docs('logo mô thức pattern and shape geometric shape', {'chapter': 'ch6'})

## t3_tab1 [table] status=answered retrieval_calls=1
**Q:** Trong bảng phím tắt nhóm FILE, CTRL + W và CTRL + ALT + S dùng để làm gì?
**Expected:** CTRL + W: đóng file; CTRL + ALT + S: lưu thêm 1 bản copy.
**Gold:** p174 (text) `CTRL + ALT + S (Save a Copy): Lưu thêm 1 bản copy`
**Context evidence:** {'all': True, 'any': True, 'groups': [True]}
**Answer:** Trong nhóm phím tắt FILE, CTRL + W dùng để đóng file, CTRL + ALT + S dùng để lưu thêm một bản copy của file. [B:colorme3:p174:t00]
- `B:colorme3:p174:t00` p174: [Phụ lục và lời kết | Danh sách phím tắt | trang 173 (PDF p174)] Danh sách phím tắt  Nhóm Phím Tắt Hệ Thống FILE - CTRL + N (New): Tạo File mới - CTRL + O (Open): Mở file - CTRL + ALT + O (Open As): Mở file từ Adobe Bridge - CTRL + W (Close): Đóng File - CTRL + S (Save): Lưu file - CTRL + SHIFT + S (Save As): Lưu ra các dạng khác - CTRL + ALT + S (Save a Copy): Lưu thêm 1 bản copy - CTRL + P (Prin
**Searches:** search_docs('phím tắt CTRL + W', {'chapter': 'appendix', 'content_type': 'text'})

## t3_tab2 [table] status=answered retrieval_calls=1
**Q:** Trong nhóm lệnh EDIT của bảng phím tắt, CTRL + ALT + Z và CTRL + SHIFT + C làm gì?
**Expected:** CTRL + ALT + Z: trở lại nhiều bước; CTRL + SHIFT + C: Copy Merged.
**Gold:** p175 (text) `CTRL + ALT + Z: Trở lại nhiều bước`
**Context evidence:** {'all': True, 'any': True, 'groups': [True]}
**Answer:** Trong nhóm lệnh EDIT của bảng phím tắt: CTRL + ALT + Z là lệnh "Trở lại nhiều bước"; CTRL + SHIFT + C là lệnh "Copy Merged". [B:colorme3:p175:t01]
- `B:colorme3:p175:t01` p175: [Phụ lục và lời kết | Danh sách phím tắt | trang 174 (PDF p175)] Các Phím Tắt Với Nhóm IMAGE - CTRL + L: Bảng Levels - CTRL + SHIFT + L: Tự động chỉnh Levels - CTRL + ALT + SHIFT + L: Tự động chỉnh Contrast - CTRL + M: Bảng Curves - CTRL + B: Bảng Color Blance - CTRL + U: Bảng Hue/Saturation - CTRL + SHIFT + U: Bảng Desaturate - CTRL + I: Bảng Invert Cách Lệnh Tắt Với Nhóm Lệnh EDIT - [: Phóng to 
**Searches:** search_docs('phím tắt CTRL + ALT + Z CTRL + SHIFT + C', {'chapter': 'appendix', 'content_type': 'text'})

## t3_tab3 [table] status=answered retrieval_calls=1
**Q:** Trong bảng phím tắt Toolbar, phím G và phím E tương ứng công cụ gì?
**Expected:** G: đổ màu/đổ màu chuyển; E: tẩy.
**Gold:** p176 (text) `G: Đổ màu/Đổ màu chuyển`
**Context evidence:** {'all': True, 'any': True, 'groups': [True]}
**Answer:** Trong bảng phím tắt Toolbar, phím G tương ứng với công cụ Đổ màu/Đổ màu chuyển, phím E tương ứng với công cụ Tẩy. [B:colorme3:p176:t00]
- `B:colorme3:p176:t00` p176: [Phụ lục và lời kết | Danh sách phím tắt | trang 175 (PDF p176)] Danh sách phím tắt  Nhóm Phím Tắt Công Cụ -Toolbar - V: Di chuyển - M: Tạo vùng chọn - L: Tạo vùng chọn tự do - W: Tạo vùng chọn theo màu - C: Cắt hình - I: Chấm màu . Thước kẻ - J: Chấm sửa chỗ chưa hoàn chỉnh - B: Nét bút - S: Lấy mẫu từ 1 ảnh - Y: Gọi lại thông số cũ của ảnh - E: Tẩy - G: Đổ màu/Đổ màu chuyển - . : Mô tả hiện tườn
**Searches:** search_docs('phím G', {'chapter': 'appendix', 'content_type': 'text'})

## t3_tab4 [table] status=answered retrieval_calls=1
**Q:** Trong ảnh Adobe Kuler, ô màu đầu tiên (đang được chọn) có giá trị RGB và mã HEX nào?
**Expected:** RGB 255 83 13; HEX FF530D.
**Gold:** p86 (visual) `FF530D`
**Context evidence:** {'all': True, 'any': True, 'groups': [True]}
**Answer:** Ô màu đầu tiên (đang được chọn) trong ảnh Adobe Kuler có giá trị RGB là 255 83 13 và mã HEX là FF530D. [B:colorme3:p086:v00]
- `B:colorme3:p086:v00` p86: [Chương 3 – Sử dụng màu sắc | Công cụ chọn màu | trang 85 (PDF p86)] Nội dung trang: Trang giới thiệu công cụ chọn màu Kuler của Adobe với hình ảnh giao diện phần mềm. Phần tử trực quan (ảnh chụp màn hình, giữa): Giao diện phần mềm Adobe Kuler với bánh xe màu và bảng màu tương ứng. Chữ trong hình: Adobe Kuler Create Explore My Themes Save My Kuler Theme Color Rule Analogous RGB 255 83 13 HEX FF530
**Searches:** search_docs('Adobe Kuler ô màu đầu tiên RGB HEX', {'chapter': 'ch3', 'content_type': 'visual'})

## t3_tab5 [table] status=answered retrieval_calls=1
**Q:** Trong bảng 8 ô màu kèm từ khóa cảm nhận (tiếng Anh), màu pink gắn với những từ khóa nào?
**Expected:** TENDERNESS, SENSITIVE, CARING, EMOTIONAL, SYMPATHETIC, LOVE, SEXUALITY.
**Gold:** p77 (visual) `TENDERNESS`
**Context evidence:** {'all': True, 'any': True, 'groups': [True]}
**Answer:** Màu pink (hồng) gắn với các từ khóa cảm nhận: TENDERNESS, SENSITIVE, CARING, EMOTIONAL, SYMPATHETIC, LOVE, SEXUALITY. [B:colorme3:p077:v00]
- `B:colorme3:p077:v00` p77: [Chương 3 – Sử dụng màu sắc | Ý nghĩa của màu sắc | trang 76 (PDF p77)] Nội dung trang: Trang trình bày ý nghĩa của các màu sắc qua bảng màu với các từ khóa mô tả cảm nhận chung về từng màu. Phần tử trực quan (bảng/ô màu, giữa trang): Bảng màu gồm 8 ô màu, mỗi ô màu có tên màu viết tay và các từ khóa mô tả cảm nhận liên quan. Chữ trong hình: blue TRUST SMART CALM FAITH NATURAL STABLE POWER red LOV
**Searches:** search_docs('pink', {'chapter': 'ch3', 'content_type': 'visual'})

## t3_tab6 [table] status=answered retrieval_calls=2
**Q:** Trong bảng màu dành cho logo, thanh màu hồng gắn với những tính từ nào?
**Expected:** Nữ tính, ngây thơ, dịu dàng, khoẻ mạnh, trẻ trung.
**Gold:** p136 (visual) `hồng`
**Context evidence:** {'all': True, 'any': True, 'groups': [True]}
**Answer:** Thanh màu hồng trong bảng màu dành cho logo gắn với các tính từ: nữ tính, ngây thơ, dịu dàng, khoẻ mạnh, trẻ trung. [B:colorme3:p136:v00]
- `B:colorme3:p136:v00` p136: [Chương 6 – Nhận diện thương hiệu | Logo – Phân loại | trang 135 (PDF p136)] Nội dung trang: Trang trình bày phân loại ý nghĩa màu sắc trong logo qua các thanh màu kèm mô tả. Phần tử trực quan (bảng/ô màu, giữa/trái): Các thanh màu kèm mô tả ý nghĩa màu sắc trong logo Chữ trong hình: Trang trọng, đặc biệt, mạnh mẽ, quyền lực, tinh tế, truyền thống Uy quyền, đỉnh đạc, an toàn, đáng tin cậy, truyền 
**Searches:** search_docs('bảng màu logo màu hồng tính từ', {'chapter': 'ch6', 'content_type': 'visual'}) | read_page('page=136', None)

## t3_tx1 [text] status=answered retrieval_calls=1
**Q:** Theo sách, sai lầm lớn nhất thường gặp của người mới bắt đầu thiết kế là gì?
**Expected:** Dùng quá nhiều màu sắc, biến tác phẩm thành mớ hỗn độn.
**Gold:** p62 (text) `các bạn dùng… quá nhiều màu sắc`
**Context evidence:** {'all': True, 'any': True, 'groups': [True]}
**Answer:** Sai lầm lớn nhất thường gặp đối với các bạn mới bắt đầu thiết kế là dùng quá nhiều màu sắc, khiến tác phẩm trở thành một mớ hỗn độn khó cảm nhận được màu chủ đạo. [B:colorme3:p062:t00]
- `B:colorme3:p062:t00` p62: [Chương 3 – Sử dụng màu sắc | Dùng 1 màu | trang 61 (PDF p62)] Dùng 1 màu  Màu chủ đạo Sai lầm lớn nhất thường gặp đối với các bạn mới bắt đầu thiết kế là các bạn dùng… quá nhiều màu sắc.  Bạn cho tất cả những màu có thể vào bức thiết kế của mình, biến nó thành một mớ hỗn độn khó cảm nhận được.  Một tác phẩm thiết kế thành công cần bảo đảm về tính chất màu chủ đạo. Nghĩa là người dùng sẽ nắm bắt n
**Searches:** search_docs('sai lầm lớn nhất người mới bắt đầu thiết kế', {'content_type': 'text'})

## t3_tx2 [text] status=answered retrieval_calls=1
**Q:** Khi tác giả hỏi lớp học colorME ai cần một CV đẹp, tỉ lệ người giơ tay thế nào?
**Expected:** Chưa lần nào dưới 80%.
**Gold:** p153 (text) `Chưa lần nào số`
**Context evidence:** {'all': True, 'any': True, 'groups': [True]}
**Answer:** Tác giả hỏi trong lớp học colorME có bao nhiêu người đã, đang và sẽ cần một CV đẹp, chưa lần nào số người giơ tay dưới 80%. [B:colorme3:p153:t00]
- `B:colorme3:p153:t00` p153: [Chương 7 – Ứng dụng thiết kế CV | CHƯƠNG 7 | trang 152 (PDF p153)] CHƯƠNG 7  Ứng dụng thiết kế CV  Đã rất nhiều lần tôi hỏi mọi người trong lớp học colorME, rằng, có bao nhiêu người đã, đang và sẽ cần 1 cái CV đẹp? Chưa lần nào số người đưa tay lên là dưới 80%.  Vậy nên, không có một lý do nào mà tôi lại không đưa những điều này vào cuốn sách đầu tiên của cuộc đời mình.  Con người có thói quen đá
**Searches:** search_docs('lớp học colorME ai cần một CV đẹp giơ tay', {'chapter': 'ch7', 'content_type': 'text'})

## t3_tx3 [text] status=answered retrieval_calls=5
**Q:** Theo sách, kích thước chữ phụ thuộc vào điều gì của nội dung?
**Expected:** Độ phân cấp thông tin.
**Gold:** p39 (text) `Câu trả lời chính là độ phân cấp thông tin.`
**Context evidence:** {'all': True, 'any': True, 'groups': [True]}
**Answer:** Kích thước chữ phụ thuộc vào độ phân cấp thông tin của nội dung. [B:colorme3:p039:t00] [B:colorme3:p039:v03]
- `B:colorme3:p039:t00` p39: [Chương 2 – Các bố cục thường gặp và ứng dụng | Phân cấp thông tin | trang 38 (PDF p39)] Phân cấp thông tin  Vấn đề chính là kích thước Thay đổi kích thước to nhỏ khác nhau có thể giúp cho người dùng dễ dàng hơn trong việc đọc các ấn phẩm của bạn.  Vây kích thước phụ thuộc vào điều gì của nội dung?  Câu trả lời chính là độ phân cấp thông tin.
- `B:colorme3:p039:v03` p39: [Chương 2 – Các bố cục thường gặp và ứng dụng | Phân cấp thông tin | trang 38 (PDF p39)] Nội dung trang: Trang trình bày về phân cấp thông tin trong thiết kế, nhấn mạnh vai trò của kích thước trong việc giúp người dùng dễ đọc. Phần tử trực quan (mẫu chữ, dưới trái): Tiêu đề màu đỏ: Vấn đề chính là kích thước, đoạn mô tả chữ xám nhạt bên dưới Chữ trong hình: Vấn đề chính là kích thước Thay đổi kích
**Searches:** search_docs('kích thước chữ phụ thuộc', {'chapter': 'ch4', 'content_type': 'text'}) | search_docs('kích thước chữ phụ thuộc vào nội dung', {'chapter': 'ch4', 'content_type': 'text'}) | search_docs('kích thước chữ phụ thuộc vào nội dung', {'chapter': 'ch4', 'content_type': 'text'}) | search_docs('kích thước chữ phụ thuộc vào nội dung', {'chapter': 'ch2', 'content_type': 'text'}) | read_page('page=39', None)

## t3_tx4 [text] status=answered retrieval_calls=1
**Q:** Vì sao cần phân bố độ to nhỏ của từng con chữ cho phù hợp (lỗi 'không có chính phụ')?
**Expected:** Để những phần nội dung có thêm không gian để có thể 'thở'.
**Gold:** p116 (text) `Để những phần nội dung có thêm không gian`
**Context evidence:** {'all': True, 'any': True, 'groups': [True]}
**Answer:** Cần phân bố độ to nhỏ của từng con chữ một cách phù hợp để tránh lỗi "không có chính phụ" và để những phần nội dung có thêm không gian để có thể “thở”. [B:colorme3:p116:t00]
- `B:colorme3:p116:t00` p116: [Chương 4 – Những điều cần biết về Typography | Một số chú ý | trang 115 (PDF p116)] Một số chú ý  Không có chính phụ Hãy phân bố độ to nhỏ của từng con chữ một cách phù hơp bạn nhé.  Để những phần nội dung có thêm không gian để có thể “thở” được.
**Searches:** search_docs('độ to nhỏ của từng con chữ không có chính phụ', {'chapter': 'ch4', 'content_type': 'text'})

## t3_un1 [unanswerable] status=abstain retrieval_calls=4
**Q:** Theo sách, xây dựng một bộ nhận diện thương hiệu đầy đủ thường tốn bao nhiêu chi phí?
**Expected:** abstain — p149-151 liệt kê thành phần bộ nhận diện, không có chi phí.
**Answer:** Sách không có thông tin về chi phí xây dựng một bộ nhận diện thương hiệu đầy đủ.
**Searches:** search_docs('chi phí xây dựng bộ nhận diện thương hiệu', {'chapter': 'ch6', 'content_type': 'text'}) | search_docs('chi phí xây dựng bộ nhận diện thương hiệu', {'chapter': 'ch6', 'content_type': 'text'}) | search_docs('chi phí', {'chapter': 'ch6', 'content_type': 'text'}) | search_docs('chi phí xây dựng bộ nhận diện thương hiệu', {'content_type': 'text'})

## t3_un2 [unanswerable] status=abstain retrieval_calls=5
**Q:** Kích thước file PSD tối đa mà Photoshop hỗ trợ là bao nhiêu?
**Expected:** abstain — Sách không nói về giới hạn kích thước file.
**Answer:** Sách không có thông tin về kích thước file PSD tối đa mà Photoshop hỗ trợ.
**Searches:** search_docs('kích thước file PSD tối đa', {'chapter': 'ch1', 'content_type': 'text'}) | search_docs('kích thước file PSD tối đa', {'chapter': 'ch1', 'content_type': 'visual'}) | search_docs('kích thước file PSD tối đa', {'chapter': 'ch1', 'content_type': 'text'}) | search_docs('PSD file size limit Photoshop', {'chapter': 'ch1', 'content_type': 'text'}) | search_docs('kích thước file PSD tối đa Photoshop', {'content_type': 'text'})

## t3_un3 [unanswerable] status=abstain retrieval_calls=3
**Q:** Sách so sánh Photoshop với phần mềm GIMP như thế nào?
**Expected:** abstain — p8 chỉ so Photoshop với Illustrator, InDesign, Lightroom; không nhắc GIMP.
**Answer:** Sách không có thông tin so sánh giữa Photoshop và phần mềm GIMP.
**Searches:** search_docs('Photoshop GIMP so sánh', {'chapter': 'ch1', 'content_type': 'text'}) | search_docs('GIMP', {'chapter': 'ch1', 'content_type': 'text'}) | search_docs('so sánh Photoshop và GIMP', {'chapter': 'ch1', 'content_type': 'text'})

## t3_un4 [unanswerable] status=abstain retrieval_calls=5
**Q:** Theo sách, mã HEX của màu đỏ trong logo colorME là gì?
**Expected:** abstain — Sách không ghi mã màu logo colorME (mã HEX duy nhất là của ảnh Kuler p86).
**Answer:** Sách không có thông tin về mã HEX của màu đỏ trong logo colorME.
**Searches:** search_docs('mã HEX màu đỏ logo colorME', {'chapter': 'ch6', 'content_type': 'text'}) | search_docs('mã HEX màu đỏ logo colorME', {'chapter': 'ch6', 'content_type': 'visual'}) | search_docs('mã HEX màu đỏ logo colorME', {'chapter': 'ch6', 'content_type': 'visual'}) | read_page('page=139', None) | search_docs('mã HEX màu đỏ logo colorME', {'chapter': 'ch6', 'content_type': 'text'})

## t3_un5 [unanswerable] status=abstain retrieval_calls=2
**Q:** Hiệu ứng Triangulation cần tối thiểu bao nhiêu đa giác?
**Expected:** abstain — p128 chỉ giới thiệu trào lưu và công cụ ngoài, không có con số.
**Answer:** Sách không cung cấp thông tin về số lượng đa giác tối thiểu cần có để tạo hiệu ứng Triangulation.
**Searches:** search_docs('hiệu ứng Triangulation đa giác tối thiểu', {'chapter': 'ch5', 'content_type': 'text'}) | read_page('page=127', None)

## t3_un6 [unanswerable] status=abstain retrieval_calls=2
**Q:** Sách khuyên CV nên dài tối đa mấy trang?
**Expected:** abstain — Chương 7 không nói về độ dài CV.
**Answer:** Sách không có thông tin cụ thể về việc CV nên dài tối đa bao nhiêu trang.
**Searches:** search_docs('CV dài tối đa mấy trang', {'chapter': 'ch7', 'content_type': 'text'}) | search_docs('CV dài tối đa mấy trang', {'chapter': 'ch7', 'content_type': 'text'})

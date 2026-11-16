# Báo cáo Day 7 — Agentic RAG trên EBOOK COLORME 3 (chữ + hình)

## Kết quả cuối cùng (vòng 3) — đọc phần này trước

Bài làm qua **3 vòng cải tiến**. Mỗi vòng chọn cấu hình trên **dev**, rồi chạy **một bộ test mới chưa từng xem**; bộ test của vòng trước bị loại khỏi đánh giá độc lập vì đã xem kết quả. Kết quả nộp là **vòng 3**. Các mục "Vòng 1 — …" bên dưới giữ nguyên để truy vết.

### Dữ liệu và cấu hình nộp

- **Vì sao dữ liệu là ColorME chứ không phải Python docs:** Day 6 ban đầu tôi làm trên tài liệu Python 3.13 (text thuần, không ảnh/bảng/biểu đồ, không có trang vật lý, embedding tiếng Anh). Vì Day 7 (thử thách nâng cao) cần tài liệu thực tế ≥ 100 trang có text, bảng, ảnh, biểu đồ, tôi **làm lại Day 6 trên `EBOOK COLORME 3.pdf`** (repo: <https://github.com/ddkhoa2605/K5-L3B-DAY06-DoanDangKhoa-2A202603766-DataIngestion-ColorME>, commit `4b574e0`) và Day 7 chỉ dùng bản này; bản Python docs giữ nguyên. Bảng so sánh hai bản: `README.md`, mục "Bối cảnh: vì sao Day 6 đổi từ Python docs sang ColorME".
- **Tài liệu:** `EBOOK COLORME 3.pdf`: 183 trang PDF (181 trang nội dung), tiếng Việt, có ảnh, bảng, biểu đồ, infographic. Nguồn tải, SHA-256 và quyền sử dụng: `DATA_NOT_INCLUDED.md` (PDF, văn bản toàn sách, mô tả hình và Chroma **không nằm trong git**).
- **Index:** ChromaDB của Day 6 (<https://github.com/ddkhoa2605/K5-L3B-DAY06-DoanDangKhoa-2A202603766-DataIngestion-ColorME>), collection `colorme3_B4`: **457 chunk = 181 chunk text** (PyMuPDF) **+ 276 chunk mô tả hình** do GPT-5.6 Luna tạo; embedding `text-embedding-3-small`, 1536 chiều, cosine.
- **Cấu hình nộp `luna_v4_fb_b4`:** agent GPT-5.6 Luna (`gpt-5.6-luna`, Responses API, reasoning `low`) · retrieval hybrid RRF (dense + BM25, k = 60), top-5 · tool `search_docs`, `read_page`, `final_answer` · filter chương `fallback` (trộn kết quả có lọc và không lọc) · prompt v4 · verifier v3 · budget 12 000 ký tự, tối đa 6 lượt tool. Chọn trên **dev 28 câu (28/28)**, chốt ở `results/SELECTION_v3.json` trước khi chạy test.
- **Benchmark cuối:** `test` (`t3_*`, còn gọi là test_v3): 30 câu = 24 có đáp án (bảng 6, ảnh 5, biểu đồ 5, multi-hop 4, text 4) + 6 thiếu bằng chứng; viết và chốt hash **trước** khi chạy (`benchmark/FROZEN_v3.json`). Dev 28 câu = 23 có đáp án + 5 thiếu bằng chứng.

### Kết quả test_v3

| Cấu hình | Đạt | Bảng | Ảnh | Biểu đồ | Multi-hop | Text | Thiếu evidence | Context Evidence | Median / chi phí 30 câu |
|---|---|---|---|---|---|---|---|---|---|
| **`luna_v4_fb_b4` (nộp)** | **27/30 (90,0 %)** | 6/6 | 5/5 | 3/5 | 4/4 | 4/4 | 5/6 | 23/24 | 8,6 s / $0,045 |
| `hpv2_b` (chọn vòng 2) | 26/30 (86,7 %) | 6/6 | 4/5 | 2/5 | 4/4 | 4/4 | 6/6 | 22/24 | 4,4 s / $0,100 |
| `dense` (baseline) | 22/30 (73,3 %) | 6/6 | 3/5 | 2/5 | 3/4 | 2/4 | 6/6 | 20/24 | 4,1 s / $0,068 |

Chỉ số agent (`starter/agent_metrics.py`) của cấu hình nộp: tool use 30/30 · grounded answer 0/1/2 = 2/0/22 (TB 1,83/2) · citation hợp lệ 28/29 · câu trả lời có citation 23/23 · abstention đúng 5/6 · từ chối nhầm 2/24 · 0 lỗi hệ thống. Retrieval một lượt bằng câu hỏi gốc (Evidence Hit@3 / 24 câu có đáp án, index B4): dense 19, BM25 21, hybrid 20.

### Các vòng cải tiến

| Vòng | Thay đổi chính (chọn trên dev) | Cấu hình chọn | Dev | Test mới của vòng | `dense` cùng test |
|---|---|---|---|---|---|
| 1 | hybrid + `read_page` + prompt grounding chặt + verifier (xóa ý không có trong đoạn trích); gpt-4.1-mini, index `colorme3_B` | `hybrid_page_verify` | 19/19 | test_v1: 26/30 | 22/30 |
| 2 | prompt v3 + verifier v2 (chặn số liệu, phép tính dùng dữ kiện ngoài sách); thử mô tả hình bằng gpt-4.1 (index B2, B3) nhưng kém hơn trên dev nên giữ index B | `hpv2_b` | 22/24 | test_v2: 26/30 | 25/30 |
| 3 | GPT-5.6 Luna; prompt v4 + filter chương `fallback`; verifier v3; index B4 (mô tả hình bằng Luna) | `luna_v4_fb_b4` | 28/28 | test_v3: 27/30 | 22/30 |

- Lỗi thấy ở mỗi bộ test được **tái hiện bằng câu dev mới** rồi mới sửa (dev 19 → 24 → 28 câu), nên điểm dev giữa các vòng không so trực tiếp; mỗi bộ test cũng khác độ khó (baseline `dense` dao động 22–25/30), nên cách đọc đúng là **chênh lệch so với baseline cùng test**: +4, +1, +5.
- Thay đổi có tác dụng rõ nhất trên dev: **verifier** (vòng 1) và **prompt v4 + filter `fallback` + verifier v3** (vòng 3: +1 câu với gpt-4.1-mini, +2 với Luna). Riêng việc **đổi model sang Luna** không tăng điểm dev (25/28 cả hai) nhưng **giảm ≈ 55 % chi phí**.
- Mô tả hình "chặt hơn" bằng gpt-4.1 (vòng 2) đếm đúng hơn nhưng làm mất vị trí và đọc sai chữ trong hình, nên bị loại; mô tả bằng Luna (B4) giữ được cả hai. Phương pháp retrieval giữ nguyên từ vòng 1 (hybrid): rerank có Hit@3 cao nhất nhưng không tăng điểm agent, đắt và chậm (≈ 2,5 s/truy vấn).

### Ba trường hợp để trình bày

1. *Có bằng chứng:* `t3_tab4` (ảnh Adobe Kuler): "RGB 255 83 13, HEX FF530D", citation `B4:colorme3:p086:v01`, đã đối chiếu ảnh trang 86.
2. *Thiếu bằng chứng:* `t3_un3` (so sánh Photoshop với GIMP): agent tìm rồi từ chối đúng, không khẳng định thêm.
3. *Lỗi:* `t3_un4` (mã HEX màu đỏ trong logo colorME): agent gán mã FF0000 của ô màu trong ảnh Kuler cho logo; verifier không chặn được. Hai câu `t3_ch4`, `t3_ch5` thì bản nháp đúng nhưng verifier v3 xóa hết ý nên thành từ chối (verifier quá chặt với câu suy ra từ mô tả hình).

### Lưu ý trung thực

- Kết quả **vừa chạm** ngưỡng 90 % (cần ≥ 27/30, không làm tròn). Khoảng tin cậy 95 % (Wilson) của 27/30 khoảng 74–96 %; chênh 1 câu với `hpv2_b` chưa đủ để kết luận cấu hình mới chắc chắn tốt hơn, chỉ chắc là ngang hoặc nhỉnh hơn với chi phí thấp hơn khoảng một nửa.
- Mọi nhãn đạt/không đạt do **agent (AI)** gán, kèm lý do từng câu. Tôi đã rà lại nhãn test_v3 của ba cấu hình và bộ câu hỏi, không đổi nhãn nào (`results/labels/luna_v4_fb_b4_test.json`, `results/agent/luna_v4_fb_b4/test/review_sheet.md`); nhãn dev và nhãn hai bộ test cũ chưa rà lại. Nếu một nhãn đổi từ đạt sang không đạt thì kết quả xuống 26/30 và **không còn đạt ngưỡng bonus**.
- Cùng một người (AI) viết benchmark, sửa hệ thống và gán nhãn, nên có rủi ro thiên lệch.
- Giá GPT-5.6 Luna ($0,20 / $1,20 mỗi 1M token input/output) lấy từ nguồn thứ cấp, chưa đối chiếu trang giá chính thức.

### Chi phí và cách chạy lại

- Cấu hình nộp trên test_v3: $0,045 cho 30 câu, median 8,6 s/câu. Toàn bộ thí nghiệm 3 vòng của Day 7 ≈ $4,6 (đã gồm mô tả hình bằng gpt-4.1 $0,99 và bằng Luna $0,18); Day 6 ban đầu ≈ $0,32.
- Chạy lại (sau khi dựng dữ liệu theo `DATA_NOT_INCLUDED.md`): `python -m src.cli export --collection colorme3_B4`, rồi `python -m src.cli agent --config luna_v4_fb_b4 --split test`, `python -m src.cli score --config luna_v4_fb_b4 --split test`.

> **Từ đây trở xuống là vòng 1** (agent `gpt-4.1-mini`, index `colorme3_B`, bộ test `test_v1` gồm các câu `ts_*`). Bộ test này đã được dùng để phân tích lỗi nên **không còn là đánh giá độc lập**; mọi chữ "test" bên dưới nghĩa là `test_v1`. Giữ nguyên để truy vết.

## Vòng 1 — Dữ liệu và benchmark

- **Nguồn, quyền, số trang, số chunk:** `EBOOK COLORME 3.pdf` (sách của colorME; **chưa xác minh giấy phép phân phối lại**; dùng cho học tập. PDF, ảnh render, văn bản toàn sách và mô tả hình đầy đủ **không nằm trong git**, xem `DATA_NOT_INCLUDED.md` và `README.md` mục "Tái tạo dữ liệu"; nguồn tải: <https://thietbigas.com.vn/upload/product/EBOOK%20COLORME%203.pdf>, bản sao do bên thứ ba lưu trữ, SHA-256 trùng file đã dùng), 183 trang PDF, 181 trang nội dung, có ảnh/bảng/biểu đồ/infographic. Index Day 6 collection `colorme3_B`: **476 chunk = 181 text + 295 mô tả hình** phủ 183/183 trang (`results/export_stats.json`).
- **Vector store / embedding:** ChromaDB 1.5.9 PersistentClient của Day 6 (`../../day6/K5-L3-Day06-ColorME/starter/chroma_db`, đọc tại chỗ, không copy), cosine HNSW; OpenAI `text-embedding-3-small`, 1536 chiều — Day 7 kiểm tra metadata collection (`embedding_model`, `dimensions`) và từ chối chạy nếu khác.
- **Agent model:** `gpt-4.1-mini` (temperature 0, OpenAI tool calling); rerank/verifier cùng model. Lệnh ở `README.md` (mục Bài làm).
- **Benchmark** (`benchmark/questions.json`, chốt trước khi chạy: `benchmark/FROZEN_v1.json`, sha256 `a92ff13c…`): dev 19 = 16 có đáp án (bảng 3, ảnh 3, biểu đồ 3, multi-hop 3, text 4) + 3 thiếu bằng chứng; **test 30 = 24 có đáp án (bảng 6, ảnh 5, biểu đồ 5, multi-hop 4, text 4) + 6 thiếu bằng chứng**. Mỗi câu có nhóm, đáp án, evidence theo trang (+ vùng hình), lý do; câu thiếu bằng chứng có `absence_reason` và `check_method`. Evidence hình: sự kiện đã xem trên ảnh render, `evidence` là cụm từ khóa để code kiểm tra chunk/context có mang thông tin đó; multi-hop có nhiều `group` bắt buộc.
- **Chấm:** đạt/không đạt theo ADVANCED (đúng + đủ, citation đúng trang/vùng, evidence hỗ trợ toàn bộ câu trả lời; thêm khẳng định ngoài tài liệu = không đạt; câu thiếu bằng chứng đạt khi từ chối và không khẳng định thêm). Kèm `answer_grade` 0-2, `citation_support`, `abstention_correct` cho `starter/agent_metrics.py`.

## Vòng 1 — Retrieval và thử nghiệm

Retrieval một lượt với **câu hỏi gốc, không filter**, top-10 xếp hạng, hit = chunk đúng trang và chứa evidence; multi-hop chỉ tính hit khi đủ mọi group (`python -m src.cli retrieval`).

| Phương pháp | Split | Hit@1 | Evidence Hit@3 | MRR@10 | Thời gian / chi phí |
|---|---|---|---|---|---|
| Dense (Chroma Day 6) | dev | 14/16 (87.5%) | 14/16 (87.5%) | 0.927 | 256 ms/q (gồm embed query) · $0.00001 |
| BM25 (âm tiết + bigram) | dev | 13/16 | 14/16 | 0.891 | 3 ms/q · $0 |
| Hybrid RRF(dense, BM25, k=60) | dev | 13/16 | **16/16** | 0.896 | 7 ms/q (embedding cache) |
| Hybrid → LLM rerank (15 → 5) | dev | **15/16** | **16/16** | **0.969** | 2.4 s/q · $0.025 |
| Dense | test | 20/24 | 19/24 | 0.889 | |
| BM25 | test | 21/24 | 21/24 | 0.924 | |
| Hybrid | test | 20/24 | 20/24 | 0.899 | |
| Rerank | test | 23/24 | 23/24 | 0.972 | $0.039 |

Agent (Context Evidence Rate = câu có đủ mọi group evidence trong context cuối / câu có đáp án; pass = chấm tay):

| Cấu hình | Phương pháp, top-k, filter, rerank, budget | Giả thuyết / thay đổi | Split | Pass (chấm tay) | Context Evidence Rate | Median latency / chi phí |
|---|---|---|---|---|---|---|
| `dense` (baseline) | dense top-5, agent tự đặt filter chương/loại, budget 12k ký tự, ≤6 lượt | — | dev | 16/19 | 15/16 | 3.2 s / $0.044 |
| `bm25` (PP 2) | BM25 top-5 | từ khóa VN/ tên riêng | dev | 17/19 | 16/16 | 2.8 s / $0.037 |
| `hybrid` (PP 3) | RRF top-5 | bù điểm yếu 2 phía | dev | 18/19 | 16/16 | 2.9 s / $0.042 |
| `hybrid_page` (CT 1) | + tool `read_page` | đọc cả trang khi cần chú giải/ngữ cảnh lân cận | dev | 18/19 | 16/16 | 2.6 s / $0.042 |
| `rerank_page` (PP 4 + CT 2) | hybrid 15 → LLM rerank → 5 + read_page | xếp hạng tốt hơn | dev | 17/19 | 16/16 | 4.7 s / $0.080 |
| `*_strict` (CT 3) | prompt v2 "mỗi ý phải có trong đoạn" | giảm bịa thêm | dev | 17–18/19 | 15–16/16 | ~2.7 s / ~$0.05 |
| `hybrid_page_strict_41` (CT 4) | controller gpt-4.1 | model mạnh hơn bớt bịa | dev | 17/19 | 16/16 | 7.4 s / **$0.79** |
| **`hybrid_page_verify` (CT 5, chọn)** | hybrid_page + prompt v2 + **verifier** (lượt LLM xóa ý không có trong chunk được trích) | sửa lỗi thêm kiến thức ngoài | dev | **19/19** | 16/16 | 4.0 s / $0.054 |
| `rerank_page_verify` | rerank_page + v2 + verifier | | dev | 19/19 | 16/16 | 5.1 s / $0.065 |
| **Cấu hình đã chọn** | `hybrid_page_verify` | | **test** | **26/30 (86.7%)** | 24/24 | 4.6 s / $0.098 (30 câu) |
| Baseline | `dense` | | test | 22/30 (73.3%) | 21/24 | 3.4 s / $0.081 |

Mỗi phương pháp mới được đo riêng (dense/BM25/hybrid/rerank: 4 phương pháp); cải thiện = read_page, prompt strict, gpt-4.1, verifier. Toàn bộ trace dev vòng 1: `results/agent/<config>/dev/`, nhãn `results/labels/<config>_dev.json` (riêng `dense` và `hybrid_page_verify`: `dev_r1/` và `*_dev_r1.json`, vì đã chạy lại ở vòng sau), bảng chọn `results/SELECTION.json` (chốt trước khi chạy test, tiêu chí: số câu dev đạt → chi phí → latency; `hybrid_page_verify` hòa `rerank_page_verify` 19/19 nhưng rẻ và nhanh hơn).

**Hai lỗi dev, nguyên nhân, thử nghiệm:**
1. `dv_ch1` (bong bóng nhỏ nhất) — dense chỉ lấy chunk "kích thước bong bóng" (p6 v00), thiếu chunk chú giải màu → trả lời "màu xanh lá nhạt" mà không nêu bài toán (Context Evidence thiếu group `legend`). Giả thuyết: BM25 khớp tên mục trong chú giải. Hybrid/BM25 lấy được cả 2 chunk → đạt ở mọi cấu hình hybrid (Context Evidence 15/16 → 16/16).
2. `dv_tx3` (vì sao logo phải vector) — mọi cấu hình v1 thêm "vector phóng to không mất chất lượng" (không có trong p137 — sách chỉ dẫn link video). Thử: prompt strict (không sửa, 18/19), gpt-4.1 (không sửa, đắt ×17), **verifier** (sửa, 19/19, +$0.01/30 câu). Ghi nhận cả kết quả không cải thiện.

## Vòng 1 — Agent và đánh giá

- **Tool:** `search_docs(query, chapter?, content_type?)` (phương pháp theo cấu hình, top-5), `read_page(page)` (mọi chunk của trang), `final_answer(answer, citations, abstain)`. Filter do model suy ra từ câu hỏi (chương/loại hình); log trong trace, không dùng gold. **Điều kiện dừng:** `final_answer`, hoặc 6 lượt tool → ép `final_answer` → nếu vẫn không có thì abstain. **Context:** mỗi chunk chỉ đưa vào 1 lần (lần sau chỉ báo ID), budget 12.000 ký tự cho toàn bộ chunk text, chunk vượt budget bị bỏ và log (`dropped_ids`). **Citation:** ID phải đã xuất hiện trong context; ID lạ bị loại, không còn citation hợp lệ → abstain. **Verifier** chỉ nhận câu hỏi + nháp + chunk được trích. **Lỗi provider** → `status=error`, không giả kết quả (test: 0 lỗi).

| Cấu hình / split | Tool use | Số lượt retrieval (TB, phân bố) | Grounded answer 0/1/2, TB | Citation hợp lệ | Câu trả lời có citation | Abstention đúng | Từ chối nhầm |
|---|---|---|---|---|---|---|---|
| `hybrid_page_verify` / test | 30/30 | 2.03 (1:18, 2:4, 3:3, 4:1, 5:2, 6:2) | 1/2/21 → 1.83 | 34/35 | 25/25 | 5/6 | 0/24 |
| `dense` / test | 30/30 | 2.03 (1:18, 2:5, 3:1, 4:2, 5:2, 6:2) | 2/4/18 → 1.67 | 32/34 | 24/24 | 4/6 | 1/24 |

(`results/agent/<config>/test_v1/agent_metrics.json` từ `starter/agent_metrics.py`.)

**Chấm context (0/1/2) trên test có đáp án** — `hybrid_page_verify`: 24/24 có đủ evidence (2), riêng ts_ch3 context có chunk biểu đồ nhưng dữ liệu sai → 1. `dense`: ts_ch1 = 1 (thiếu chú giải), ts_ch2 = 0 (không tìm thấy p41), ts_mh1 = 1 (thiếu p145), ts_ch3 = 1, còn lại 2.

| Query ID | Loại | Tool call và kết quả | Câu trả lời và citation | Nhãn, lý do |
|---|---|---|---|---|
| ts_tab1 | bảng | 1 lượt: search("mật độ điểm ảnh iPhone 6 5.5 inch iPhone 5 4 inch", content_type=visual) → p14 v00 (rank 1) | "401 − 326 = 75 ppi" [p014:v00] | **Đạt** — đúng phép tính, đối chiếu ảnh p14 |
| ts_mh2 | multi-hop | 4 lượt: search("bảng màu logo màu tím", ch6, visual) → p136 v00 (rank 2); search("màu bổ túc của tím", ch3, text) → p70 t00; search thêm; read_page(136) | tím = tinh tế…bí ẩn; bổ túc vàng; TPBank [p136:v00][p070:t00] | **Đạt** — 2 trang, 2 loại evidence |
| ts_un4 | thiếu evidence | 5 lượt search "font chữ (cho CV)" trong ch7, cả text và visual → chỉ p155-162 không nói về font | "Sách không có thông tin…" | **Đạt** — từ chối đúng |
| ts_ch3 | biểu đồ | 1 lượt: search("CV – Charts", ch7, visual) → p160 v00/v01/v03, v02 trong top-5 | "4/5 chấm" [p160:v02] | **Không đạt** — ảnh gốc 5/6; lỗi mô tả vision |
| ts_un5 | thiếu evidence | 3 lượt: search "A4 300 ppi kích thước pixel" (ch1, text/visual) → p12, p11, p10 | tự tính 2481×3507 [p012:t00] | **Không đạt** — dùng kích thước A4 ngoài sách; verifier không chặn |

## Vòng 1 — Thử thách nâng cao (test_v1)

- **Tài liệu:** như trên (183 trang, PDF 1.5, Word 2016, creationDate 2016-03-14). Text: PyMuPDF; hình: render 120 dpi → `gpt-4.1-mini` mô tả từng phần tử (bảng → hàng/cột, biểu đồ → giá trị/chú giải, ô màu → cặp màu–nhãn) → chunk visual có trang + bbox ảnh + file render. Index toàn bộ 183 trang. **Phần chưa xử lý tốt:** đếm phần tử nhỏ trong biểu đồ (p160), tỉ lệ % donut/pie chỉ là ước lượng; không có OCR độc lập để đối chứng chữ trong hình; ảnh trang trí được đánh `informative` lẫn lộn (thừa chunk).
- **Benchmark & cấu hình:** dev/test chia trước, test không dùng để chọn; cấu hình chốt trên dev: `hybrid_page_verify`.

| Nhóm test | Đạt / tổng | Tỷ lệ | Lỗi / nhận xét |
|---|---|---|---|
| Bảng | 6/6 | 100% | |
| Ảnh, sơ đồ | 4/5 | 80% | ts_img3: trả lời "TIME" (tên tạp chí) thay vì tiêu đề "THE 100 MOST INFLUENTIAL PEOPLE…" — câu hỏi "dòng tiêu đề lớn" viết mơ hồ (lỗi benchmark, vẫn tính không đạt) |
| Biểu đồ | 3/5 | 60% | ts_ch3, ts_ch5: lỗi mô tả vision p160 (5/6 chấm thành 4/5) |
| Multi-hop | 4/4 | 100% | |
| Text | 4/4 | 100% | |
| Thiếu bằng chứng | 5/6 | 83% | ts_un5: tự tính từ kiến thức ngoài |
| **Toàn bộ** | **26/30** | **86.7%** | **Chưa đạt ngưỡng 90% (cần 27/30)** · 0 lỗi hệ thống |

- Baseline `dense` trên cùng test: 22/30 (73.3%).
- **Trace / nhãn / evidence:** `results/agent/hybrid_page_verify/test_v1/{traces.json, summary.json, pass_summary.json, review_sheet.md}`, `results/labels/hybrid_page_verify_test_v1.json`; thời gian median 4.6 s/câu, tổng $0.098 cho 30 câu (agent $0.087 + verifier $0.011); toàn bộ thí nghiệm Day 7 ≈ $1.55 (riêng thử gpt-4.1 $0.79); Day 6 (vision + embed) ≈ $0.32.
- **Giới hạn và trung thực:** lỗi p160 đã được phát hiện khi kiểm tra gold **trước** khi chạy test nhưng không sửa pipeline hay đổi câu hỏi (sẽ là chỉnh theo test). Một chỉnh sửa duy nhất sau khi viết benchmark: cụm khóa của ts_ch3 `"5"` → `"chấm"` (sửa bộ so khớp, trước mọi lần chạy, ghi trong `FROZEN_v1.json`). Nhãn do AI gán, cùng tác giả benchmark → rủi ro thiên lệch; test 30 câu → ±1 câu = 3.3 điểm %.
- **Muốn đạt ≥90% hợp lệ:** cải tiến trên dev (pass vision thứ hai chuyên cho biểu đồ/đếm; verifier chặn số liệu/tính toán không có trong đoạn), sau đó **tạo bộ test mới** trước khi báo điểm (theo ADVANCED: test đã xem không dùng lại để báo cáo độc lập).

# Day 7 — Agentic RAG

**Bài cá nhân · Python 3.11+ · tiếp nối Day 6**

Dùng embedding và vector store từ Day 6 để xây một agent biết tìm bằng chứng, trả lời có nguồn và nhận biết khi không đủ thông tin. Bạn tự chọn kiến trúc, số tool và cách tổ chức retrieval.

> **Tùy chọn:** [Gợi ý dùng AI để lập trình](AGENT_SETUP.md) giúp bạn làm lab; phần này không bắt buộc và không tính điểm.

## Bài cần làm

![Agent tìm tài liệu trong kho Day 6 và trả lời có nguồn](assets/retrieval-pipeline.svg)

1. Kết nối dữ liệu, embedding và vector store Day 6.
2. Xây agent dùng model thật và ít nhất một khả năng truy xuất dữ liệu. Agent có thể dùng nhiều tool và nhiều lượt gọi.
3. Thử **ít nhất 3 phương pháp retrieval khác nhau**, trong đó có dense retrieval dùng vector store Day 6. Tự chọn các phương pháp còn lại; xem [gợi ý](GUIDE.md#2-thử-các-phương-pháp-retrieval).
4. Thử nhiều cấu hình, benchmark, phân tích lỗi và chọn cấu hình tốt trên **dev**; sau đó đánh giá trên **test**.

Benchmark tối thiểu có **24 câu**: dev gồm 15 câu có đáp án và 2 câu thiếu bằng chứng; test gồm 5 câu có đáp án và 2 câu thiếu bằng chứng. Xem [benchmark](BENCHMARK.md) và [rubric](RUBRIC.md).

## Thử thách nâng cao · +15 điểm

Index một tài liệu thực tế từ **100 trang** có bảng, ảnh và biểu đồ; xây agent truy xuất và trả lời các câu hỏi về nội dung đó. Hoàn thành [thử thách nâng cao](ADVANCED.md) và đạt **ít nhất 90% benchmark test** để nhận 15 điểm bonus. Phần cơ bản tối đa 85 điểm; toàn bài tối đa 100 điểm.

## Bắt đầu

1. Đọc [hướng dẫn](GUIDE.md), [rubric](RUBRIC.md) và [quy tắc](RULES.md).
2. Tạo repo cá nhân theo [cách nộp bài](SUBMISSION.md), chuẩn bị đầu ra Day 6 và model hỗ trợ tool calling.
3. Dùng hoặc thay thế [starter](starter/README.md); bạn cần kết nối model và vector store thật.
4. Chạy `python -m unittest discover -s tests -v`. Test mock chỉ kiểm tra code, không phải benchmark agent thật.

![Các bước thử nghiệm trên dev và đánh giá trên test](assets/experiment-loop.svg)

Nộp code, cách chạy, cấu hình, benchmark, trace và [báo cáo](report/individual/MSSV_HoTen.md). Thời gian ở [checkpoints](CHECKPOINTS.md) là gợi ý, có thể điều chỉnh theo lớp và phạm vi thử nghiệm.

---

## Bài làm: Agentic RAG trên EBOOK COLORME 3 (PDF chữ + hình, 183 trang)

Dùng lại index Day 6 (repo <https://github.com/ddkhoa2605/K5-L3B-DAY06-DoanDangKhoa-2A202603766-DataIngestion-ColorME>): ChromaDB, embedding `text-embedding-3-small` (1536 chiều). Cấu hình nộp **`luna_v4_fb_b4`**: agent **GPT-5.6 Luna** (Responses API, reasoning `low`) dùng tool calling (`search_docs`, `read_page`, `final_answer`) trên collection **`colorme3_B4`** (457 chunk = 181 chunk text + 276 chunk mô tả hình do Luna tạo); retrieval hybrid RRF (dense + BM25), filter chương `fallback`, prompt v4, verifier v3. Bốn phương pháp retrieval đã so sánh: dense, BM25 tiếng Việt, hybrid RRF, hybrid + LLM rerank. Hai vòng trước dùng gpt-4.1-mini trên `colorme3_B`.

```bash
# Yêu cầu: đã dựng dữ liệu Day 6 (xem "Tái tạo dữ liệu" bên dưới) và OPENAI_API_KEY trong .env
# (hoặc starter/.env của Day 6). Windows: đặt PYTHONUTF8=1
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v                           # 25 test offline (fake client)
python -m src.cli export --collection colorme3_B4                 # Day 6 Chroma -> data/colorme_chunks_colorme3_B4.json
python -m src.cli validate --collection colorme3_B4               # evidence nằm trong chunk, đếm nhóm, hash benchmark
python -m src.cli retrieval --split dev --collection colorme3_B4  # Hit@1 / Evidence Hit@3 / MRR (dense, bm25, hybrid, rerank)
python -m src.cli agent --config luna_v4_fb_b4 --split dev
python -m src.cli agent --config luna_v4_fb_b4 --split test       # đã chốt trước khi chạy: results/SELECTION_v3.json
python -m src.cli sheet --config luna_v4_fb_b4 --split test       # sheet đọc để chấm tay
python -m src.cli score --config luna_v4_fb_b4 --split test       # tỷ lệ đạt theo nhóm + input cho starter/agent_metrics.py
```

| Vòng | Cấu hình chọn | Dev | Test mới của vòng |
|---|---|---|---|
| 1 | `hybrid_page_verify` (gpt-4.1-mini) | 19/19 | test_v1: 26/30 (86.7%) |
| 2 | `hpv2_b` (+ prompt v3, verifier v2) | 22/24 | test_v2: 26/30 (86.7%) |
| **3** | **`luna_v4_fb_b4`** (GPT-5.6 Luna qua Responses API, index B4 mô tả hình bằng Luna, filter fallback, prompt v4, verifier v3) | **28/28** | **test_v3: 27/30 (90.0%)** |

Baseline `dense` trên test_v3: 22/30. Cấu hình vòng 3 vừa chạm ngưỡng 90% của thử thách nâng cao (nhãn do agent gán; nhãn test_v3 và bộ câu hỏi đã được học viên rà lại). Chi tiết từng vòng, kết quả theo nhóm và phân tích lỗi: [báo cáo](report/individual/2A202603766_DoanDangKhoa.md).

### Bối cảnh: vì sao Day 6 đổi từ Python docs sang ColorME

**Day 6 ban đầu của tôi làm trên tài liệu Python 3.13** (bản text chính thức của docs.python.org: 6 chương Tutorial + 4 trang Library, ChromaDB, `all-MiniLM-L6-v2`). Bản đó đã hoàn thành đầy đủ (repo gốc ghi ở `STUDENT.md` của bài đó: https://github.com/ddkhoa2605/K5-L3B-DAY06-DoanDangKhoa-2A202603766-DataIngestion, thư mục máy `day6/K5-L3-Day06-DataIngestionEngineering`) và **vẫn giữ nguyên, không bị sửa**.

**Vì sao đổi sang ColorME cho Day 7:** Day 7 yêu cầu dùng index của Day 6, và thử thách nâng cao ([`ADVANCED.md`](ADVANCED.md), +15 điểm) cần *một tài liệu thực tế ≥ 100 trang có text, bảng, ảnh và biểu đồ chứa thông tin hữu ích*, với benchmark riêng cho bảng, ảnh/sơ đồ, biểu đồ, multi-hop và text. Dữ liệu Python docs không đáp ứng được vì:

- bản text thuần **không có ảnh, bảng, biểu đồ** (chỉ chữ), nên không thể hỏi các nhóm bảng/ảnh/biểu đồ;
- **không có trang vật lý**: 117 "đơn vị trang" là do tôi tự chia theo heading (≥ 1.500 ký tự), không truy về trang PDF/vùng ảnh gốc được;
- embedding `all-MiniLM-L6-v2` là **tiếng Anh**, còn câu hỏi và nội dung cần xử lý lần này là tiếng Việt.

Vì vậy tôi **làm lại Day 6 trên `EBOOK COLORME 3.pdf`** (183 trang PDF thật, tiếng Việt, có ảnh, bảng màu, infographic, biểu đồ) trong thư mục mới `day6/K5-L3-Day06-ColorME` (repo: <https://github.com/ddkhoa2605/K5-L3B-DAY06-DoanDangKhoa-2A202603766-DataIngestion-ColorME>), và Day 7 chỉ dùng bản này.

| | Day 6 gốc (Python docs) | Day 6 làm lại (ColorME), dùng cho Day 7 |
|---|---|---|
| Nguồn | docs.python.org, 10 file text | PDF 183 trang (Word 2016), tiếng Việt |
| Đơn vị "trang" | 117 đơn vị tự chia theo heading | **183 trang PDF thật** (`page`, `printed_page`) |
| Nội dung hình | không có | **vision model mô tả từng ảnh/bảng/biểu đồ** (gpt-4.1-mini; Luna cho index B4) |
| Embedding | `all-MiniLM-L6-v2`, 384 chiều, chạy máy | `text-embedding-3-small`, 1536 chiều, API |
| Vector store | ChromaDB (cosine, HNSW) | ChromaDB (cosine, HNSW), giữ nguyên |
| Chiến lược A / B / C | A: cắt 500 ký tự; B: theo heading; C: B + lọc `doc_type` | A: chỉ text; **B: text + mô tả hình**; C: B + lọc `chapter` |
| Trường lọc | `doc_type` (tutorial / library) | `chapter` (ch1…ch8, phụ lục) |
| Benchmark Day 6 | 28 câu (22 dev / 6 test) | 24 câu (17 dev / 7 test), có 4 câu bằng chứng nằm trong hình |
| Số chunk (A / B / C) | 597 / 352 / 352 | 181 / 476 / 476 |
| Evidence Hit@3 (dev / test) | A 11/22 · 2/6; B và C 19/22 · 6/6 | A 15/17 · 5/7; B và C 16/17 · 6/7 |
| Chi phí | $0 (chạy cục bộ) | ≈ $0,32 (vision + embedding), thêm ≈ $0,18 cho index Luna |

Hai bộ số Day 6 **không so sánh trực tiếp được** (khác tài liệu, ngôn ngữ, embedding, benchmark và kích thước mẫu). Phần giữ nguyên: cấu trúc pipeline (đọc → chuẩn hóa → chunk → embed → upsert), upsert idempotent kèm kiểm tra nạp lại, kiểm chứng evidence trước khi chạy retrieval, hash benchmark, và cách chấm coherence / metadata / grounding.

Lưu ý: lịch sử git của repo ColorME kế thừa các commit của bản Python docs (vì tạo bằng cách sao chép repo Day 6 gốc); kết quả và dữ liệu Python docs đã được gỡ khỏi bản làm việc của ColorME.

### Tái tạo dữ liệu (không có trong git)

Văn bản toàn sách, mô tả hình và Chroma **không nằm trong git** (bản quyền colorME chưa xác minh). Day 7 cần repo Day 6 (<https://github.com/ddkhoa2605/K5-L3B-DAY06-DoanDangKhoa-2A202603766-DataIngestion-ColorME>, commit `4b574e0`) để dựng Chroma, rồi export chunk:

```bash
# 0) clone repo Day 6 (cạnh repo Day 7) và trỏ DAY6_ROOT tới nó
git clone https://github.com/ddkhoa2605/K5-L3B-DAY06-DoanDangKhoa-2A202603766-DataIngestion-ColorME.git day6-colorme
#    bash:        export DAY6_ROOT="$PWD/day6-colorme"
#    PowerShell:  $env:DAY6_ROOT = "$PWD\day6-colorme"
#    (không đặt DAY6_ROOT thì code tìm ở ../../day6/K5-L3-Day06-ColorME so với repo Day 7)
# 1) dựng dữ liệu Day 6 theo DATA_NOT_INCLUDED.md của repo Day 6 (tải PDF, chạy pipeline), rồi trong repo Day 7:
python -m src.cli export --collection colorme3_B
python -m src.cli export --collection colorme3_B4
python -m src.cli validate --collection colorme3_B4
```

Danh sách file, SHA-256 và các bước đầy đủ: [`DATA_NOT_INCLUDED.md`](DATA_NOT_INCLUDED.md).

### UI test (Streamlit)

```bash
python -m pip install -r requirements.txt   # gồm streamlit, pandas
streamlit run app.py        # mở http://localhost:8501
```

| Tab | Chức năng |
|---|---|
| 💬 Hỏi agent | Chọn cấu hình (mặc định `luna_v4_fb_b4`), ghi đè top_k / max_steps / budget / collection / filter_mode / verifier / reasoning; nhập câu hỏi hoặc chọn câu benchmark; xem câu trả lời, citation (kèm ảnh trang), trace tool call, bản nháp trước verifier, context cuối, token, thời gian, chi phí; **so sánh 2 cấu hình song song**. |
| 🔎 Retrieval | Thử dense / BM25 / hybrid / rerank trên B, B2, B3, B4; lọc chương, loại; đánh dấu hit theo gold của một câu benchmark. |
| 📋 Benchmark | Duyệt dev / test / test_v1 / test_v2 theo nhóm; xem gold + ảnh trang; chạy 1 câu hoặc cả split đang lọc (chỉ hiển thị, không ghi đè `results/`). |
| 📊 Kết quả đã lưu | Mở mọi lần chạy trong `results/agent/<config>/<split>`: tỷ lệ đạt theo nhóm từ nhãn chấm tay, lọc câu không đạt, trace từng câu. |
| 📄 Trang sách | Xem ảnh render một trang + toàn bộ chunk text/mô tả hình của trang đó theo collection. |


| Đường dẫn | Nội dung |
|---|---|
| `src/` | `retrievers.py` (dense/BM25/hybrid/rerank), `agent.py` (vòng tool, context budget, kiểm tra citation, verifier; Chat Completions và Responses API), `cli.py` (các lệnh và toàn bộ cấu hình), `config.py` |
| `app.py`, `requirements.txt` | UI test Streamlit; thư viện cần cài |
| `benchmark/questions.json` | 118 câu: `dev` 28, `test` 30 (test_v3, bộ đang dùng), `test_v1` và `test_v2` 30 câu mỗi bộ (đã dùng ở vòng trước, giữ để truy vết); nhóm bảng/ảnh/biểu đồ/multi-hop/text/thiếu evidence |
| `benchmark/FROZEN_v1.json`, `FROZEN_v2.json`, `FROZEN_v3.json` | hash bộ câu hỏi chốt trước khi chạy test của từng vòng |
| `results/retrieval/`, `results/agent/<config>/<split>/` | trace từng câu (tool call, query, filter, kết quả, context, câu trả lời, citation, token, chi phí, latency), summary |
| `results/labels/`, `results/SELECTION_v3.json` | nhãn chấm tay từng câu; bảng chọn cấu hình trên dev của vòng 3 (`SELECTION.json`, `SELECTION_v2.json` là vòng 1, 2) |
| `DATA_NOT_INCLUDED.md` | dữ liệu không nằm trong git (văn bản sách, Chroma), SHA-256 và cách tái tạo |
| `report/individual/2A202603766_DoanDangKhoa.md` | báo cáo |

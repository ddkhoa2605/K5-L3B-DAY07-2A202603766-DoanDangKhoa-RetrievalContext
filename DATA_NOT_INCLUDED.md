# Dữ liệu KHÔNG nằm trong git (Day 7)

**Lý do:** các file dưới đây là bản export văn bản toàn sách + mô tả hình từ index Day 6; cuốn *EBOOK COLORME 3* thuộc bản quyền colorME/tác giả và giấy phép phân phối lại **chưa được xác minh**. Xem thêm `DATA_NOT_INCLUDED.md` và `data/manifest.json` của repo Day 6.

| File | Kích thước | SHA-256 của bản dùng để báo cáo |
|---|---|---|
| `data/colorme_chunks.json` | 699 KB | `1aa467211811490f22bf41973924e6fa4fd077a3854631c6dce96ec5c035535f` |
| `data/colorme_chunks_colorme3_B2.json` | 728 KB | `aa6a8df963c116e5c9d63ae415e4939012644b887be80b74d7a3b4b8610d5b8a` |
| `data/colorme_chunks_colorme3_B3.json` | 1086 KB | `10303f1e4e868e0d6dd6282d8aee8f39de5fa2e96fa94b6fd3059ffe8b79592b` |
| `data/colorme_chunks_colorme3_B4.json` | 720 KB | `cdeac1019375e421aacfddecfcfaa20275a4181388d6506681797c245d02c516` |

Day 7 cũng **cần Chroma của Day 6** (`starter/chroma_db/`, không có trong git) cho dense retrieval.

## Tái tạo

1. Dựng dữ liệu Day 6 theo `DATA_NOT_INCLUDED.md` của repo Day 6 (<https://github.com/ddkhoa2605/K5-L3B-DAY06-DoanDangKhoa-2A202603766-DataIngestion-ColorME>, commit `4b574e0`). Day 7 tìm repo đó ở `../../day6/K5-L3-Day06-ColorME`; nếu để chỗ khác (vd clone thành `day6-colorme`), đặt biến môi trường `DAY6_ROOT` trỏ tới thư mục đó:
   ```bash
   git clone https://github.com/ddkhoa2605/K5-L3B-DAY06-DoanDangKhoa-2A202603766-DataIngestion-ColorME.git day6-colorme
   export DAY6_ROOT="$PWD/day6-colorme"     # PowerShell: $env:DAY6_ROOT = "$PWD\day6-colorme"
   ```
2. Trong repo Day 7, export chunk từ Chroma (BM25, kiểm tra evidence và UI cần các file này):
   ```bash
   python -m src.cli export --collection colorme3_B     # data/colorme_chunks.json
   python -m src.cli export --collection colorme3_B4    # cấu hình nộp: luna_v4_fb_b4
   # tùy chọn (thí nghiệm vòng 2): colorme3_B2, colorme3_B3
   python -m src.cli validate --collection colorme3_B4
   ```
3. Chạy lại cấu hình nộp: `python -m src.cli agent --config luna_v4_fb_b4 --split test` (cần `OPENAI_API_KEY`; đặt `PYTHONUTF8=1` trên Windows).

**Vẫn có trong git:** `benchmark/`, `results/` (trace, nhãn, tóm tắt; trace có chứa trích đoạn ngắn của sách làm bằng chứng chấm) và toàn bộ code. Nếu cần loại hoàn toàn các trích đoạn, xóa trường `context` trong `results/agent/*/*/traces.json`.

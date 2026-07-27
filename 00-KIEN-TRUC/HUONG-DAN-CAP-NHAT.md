# HƯỚNG DẪN CẬP NHẬT & TRÍCH DẪN — Living Knowledge Base

> Bộ sách này **không phải tài liệu tĩnh**. Nó là một *kho tri thức sống*: con người và AI cùng bổ sung, sửa chữa, cập nhật qua nhiều năm. File này là bộ quy tắc để giữ cho kho tri thức **chính xác, nhất quán và đáng tin** khi mở rộng.

---

## 1. Nguyên tắc trích dẫn (bắt buộc)

Đây là ranh giới đạo đức của toàn bộ tác phẩm. Vi phạm = làm hỏng độ tin cậy của cả bộ sách.

1. **Không bao giờ bịa số liệu.** Không tự chế thị phần, doanh thu, tỷ lệ %, kết quả nghiên cứu.
2. **Số liệu thật phải có nguồn + năm.** Ví dụ: *"(Nguồn: Kantar Worldpanel, 2023)"*. Không có nguồn tin cậy → không nêu con số cụ thể.
3. **Phân biệt 3 loại phát biểu:**
   - **Dữ kiện** — có thể kiểm chứng, có nguồn. ("Apple ra iPhone năm 2007.")
   - **Phân tích** — suy luận từ dữ kiện. ("Việc kiểm soát hệ sinh thái giúp Apple giữ biên lợi nhuận cao.")
   - **Ý kiến** — quan điểm biên soạn. ("Theo chúng tôi, đây là nước đi định vị thông minh nhất thập kỷ.")
4. **Chưa xác minh được → ghi rõ `(cần kiểm chứng)`.** Thà thừa nhận giới hạn còn hơn khẳng định sai.
5. **Số minh họa cho công thức → ghi rõ `(số minh họa)`.** Để người đọc không nhầm là số liệu thực tế.
6. **Không bịa link, không bịa tên nghiên cứu.** Nguồn tham khảo chỉ liệt kê sách/khung/tác giả có thật.
7. **Không sao chép nguyên văn.** Luôn tổng hợp, diễn giải, đối chiếu — tạo giá trị mới.

## 2. Mục "Cần cập nhật trong tương lai"

Mỗi chương kết thúc bằng mục này — đó là **điểm neo** cho lần cập nhật sau. Khi viết, hãy trả lời:
- Phần nào của chương **dễ lỗi thời** nhất? (nền tảng, thuật toán, quy định, công cụ, số liệu)
- **Tín hiệu** nào cho biết đã đến lúc cập nhật? (nền tảng đổi chính sách, công nghệ mới, luật mới)
- Câu hỏi mở nào chương **chưa trả lời được** ở thời điểm viết?

Đây là cách bộ sách "tự chỉ đường" cho AI/biên tập viên tương lai.

## 3. Quy tắc phiên bản (versioning)

- Toàn bộ sách theo **năm phát hành lớn**: `v1.0 (2026)`, `v2.0 (2027)`...
- Mỗi chương ghi phiên bản riêng ở dòng metadata đầu chương.
- Sửa nhỏ (sửa lỗi, cập nhật 1 số liệu): tăng số phụ, ví dụ `v1.1`.
- Viết lại lớn / đổi framework chủ đạo: tăng số chính, ví dụ `v2.0`.
- Ghi lịch sử thay đổi quan trọng ở cuối chương nếu cần (mục tùy chọn "Lịch sử phiên bản").

## 4. Quy trình thêm/sửa chương

```
1. Kiểm tra MASTER-OUTLINE.md — chương đã có chỗ chưa? Nếu chưa, khai báo trước.
2. cp CHUONG-TEMPLATE.md  →  TAP-XX-.../NN-slug-khong-dau.md
3. Viết đủ 24 mục + "Cần cập nhật trong tương lai".
4. Tự kiểm theo Checklist chất lượng (mục 6 bên dưới).
5. Cập nhật trạng thái ở MASTER-OUTLINE.md (⚪ → 🟡 → 🟢).
6. Commit với message rõ ràng: "Tập X · Chương Y — <tên>".
```

## 5. Quy ước đặt tên & định dạng

- File chương: `NN-slug-khong-dau.md` (2 chữ số + slug tiếng Việt không dấu). Ví dụ `03-marketing-mix.md`.
- Thư mục tập: `TAP-NN-TEN-VIET-HOA/`.
- Heading mục dùng `##` và đánh số 1–24 đúng template.
- Bảng, sơ đồ: ưu tiên Markdown table, ASCII art hoặc khối ```mermaid```.

## 6. Checklist chất lượng trước khi phát hành một chương

- [ ] Có đủ 24 mục + "Cần cập nhật trong tương lai", đúng thứ tự.
- [ ] Không có số liệu nào thiếu nguồn/năm hoặc thiếu nhãn `(cần kiểm chứng)`/`(số minh họa)`.
- [ ] Có ít nhất 1 ví dụ Việt Nam thật và 1 ví dụ quốc tế thật.
- [ ] Có Case Study gồm cả **thành công và thất bại**.
- [ ] Có Prompt AI cho đủ 6 công cụ (ChatGPT, Claude, Gemini, Perplexity, NotebookLM, AI Agent).
- [ ] Có Checklist, SOP, KPI, Biểu mẫu dùng được ngay.
- [ ] Văn phong dễ hiểu cho người mới, đủ sâu cho CEO.
- [ ] Đã cập nhật trạng thái ở MASTER-OUTLINE.md.

## 7. Hướng dẫn dành riêng cho AI mở rộng bộ sách

Nếu bạn là một hệ thống AI được giao mở rộng kho tri thức này:
- **Luôn đọc** `MASTER-OUTLINE.md` và `CHUONG-TEMPLATE.md` trước khi viết.
- **Không phá vỡ** cấu trúc 24 mục.
- **Ưu tiên** viết các chương đang ở trạng thái ⚪ theo thứ tự trong outline.
- **Tuyệt đối tuân thủ** Mục 1 (trích dẫn) — đây là điều kiện tồn tại của bộ sách.
- Khi không chắc, hãy **giữ định tính và đánh dấu (cần kiểm chứng)** thay vì bịa.

---

*Phiên bản hướng dẫn: v1.0 · 2026*

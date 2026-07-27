# Tập 8 · Chương 2 — Prompt Engineering cho Marketer

> **Bộ giáo trình:** MARKETING THỰC CHIẾN 2026–2035
> **Tập 8:** AI Marketing & Chuyển đổi số
> **Chương 2:** Prompt Engineering cho Marketer — Ra lệnh cho AI hiệu quả
> **Cấp độ:** Nền tảng → Ứng dụng
> **Thời lượng học đề xuất:** 6–8 giờ (lý thuyết + thực hành)
> **Điều kiện tiên quyết:** Tập 8 Chương 1 (Tổng quan AI trong Marketing)
> **Phiên bản:** 1.0 · Cập nhật 07/2026

**Tóm tắt một câu:** Prompt Engineering là kỹ năng thiết kế câu lệnh có cấu trúc để biến các mô hình AI ngôn ngữ thành một cộng sự marketing đáng tin cậy — nhanh hơn, đúng ý hơn và kiểm soát được.

---

## 1. Giới thiệu

Năm 2023, một câu lệnh AI kiểu "viết bài quảng cáo cho sản phẩm của tôi" còn được xem là đủ. Đến giai đoạn 2026–2035, khi các mô hình ngôn ngữ lớn (LLM) trở thành công cụ làm việc hằng ngày của phòng marketing, khoảng cách năng suất giữa hai marketer không còn nằm ở việc "ai biết dùng AI" mà ở việc "ai ra lệnh cho AI giỏi hơn".

Prompt Engineering — nghệ thuật và kỹ thuật viết câu lệnh cho AI — chính là lớp kỹ năng bản lề đó. Nó không đòi hỏi bạn biết lập trình. Nó đòi hỏi bạn biết tư duy rõ ràng, diễn đạt mạch lạc và hiểu cách "cỗ máy đoán chữ" bên trong AI vận hành để khai thác đúng cách.

Chương này viết cho marketer thực chiến: người viết content, người chạy quảng cáo, người làm nghiên cứu thị trường, trưởng nhóm cần chuẩn hóa quy trình. Bạn sẽ học cách cấu trúc một prompt tốt, các kỹ thuật nâng cao (few-shot, chain-of-thought, role prompting), cách xây thư viện prompt cho cả phòng, cách chọn đúng model cho từng việc, và quan trọng nhất — cách kiểm chứng đầu ra để không bị AI "bịa" làm hại thương hiệu.

## 2. Khái niệm

**Prompt** là toàn bộ nội dung bạn nhập vào một mô hình AI ngôn ngữ để nhận về kết quả: có thể là một câu hỏi, một chỉ dẫn, một đoạn ngữ cảnh kèm yêu cầu, hoặc tổ hợp cả ba.

**Prompt Engineering** là quá trình thiết kế, thử nghiệm và tinh chỉnh prompt một cách có phương pháp nhằm đạt được đầu ra chính xác, nhất quán và phù hợp mục tiêu.

Một số khái niệm nền cần phân biệt:

| Thuật ngữ | Ý nghĩa ngắn gọn |
|---|---|
| **LLM (Large Language Model)** | Mô hình ngôn ngữ lớn, dự đoán từ tiếp theo dựa trên xác suất. Ví dụ: GPT, Claude, Gemini. |
| **Token** | Đơn vị nhỏ AI xử lý (một từ có thể là 1–3 token). Ảnh hưởng độ dài và chi phí. |
| **Context window** | Lượng thông tin tối đa AI "nhớ" trong một phiên (tính bằng token). |
| **Temperature** | Tham số điều chỉnh độ "sáng tạo/ngẫu nhiên" của đầu ra (thấp = an toàn, cao = bay bổng). |
| **Hallucination** | Hiện tượng AI tạo ra thông tin sai nhưng nghe rất thuyết phục. |
| **System prompt** | Chỉ dẫn nền quy định vai trò và hành vi của AI xuyên suốt phiên làm việc. |

Điểm mấu chốt cần nhớ: AI **không hiểu** theo nghĩa con người. Nó dự đoán chuỗi từ có xác suất cao nhất dựa trên dữ liệu huấn luyện và prompt của bạn. Prompt càng rõ ràng và giàu ngữ cảnh, "vùng xác suất" AI tìm kiếm càng thu hẹp đúng hướng.

## 3. Lịch sử hình thành

- **2017:** Kiến trúc Transformer ra đời (bài báo "Attention Is All You Need" của Google) — nền móng cho mọi LLM hiện đại.
- **2018–2020:** Các mô hình GPT-2, GPT-3 (OpenAI) cho thấy khả năng làm nhiều việc chỉ bằng chỉ dẫn ngôn ngữ tự nhiên, khai sinh khái niệm "prompting".
- **2020–2022:** Xuất hiện các kỹ thuật nền: few-shot learning (học từ vài ví dụ trong prompt) và sau đó là chain-of-thought (khuyến khích AI "suy nghĩ từng bước").
- **Cuối 2022:** ChatGPT ra mắt công chúng, đưa việc "ra lệnh cho AI" từ giới nghiên cứu ra đại chúng. "Prompt engineer" bắt đầu được nhắc như một vai trò công việc.
- **2023–2024:** Bùng nổ Claude (Anthropic), Gemini (Google), cùng các công cụ như Perplexity (tìm kiếm có trích nguồn) và NotebookLM (làm việc trên tài liệu của người dùng). Prompt engineering phân hóa theo từng nền tảng.
- **2025 trở đi:** Xu hướng dịch chuyển từ "prompt đơn lẻ" sang **AI Agent** (AI tự lập kế hoạch và thực thi nhiều bước) và "context engineering" (thiết kế toàn bộ ngữ cảnh, dữ liệu, công cụ cấp cho AI). Kỹ năng viết prompt vẫn là lõi, nhưng mở rộng thành thiết kế hệ thống.

*(Mốc thời gian mang tính khái quát; một số chi tiết sản phẩm có thể thay đổi — cần kiểm chứng khi trích dẫn học thuật.)*

## 4. Tại sao quan trọng

Với marketer, prompt engineering không phải kỹ năng "hay thì có", mà là đòn bẩy năng suất trực tiếp:

1. **Tốc độ sản xuất nội dung:** Rút ngắn thời gian tạo bản nháp bài viết, email, kịch bản từ hàng giờ xuống vài phút.
2. **Chất lượng và nhất quán:** Prompt tốt giữ đúng giọng thương hiệu (brand voice), đúng định dạng, đúng thông điệp cốt lõi qua hàng trăm đầu ra.
3. **Mở rộng quy mô cá nhân hóa:** Cùng một khung prompt có thể sinh 50 biến thể quảng cáo cho 50 phân khúc khác nhau.
4. **Dân chủ hóa chuyên môn:** Một nhân viên mới có thể tạo ra kết quả gần với chuyên gia nếu dùng đúng prompt library của phòng.
5. **Giảm chi phí và rủi ro:** Prompt kém tạo ra đầu ra sai, phải sửa nhiều lần, tốn token và thời gian; tệ hơn là đăng nhầm thông tin sai gây khủng hoảng thương hiệu.

Nói ngắn gọn: AI là bộ khuếch đại. Prompt tốt khuếch đại năng lực; prompt tồi khuếch đại sai lầm.

## 5. Nguyên lý hoạt động

Để ra lệnh giỏi, cần hiểu (ở mức marketer) AI hoạt động ra sao:

- **AI dự đoán, không tra cứu.** Mặc định, LLM sinh văn bản dựa trên xác suất, không "tra" một cơ sở dữ liệu sự thật. Đây là lý do nó có thể bịa số liệu rất trơn tru.
- **Prompt định hình "vùng tìm kiếm".** Mỗi từ trong prompt là một tín hiệu thu hẹp khả năng. "Viết bài" cho vùng rất rộng; "Viết caption Facebook 3 câu, giọng hài hước, cho mẹ bỉm sữa 28–35 tuổi ở TP.HCM" thu hẹp mạnh về đúng đích.
- **Ngữ cảnh gần cuối được ưu tiên.** AI thường bám sát chỉ dẫn đặt gần cuối prompt và các ví dụ bạn cung cấp.
- **Vai trò (role) kích hoạt phong cách.** Khi bạn nói "Bạn là copywriter 10 năm kinh nghiệm mảng mỹ phẩm", AI dịch chuyển sang vùng ngôn ngữ đặc trưng của vai trò đó.
- **Không có trí nhớ dài hạn mặc định.** Ngoài context window của phiên, AI không tự nhớ dự án của bạn. Muốn nhất quán, phải nạp lại ngữ cảnh (hoặc dùng công cụ có bộ nhớ/tài liệu như NotebookLM).
- **Có giới hạn dữ liệu và thời điểm.** Model có "ngày cắt kiến thức"; thông tin mới hơn có thể sai hoặc thiếu, trừ khi model được kết nối tìm kiếm trực tuyến.

Hiểu sáu điểm này giúp bạn không "thần thánh hóa" cũng không xem thường AI, mà điều khiển nó như một cộng sự có điểm mạnh và điểm mù rõ ràng.

## 6. Mô hình

Mô hình tư duy nền tảng của một prompt tốt gồm **6 thành phần**, viết tắt dễ nhớ theo tiếng Việt: **V–N–N–R–V–Đ**.

| Thành phần | Vai trò | Câu hỏi cần trả lời |
|---|---|---|
| **Vai trò (Role)** | Đặt AI vào đúng "tư cách" chuyên môn | AI đang đóng vai ai? |
| **Ngữ cảnh (Context)** | Cung cấp bối cảnh, sản phẩm, đối tượng | AI cần biết gì để làm đúng? |
| **Nhiệm vụ (Task)** | Nêu rõ việc cần làm | AI phải tạo ra cái gì? |
| **Ràng buộc (Constraints)** | Giới hạn: độ dài, giọng điệu, điều cấm | Đâu là biên không được vượt? |
| **Ví dụ (Examples)** | Mẫu tham chiếu để bắt chước | "Tốt" trông như thế nào? |
| **Định dạng đầu ra (Format)** | Cấu trúc kết quả | Trả về dạng gì (bảng, danh sách, JSON...)? |

Không phải prompt nào cũng cần đủ 6 thành phần. Việc đơn giản có thể chỉ cần Nhiệm vụ + Định dạng. Nhưng với công việc marketing quan trọng, càng đầy đủ càng ổn định.

## 7. Framework

Ba framework tư duy nên thuộc lòng:

**Framework A — RTF (Role – Task – Format):** Dành cho việc nhanh.
> "Bạn là chuyên gia SEO. Viết 10 tiêu đề bài blog về kem chống nắng cho da dầu. Trình bày dạng danh sách đánh số."

**Framework B — CO-STAR:** Chuẩn cho nội dung marketing bài bản.
- **C**ontext (Ngữ cảnh)
- **O**bjective (Mục tiêu)
- **S**tyle (Phong cách)
- **T**one (Giọng điệu)
- **A**udience (Đối tượng)
- **R**esponse format (Định dạng phản hồi)

**Framework C — Vòng lặp tinh chỉnh (Iterative Loop):** Prompt hiếm khi hoàn hảo ngay lần đầu.
> Prompt → Đánh giá đầu ra → Chỉ ra điểm chưa đạt → Yêu cầu sửa cụ thể → Lặp lại.

Ba framework này bổ trợ nhau: RTF để phác nhanh, CO-STAR để làm chuẩn, Vòng lặp để hoàn thiện.

## 8. Công thức

Công thức khung prompt chuẩn cho marketer (có thể copy và điền vào):

```
[VAI TRÒ] Bạn là {chuyên gia/vai trò cụ thể + số năm kinh nghiệm + lĩnh vực}.

[NGỮ CẢNH] Bối cảnh: {sản phẩm/dịch vụ}. Khách hàng mục tiêu: {chân dung}.
Vấn đề họ gặp: {nỗi đau}. Điểm khác biệt của sản phẩm: {USP}.

[NHIỆM VỤ] Hãy {động từ hành động rõ ràng + sản phẩm đầu ra cụ thể}.

[RÀNG BUỘC] Yêu cầu: độ dài {…}; giọng điệu {…}; ngôn ngữ tiếng Việt tự nhiên;
KHÔNG {điều cấm: sáo rỗng/cường điệu/vi phạm quy định quảng cáo}.

[VÍ DỤ] Tham khảo phong cách mẫu sau: "{dán 1–3 ví dụ đạt chuẩn}".

[ĐỊNH DẠNG] Trả về dưới dạng {bảng/danh sách/đoạn văn/khung có tiêu đề}.
```

Ba biến thể kỹ thuật quan trọng cần kết hợp vào công thức trên:

- **Zero-shot:** Không đưa ví dụ, chỉ mô tả nhiệm vụ. Nhanh nhưng kém ổn định với việc khó.
- **Few-shot:** Đưa 2–5 ví dụ mẫu để AI bắt chước phong cách/định dạng. Tăng độ chính xác rõ rệt cho việc cần nhất quán.
- **Chain-of-thought (CoT):** Thêm câu "Hãy suy nghĩ và phân tích từng bước trước khi đưa kết luận". Hữu ích cho phân tích dữ liệu, chọn chiến lược, lập luận — không cần thiết cho việc sáng tạo ngắn.

## 9. Quy trình

Quy trình 7 bước áp dụng cho mọi tác vụ prompt trong marketing:

1. **Xác định mục tiêu đầu ra:** Bạn cần chính xác cái gì? (VD: 5 caption, 1 báo cáo phân tích, 20 ý tưởng.)
2. **Chọn công cụ/model phù hợp:** Việc cần trích nguồn → Perplexity; việc trên tài liệu riêng → NotebookLM; việc viết dài, lập luận → Claude/GPT/Gemini (xem Mục 19 & bảng so sánh).
3. **Soạn prompt theo khung V–N–N–R–V–Đ.**
4. **Chạy thử và đọc kỹ đầu ra** — không copy mù.
5. **Đánh giá theo tiêu chí:** Đúng ý? Đúng giọng? Có bịa? Có vi phạm?
6. **Tinh chỉnh (iterate):** Nêu cụ thể điểm sửa, chạy lại. Lưu prompt tốt lại.
7. **Kiểm chứng & biên tập cuối:** Đối chiếu sự thật, thêm chất người, phê duyệt trước khi dùng.

Bước 7 không bao giờ được bỏ. AI tạo bản nháp; con người chịu trách nhiệm cuối cùng.

## 10. Ví dụ đơn giản

**Prompt tồi (zero-context):**
> "Viết quảng cáo cho serum của tôi."

Kết quả: chung chung, sáo rỗng, không dùng được.

**Prompt tốt (đủ khung):**
> "Bạn là copywriter mảng mỹ phẩm 8 năm kinh nghiệm. Sản phẩm: serum vitamin C 15% cho da xỉn màu. Khách hàng: nữ 25–35 tuổi, dân văn phòng, da mệt mỏi vì thức khuya. USP: thẩm thấu nhanh, không nhờn rít. Hãy viết 3 caption Facebook, mỗi caption tối đa 4 dòng, giọng thân thiện gần gũi, có 1 câu hook mở đầu và 1 CTA. KHÔNG dùng từ 'thần dược', 'số 1', hay cam kết chữa bệnh. Trình bày mỗi caption cách nhau bằng gạch ngang."

Sự khác biệt: prompt thứ hai cho AI đủ vai trò, ngữ cảnh, ràng buộc pháp lý và định dạng — kết quả gần như dùng được ngay sau biên tập nhẹ.

## 11. Ví dụ doanh nghiệp

Bối cảnh: một thương hiệu mỹ phẩm nội địa (SME) cần sản xuất nội dung đều đặn cho 4 kênh. Họ xây một prompt "xưởng nội dung" tái sử dụng:

```
[VAI TRÒ] Bạn là Content Lead của thương hiệu mỹ phẩm sạch "ABC".
[NGỮ CẢNH] Brand voice: ấm áp, trung thực, không hù dọa. Đối tượng: nữ 25–40,
quan tâm thành phần lành tính. Đọc kỹ tài liệu brand guideline đính kèm trước khi viết.
[NHIỆM VỤ] Từ 1 thông điệp gốc tôi cung cấp, hãy chuyển thể thành:
  1) 1 bài Facebook (150–200 từ)
  2) 3 caption Instagram (kèm 5 hashtag mỗi bài)
  3) 1 kịch bản TikTok 30 giây (chia cảnh + lời thoại)
  4) 1 email ngắn (tiêu đề + thân bài 120 từ)
[RÀNG BUỘC] Giữ nhất quán thông điệp gốc; tuân thủ quy định quảng cáo mỹ phẩm
(không cam kết chữa bệnh, không so sánh hạ thấp đối thủ). Tiếng Việt tự nhiên.
[ĐỊNH DẠNG] Trình bày theo 4 mục có tiêu đề rõ ràng.

Thông điệp gốc: "{điền vào đây}"
```

Giá trị doanh nghiệp: một prompt chuẩn hóa cho phép nhân viên bất kỳ tạo ra bộ nội dung 4 kênh nhất quán chỉ trong vài phút, thay vì bốn người làm rời rạc. Đây chính là hạt nhân của một **prompt library** (xem Mục 18).

## 12. Ví dụ Việt Nam

Đặc thù thị trường Việt Nam đòi hỏi prompt phải "nội địa hóa" — nếu không, AI dễ cho ra văn phong dịch máy, cứng và Tây hóa.

**Prompt tối ưu cho ngữ cảnh Việt:**
> "Bạn là người viết content bản địa Việt Nam. Viết caption cho chương trình sale 'Mua 1 tặng 1' dịp Tết. Giọng điệu vui tươi, đời thường, dùng cách nói tự nhiên của người Việt (tránh văn dịch, tránh từ Hán-Việt nặng nề). Đối tượng: các bạn nữ Gen Z ở Hà Nội và TP.HCM. Chèn hợp lý 1–2 từ ngữ đang thịnh hành nhưng không lạm dụng. Độ dài 3–4 dòng, có emoji vừa phải, kết bằng CTA dẫn về Zalo OA."

Lưu ý thực chiến cho thị trường Việt:
- Yêu cầu AI tránh "văn dịch máy" một cách tường minh — đây là lỗi phổ biến nhất.
- Nêu rõ nền tảng bản địa (Zalo, TikTok Shop, Shopee Live) vì AI mặc định nghiêng về nền tảng phương Tây.
- Với slang/trend, tự cung cấp từ khóa hiện hành thay vì để AI đoán, vì kiến thức model có độ trễ thời gian *(cần kiểm chứng độ mới)*.
- Luôn rà lại yếu tố văn hóa, vùng miền và quy định quảng cáo trong nước.

## 13. Ví dụ quốc tế

Khi làm nội dung cho thị trường nước ngoài, prompt cần khai báo rõ thị trường, ngôn ngữ và chuẩn văn hóa:

> "You are a senior copywriter for the US market. Product: a Vietnamese-origin natural skincare serum entering Amazon US. Target: women 25–40, ingredient-conscious, value transparency. Write a product description of ~200 words. Tone: confident but not exaggerated; comply with US cosmetic advertising norms (no disease-treatment claims). Avoid clichés. Format: 1 headline + 3 short benefit bullets + 1 closing line."

Bài học chuyển ngữ:
- **Không dịch prompt Việt sang tiếng Anh rồi mong kết quả bản địa.** Hãy prompt trực tiếp bằng ngôn ngữ và tư duy của thị trường đích.
- Khai báo chuẩn pháp lý địa phương (FDA/FTC ở Mỹ, GDPR khi liên quan dữ liệu ở EU...) — dù vẫn phải để bộ phận pháp lý kiểm tra lại, đây không phải tư vấn pháp lý.
- Yêu cầu AI nêu giả định về khác biệt văn hóa nếu có, để bạn kiểm soát.

## 14. Sai lầm thường gặp

| Sai lầm | Hệ quả | Cách khắc phục |
|---|---|---|
| Prompt quá mơ hồ ("viết hay vào") | Đầu ra chung chung | Thêm vai trò, ngữ cảnh, ràng buộc cụ thể |
| Nhồi quá nhiều nhiệm vụ trong 1 prompt | AI làm hời hợt, bỏ sót | Tách thành các bước tuần tự |
| Không nêu định dạng đầu ra | Kết quả khó dùng lại | Luôn khai báo format |
| Tin tuyệt đối số liệu AI đưa ra | Đăng thông tin sai, rủi ro pháp lý | Bắt buộc kiểm chứng nguồn |
| Không đưa ví dụ khi cần nhất quán | Giọng điệu trôi dạt | Dùng few-shot |
| Copy nguyên đầu ra, không biên tập | Nội dung "nhạt AI", thiếu chất người | Luôn có bước edit của người |
| Dùng sai model cho việc | Tốn thời gian, kết quả kém | Chọn model theo tác vụ (Mục 19) |
| Bỏ ràng buộc pháp lý/quảng cáo | Vi phạm quy định, gỡ bài, phạt | Ghi rõ điều cấm trong prompt |
| Dán dữ liệu nhạy cảm của khách vào AI công cộng | Rò rỉ dữ liệu, vi phạm bảo mật | Ẩn danh dữ liệu, dùng công cụ có cam kết bảo mật |

## 15. Checklist

Checklist trước khi bấm "gửi" một prompt quan trọng:

- [ ] Đã nêu **vai trò** cho AI chưa?
- [ ] Đã cung cấp đủ **ngữ cảnh** (sản phẩm, đối tượng, USP)?
- [ ] **Nhiệm vụ** đã rõ ràng, một mục tiêu chính?
- [ ] Đã đặt **ràng buộc** (độ dài, giọng, điều cấm)?
- [ ] Có cần **ví dụ** (few-shot) để đảm bảo nhất quán không?
- [ ] Đã chỉ định **định dạng đầu ra** chưa?
- [ ] Đã chọn **đúng model/công cụ** cho tác vụ này?
- [ ] Đã ghi rõ **yêu cầu pháp lý/thương hiệu**?
- [ ] Không dán **dữ liệu nhạy cảm** trái phép?
- [ ] Đã lên kế hoạch **kiểm chứng** đầu ra?

Checklist sau khi nhận đầu ra:

- [ ] Có thông tin nào **cần verify** (số liệu, tên, ngày, dẫn chứng)?
- [ ] Giọng điệu có **đúng brand voice**?
- [ ] Có yếu tố **sáo rỗng/lỗi văn dịch** cần sửa?
- [ ] Đã thêm **chất người** và bối cảnh riêng?
- [ ] Đã **lưu prompt tốt** vào thư viện?

## 16. SOP

**SOP: Quy trình chuẩn tạo nội dung marketing bằng AI (áp dụng cấp phòng)**

1. **Tiếp nhận yêu cầu:** Ghi rõ loại nội dung, kênh, mục tiêu, deadline.
2. **Chọn prompt mẫu** từ Prompt Library của phòng (nếu chưa có, chuyển bước 3, sau đó bổ sung vào library).
3. **Điền biến ngữ cảnh** (sản phẩm, đối tượng, USP, chương trình).
4. **Chọn model** theo bảng phân công tác vụ.
5. **Chạy prompt, đọc và đánh giá** theo tiêu chí chuẩn (đúng ý/đúng giọng/không bịa/tuân thủ).
6. **Tinh chỉnh tối đa 2–3 vòng.** Nếu vẫn lệch, đổi cách tiếp cận hoặc model.
7. **Kiểm chứng dữ kiện** với nguồn đáng tin (không dựa vào AI để tự xác minh).
8. **Biên tập bởi người**, thêm bản sắc thương hiệu.
9. **Phê duyệt** theo phân cấp (người viết → trưởng nhóm → pháp lý nếu cần).
10. **Xuất bản & ghi log:** Lưu lại prompt cuối, model, người duyệt để truy vết.
11. **Cập nhật Prompt Library** nếu tạo ra prompt tốt mới.

## 17. KPI

Đo lường hiệu quả prompt engineering ở cả cấp cá nhân và phòng ban:

| Nhóm KPI | Chỉ số gợi ý | Ý nghĩa |
|---|---|---|
| **Năng suất** | Thời gian trung bình tạo 1 đơn vị nội dung; số nội dung/tuần | AI có thực sự tăng tốc? |
| **Chất lượng** | Số vòng chỉnh sửa trung bình; tỷ lệ đầu ra dùng được sau lần chạy đầu | Prompt có tốt lên không? |
| **Độ chính xác** | Số lỗi/bịa phát hiện khi kiểm chứng; số sự cố đăng nhầm | Rủi ro hallucination được kiểm soát? |
| **Hiệu quả marketing** | So sánh chỉ số hiệu suất (tương tác, chuyển đổi) giữa nội dung hỗ trợ-AI và nội dung thường | AI có tác động kết quả kinh doanh? |
| **Tài sản tri thức** | Số prompt trong library; tỷ lệ tái sử dụng | Kiến thức có được tích lũy? |

Lưu ý: KPI năng suất phải luôn đi cùng KPI chất lượng và độ chính xác — nhanh mà sai là phản tác dụng. Các con số ngưỡng cụ thể (VD "giảm 50% thời gian") tùy tổ chức tự thiết lập baseline, *không nên copy con số từ nơi khác*.

## 18. Biểu mẫu

**Biểu mẫu A — Thẻ Prompt trong Prompt Library:**

| Trường | Nội dung |
|---|---|
| Mã prompt | VD: CONTENT-FB-001 |
| Tên | Caption Facebook bán hàng |
| Mục đích sử dụng | Tạo caption FB cho chương trình khuyến mãi |
| Model khuyến nghị | (điền) |
| Nội dung prompt | (khung đầy đủ, có biến {…}) |
| Biến cần điền | {sản phẩm}, {USP}, {đối tượng}, {CTA} |
| Ví dụ đầu ra tốt | (dán mẫu) |
| Lưu ý/ràng buộc | Không dùng từ cấm; tuân thủ quảng cáo |
| Người tạo / cập nhật | (tên, ngày) |

**Biểu mẫu B — Nhật ký kiểm chứng đầu ra:**

| Nội dung | Thông tin cần verify | Nguồn kiểm chứng | Kết quả (Đúng/Sai/Sửa) | Người kiểm |
|---|---|---|---|---|
| | | | | |

## 19. Prompt AI (Meta-Prompt)

> **Lưu ý:** Mục này là các **META-PROMPT** — prompt dùng để *tạo ra prompt*. Bạn đưa meta-prompt vào AI, mô tả việc cần làm, AI sẽ soạn giúp bạn một prompt hoàn chỉnh. Đây là kỹ thuật "dùng AI để nâng cấp cách ra lệnh cho AI".

**ChatGPT (OpenAI) — Meta-prompt tạo prompt marketing:**
> "Bạn là chuyên gia prompt engineering cho marketing. Tôi cần một prompt để {mô tả tác vụ, VD: viết email chăm sóc khách hàng cũ}. Hãy hỏi tôi tối đa 5 câu để làm rõ ngữ cảnh còn thiếu, sau đó soạn cho tôi một prompt hoàn chỉnh theo cấu trúc Vai trò – Ngữ cảnh – Nhiệm vụ – Ràng buộc – Ví dụ – Định dạng. Cuối cùng, giải thích ngắn gọn vì sao bạn thiết kế như vậy."

**Claude (Anthropic) — Meta-prompt tinh chỉnh và phản biện prompt:**
> "Đây là prompt hiện tại của tôi: '{dán prompt}'. Với vai trò một reviewer khó tính, hãy: (1) chỉ ra các điểm mơ hồ hoặc thiếu ràng buộc có thể khiến đầu ra sai lệch; (2) viết lại prompt thành phiên bản rõ ràng, đầy đủ hơn; (3) đề xuất 2 biến thể — một thiên về an toàn/nhất quán, một thiên về sáng tạo. Suy nghĩ từng bước trước khi trả lời."

**Gemini (Google) — Meta-prompt tạo bộ prompt đa kênh:**
> "Hãy đóng vai Content Strategist. Từ một chiến dịch marketing mà tôi mô tả dưới đây, hãy tạo cho tôi một BỘ prompt riêng cho từng kênh (Facebook, Instagram, TikTok, Email, Google Ads). Mỗi prompt phải đầy đủ vai trò, ngữ cảnh, ràng buộc và định dạng để tôi dùng lại độc lập. Chiến dịch: {mô tả}."

**Perplexity — Meta-prompt cho prompt nghiên cứu có trích nguồn:**
> "Tôi cần nghiên cứu {chủ đề, VD: xu hướng tiêu dùng mỹ phẩm thuần chay tại Đông Nam Á}. Hãy soạn giúp tôi một prompt nghiên cứu tối ưu để dùng trên công cụ tìm kiếm AI: yêu cầu trả lời phải kèm nguồn trích dẫn, ưu tiên nguồn cập nhật, và tách rõ đâu là dữ kiện có nguồn đâu là suy luận. Sau đó thực thi luôn prompt đó và trả về kết quả kèm link nguồn."

**NotebookLM — Meta-prompt làm việc trên tài liệu riêng:**
> "Tôi sẽ nạp vào đây các tài liệu nội bộ (brand guideline, báo cáo thị trường, phản hồi khách hàng). Hãy gợi ý cho tôi một danh sách 10 câu prompt hiệu quả để khai thác đúng các tài liệu NÀY phục vụ việc lập kế hoạch nội dung — mỗi prompt chỉ dựa trên nội dung tài liệu đã nạp, không bịa thông tin ngoài."

**AI Agent — Meta-prompt cho tác vụ nhiều bước:**
> "Bạn là một AI agent marketing. Mục tiêu của tôi: {VD: chuẩn bị ra mắt sản phẩm mới}. Hãy (1) tự lập kế hoạch các bước cần làm (nghiên cứu đối thủ → xác định thông điệp → lên lịch nội dung → soạn nháp); (2) với mỗi bước, nêu rõ bạn cần dữ liệu/công cụ gì từ tôi; (3) thực hiện lần lượt, dừng lại xin xác nhận ở các điểm quyết định quan trọng thay vì tự ý làm hết. Không bịa dữ liệu — chỗ nào cần dữ kiện thật, hãy đánh dấu để tôi cung cấp."

## 20. Bài tập

1. **Nâng cấp prompt:** Lấy một prompt mơ hồ của chính bạn ("viết bài giới thiệu sản phẩm") và viết lại theo đủ khung V–N–N–R–V–Đ. So sánh hai đầu ra.
2. **Few-shot:** Chọn 3 caption cũ đạt chuẩn brand voice, đưa làm ví dụ, yêu cầu AI viết 5 caption mới cùng phong cách. Đánh giá độ khớp.
3. **Chain-of-thought:** Đưa cho AI một bảng số liệu quảng cáo giả định và yêu cầu phân tích "từng bước" để đề xuất tối ưu ngân sách. Nhận xét chất lượng lập luận.
4. **Meta-prompt:** Dùng meta-prompt Claude ở Mục 19 để phản biện một prompt bạn đang dùng thật.
5. **So sánh model:** Chạy cùng một prompt nghiên cứu trên hai công cụ khác nhau (một công cụ có trích nguồn, một không). Ghi lại khác biệt về độ tin cậy.
6. **Săn hallucination:** Cố tình hỏi AI một số liệu thị trường cụ thể, rồi đi kiểm chứng. Ghi lại kết quả vào Biểu mẫu B.
7. **Xây library:** Tạo 5 thẻ prompt (Biểu mẫu A) cho 5 tác vụ bạn làm thường xuyên nhất.

## 21. Câu hỏi ôn tập

1. Sáu thành phần của một prompt tốt là gì? Cái nào có thể lược bỏ với việc đơn giản?
2. Phân biệt zero-shot, few-shot và chain-of-thought. Mỗi kỹ thuật hợp với loại tác vụ nào?
3. Vì sao AI có thể "bịa" số liệu một cách thuyết phục, và điều đó xuất phát từ nguyên lý hoạt động nào?
4. Khi nào nên chọn công cụ tìm kiếm có trích nguồn thay vì một LLM hội thoại thông thường?
5. Role prompting tác động thế nào đến đầu ra? Cho một ví dụ marketing.
6. Kể ba lỗi phổ biến khi viết prompt và cách khắc phục.
7. Vì sao bước "kiểm chứng và biên tập bởi người" không được bỏ, kể cả khi AI cho đầu ra mượt?
8. Prompt Library mang lại giá trị gì cho một phòng marketing?
9. Những rủi ro đạo đức và bản quyền nào cần lưu ý khi dùng AI tạo nội dung?
10. Vì sao không nên dán dữ liệu khách hàng nhạy cảm vào công cụ AI công cộng?

## 22. Case Study

**Case thành công (mô hình hóa — minh họa phương pháp):**
Một SME mỹ phẩm Việt xây dựng Prompt Library gồm ~20 thẻ prompt chuẩn cho các tác vụ lặp lại (caption, email, kịch bản video, mô tả sản phẩm), kèm SOP kiểm chứng bắt buộc. Kết quả quan sát được: thời gian tạo nội dung giảm mạnh, nội dung nhất quán giọng thương hiệu hơn giữa các nhân viên, nhân sự mới hòa nhập nhanh vì "kế thừa" được cách ra lệnh của người giỏi. Yếu tố quyết định thành công: (1) chuẩn hóa prompt, không phụ thuộc cảm hứng cá nhân; (2) luôn có bước người biên tập; (3) đo lường và cải tiến prompt theo thời gian. *(Đây là mô hình điển hình để học phương pháp, không phải case định danh; các con số cụ thể cần tổ chức tự đo.)*

**Case thất bại (bài học cảnh báo):**
Nhiều tổ chức trên thế giới đã gặp sự cố khi dùng AI mà bỏ khâu kiểm chứng: chatbot hoặc nội dung tự động đưa ra thông tin sai (giá sai, chính sách sai, dẫn chứng bịa) và bị lan truyền, gây thiệt hại uy tín, thậm chí tranh chấp. Nguyên nhân gốc luôn giống nhau: **tin AI như một nguồn sự thật, prompt thiếu ràng buộc, và không có người kiểm duyệt cuối.** Bài học: AI càng nói mượt càng nguy hiểm nếu không verify; một prompt tốt phải kèm quy trình kiểm chứng, nếu không chính sự trôi chảy của AI sẽ trở thành rủi ro. *(Các sự cố dạng này có thật và được đưa tin rộng rãi giai đoạn 2023–2025; chi tiết từng vụ việc cần kiểm chứng nguồn trước khi trích dẫn đích danh.)*

## 23. Tổng kết

Prompt Engineering không phải "mẹo bấm nút" mà là một kỹ năng tư duy: diễn đạt rõ ràng, cung cấp đúng ngữ cảnh, đặt ràng buộc hợp lý và kiểm soát đầu ra. Với marketer giai đoạn 2026–2035, đây là năng lực bản lề quyết định năng suất và chất lượng.

Năm điều cần khắc cốt:
1. **Cấu trúc thắng ngẫu hứng** — dùng khung V–N–N–R–V–Đ.
2. **Kỹ thuật đúng cho tác vụ** — few-shot cho nhất quán, chain-of-thought cho lập luận, role prompting cho phong cách.
3. **Chọn đúng công cụ** — mỗi model có thế mạnh riêng; việc cần nguồn thì dùng công cụ có trích dẫn.
4. **Người luôn ở khâu cuối** — AI tạo nháp, con người chịu trách nhiệm, kiểm chứng và giữ đạo đức/bản quyền.
5. **Tích lũy tài sản** — biến prompt tốt thành Library dùng chung cho cả phòng.

AI là bộ khuếch đại. Ra lệnh giỏi, bạn khuếch đại chuyên môn. Ra lệnh cẩu thả, bạn khuếch đại rủi ro. Kỹ năng này, cuối cùng, là kỹ năng tư duy rõ ràng — thứ marketer giỏi vốn đã cần.

## 24. Nguồn tham khảo

> **Lưu ý minh bạch:** Phần này liệt kê loại nguồn nên tra cứu, KHÔNG bịa link cụ thể. Người học nên tự truy cập trang chính thức để lấy tài liệu mới nhất.

- Tài liệu hướng dẫn prompt chính thức từ nhà phát triển model: OpenAI, Anthropic (Claude), Google (Gemini) — trang tài liệu/help center chính thức.
- Bài báo nền tảng học thuật: "Attention Is All You Need" (2017); các nghiên cứu về few-shot learning và chain-of-thought prompting (2020–2022) — *tra cứu qua Google Scholar / arXiv, cần kiểm chứng bản gốc*.
- Tài liệu công cụ: trang chính thức của Perplexity, NotebookLM về cách đặt câu hỏi hiệu quả.
- Quy định quảng cáo tại Việt Nam: các văn bản pháp luật về quảng cáo, đặc biệt với ngành mỹ phẩm/thực phẩm chức năng — *tham chiếu nguồn pháp lý chính thống, không dựa vào AI*.
- Sách/khóa học về prompt engineering và AI marketing từ các nền tảng học tập uy tín — *đánh giá độ cập nhật trước khi dùng vì lĩnh vực thay đổi nhanh*.

## Cần cập nhật trong tương lai

Lĩnh vực AI thay đổi theo tháng, không theo năm. Các nội dung sau cần rà soát định kỳ (đề xuất mỗi quý):

- **Tên và phiên bản model:** ChatGPT/GPT, Claude, Gemini, Perplexity, NotebookLM liên tục ra bản mới với năng lực khác nhau. Bảng so sánh "khi nào dùng model nào" cần cập nhật theo phiên bản hiện hành.
- **Kích thước context window & khả năng đa phương thức:** Đang tăng nhanh (văn bản, hình ảnh, âm thanh, video); ảnh hưởng trực tiếp đến cách thiết kế prompt.
- **Dịch chuyển từ prompt sang AI Agent & context engineering:** Xu hướng AI tự lập kế hoạch/thực thi nhiều bước sẽ làm thay đổi trọng tâm kỹ năng — cần bổ sung chương/mục chuyên sâu.
- **Giá và giới hạn sử dụng (token, gói cước):** Biến động thường xuyên; không nên chốt con số cứng trong giáo trình.
- **Khả năng kết nối dữ liệu thời gian thực & công cụ:** Việc model tự tra cứu web, gọi công cụ, dùng bộ nhớ dài hạn sẽ thay đổi cách kiểm soát hallucination.
- **Khung pháp lý về AI, bản quyền và dữ liệu:** Quy định về nội dung do AI tạo, ghi nhãn AI, bản quyền và bảo vệ dữ liệu (trong nước và quốc tế) đang hình thành — cần theo dõi sát.
- **Tiêu chuẩn ghi nhãn nội dung AI:** Yêu cầu công khai "nội dung có sự hỗ trợ của AI" có thể trở thành bắt buộc trên một số nền tảng/thị trường.
- **Số liệu và case study:** Các con số hiệu suất, KPI tham chiếu và case study cần được thay bằng dữ liệu thực, có kiểm chứng, thay cho các minh họa mô hình hóa trong bản này.

---

*Kết thúc Tập 8 · Chương 2. Chương tiếp theo đề xuất: "AI Agent cho Marketing — Tự động hóa quy trình nhiều bước".*

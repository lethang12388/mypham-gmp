# Tập 7 · Chương 4 — Attribution & Đo lường thời hậu-cookie

> **Metadata**
> - **Bộ giáo trình:** MARKETING THỰC CHIẾN 2026–2035
> - **Tập:** 7 — Growth & Performance Marketing
> - **Chương:** 4 — Attribution & Đo lường thời hậu-cookie
> - **Cấp độ:** Trung cấp → Nâng cao
> - **Đối tượng:** Performance marketer, growth lead, data analyst, giám đốc marketing
> - **Thời lượng học gợi ý:** 6–8 giờ (lý thuyết + thực hành)
> - **Phiên bản:** 1.0 · Cập nhật lần cuối: 2026-07
> - **Cảnh báo:** Lĩnh vực privacy & attribution thay đổi rất nhanh. Mọi số liệu trong chương đều được đánh dấu "(số minh họa)" hoặc "(cần kiểm chứng)". Hãy đọc kèm mục 24 và "Cần cập nhật trong tương lai".

**Tóm tắt một câu:** Attribution là nghệ thuật — không phải khoa học chính xác — phân bổ công lao chuyển đổi cho các điểm chạm marketing, và trong thời hậu-cookie, không tồn tại mô hình hoàn hảo, chỉ có bộ phương pháp bổ trợ (MTA + MMM + incrementality) giúp ra quyết định phân bổ ngân sách tốt hơn.

---

## 1. Giới thiệu

Hãy tưởng tượng bạn là giám đốc marketing một thương hiệu mỹ phẩm Việt Nam. Tháng vừa rồi bạn chi tiền cho Facebook Ads, TikTok, Google Search, KOL review, email và một chiến dịch billboard. Doanh thu tăng 30%. Câu hỏi triệu đô: **kênh nào thực sự tạo ra tăng trưởng đó?** Nếu bạn cắt Facebook, doanh thu có sụt không? Nếu tăng gấp đôi ngân sách TikTok, có tăng gấp đôi đơn không?

Đây chính là bài toán **attribution** (phân bổ đóng góp) — và là một trong những bài toán khó nhất, gây tranh cãi nhất, tốn ngân sách sai lầm nhất trong marketing hiện đại.

Trước 2020, câu trả lời tương đối dễ: gắn cookie theo dõi người dùng xuyên suốt hành trình, xem điểm chạm cuối cùng trước khi mua, gán công cho nó. Nhưng từ 2021 trở đi, thế giới đo lường bị đảo lộn bởi ba lực: Apple ATT (App Tracking Transparency), việc trình duyệt khai tử third-party cookie, và làn sóng luật bảo vệ dữ liệu (GDPR, và tại Việt Nam là **Nghị định 13/2023/NĐ-CP** về bảo vệ dữ liệu cá nhân).

Chương này trang bị cho bạn tư duy và bộ công cụ để đo lường marketing một cách trung thực trong thời đại mà **dữ liệu ngày càng mờ, người tiêu dùng ngày càng ẩn danh**.

## 2. Khái niệm

**Attribution** (phân bổ đóng góp/quy công) là quá trình xác định và gán "công lao" (credit) cho các điểm chạm marketing (touchpoints) đã góp phần dẫn đến một hành động chuyển đổi mong muốn (mua hàng, đăng ký, cài app).

Các thuật ngữ cốt lõi:

- **Touchpoint (điểm chạm):** mỗi lần khách hàng tương tác với thương hiệu (click ad, xem video, mở email, ghé web).
- **Conversion path (hành trình chuyển đổi):** chuỗi các điểm chạm theo thứ tự thời gian dẫn đến chuyển đổi.
- **Attribution model (mô hình phân bổ):** quy tắc quyết định điểm chạm nào nhận bao nhiêu phần trăm công.
- **Multi-Touch Attribution (MTA):** phương pháp gán công cho nhiều điểm chạm dựa trên dữ liệu cấp cá nhân (user-level).
- **Media Mix Modeling / Marketing Mix Modeling (MMM):** mô hình thống kê hồi quy dùng dữ liệu tổng hợp (aggregate) để ước lượng đóng góp của từng kênh.
- **Incrementality (tính gia tăng):** phần chuyển đổi *tăng thêm* thực sự nhờ marketing, so với kịch bản không chạy marketing.
- **Post-cookie (hậu-cookie):** giai đoạn khi third-party cookie và định danh xuyên trang bị hạn chế/loại bỏ.

## 3. Lịch sử hình thành

- **Thập niên 1960–1990 — MMM ra đời:** Các tập đoàn FMCG (Procter & Gamble, Unilever) dùng hồi quy kinh tế lượng để đo hiệu quả TV, báo, radio khi chưa có internet. MMM là "ông tổ" của đo lường marketing (cần kiểm chứng chi tiết mốc thời gian).
- **1993 — Cookie ra đời:** Lou Montulli (Netscape) phát minh HTTP cookie, mở đường cho theo dõi người dùng trên web.
- **2000s — Kỷ nguyên last-click:** Google Analytics (ra mắt 2005) phổ cập mô hình last-click, biến nó thành "tiêu chuẩn mặc định" toàn ngành.
- **2010s — MTA lên ngôi:** Các nền tảng như Google Attribution, Adobe, các DMP hứa hẹn theo dõi hành trình đa chạm cấp cá nhân nhờ cookie và mobile ID.
- **2018 — GDPR có hiệu lực** tại EU, siết consent.
- **2021 — Apple iOS 14.5 / ATT:** buộc app xin phép trước khi theo dõi; tỷ lệ opt-in thấp làm sụp đổ nhiều mô hình MTA trên mobile.
- **2022–2024 — Google Consent Mode & lộ trình khai tử third-party cookie trên Chrome** (nhiều lần trì hoãn; năm 2024 Google tuyên bố đổi hướng sang cơ chế lựa chọn cho người dùng thay vì bỏ hẳn — cần kiểm chứng trạng thái mới nhất).
- **2023 — Việt Nam ban hành Nghị định 13/2023/NĐ-CP** về bảo vệ dữ liệu cá nhân, hiệu lực từ 01/07/2023.
- **2023–2026 — MMM & incrementality hồi sinh:** Ngành quay lại các phương pháp không phụ thuộc định danh cá nhân; Google phát hành Meridian, Meta phát hành Robyn (thư viện MMM mã nguồn mở).

## 4. Tại sao quan trọng

1. **Phân bổ ngân sách đúng:** Attribution quyết định bạn đổ tiền vào đâu. Sai attribution → dồn tiền vào kênh "ăn công" (như last-click ưu ái Search thương hiệu) và cắt oan kênh tạo nhu cầu (như TikTok, KOL).
2. **Định giá hiệu quả (ROAS/CAC):** Không đo đúng đóng góp thì mọi chỉ số ROAS đều méo.
3. **Bảo vệ ngân sách trước CFO:** Khi bị hỏi "cắt marketing thì sao?", chỉ incrementality mới trả lời trung thực.
4. **Tuân thủ pháp luật:** Đo lường sai cách (thu thập dữ liệu không consent) là rủi ro pháp lý dưới Nghị định 13 và GDPR.
5. **Sinh tồn hậu-cookie:** Đội nào vẫn bám last-click cookie sẽ "mù dần" khi tín hiệu biến mất.

## 5. Nguyên lý hoạt động

Attribution hoạt động qua bốn lớp:

1. **Thu thập tín hiệu (signal collection):** ghi nhận điểm chạm bằng cookie/pixel, tham số UTM, mobile ID, hoặc dữ liệu server-side (first-party).
2. **Ghép nối danh tính (identity resolution):** nối các điểm chạm rời rạc về cùng một người/hộ. Đây là lớp bị hậu-cookie phá vỡ mạnh nhất.
3. **Áp mô hình phân bổ (credit assignment):** áp quy tắc (heuristic như last-click) hoặc mô hình học máy (data-driven) để chia công.
4. **Suy luận & ra quyết định (inference):** dịch kết quả thành hành động phân bổ ngân sách.

Điểm mấu chốt: **MTA đo "đường đi" (path-based, bottom-up)**, còn **MMM đo "mối tương quan tổng thể" (correlation-based, top-down)**, còn **incrementality đo "quan hệ nhân quả" (causal) bằng thực nghiệm**. Ba lớp trả lời ba câu hỏi khác nhau và bổ sung cho nhau.

## 6. Mô hình

### 6.1 Nhóm mô hình dựa trên quy tắc (rule-based / heuristic)

| Mô hình | Cách chia công | Ưu điểm | Nhược điểm | Hợp với |
|---|---|---|---|---|
| **Last-click** | 100% cho điểm chạm cuối | Đơn giản, mặc định | Bỏ qua toàn bộ giai đoạn tạo nhu cầu | Chu kỳ mua ngắn, đo tối thiểu |
| **First-click** | 100% cho điểm chạm đầu | Tôn vinh kênh khám phá | Bỏ qua kênh chốt đơn | Đo hiệu quả nhận biết |
| **Linear** | Chia đều mọi điểm chạm | Công bằng, dễ hiểu | Không phản ánh trọng số thực | Hành trình nhiều chạm ngang nhau |
| **Time-decay** | Điểm chạm càng gần lúc mua càng nhiều công | Hợp với bán hàng thúc đẩy | Vẫn coi nhẹ đầu phễu | Chu kỳ bán dài, chốt đơn |
| **Position-based (U-shaped)** | Thường 40% đầu + 40% cuối + 20% giữa | Cân bằng khám phá & chốt | Tỷ lệ 40/20/40 mang tính quy ước | Cân đối cả hai đầu phễu |

### 6.2 Mô hình dựa trên dữ liệu (data-driven attribution — DDA)

Dùng thuật toán (thường là giá trị Shapley từ lý thuyết trò chơi, hoặc mô hình Markov) để tính đóng góp thực của từng kênh dựa trên hàng loạt hành trình có/không chuyển đổi. Ưu điểm: khách quan hơn quy tắc cứng. Nhược điểm: hộp đen, cần lượng dữ liệu lớn, và **vẫn phụ thuộc dữ liệu định danh cá nhân** — nên bị suy yếu trong thời hậu-cookie.

### 6.3 MMM (Media/Marketing Mix Modeling)

Hồi quy dữ liệu tổng hợp theo thời gian (doanh thu theo tuần vs. chi tiêu từng kênh, giá, mùa vụ, khuyến mãi) để ước lượng đóng góp và đường cong bão hòa của từng kênh. Không cần dữ liệu cá nhân → **thân thiện privacy**. Dùng được cả kênh offline (TV, billboard).

### 6.4 Incrementality testing

Thực nghiệm có nhóm đối chứng: **geo-lift test** (bật quảng cáo ở một số tỉnh/thành, tắt ở nhóm tương đương rồi so chênh lệch), **holdout/ghost ads** (một nhóm người dùng bị giữ lại không thấy quảng cáo). Đây là "chuẩn vàng" vì đo nhân quả thật, nhưng tốn kém và mất thời gian.

## 7. Framework

**Framework "3 tầng đo lường bổ trợ" (Triangulation Framework)** — quan điểm chủ đạo được nhiều đội growth 2024–2026 áp dụng:

```
Tầng 1 — MMM (top-down, chiến lược)
  → Trả lời: Phân bổ ngân sách giữa các kênh lớn ra sao? (theo quý/năm)
        │
Tầng 2 — Incrementality (causal, kiểm chứng)
  → Trả lời: Kênh/chiến dịch này có thật sự tạo tăng thêm không? (theo chiến dịch)
        │
Tầng 3 — MTA / Platform reporting (bottom-up, chiến thuật)
  → Trả lời: Trong một kênh, tối ưu sáng tạo/đối tượng nào? (hằng ngày)
```

Nguyên tắc: **dùng MMM để chia miếng bánh lớn, incrementality để kiểm tra giả định, MTA để tối ưu chi tiết trong ngày**. Không mô hình nào là "sự thật tuyệt đối"; ta *tam giác đạc* (triangulate) — khi ba phương pháp cùng chỉ về một hướng, độ tin cậy cao.

## 8. Công thức

> **Lưu ý: toàn bộ số dưới đây là (số minh họa) để dạy cách tính, không phải dữ liệu thật.**

Giả sử một hành trình có 4 điểm chạm dẫn đến 1 đơn hàng giá trị **1.000.000đ**:
`TikTok (T1) → Facebook (T2) → Google Search (T3) → Email (T4 = chạm cuối)`

**a) Last-click:**
`Credit(kênh) = Giá trị × (1 nếu là chạm cuối, else 0)`
→ Email nhận 1.000.000đ; ba kênh còn lại 0đ.

**b) First-click:** TikTok nhận 1.000.000đ; còn lại 0đ.

**c) Linear:**
`Credit = Giá trị / N` với N = số điểm chạm = 4
→ Mỗi kênh nhận 250.000đ.

**d) Time-decay** (hệ số nhân đôi mỗi bước tiến gần lúc mua, ví dụ trọng số 1-2-4-8, tổng = 15):
- TikTok: 1/15 × 1.000.000 ≈ 66.667đ
- Facebook: 2/15 ≈ 133.333đ
- Google: 4/15 ≈ 266.667đ
- Email: 8/15 ≈ 533.333đ

**e) Position-based (40/20/40):**
- TikTok (đầu): 400.000đ
- Facebook (giữa): 100.000đ
- Google (giữa): 100.000đ
- Email (cuối): 400.000đ

**f) ROAS theo mô hình:**
`ROAS(kênh) = Doanh thu được quy công cho kênh / Chi phí kênh`
→ Cùng một kênh, ROAS thay đổi hoàn toàn tùy mô hình. Đây chính là lý do "không có mô hình hoàn hảo".

**g) Incrementality (lift):**
`Incremental conversions = Conv(nhóm test) − Conv(nhóm control) × (quy mô test/control)`
`iROAS = (Doanh thu tăng thêm) / (Chi phí quảng cáo tăng thêm)`

## 9. Quy trình

1. **Xác định mục tiêu & sự kiện chuyển đổi** (mua, lead, cài app) và giá trị mỗi sự kiện.
2. **Kiểm kê điểm chạm & gắn thẻ nhất quán** (chuẩn hóa UTM, đặt tên chiến dịch).
3. **Dựng hạ tầng thu thập first-party** (server-side tagging, Conversions API).
4. **Cấu hình consent** (Consent Mode, banner theo Nghị định 13/GDPR).
5. **Chọn mô hình MTA nền tảng** để tối ưu chiến thuật hằng ngày.
6. **Xây/mua MMM** để phân bổ ngân sách chiến lược theo quý.
7. **Thiết kế lịch incrementality test** (geo-lift/holdout) cho các kênh nghi ngờ.
8. **Tam giác đạc kết quả** — đối chiếu 3 nguồn.
9. **Ra quyết định phân bổ & ghi lại giả định.**
10. **Đo lại, hiệu chỉnh, lặp** (calibrate MMM bằng kết quả incrementality).

## 10. Ví dụ đơn giản

Chị Lan bán nến thơm handmade qua Instagram và Shopee. Một khách kể lại: "Em thấy video reels của chị (1), rồi bấm theo dõi, tuần sau thấy story khuyến mãi (2), search tên shop trên Google (3), rồi vào Shopee mua (4)."

- **Nếu chị Lan dùng last-click:** Shopee/Google được ghi công → chị tưởng reels vô dụng, giảm làm video → doanh thu tụt sau 2 tháng.
- **Nếu dùng position-based:** reels (đầu) được ghi công 40% → chị hiểu video là nguồn tạo nhu cầu, tiếp tục đầu tư.

Bài học: mô hình attribution định hình cả quyết định kinh doanh của một shop nhỏ.

## 11. Ví dụ doanh nghiệp

Một sàn TMĐT tầm trung (số minh họa) chạy đồng thời: Google Search brand, Google Search non-brand, Meta prospecting, Meta retargeting, TikTok, Affiliate, Email/CRM.

Vấn đề kinh điển: **last-click luôn tôn vinh Search brand và Retargeting & Affiliate** (những kênh xuất hiện ở cuối phễu, "hớt váng" đơn đã sẵn sàng mua), trong khi TikTok và Meta prospecting (tạo nhu cầu đầu phễu) bị đánh giá thấp.

Khi doanh nghiệp chạy geo-lift test tắt Affiliate ở nửa số tỉnh, họ phát hiện phần lớn đơn "do Affiliate" vẫn xảy ra → tính incremental của Affiliate thấp hơn nhiều so với last-click báo cáo (số minh họa). Kết quả: tái phân bổ ngân sách từ retargeting sang prospecting.

## 12. Ví dụ Việt Nam

**Bối cảnh phổ biến tại Việt Nam:** hành trình mua thường đi qua **Facebook/TikTok → inbox/Zalo → chốt đơn qua tin nhắn hoặc COD**, không phải qua giỏ hàng web chuẩn. Điều này khiến attribution ở Việt Nam có đặc thù riêng:

- **Đứt gãy dữ liệu tại khâu inbox/Zalo:** click từ ad vào tin nhắn thường mất UTM; chuyển đổi xảy ra trong hội thoại, pixel không thấy.
- **COD (thu tiền khi nhận):** đơn "chốt" trên chat nhưng có tỷ lệ hoàn/bom hàng cao → nếu quy công theo lúc chốt sẽ thổi phồng hiệu quả kênh.
- **Ecosystem nội địa:** Zalo OA, Shopee/Lazada/TikTok Shop có hệ thống báo cáo riêng, khó ghép chung.

Thực hành khuyến nghị cho SMB Việt: dùng **mã giảm giá/mã kênh riêng cho mỗi nguồn** (ví dụ mã "TIKTOK10" vs "ZALO10") như một dạng attribution thủ công đơn giản, kết hợp câu hỏi "Bạn biết shop qua đâu?" lúc chốt đơn (post-purchase survey) — một hình thức **self-reported attribution** đang được nhiều D2C toàn cầu dùng lại. (Các đặc điểm hành vi trên là mô tả định tính phổ biến — con số cụ thể cần kiểm chứng theo ngành hàng.)

## 13. Ví dụ quốc tế

- **Airbnb (2019):** công khai cắt giảm mạnh chi tiêu performance marketing dựa nhiều vào phân tích rằng phần lớn traffic là **organic/brand** và quảng cáo có tính incremental thấp; họ chuyển trọng tâm sang brand marketing (cần kiểm chứng chi tiết con số cụ thể).
- **Uber (2017):** phát hiện đã lãng phí lớn cho quảng cáo hiển thị/ứng dụng do gian lận và **quảng cáo không tạo incremental** — tắt hàng chục triệu USD ad mà cài đặt gần như không đổi (con số được báo chí ngành đưa tin; cần kiểm chứng).
- **Procter & Gamble (2017):** cắt hơn 100 triệu USD quảng cáo digital "không hiệu quả/không an toàn thương hiệu" mà tăng trưởng không giảm — bằng chứng cổ điển cho tư duy incrementality (cần kiểm chứng con số).
- **eBay (nghiên cứu ~2014):** thực nghiệm cho thấy quảng cáo search brand có incremental rất thấp vì người dùng vốn đã tìm eBay (kinh điển trong tài liệu học thuật; cần kiểm chứng nguồn gốc).

Bài học chung: các thương hiệu lớn ngày càng tin **incrementality thay vì báo cáo last-click của nền tảng**.

## 14. Sai lầm thường gặp

1. **Thờ phụng last-click:** để mặc định của GA/nền tảng quyết định ngân sách.
2. **Tin tuyệt đối báo cáo của nền tảng:** Meta, Google, TikTok đều tự báo cáo và có xu hướng "nhận công" chồng lấn — cộng lại vượt 100% doanh thu thật.
3. **Nhầm tương quan với nhân quả:** kênh xuất hiện gần lúc mua ≠ kênh gây ra việc mua.
4. **Bỏ qua organic/baseline:** không trừ phần doanh thu vốn đã có nếu không quảng cáo.
5. **So sánh táo với cam:** đối chiếu ROAS giữa hai mô hình khác nhau rồi kết luận.
6. **Bỏ quên kênh offline & word-of-mouth** trong MMM.
7. **Không cấu hình consent đúng** → mất dữ liệu và rủi ro pháp lý.
8. **Chốt-đơn-trên-chat = doanh thu** mà quên tỷ lệ hoàn/hủy (đặc thù COD Việt Nam).
9. **Chạy MMM một lần rồi để yên:** MMM cần hiệu chỉnh định kỳ bằng incrementality.
10. **Kỳ vọng một con số duy nhất** — đòi hỏi "mô hình hoàn hảo" thay vì tam giác đạc.

## 15. Checklist

- [ ] Đã định nghĩa rõ sự kiện chuyển đổi và giá trị mỗi sự kiện?
- [ ] UTM & quy ước đặt tên chiến dịch đã chuẩn hóa toàn đội?
- [ ] Đã triển khai server-side tracking (GTM server-side)?
- [ ] Đã bật Conversions API (Meta) / Enhanced Conversions (Google)?
- [ ] Consent Mode & banner tuân thủ Nghị định 13/GDPR đã cấu hình?
- [ ] Đã chọn mô hình MTA phù hợp (không mặc định last-click)?
- [ ] Có nguồn dữ liệu baseline/organic để trừ?
- [ ] Đã lên lịch ít nhất 1 incrementality test/quý cho kênh lớn?
- [ ] Có kế hoạch MMM (tự xây Robyn/Meridian hoặc thuê)?
- [ ] Có quy trình tam giác đạc 3 nguồn trước khi đổi ngân sách?
- [ ] Đã tính tỷ lệ hoàn/hủy vào doanh thu quy công (nếu COD)?
- [ ] Có tài liệu ghi lại giả định & phiên bản mô hình?

## 16. SOP

**SOP: Chu trình attribution hằng quý (đề xuất)**

1. **Tuần 1 — Thu thập & làm sạch dữ liệu:** trích xuất chi tiêu, doanh thu theo tuần/kênh; đối chiếu số nền tảng vs. hệ thống bán hàng nội bộ.
2. **Tuần 1 — Kiểm tra hạ tầng:** xác nhận server-side & CAPI hoạt động, tỷ lệ khớp sự kiện (event match quality) đạt ngưỡng.
3. **Tuần 2 — Chạy/cập nhật MMM:** đưa dữ liệu tối thiểu 1–2 năm (nếu có) vào mô hình; xuất đóng góp & đường cong bão hòa từng kênh.
4. **Tuần 2–3 — Thiết kế incrementality test:** chọn 1 kênh nghi ngờ, chia geo test/control tương đương, xác định thời lượng & ngân sách.
5. **Tuần 3–8 — Chạy test & theo dõi:** không can thiệp giữa chừng; ghi log.
6. **Tuần 9 — Hiệu chỉnh MMM bằng kết quả test** (calibration).
7. **Tuần 10 — Tam giác đạc & họp phân bổ:** đối chiếu MMM, incrementality, MTA; ra quyết định ngân sách quý sau.
8. **Tuần 10 — Lập báo cáo & lưu giả định** vào kho tài liệu.
9. **Lặp lại** mỗi quý; audit consent/pháp lý mỗi 6 tháng.

## 17. KPI

| KPI | Ý nghĩa | Ghi chú |
|---|---|---|
| **iROAS (Incremental ROAS)** | Doanh thu *tăng thêm* / chi phí tăng thêm | Chuẩn vàng, ưu tiên hơn ROAS nền tảng |
| **CAC & Payback period** | Chi phí có được 1 khách & thời gian hoàn vốn | Nên tính theo incremental CAC |
| **Blended ROAS/CAC** | Tổng doanh thu / tổng chi (mọi kênh) | Không bị lệch bởi quy công |
| **MER (Marketing Efficiency Ratio)** | Tổng doanh thu / tổng chi marketing | "La bàn" top-down đơn giản |
| **Event Match Quality** | Chất lượng khớp sự kiện server-side | Ảnh hưởng độ chính xác CAPI |
| **Consent rate** | % người dùng đồng ý theo dõi | Ảnh hưởng độ phủ dữ liệu |
| **Saturation point** | Ngưỡng bão hòa chi tiêu mỗi kênh (từ MMM) | Quyết định trần ngân sách |
| **Lift %** | % chuyển đổi tăng thêm từ test | Đầu ra của incrementality |

## 18. Biểu mẫu

**Biểu mẫu 18.1 — So sánh mô hình attribution** (điền số thật của bạn; ví dụ dưới là số minh họa)

| Kênh | Chi phí | Last-click | First-click | Linear | Time-decay | Position | DDA | iROAS (test) |
|---|---|---|---|---|---|---|---|---|
| TikTok | 30.000.000đ | 5.000.000đ | 40.000.000đ | 22.000.000đ | 15.000.000đ | 30.000.000đ | 28.000.000đ | 2,1 |
| Meta prospecting | 40.000.000đ | 8.000.000đ | 25.000.000đ | 20.000.000đ | 16.000.000đ | 22.000.000đ | 24.000.000đ | 1,8 |
| Google non-brand | 25.000.000đ | 18.000.000đ | 12.000.000đ | 18.000.000đ | 20.000.000đ | 16.000.000đ | 17.000.000đ | 1,5 |
| Google brand | 10.000.000đ | 35.000.000đ | 3.000.000đ | 18.000.000đ | 28.000.000đ | 12.000.000đ | 9.000.000đ | 0,4 |
| Email/CRM | 5.000.000đ | 22.000.000đ | 1.000.000đ | 12.000.000đ | 18.000.000đ | 8.000.000đ | 10.000.000đ | 3,0 |

*(Toàn bộ con số trên là số minh họa cho mục đích so sánh cách các mô hình chia công khác nhau — hãy thay bằng dữ liệu thực tế.)* Nhận xét mẫu: Google brand "ăn công" rất cao ở last-click (35 triệu) nhưng iROAS chỉ 0,4 → dấu hiệu incremental thấp.

**Biểu mẫu 18.2 — Thẻ thiết kế incrementality test**
| Trường | Nội dung |
|---|---|
| Giả thuyết | (VD: Google brand có incremental thấp) |
| Kênh test | |
| Nhóm test (geo) | |
| Nhóm control (geo tương đương) | |
| Chỉ số chính | iROAS / lift % |
| Thời lượng | |
| Ngân sách | |
| Kết quả & quyết định | |

## 19. Prompt AI (6 công cụ)

> Lưu ý: AI hỗ trợ tư duy & tính toán, **không thay thế dữ liệu thật**. Luôn kiểm chứng đầu ra.

1. **ChatGPT / GPT (OpenAI):**
   *"Đóng vai chuyên gia measurement. Tôi có bảng chi tiêu và doanh thu 8 kênh dưới đây [dán dữ liệu]. Hãy tính doanh thu quy công theo 5 mô hình (last-click, first-click, linear, time-decay, position-based), chỉ ra kênh nào bị thổi phồng bởi last-click, và đề xuất 2 giả thuyết incrementality nên test. Ghi rõ giả định."*

2. **Claude (Anthropic):**
   *"Rà soát kế hoạch đo lường hậu-cookie của tôi [dán]. Kiểm tra tuân thủ Nghị định 13/2023/NĐ-CP và GDPR, chỉ ra lỗ hổng consent, và viết lại quy trình thu thập first-party an toàn. Nêu rủi ro pháp lý cụ thể."*

3. **Gemini (Google):**
   *"Hướng dẫn từng bước thiết lập Google Consent Mode v2 + Enhanced Conversions + GA4 data-driven attribution cho website Shopify tại Việt Nam. Nêu các cấu hình dễ sai và cách kiểm tra."*

4. **Perplexity:**
   *"Tổng hợp các nghiên cứu/case công khai (kèm nguồn và năm) về incrementality của quảng cáo Search brand và Retargeting. Chỉ liệt kê nguồn có thật, ghi rõ đường link gốc."*

5. **Julius AI / Code Interpreter (phân tích dữ liệu):**
   *"Từ file CSV hành trình khách hàng đính kèm, dựng mô hình Markov attribution và tính removal effect từng kênh; xuất bảng so sánh với linear và biểu đồ đóng góp."*

6. **Meta AI / Robyn (MMM mã nguồn mở của Meta) — trợ lý code:**
   *"Viết script R dùng thư viện Robyn để chạy MMM với dữ liệu doanh thu theo tuần và chi tiêu 6 kênh [mô tả cột]; giải thích cách đọc đường cong bão hòa và cách calibrate bằng kết quả geo-lift."*

## 20. Bài tập

1. **Tính tay:** Với hành trình `Google (đầu) → TikTok → Meta → Zalo (cuối)`, đơn 2.000.000đ, hãy chia công theo cả 5 mô hình quy tắc. Kênh nào lợi nhất ở time-decay?
2. **Phản biện:** Sếp muốn cắt TikTok vì last-click cho thấy ROAS 0,3. Viết 1 đoạn phản biện dựa trên khái niệm incrementality & vị trí đầu phễu.
3. **Thiết kế test:** Hãy điền Biểu mẫu 18.2 cho giả thuyết "Retargeting của shop tôi có incremental thấp". Chọn geo test/control ở Việt Nam.
4. **Pháp lý:** Liệt kê 3 nghĩa vụ theo Nghị định 13/2023/NĐ-CP mà việc gắn tracking phải tuân thủ (tự tra cứu văn bản gốc).
5. **Thực hành SMB:** Thiết kế hệ thống mã giảm giá theo kênh cho một shop bán qua Facebook + TikTok + Zalo để attribution thủ công.

## 21. Câu hỏi ôn tập

1. Phân biệt MTA, MMM và incrementality theo tiêu chí: dữ liệu đầu vào, câu hỏi trả lời, ảnh hưởng của hậu-cookie.
2. Vì sao last-click có xu hướng "thổi phồng" kênh cuối phễu và Search brand?
3. Consent Mode giải quyết vấn đề gì? Vì sao dữ liệu vẫn không đầy đủ như trước?
4. Server-side tracking và Conversions API khác gì tracking bằng pixel client-side truyền thống?
5. Vì sao nói "không có mô hình attribution hoàn hảo"? Framework tam giác đạc khắc phục ra sao?
6. Đặc thù nào của thị trường Việt Nam (Zalo, COD, chat) làm attribution khó hơn?
7. iOS ATT đã phá vỡ điều gì trong đo lường mobile?

## 22. Case Study

### 22.1 Thành công — Chuyển từ last-click sang tam giác đạc (mô hình D2C)

Một thương hiệu D2C (mô tả tổng hợp từ các mẫu hình phổ biến, không nêu tên cụ thể; số minh họa) từng phân bổ 60% ngân sách theo last-click, dồn vào retargeting và Search brand. Sau khi (1) dựng MMM bằng Robyn, (2) chạy geo-lift test cho retargeting và prospecting, họ phát hiện retargeting có iROAS thấp còn prospecting bị đánh giá thấp bởi last-click. Họ tái phân bổ ~20% ngân sách từ cuối phễu sang đầu phễu, kết quả MER cải thiện trong 2 quý (số minh họa). **Bài học: incrementality + MMM cứu ngân sách khỏi ảo giác last-click.**

### 22.2 Thất bại — Cắt kênh dựa trên báo cáo nền tảng đơn lẻ

Một nhà bán lẻ (mô tả tổng hợp; số minh họa) thấy TikTok báo ROAS thấp trong dashboard riêng của nền tảng, liền cắt toàn bộ ngân sách TikTok. Ba tháng sau, **tổng doanh thu blended sụt** dù các kênh khác không đổi — vì TikTok vốn tạo nhu cầu đầu phễu mà last-click/nền tảng không ghi nhận. Khắc phục bằng cách bật lại TikTok và chạy geo-lift để đo đúng đóng góp. **Bài học: đừng ra quyết định cắt kênh từ một báo cáo tự-quy-công duy nhất; hãy đo blended & incremental.**

## 23. Tổng kết

- Attribution là **nghệ thuật ra quyết định dưới bất định**, không phải phép đo tuyệt đối.
- Có ba họ phương pháp: **MTA** (chi tiết, phụ thuộc định danh — yếu đi hậu-cookie), **MMM** (top-down, thân thiện privacy), **incrementality** (nhân quả, chuẩn vàng).
- **Không có mô hình hoàn hảo** — mỗi mô hình trả lời một câu hỏi khác nhau; hãy **tam giác đạc** ba nguồn.
- Thời hậu-cookie (ATT, khai tử third-party cookie, GDPR/Nghị định 13) buộc chuyển từ tracking cá nhân sang **first-party data + server-side + MMM + thực nghiệm**.
- Ở Việt Nam, chú ý đứt gãy dữ liệu tại Zalo/chat và ảo giác doanh thu do COD.
- Ưu tiên **iROAS và blended metrics** hơn ROAS tự-báo-cáo của nền tảng.

## 24. Nguồn tham khảo

> Danh sách nguồn để tự tra cứu (không dẫn link để tránh link sai/lỗi thời — hãy tìm trực tiếp bằng tên). Trạng thái chính sách thay đổi nhanh, cần kiểm chứng theo thời điểm đọc.

1. **Nghị định 13/2023/NĐ-CP** về bảo vệ dữ liệu cá nhân (Chính phủ Việt Nam, hiệu lực 01/07/2023) — văn bản gốc trên Cổng thông tin pháp luật.
2. **Regulation (EU) 2016/679 — GDPR** (2016/2018).
3. **Apple — App Tracking Transparency (ATT)**, tài liệu nhà phát triển Apple (iOS 14.5, 2021).
4. **Google — Consent Mode v2 & Enhanced Conversions**, Google Ads/Analytics Help (cần kiểm chứng trạng thái mới nhất).
5. **Google — lộ trình third-party cookie trên Chrome / Privacy Sandbox** (cập nhật nhiều lần 2020–2025, cần kiểm chứng).
6. **Meta — Conversions API (CAPI)** & **Robyn** (thư viện MMM mã nguồn mở), tài liệu Meta for Developers / GitHub.
7. **Google — Meridian** (thư viện MMM mã nguồn mở), tài liệu Google.
8. **Google Analytics 4 — Data-driven attribution**, tài liệu chính thức.
9. Nghiên cứu học thuật về incrementality quảng cáo search (ví dụ nghiên cứu của Blake, Nosko & Tadelis liên quan eBay ~2014 — cần kiểm chứng tên/năm chính xác).
10. Các bài phân tích ngành về P&G, Uber, Airbnb cắt giảm digital ad (2017–2019) — báo chí ngành marketing, cần kiểm chứng con số cụ thể.
11. Lý thuyết **Shapley value** & **Markov chain attribution** — tài liệu học thuật/khoa học dữ liệu.
12. Tài liệu về **Marketing Mix Modeling** (nền tảng kinh tế lượng, từ thực tiễn FMCG) — sách/giáo trình chuyên ngành.

---

## Cần cập nhật trong tương lai

> **Cảnh báo mức độ ưu tiên cao:** đây là lĩnh vực biến động nhanh nhất trong marketing. Hãy rà soát chương này ít nhất mỗi 6 tháng.

Các điểm cần theo dõi và cập nhật:

1. **Trạng thái third-party cookie trên Chrome:** Google đã nhiều lần đổi hướng (từ "khai tử" sang cơ chế cho người dùng lựa chọn). Cần cập nhật quyết định mới nhất và tác động thực tế lên đo lường.
2. **Privacy Sandbox (Topics API, Attribution Reporting API):** các API đo lường bảo mật đang tiến hóa; theo dõi mức độ áp dụng thực tế của ngành.
3. **Consent Mode / các phiên bản mới:** yêu cầu consent của Google/Meta thay đổi liên tục theo áp lực pháp lý EU.
4. **Apple ATT & các thay đổi iOS/SKAdNetwork/AdAttributionKit:** cơ chế đo lường mobile của Apple tiếp tục thay đổi qua từng phiên bản iOS.
5. **Thực thi Nghị định 13/2023/NĐ-CP tại Việt Nam:** các văn bản hướng dẫn, nghị định sửa đổi, mức phạt và án lệ thực tế; khả năng có luật bảo vệ dữ liệu cá nhân cấp Luật (đang trong lộ trình — cần kiểm chứng).
6. **AI trong attribution:** các mô hình MMM/incrementality dùng học máy (Meridian, Robyn) cập nhật nhanh; công cụ mới có thể xuất hiện.
7. **Chuẩn đo lường mới của các nền tảng** (TikTok, Meta, Google) và mức độ đáng tin của báo cáo tự-quy-công.
8. **Số liệu minh họa trong chương:** cần thay bằng benchmark ngành cập nhật khi có nguồn đáng tin cậy; hiện tất cả đang đánh dấu "(số minh họa)".
9. **Đặc thù hệ sinh thái Việt Nam:** Zalo OA, TikTok Shop, Shopee/Lazada liên tục thay đổi khả năng tracking & API — cập nhật cách attribution cho social commerce nội địa.

*(Kết thúc Chương 4 — Tập 7.)*

# Prompt Seedance 2.5: xem, sao chép và tạo

[English](README_EN.md) · [简体中文](README_ZH.md) · [繁體中文](README_TW.md) · [日本語](README_JA.md) · [Português](README_PT.md) · [Español](README_ES.md) · [Deutsch](README_DE.md) · [Русский](README_RU.md) · [Français](README_FR.md) · [한국어](README_KO.md) · [ไทย](README_TH.md) · [Tiếng Việt](README_VI.md) · [العربية](README_AR.md) · [Bahasa Indonesia](README_ID.md) · [Italiano](README_IT.md)

![Ảnh bìa tạo bằng AI, không phải video do Seedance tạo](assets/seaimagine-seedance-hero-v2.png)

Ảnh tham chiếu → chỉ dẫn máy quay → hoàn thiện cảnh quay. Ảnh bìa dùng các ví dụ cứu hộ trong bão, trà có ga và cáo giấy trong thư viện.

Bản SeaImagine được biên soạn từ kho Flaq của công ty: 120 công thức, gồm 60 bằng tiếng Trung và 60 bằng tiếng Anh. Các tệp bổ sung cho 14 ngôn ngữ có sáu bài thực hành mỗi ngôn ngữ; không phải toàn bộ 120 công thức đều đã được dịch.

## Bắt đầu với một cảnh quay

Chọn cảnh trong mục lục, sao chép prompt rồi thay chủ thể, chất liệu và chuyển động máy quay. Hãy chuẩn bị ảnh mà bạn có quyền sử dụng. Chọn chế độ đầu vào và thời lượng được hỗ trợ trong SeaImagine; kiểm tra kết quả trước khi kéo dài video.

[Mục lục 120 công thức](prompts/README.md) · [Sáu bài thực hành tiếng Việt](prompts/i18n/prompt-library.vi.md)

## Tạo với SeaImagine

Mở trang Seedance để dùng mô hình. Vào Create để chuẩn bị ảnh tham chiếu và tìm công cụ ảnh, video. Kiểm tra tình trạng cung cấp, giá và giới hạn trong giao diện. Thời lượng trong ví dụ là đề bài sáng tạo, không phải cam kết của dịch vụ.

[SeaImagine · Seedance 2.5](https://seaimagine.com/vi/model/seedance-2-5/) · [SeaImagine · Create](https://seaimagine.com/vi/create/)

## Học từ video cộng đồng

Tên mô hình dựa trên lời của người đăng. Đây là tác phẩm của các nhà sáng tạo bên ngoài; chúng tôi chưa xác minh liệu các video có được tạo qua SeaImagine hay không. Nhấp vào ảnh xem trước để xem video và đọc prompt trong bài gốc của tác giả. Đây là các ví dụ do biên tập chọn, không phải bảng xếp hạng độ phổ biến đã xác minh.

### Nấu ăn và nhịp âm thanh

[![Nấu ăn và nhịp âm thanh — @Goodmanprotocol](https://pbs.twimg.com/amplify_video_thumb/2099186062715404288/img/D-iYamhA_iFRBooM.jpg)](https://video.twimg.com/amplify_video/2099186062715404288/vid/avc1/1920x1080/H8uxwKxVsSU09_LW.mp4?tag=29)

[Bài gốc và prompt của tác giả](https://x.com/Goodmanprotocol/status/2099186117769822462) · **@Goodmanprotocol**

Quan sát cách các cảnh cận nguyên liệu và âm thanh đồng bộ chuẩn bị cho đoạn kết hài hước.

### Một chiếc áo, nhiều cách phối

[![Một chiếc áo, nhiều cách phối — @Goodmanprotocol](https://pbs.twimg.com/amplify_video_thumb/2095216899445649408/img/690ykZJzst5uQLwH.jpg)](https://video.twimg.com/amplify_video/2095216899445649408/vid/avc1/1920x1080/LZt4YKiTkMag5Db1.mp4?tag=29)

[Bài gốc và prompt của tác giả](https://x.com/Goodmanprotocol/status/2095216981624721691) · **@Goodmanprotocol**

Giữ nguyên màu và cấu trúc áo; nối các bộ đồ bằng những chuyển động tương tự.

[Đủ 12 ví dụ cộng đồng](README.md) · [Ví dụ và nguồn chính thức](docs/official-examples.md)

## Cấu trúc prompt

```text
[Chế độ] Văn bản / ảnh / tham chiếu / chỉnh sửa
[Mục tiêu] Người xem, cảm xúc, thời lượng, tỷ lệ khung hình
[Tham chiếu] Ảnh 1: chủ thể; video 1: chỉ chuyển động máy quay
[Giữ nguyên] Khuôn mặt, trang phục, hình dáng sản phẩm, ánh sáng, số vật thể
[Trình tự] Mở đầu → hành động → thay đổi → khung hình cuối
[Máy quay] Điểm đầu, đường đi, tốc độ, lấy nét, điểm dừng
[Vật lý] Ánh mắt, bàn tay, trọng lượng, tiếp xúc, vải, nước
[Âm thanh] Lời thoại, môi trường, hiệu ứng, điểm đồng bộ
[Tránh] Biến dạng, vật thể trùng, thừa chi, chữ giả, logo
```

## Sao chép prompt sản phẩm đầy đủ

![Ảnh tham chiếu trà có ga](assets/product-sparkling-tea-reference.png)

Ảnh tham chiếu từ kho nguồn Flaq, không phải kết quả video. Bạn có thể dùng trực tiếp làm ảnh đầu vào cho bài thực hành này.

Chuẩn bị một ảnh tham chiếu của chai không có thương hiệu. Đây là bài thực hành, không phải prompt của các video trên; không khẳng định đã thử tạo kết quả. Rút ngắn hoặc chia cảnh theo giới hạn của giao diện.

```text
Dùng chai thủy tinh trong ở Hình 1 làm điểm neo sản phẩm duy nhất. Giữ nguyên đường nét, nắp, tỷ lệ nhãn trống, mức chất lỏng màu hổ phách, hơi nước và hướng sáng chính. Không tạo chữ.

00:00–00:05: cận cảnh một giọt nước, sau đó chuyển nét sang các bọt khí nhỏ đang nổi lên. 00:05–00:11: camera xoay theo chiều kim đồng hồ 35 độ và lùi chậm; bệ băng khúc xạ tự nhiên, chai đứng yên tuyệt đối. 00:11–00:17: ánh sáng ấm đi qua phía sau; nắp chỉ nhấc nhẹ với tiếng tách gọn và một làn sương mỏng. 00:17–00:24: hạ xuống góc hero vừa phải, kết thúc ở chính diện sạch với khoảng trống phía trên.

Âm thanh: tiếng mở nắp, ga nhẹ, tiếng băng nhỏ và nhịp nền nguyên bản tối giản. Không thêm chai, không trôi nhãn, méo thủy tinh, chất lỏng xuyên thành chai, chữ giả, logo, nhãn hiệu hoặc watermark.
```

[Sáu bài thực hành tiếng Việt](prompts/i18n/prompt-library.vi.md) · [Mục lục 120 công thức](prompts/README.md) · [Hướng dẫn tạo video](docs/seaimagine-workflow.md) · [Nguồn và ghi công](docs/PROVENANCE.md)

[Flaq · GitHub](https://github.com/flaqai/awesome_seedance_2_5) · [SeaImagine · GitHub](https://github.com/seaimagineai/awesome-seedance-2-5-prompts)

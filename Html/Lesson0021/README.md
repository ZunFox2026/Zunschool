# Tạo trang web về du lịch
Đây là dự án tạo trang web về du lịch, nơi bạn có thể tìm hiểu và khám phá các địa điểm du lịch hấp dẫn trên thế giới.

## Giới thiệu
Trong dự án này, chúng ta sẽ tạo một trang web về du lịch đơn giản, bao gồm các phần như trang chủ, giới thiệu, địa điểm du lịch và liên hệ. Chúng ta sẽ sử dụng HTML và CSS để thiết kế và xây dựng trang web.

Ví dụ về cấu trúc HTML cơ bản:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Trang web về du lịch</title>
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#">Trang chủ</a></li>
                <li><a href="#">Giới thiệu</a></li>
                <li><a href="#">Địa điểm du lịch</a></li>
                <li><a href="#">Liên hệ</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <!-- Nội dung trang web -->
    </main>
    <footer>
        <!-- Thông tin chân trang -->
    </footer>
</body>
</html>
```
Và ví dụ về CSS cơ bản:
```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

header {
    background-color: #333;
    color: #fff;
    padding: 20px;
    text-align: center;
}

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
}
```

## Lý thuyết
Để tạo trang web về du lịch, chúng ta cần hiểu về các khái niệm cơ bản của HTML và CSS. HTML (HyperText Markup Language) là ngôn ngữ dùng để tạo cấu trúc và nội dung của trang web, trong khi CSS (Cascading Style Sheets) là ngôn ngữ dùng để thiết kế và định dạng trang web.

Một số khái niệm quan trọng của HTML bao gồm:
- Thẻ html: `<html>` là thẻ gốc của trang web
- Thẻ head: `<head>` chứa thông tin về trang web, bao gồm cả thẻ `<title>`
- Thẻ body: `<body>` chứa nội dung của trang web

Một số khái niệm quan trọng của CSS bao gồm:
- Bộ chọn (selector): dùng để chọn các phần tử HTML để áp dụng样式
- Thuộc tính (property): dùng để định dạng các phần tử HTML, bao gồm màu sắc, kích thước, phông chữ, v.v.

Ví dụ về sử dụng CSS để định dạng một đoạn văn:
```css
p {
    font-size: 18px;
    color: #666;
    padding: 10px;
}
```
Và ví dụ về sử dụng HTML để tạo một danh sách:
```html
<ul>
    <li>Địa điểm 1</li>
    <li>Địa điểm 2</li>
    <li>Địa điểm 3</li>
</ul>
```

## Ví dụ
Dưới đây là một ví dụ về trang web về du lịch đơn giản:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Trang web về du lịch</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#">Trang chủ</a></li>
                <li><a href="#">Giới thiệu</a></li>
                <li><a href="#">Địa điểm du lịch</a></li>
                <li><a href="#">Liên hệ</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <h1>Địa điểm du lịch hấp dẫn</h1>
        <p>Địa điểm 1: Hà Nội</p>
        <p>Địa điểm 2: TP. Hồ Chí Minh</p>
        <p>Địa điểm 3: Đà Nẵng</p>
    </main>
    <footer>
        <p>&copy; 2024 Trang web về du lịch</p>
    </footer>
</body>
</html>
```
Và ví dụ về CSS đi kèm:
```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

header {
    background-color: #333;
    color: #fff;
    padding: 20px;
    text-align: center;
}

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
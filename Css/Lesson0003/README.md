# Tìm hiểu về Box Shadow
## Giới thiệu
Box Shadow là một thuộc tính CSS dùng để tạo bóng cho các phần tử HTML. Thuộc tính này cho phép bạn tạo bóng đơn giản hoặc phức tạp tùy theo nhu cầu thiết kế. Trong bài này, chúng ta sẽ tìm hiểu về cách sử dụng Box Shadow và các thuộc tính liên quan.

## Lý thuyết
Thuộc tính Box Shadow có cú pháp như sau: `box-shadow: offset-x offset-y blur-radius spread-radius color;`. Các giá trị trong cú pháp này có ý nghĩa như sau:
- `offset-x`: Chỉ định vị trí bóng theo trục x (trái/phải).
- `offset-y`: Chỉ định vị trí bóng theo trục y (lên/xuống).
- `blur-radius`: Chỉ định độ mờ của bóng.
- `spread-radius`: Chỉ định độ rộng của bóng.
- `color`: Chỉ định màu của bóng.

Ví dụ:
```css
.example {
  box-shadow: 10px 5px 5px 0px rgba(0,0,0,0.2);
}
```
Trong ví dụ trên, phần tử có lớp `example` sẽ có bóng với các thuộc tính như sau: cách trái 10px, cách trên 5px, độ mờ 5px, không có độ rộng bóng và màu bóng là đen với độ trong suốt 0.2.

## Ví dụ
Dưới đây là một số ví dụ minh họa cách sử dụng Box Shadow:
- Tạo bóng đơn giản:
```css
.box {
  width: 100px;
  height: 100px;
  background-color: #fff;
  box-shadow: 0 0 10px rgba(0,0,0,0.2);
}
```
- Tạo bóng nhiều lớp:
```css
.box {
  width: 100px;
  height: 100px;
  background-color: #fff;
  box-shadow: 0 0 10px rgba(0,0,0,0.2), 0 0 20px rgba(0,0,0,0.4);
}
```
## Bài tập
Bài tập 1: Tạo một phần tử div có kích thước 200x200 pixel, màu nền là màu xanh lam (#0000ff) và có bóng với các thuộc tính như sau: cách trái 5px, cách trên 10px, độ mờ 5px, không có độ rộng bóng và màu bóng là đen với độ trong suốt 0.2.
Bài tập 2: Tạo một phần tử div có kích thước 150x150 pixel, màu nền là màu vàng (#ffff00) và có bóng nhiều lớp với các thuộc tính như sau:
- Lớp 1: cách trái 0px, cách trên 0px, độ mờ 10px, không có độ rộng bóng và màu bóng là đen với độ trong suốt 0.2.
- Lớp 2: cách trái 0px, cách trên 0px, độ mờ 20px, không có độ rộng bóng và màu bóng là đen với độ trong suốt 0.4.
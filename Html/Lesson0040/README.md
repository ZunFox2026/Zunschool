# Tạo hiệu ứng bóng đổ
## Giới thiệu
Tạo hiệu ứng bóng đổ là một kỹ thuật quan trọng trong thiết kế web, giúp tạo ra sự sâu sắc và chiều sâu cho các yếu tố trên trang web. Trong bài này, chúng ta sẽ tìm hiểu về cách tạo hiệu ứng bóng đổ sử dụng CSS.

## Lý thuyết
Để tạo hiệu ứng bóng đổ, chúng ta sử dụng thuộc tính `box-shadow` trong CSS. Thuộc tính này cho phép chúng ta tạo ra một bóng đổ cho các yếu tố trên trang web. Cú pháp của thuộc tính `box-shadow` như sau:
```html
box-shadow: offset-x offset-y blur-radius spread-radius color;
```
Trong đó:
- `offset-x` và `offset-y` là khoảng cách của bóng đổ so với yếu tố.
- `blur-radius` là bán kính mờ của bóng đổ.
- `spread-radius` là bán kính lan rộng của bóng đổ.
- `color` là màu của bóng đổ.

Ví dụ:
```html
<div class="box"></div>
```

```css
.box {
  width: 100px;
  height: 100px;
  background-color: #fff;
  box-shadow: 10px 10px 5px 0px rgba(0,0,0,0.5);
}
```
Trong ví dụ trên, chúng ta tạo ra một bóng đổ cho yếu tố `div` với khoảng cách 10px về phía phải và xuống dưới, bán kính mờ 5px, không lan rộng và màu đen với độ trong suốt 50%.

## Ví dụ
Chúng ta có thể sử dụng thuộc tính `box-shadow` để tạo ra nhiều loại bóng đổ khác nhau. Ví dụ, chúng ta có thể tạo ra một bóng đổ nhỏ và gần với yếu tố:
```html
<div class="box-small"></div>
```

```css
.box-small {
  width: 100px;
  height: 100px;
  background-color: #fff;
  box-shadow: 2px 2px 2px 0px rgba(0,0,0,0.2);
}
```
Hoặc chúng ta có thể tạo ra một bóng đổ lớn và xa với yếu tố:
```html
<div class="box-large"></div>
```

```css
.box-large {
  width: 100px;
  height: 100px;
  background-color: #fff;
  box-shadow: 20px 20px 10px 0px rgba(0,0,0,0.8);
}
```
## Bài tập
Bài tập: Tạo một trang web với một hình chữ nhật có bóng đổ. Sử dụng thuộc tính `box-shadow` để tạo ra một bóng đổ với khoảng cách 15px về phía phải và xuống dưới, bán kính mờ 8px, không lan rộng và màu đen với độ trong suốt 60%. 
```html
<div class="box-exercise"></div>
```

```css
.box-exercise {
  width: 200px;
  height: 200px;
  background-color: #fff;
  box-shadow: 15px 15px 8px 0px rgba(0,0,0,0.6);
}
```
Chúng ta có thể điều chỉnh các giá trị của thuộc tính `box-shadow` để tạo ra nhiều loại bóng đổ khác nhau và áp dụng vào các yếu tố trên trang web.
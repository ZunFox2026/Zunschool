# Python 9 Cấp Cơ Bản

## Giới thiệu

Bài 9 trong chuỗi bài học "Python 9 Cấp Cơ Bản" tập trung vào chủ đề **vòng lặp `for`** – một trong những cấu trúc điều khiển quan trọng nhất trong lập trình Python. Vòng lặp `for` giúp lặp lại một khối lệnh với từng phần tử trong một dãy dữ liệu như danh sách, chuỗi hoặc dãy số. Việc nắm vững vòng lặp `for` sẽ giúp bạn xử lý dữ liệu hiệu quả hơn, đặc biệt khi làm việc với các cấu trúc dữ liệu như danh sách, bộ, hoặc từ điển.

## Lý thuyết

Vòng lặp `for` trong Python được sử dụng để duyệt qua các phần tử của một chuỗi (iterable) như danh sách (`list`), chuỗi (`string`), hoặc dãy số được tạo bởi hàm `range()`.

Cú pháp cơ bản:
```python
for biến in chuỗi:
    # Khối lệnh lặp lại
```

- Hàm `range(start, stop, step)` giúp tạo ra một dãy số:
  - `start`: giá trị bắt đầu (mặc định là 0)
  - `stop`: giá trị kết thúc (không bao gồm)
  - `step`: bước nhảy (mặc định là 1)

## Ví dụ

Dưới đây là ví dụ in các số từ 1 đến 5:
```python
for i in range(1, 6):
    print(i)
```

Kết quả:
```
1
2
3
4
5
```

Ví dụ duyệt qua danh sách:
```python
fruits = ["táo", "chuối", "dưa"]
for fruit in fruits:
    print("Tôi thích", fruit)
```

## Bài tập

1. Viết chương trình in ra các số chẵn từ 2 đến 10.
2. Tạo một danh sách tên bạn bè và in lời chào cho từng người.
3. Tính tổng các số từ 1 đến 100 bằng vòng lặp `for`.

Hãy thực hành để làm chủ vòng lặp `for` – công cụ mạnh mẽ giúp bạn tự động hóa các công việc lặp lại trong Python!
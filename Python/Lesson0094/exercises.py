### Bài tập 1
# Viết một metaclass tên là VersionRequiredMeta
# Đảm bảo rằng mọi lớp sử dụng nó đều có thuộc tính 'version' là số nguyên.
# Nếu không có, ném lỗi TypeError.

class VersionRequiredMeta(type):
    # Viết code tại đây
    pass


class MyComponent(metaclass=VersionRequiredMeta):
    version = 1  # Phải có dòng này


### Bài tập 2
# Tạo metaclass PluginRegistryMeta để đăng ký tất cả các lớp con vào từ điển
# Khóa là tên lớp, giá trị là đối tượng lớp
# Gợi ý: dùng một dict ở cấp module

registry = {}  # Dùng để lưu trữ

class PluginRegistryMeta(type):
    # Viết code tại đây
    pass

class AudioPlugin(metaclass=PluginRegistryMeta):
    pass

class VideoPlugin(metaclass=PluginRegistryMeta):
    pass


### Bài tập 3
# Viết metaclass tên là ValidClassNameMeta
# Kiểm tra tên lớp phải bắt đầu bằng chữ in hoa
# Nếu không, ném lỗi

class ValidClassNameMeta(type):
    # Viết code tại đây
    pass

class MyValidClass(metaclass=ValidClassNameMeta):
    pass


### Bài tập 4
# Tạo metaclass AutoToDictMeta2 để thêm phương thức to_dict
# Nhưng chỉ áp dụng với các thuộc tính public (không bắt đầu bằng _)
# Nếu lớp đã có to_dict thì giữ nguyên

class AutoToDictMeta2(type):
    # Viết code tại đây
    pass

class Product(metaclass=AutoToDictMeta2):
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self._id = 123  # ẩn


### Bài tập 5 (Nâng cao)
# Viết metaclass SingletonMeta
# Khiến tất cả các lớp dùng metaclass này chỉ có một instance duy nhất
# Khi gọi() nhiều lần, trả về cùng một instance

class SingletonMeta(type):
    # Viết code tại đây
    pass

class Database(metaclass=SingletonMeta):
    def __init__(self):
        self.connection = "connected"

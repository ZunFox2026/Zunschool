###################
# Lời giải bài tập - Bài 77
# File: solutions.py
# Chứa lời giải đầy đủ với comment tiếng Việt
###################

import time
import re

class EmailDescriptor:
    """Descriptor kiểm tra định dạng email đơn giản"""
    def __init__(self):
        self.value = ""

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.value

    def __set__(self, instance, value):
        # Kiểm tra định dạng email đơn giản
        if not isinstance(value, str):
            raise TypeError("Email phải là chuỗi")
        if "@" not in value or "." not in value:
            raise ValueError("Email phải chứa @ và .")
        if value.startswith("@") or value.endswith("@"):
            raise ValueError("Email không được bắt đầu hoặc kết thúc bằng @")
        self.value = value

    def __delete__(self, instance):
        self.value = ""

class Person:
    email = EmailDescriptor()
    def __init__(self, email):
        self.email = email


class LimitedAccessDescriptor:
    """Descriptor giới hạn số lần truy cập"""
    def __init__(self, max_access=1):
        self.max_access = max_access
        self.access_count = 0
        self.value = None

    def __get__(self, instance, owner):
        if instance is None:
            return self
        self.access_count += 1
        if self.access_count > self.max_access:
            raise RuntimeError(f"Đã vượt quá giới hạn truy cập ({self.max_access} lần)")
        return self.value

    def __set__(self, instance, value):
        self.value = value
        self.access_count = 0  # Reset khi gán lại


class SecretData:
    secret = LimitedAccessDescriptor(max_access=3)
    def __init__(self, value):
        self.secret = value


class ReadOnlyDescriptor:
    """Descriptor chỉ cho phép đọc, không cho phép ghi"""
    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.value

    def __set__(self, instance, value):
        raise AttributeError("Thuộc tính này là chỉ đọc")

    def __delete__(self, instance):
        raise AttributeError("Không thể xóa thuộc tính chỉ đọc")

class Configuration:
    api_key = ReadOnlyDescriptor("abc123")
    def __init__(self):
        pass


class TimeTrackerDescriptor:
    """Ghi lại thời gian truy cập cuối cùng"""
    def __init__(self):
        self.value = None
        self.last_accessed = None

    def __get__(self, instance, owner):
        if instance is None:
            return self
        self.last_accessed = time.time()
        return self.value

    def __set__(self, instance, value):
        self.value = value

    def get_last_accessed(self):
        """Trả về thời gian truy cập cuối (dạng chuỗi)"""
        if self.last_accessed:
            return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.last_accessed))
        return "Chưa truy cập"


class TrackedValue:
    value = TimeTrackerDescriptor()
    def __init__(self, val):
        self.value = val


class TypeEnforcedDescriptor:
    """Buộc kiểu dữ liệu cho thuộc tính"""
    def __init__(self, expected_type):
        self.expected_type = expected_type
        self.value = None

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f"Giá trị phải là kiểu {self.expected_type.__name__}")
        self.value = value


class DataRecord:
    name = TypeEnforcedDescriptor(str)
    age = TypeEnforcedDescriptor(int)
    def __init__(self, name, age):
        self.name = name
        self.age = age

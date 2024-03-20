from ._anvil_designer import Form1Template
from anvil import *
import random
from ..Form2 import bubble_sort
from ..Form2 import selection_sort
from ..Form2 import insertion_sort
from ..Form2 import quick_sort
from ..Form2 import merge_sort
class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.drop_down_1.items = [
            ("                              "),
            ("SẮP XẾP NỔI BỌT", "bubble_sort"),
            ("SẮP XẾP CHỌN", "selection_sort"),
            ("SẮP XẾP CHÈN", "insertion_sort"),
            ("SẮP XẾP NHANH", "quick_sort"),
            ("SẮP XẾP TRỘN", "merge_sort"),]
   
    self.drop_down_2.items = [
            ("                              "),
            ("SẮP XẾP NỔI BỌT", "bubble_sort"),
            ("SẮP XẾP CHỌN", "selection_sort"),
            ("SẮP XẾP CHÈN", "insertion_sort"),
            ("SẮP XẾP NHANH", "quick_sort"),
            ("SẮP XẾP TRỘN", "merge_sort"),]
  # Hàm tạo dãy số ngẫu nhiên
  def button_1_click(self, **event_args):
    SoLuong_PT = int(self.text_area_SoLuongPT.text)
    self.DaySo = random.sample(range(1, 101), SoLuong_PT);
    self.label_4.text = ( ", ".join(map(str,self.DaySo)))

  # Hàm sắp xếp dãy số
  def button_2_click(self, **event_args):
     # Lấy thuật toán được chọn từ menu Dropdown
    luaChon = self.drop_down_1.selected_value
    # Lấy dãy số từ ô dãy số random
    self.DaySo = [int(x) for x in self.label_4.text.split(", ")]
    if luaChon == "bubble_sort":
            self.DaySo = bubble_sort(self.DaySo)
    elif luaChon == "selection_sort":
            self.DaySo = selection_sort(self.DaySo)
    elif luaChon == "insertion_sort":
            self.DaySo = insertion_sort(self.DaySo)
    elif luaChon == "quick_sort":
            self.DaySo = quick_sort(self.DaySo)
    elif luaChon == "merge_sort":
            self.DaySo = merge_sort(self.DaySo)
     
    self.label_6.text = ", ".join(map(str, self.DaySo))

  def button_3_click(self, **event_args):
    self.array = self.text_area_DaySo.text
    self.label_5.text = ( "".join(map(str, self.array)))
  def button_4_click(self, **event_args):
    # Lấy thuật toán được chọn từ menu Dropdown
    luaChon2 = self.drop_down_2.selected_value
    # Lấy dãy số từ ô nhập dãy số
    self.array= [int(x) for x in self.label_5.text.split(", ")]
    if luaChon2 == "bubble_sort":
            self.array = bubble_sort(self.array)
    elif luaChon2 == "selection_sort":
            self.array = selection_sort(self.array)
    elif luaChon2 == "insertion_sort":
            self.array = insertion_sort(self.array)
    elif luaChon2 == "quick_sort":
            self.array = quick_sort(self.array)
    elif luaChon2 == "merge_sort":
            self.array = merge_sort(self.array)
     
    self.label_DaySoSX.text = ", ".join(map(str, self.array))
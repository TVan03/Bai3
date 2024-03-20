from ._anvil_designer import Form2Template
from anvil import *
import anvil.server

class Form2(Form2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
def bubble_sort(DaySo):
    # Duyệt qua từng phần tử trong dãy số
      for i in range(len(DaySo) - 1):
        for j in range(len(DaySo) - i - 1):
            # So sánh hai phần tử cạnh nhau
            if DaySo[j] > DaySo[j + 1]:
                # Đổi chỗ hai phần tử nếu phần tử bên trái lớn hơn
                DaySo[j], DaySo[j + 1] = DaySo[j + 1], DaySo[j]
 
    # Trả về dãy số sau khi sắp xếp
      return DaySo
def selection_sort(DaySo):
    # Duyệt qua từng phần tử trong dãy số
      for i in range(len(DaySo)):
        # Lấy vị trí phần tử nhỏ nhất
        min_index = i
        for j in range(i + 1, len(DaySo)):
            # So sánh phần tử hiện tại với phần tử nhỏ nhất
            if DaySo[j] < DaySo[min_index]:
                # Cập nhật vị trí phần tử nhỏ nhất
                min_index = j

        # Đổi chỗ phần tử hiện tại với phần tử nhỏ nhất
        DaySo[i], DaySo[min_index] = DaySo[min_index], DaySo[i]

    # Trả về dãy số sau khi sắp xếp
      return DaySo
def insertion_sort(DaySo):
    # Duyệt qua từng phần tử trong dãy số
      for i in range(1, len(DaySo)):
        # Lưu giá trị của phần tử hiện tại
        current = DaySo[i]
        j = i - 1

        # Duyệt ngược từ phần tử trước cho đến đầu dãy
        while j >= 0 and DaySo[j] > current:
            # Di chuyển phần tử lớn hơn sang vị trí sau
            DaySo[j + 1] = DaySo[j]
            j -= 1

        # Chèn phần tử hiện tại vào vị trí thích hợp
        DaySo[j + 1] = current

    # Trả về dãy số sau khi sắp xếp
      return DaySo
def quick_sort(DaySo):
  if len(DaySo) <= 1:
    return DaySo
  pivot = DaySo[0]  # Chọn pivot là phần tử đầu tiên
  smaller = [x for x in DaySo if x < pivot]
  larger = [x for x in DaySo if x > pivot]  # So sánh với ">" để đảm bảo vòng lặp kết thúc

  return quick_sort(smaller) + [pivot] + quick_sort(larger)

def merge_sort(DaySo):
  # Lấy độ dài mảng
  n = len(DaySo)
  # Trả về mảng rỗng nếu n <= 1
  if n <= 1:
    return DaySo
  # Chia mảng thành hai phần con
  mid = n // 2
  left = merge_sort(DaySo[:mid])
  right = merge_sort(DaySo[mid:])
  # Gộp mảng con
  return merge(left, right)
def merge(left, right):
  result = []
  i, j = 0, 0
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1
  # Gộp phần còn lại của mảng
  result += left[i:]
  result += right[j:]
  return result

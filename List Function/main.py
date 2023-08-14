"""append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list"""

lst = [i for i in range(11)]

# appending function -> hàm chèn vào cuối list
lst.append(11)
print(lst)

# copy list (shallow copy) -> thay đổi 1 list, list kia thay đổi theo ??
# (thường trong trường hợp phức tạp như object, array, các kiểu dữ liệu cơ bản k vấn đề !!)
lst[0] = 999
copy_lst = lst.copy()  # shallow copy
print(copy_lst)
print(lst)

lst += [999, 999, 999]
# count function -> đếm số lần xuất hiện của value trong list
print(lst)
print(lst.count(999))

# extend function -> thêm các giá trị của list khác vào list chỉ định
dummy_lst = [1, 2, 3, 4]
dummy_lst.extend(lst)
print(dummy_lst)

"""index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list"""

# index function -> trả về vị trí đầu tiên xuất hiện giá trị đầu tiên:
print(dummy_lst.index(1))

# hàm insert -> chèn tại vị trí đã cho
dummy_lst.insert(1, -1)
print(dummy_lst)

# hàm pop -> xóa tại vị trí đã cho
dummy_lst.pop(1)
print(dummy_lst)

# hàm reverse -> đảo mảng
dummy_lst.reverse()
print(dummy_lst)

# hàm sort -> sắp xếp mảng
dummy_lst.sort()
print(dummy_lst)
dummy_lst.sort(reverse=True)
print(dummy_lst)

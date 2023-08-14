"""1. Giả sử Công ty có hai loại nhân viên: Nhân viên văn phòng và Nhân viên sản
xuất. Viết chương trình quản lý và tính lương cho từng nhân viên của công ty:
Mỗi nhân viên cần quản lý các thông tin sau: Họ tên, ngày sinh, lương
Công ty cần tính lương cho nhân viên như sau:
- Đối với nhân viên sản xuất:
▪ Lương = lương căn bản + số sản phẩm * 5.000
- Đối nhân viên văn phòng:
▪ lương = số ngày làm việc * 100.000
Viết chương trình cho phép thực hiện các chức năng sau:
1. Nhập danh sách nhân viên -> input
2. Tính lương cho từng nhân viên -> abstract
3. Xuất thông tin các nhân viên -> print (str)
4. Tính tổng lương mà công ty phải trả cho các nhân viên -> total salary
5. Tìm nhân viên có lương cao nhất, thấp nhất,… -> most, least
6. Sắp xếp và xuất ra danh sách nhân viên theo lương giảm dần.-> sort """


import abc


class Employee(metaclass=abc.ABCMeta):
    def __init__(self, name='', birthday='', salary=0):
        self._name = name
        self._birthday = birthday
        self._salary = salary

    def get_name(self):
        return self._name

    def get_birthday(self):
        return self._birthday

    def get_salary(self):
        return self._salary

    @abc.abstractmethod
    def input(self):
        self._name = input("Nhap ten nhan vien: ")
        self._birthday = input("Nhap ngay sinh nhan vien: ")

    @abc.abstractmethod
    def output(self):
        print("Ten nhan vien:", self._name)
        print("Ngay sinh nhan vien:", self._birthday)
        print("Luong cua nhan vien:", self._salary)

    @abc.abstractmethod
    def calculating_salary(self):
        raise NotImplementedError()


class ManufacturingEmployee(Employee):
    def __init__(self, base_salary=0, product_num=0):
        super().__init__()
        self._base_salary = base_salary
        self._product_num = product_num

    def get_basesalary(self):
        return self._base_salary

    def get_productnum(self):
        return self._product_num

    def input(self):
        super().input()
        self._base_salary = float(input("Hay nhap luong co ban: "))
        self._product_num = float(input("Hay nhap so san pham: "))

    def output(self):
        super().output()
        print("Luong co ban:", self._base_salary)
        print("So san pham:", self._product_num)

    def calculating_salary(self):
        self._salary = float(self._base_salary + self._product_num * 5000)


class OfficeEmployee(Employee):
    def __init__(self, working_days=0):
        super().__init__()
        self._working_days = working_days

    def get_workingdays(self):
        return self._working_days

    def input(self):
        super().input()
        self._working_days = int(input("Hay nhap so ngay lam viec: "))

    def output(self):
        super().output()
        print("So ngay lam viec:", self._working_days)

    def calculating_salary(self):
        self._salary = float(self._working_days * 100000)


if __name__ == "__main__":
    size = int(input("Hay nhap so nhan vien: "))
    lst = []
    # Thuc hien nhap nhan vien va tinh luong
    for i in range(size):
        print("Chon 1 neu la nhan vien san xuat")
        print("Chon 2 neu la nhan vien van phong")
        type_employee = int(input())
        if type_employee == 1:
            temp = ManufacturingEmployee()
            lst.append(temp)
        elif type_employee == 2:
            temp = OfficeEmployee()
            lst.append(temp)
        temp.input()
        temp.calculating_salary()
    # Xuat thong tin nhan vien
    print("")
    print("Danh sach thong tin nhan vien:")
    for v in lst:
        v.output()
    # Tinh tong luong va xuat ket qua
    total_salary = 0
    for v in lst:
        total_salary += v.get_salary()
    print("")
    print("Tong luong la:", total_salary)
    # Tim nhan vien luong cao nhat va thap nhat
    mvp = lst[0]
    lvp = lst[0]
    for v in lst:
        if mvp.get_salary() < v.get_salary():
            mvp = v
        if lvp.get_salary() > v.get_salary():
            lvp = v
    print("")
    print("Nhan vien co luong cao nhat va thap nhat lan luot la:")
    mvp.output()
    lvp.output()
    # Sort nhan vien theo luong giam dan
    print("")
    print("Danh sach nhan vien sap xep theo luong giam dan:")
    lst.sort(key=lambda x: x.get_salary(), reverse=True)
    for v in lst:
        v.output()













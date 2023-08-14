import random
# 63 Tỉnh thành
vietnamese_provinces = ['An Giang', 'Bà Rịa-Vũng Tàu', 'Bạc Liêu',
                        'Bắc Giang', 'Bắc Kạn', 'Bắc Ninh', 'Bến Tre', 'Bình Dương', 'Bình Định'
                        , 'Bình Phước', 'Bình Thuận', 'Cà Mau', 'Cao Bằng', 'Cần Thơ', 'Đà Nẵng'
                        , 'Đắk Lắk', 'Đắk Nông', 'Điện Biên', 'Đồng Nai', 'Đồng Tháp'
                        , 'Gia Lai', 'Hà Giang', 'Hà Nam', 'Hà Nội', 'Hà Tĩnh'
                        , 'Hải Dương', 'Hải Phòng', 'Hậu Giang', 'Hòa Bình', 'Hưng Yên'
                        , 'Khánh Hòa', 'Kiên Giang', 'Kon Tum', 'Lai Châu'
                        , 'Lạng Sơn', 'Lào Cai', 'Lâm Đồng', 'Long An', 'Nam Định'
                        , 'Nghệ An', 'Ninh Bình', 'Ninh Thuận', 'Phú Thọ', 'Phú Yên'
                        , 'Quảng Bình', 'Quảng Nam', 'Quảng Ngãi', 'Quảng Ninh', 'Quảng Trị', 'Sóc Trăng'
                        , 'Sơn La', 'Tây Ninh', 'Thái Bình', 'Thái Nguyên', 'Thanh Hóa', 'Thừa Thiên Huế', 'Tiền Giang'
                        , 'TP Hồ Chí Minh', 'Trà Vinh', 'Tuyên Quang', 'Vĩnh Long', 'Vĩnh Phúc', 'Yên Bái']

for i in range(63):
    random_shipping_charges = random.randint(1, 101) * 1000
    print("INSERT INTO province VALUES(" + str(i+1) + "," + "'" + vietnamese_provinces[i] + "'" + ","
          + str(random_shipping_charges) + ")")






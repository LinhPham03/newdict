pro_list = {
    101 : 'watch',
    102 : 'phone',
    103 : 'CDs',
    104 : 'Laptop',
    105 : 'tablet',
    106 : 'Music player'
    }

def pro_info(pro_list, pro_id):
    if pro_id in pro_list:
        return pro_list[pro_id]
    else:
        print(pro_id, "doesn't exist")
        return

def pro_update(pro_list, update_id, update_name):
    pro_list[update_id] = update_name
    return pro_list

def pro_del(pro_list, pro_id):
    if pro_id in pro_list:
        del pro_list[pro_id]
    else:
        print(pro_id, "haven't existed in the list")
        return

while True:
    print(" Chức năng quản lí sản phẩm: \n" 
        "1. Hiển thị danh sách sản phẩm \n"
        "2. Thêm sản phẩm mới vào danh sách \n"
        "3. Sửa tên của sản phẩm trong danh sách \n"
        "4. Xoá một sản phẩm khỏi danh sách \n"
        "5. Thoát")
    option = int(input('Bạn chọn số 1/2/3/4/5: '))
    
    if option == 1:
        pro_id = int(input('Nhập ID sản phẩm: '))
        pro_info(pro_list, pro_id)
        print(pro_id, ':', pro_list[pro_id])

    elif option ==2:
        id = input('Nhập ID sản phẩm muốn thêm: ')
        update_id = int(id)
        if update_id not in pro_list:
            update_name = input('Nhập tên sản phẩm muốn thêm: ')
            pro_update(pro_list, update_id, update_name)
        else: 
            pro_info(pro_list, pro_id)

    elif option == 3:
        id = input('Nhập ID sản phẩm muốn sửa: ')
        update_id = int(id)
        if update_id in pro_list:
            update_name = input('Nhập tên sản phẩm muốn sửa: ')
            pro_update(pro_list, update_id, update_name)
        else: 
            print("Sản phẩm không có trong danh sách")

    elif option ==4:
        id = input('Nhập ID sản phẩm muốn xóa: ')
        pro_id = int(id)
        pro_del(pro_list, pro_id)
    
    elif option == 5:
        break
    else: 
        print('Bạn đã nhập sai yêu cầu!!')
        option = int(input('Bạn chọn số 1/2/3/4/5: '))

    print(pro_list)
def tra_cuu_gia_ngan_gon():
    # Dữ liệu sản phẩm: {Tên sản phẩm: Giá}
    san_pham = {
        "Laptop XYZ": 15000000,
        "Điện thoại ABC": 8500000,
        "Tai nghe Bluetooth": 1200000
    }
    
    # Tạo danh sách các tên sản phẩm (để hiển thị)
    ds_ten_sp = list(san_pham.keys()) 
    
    print("--- 📋 Danh sách Sản phẩm ---")
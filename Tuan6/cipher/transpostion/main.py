import sys
import os
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6 import uic

# Import các hàm xử lý từ file transpotion.py tương ứng với cấu trúc thư mục
from cipher.transpostion.transpotion import encrypt_transposition, decrypt_transposition

class TranspositionApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Xác định đường dẫn file untitled.ui một cách chính xác
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(current_dir, '..', 'untitled.ui') # Đi ngược ra 1 cấp để tìm file .ui
        
        # Load trực tiếp file giao diện từ Qt Designer
        uic.loadUi(ui_path, self)
        
        # Kết nối các nút bấm trên UI với hàm xử lý (Slots)
        self.btn_gen.clicked.connect(self.generate_random_key)
        self.btn_encrypt.clicked.connect(self.handle_encrypt)
        self.btn_decrypt.clicked.connect(self.handle_decrypt)

    def generate_random_key(self):
        """Tự động tạo Key ngẫu nhiên từ 2 đến 15 khi bấm nút GEN"""
        random_key = random.randint(2, 15)
        # Điền số vừa tạo vào ô Key
        self.key_input.setText(str(random_key))

    def get_key(self):
        """Hàm phụ giúp kiểm tra và lấy giá trị số từ ô Key"""
        key_str = self.key_input.text().strip() if hasattr(self.key_input, 'text') else self.key_input.toPlainText().strip()
        
        if not key_str.isdigit():
            QMessageBox.warning(self, "Lỗi nhập liệu", "Vui lòng nhập hoặc bấm GEN để tạo Khóa (Key) là số nguyên dương!")
            return None
        return int(key_str)

    def handle_encrypt(self):
        key = self.get_key()
        if key is None:
            return
            
        text = self.txt_input.toPlainText()
        if not text:
            QMessageBox.warning(self, "Lỗi nhập liệu", "Vui lòng nhập văn bản cần mã hóa.")
            return
            
        # Gọi hàm xử lý mã hóa
        result = encrypt_transposition(text, key)
        self.txt_output.setPlainText(result)

    def handle_decrypt(self):
        key = self.get_key()
        if key is None:
            return
            
        ciphertext = self.txt_input.toPlainText()
        if not ciphertext:
            QMessageBox.warning(self, "Lỗi nhập liệu", "Vui lòng nhập văn bản cần giải mã.")
            return
            
        # Gọi hàm xử lý giải mã
        result = decrypt_transposition(ciphertext, key)
        self.txt_output.setPlainText(result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TranspositionApp()
    window.show()
    sys.exit(app.exec())
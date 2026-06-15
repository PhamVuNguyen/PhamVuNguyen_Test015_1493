import math

def encrypt_transposition(text, key):
    """Thuật toán mã hóa Columnar Transposition"""
    if not text or key <= 0:
        return ""
    
    ciphertext = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(text):
            ciphertext[col] += text[pointer]
            pointer += key
    return ''.join(ciphertext)

def decrypt_transposition(ciphertext, key):
    """Thuật toán giải mã Columnar Transposition"""
    if not ciphertext or key <= 0:
        return ""
        
    num_of_cols = key
    num_of_rows = int(math.ceil(len(ciphertext) / num_of_cols))
    num_of_shaded_boxes = (num_of_cols * num_of_rows) - len(ciphertext)
    
    plaintext = [''] * num_of_rows
    col = 0
    row = 0
    
    for symbol in ciphertext:
        plaintext[row] += symbol
        row += 1
        if (row == num_of_rows) or (row == num_of_rows - 1 and col >= num_of_cols - num_of_shaded_boxes):
            row = 0
            col += 1
    return ''.join(plaintext)   
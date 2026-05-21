# Koi bhi nayi working image ka naam yahan likhein
image_path = r"C:\Users\PC\Pictures\Screenshots\Screenshot 2025-11-18 214923.png"

with open(image_path, "rb+") as f:
    # 1. Pointer ko file ke bilkul END (aakhri byte) par le jao
    # (0, 2) ka matlab hai: Move 0 bytes from the END of the file
    f.seek(0, 2) 
    
    # 2. Ab bilkul end mein apna secret data write karo
    f.write(b"SECRET_KEY_1234")

print("Data successfully added without corrupting the image!")
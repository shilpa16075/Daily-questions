# Binary file handling is used to read and write data in the form of raw bytes (0s and 1s) instead of plain text, 
# which is essential for processing media like images, videos, and executables.
with open(r"C:\Users\PC\Pictures\Screenshots\Screenshot 2026-05-17 213046.png",'rb') as source:
    data = source.read()

with open(r"C:\Users\PC\Pictures\Screenshots\Screenshot 2026-05-17 213046.png",'wb') as destination:
    data = destination.write("")

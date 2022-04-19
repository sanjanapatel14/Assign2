"""
AIM: Generate PDF file of your 3rd Semester Mark-sheet
"""
from PIL import Image
image1 = Image.open(r'C:\Users\Sanjana\PycharmProjects\pythonProject1\image_result.png')
im1 = image1.convert('RGB')
im1.save(r'C:\Users\Sanjana\PycharmProjects\pythonProject1\image_result_py.pdf')
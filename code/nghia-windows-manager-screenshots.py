import os
import shutil
from datetime import datetime

# Định nghĩa thư mục nguồn và đích
pictures_screenshots_folder = os.path.expanduser("~/Pictures/Screenshots")
nghia_screenshots_folder = os.path.expanduser("~/Pictures/NghiaScreenshots")

# Kiểm tra nếu thư mục nguồn không tồn tại
if not os.path.exists(pictures_screenshots_folder):
    print(f"Thư mục '{pictures_screenshots_folder}' không tồn tại!")
    exit(1)

# Kiểm tra nếu thư mục đích không tồn tại, tạo mới
if not os.path.exists(nghia_screenshots_folder):
    os.makedirs(nghia_screenshots_folder)

# Kiểm tra nếu thư mục nguồn trống, thoát chương trình
if not os.listdir(pictures_screenshots_folder):
    print(f"Thư mục '{
          pictures_screenshots_folder}' không có file, folder, không cần di chuyển.")
    exit()

# Tạo thư mục theo ngày tháng năm
now = datetime.now().strftime("%Y_%m_%d_%H_%M_%S_%f")
destination_path = os.path.join(nghia_screenshots_folder, now)

# Nếu thư mục theo ngày chưa tồn tại, tạo mới
if not os.path.exists(destination_path):
    os.makedirs(destination_path)

# Di chuyển tất cả file và thư mục con từ nguồn sang thư mục đích
for item in os.listdir(pictures_screenshots_folder):
    source_item = os.path.join(pictures_screenshots_folder, item)
    dest_item = os.path.join(destination_path, item)
    shutil.move(source_item, dest_item)
    print(f"Đã di chuyển: {source_item} ➝ {dest_item}")

print("✔️ Hoàn thành di chuyển toàn bộ nội dung!")

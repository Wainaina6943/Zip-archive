import os
import pathlib
import zipfile

def compress_directory(src_dir, dst_dir):
    zip_name = pathlib.Path(src_dir).with_suffix('.zip').name
    zip_path = os.path.join(dst_dir, zip_name)

    if os.path.exists(dst_dir):
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            for root, dirs, files in os.walk(src_dir):
                for file in files:
                    zip_file.write(os.path.join(root, file), arcname=os.path.relpath(os.path.join(root, file), src_dir))
        return zip_path
    else:
        raise FileNotFoundError(f"Directory '{dst_dir}' not found.")

src_dir = "C:/Users/intuser.7032MH2-KEN/Downloads/NEW TASK"
dst_dir = "C:/Users/intuser.7032MH2-KEN/Downloads"
zip_path = compress_directory(src_dir, dst_dir)

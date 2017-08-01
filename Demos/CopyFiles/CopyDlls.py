import os
import shutil

def copyFile(base_root_dir):
    p4_brom_full_dir = base_root_dir.replace("Download_Agent_Main", "brom_full")
    brom_full_lib_dir = os.path.join(p4_brom_full_dir, "lib")
    gui_lib_dir = os.path.join(base_root_dir, "flashtool", "Lib")
    for file_name in os.listdir(brom_full_lib_dir):
        file_extension = os.path.splitext(file_name)[1]
        if file_extension.find("so") == -1:
            src_file = os.path.join(brom_full_lib_dir, file_name)
            dest_file = os.path.join(gui_lib_dir, file_name)
            shutil.copy(src_file, dest_file)


if __name__ == "__main__":
    copyFile(r"D:\WorkSpace\FlashTool\Code\Download_Agent_Main")
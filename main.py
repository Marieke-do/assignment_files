__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

import os
import shutil

cache_folder_path = "./files/cache"
zip_path_data = "./files/data.zip"


# 1. Clean_cache


def clean_cache():
    if os.path.exists(cache_folder_path):
        shutil.rmtree(cache_folder_path)
        os.mkdir(cache_folder_path)
    else:
        return os.mkdir(cache_folder_path)


clean_cache()

# 2. Cache_zip


def cache_zip(zip_path, cache_dir_path):
    shutil.unpack_archive(zip_path, cache_dir_path)


cache_zip(zip_path_data, cache_folder_path)


# 3. Cached_files


def cached_files():
    files_list = []
    # files_list = [os.path.abspath(file) for file in os.listdir(cache_folder_path)]
    # print(files_list)
    # return files_list

    for root, directories, files in os.walk(cache_folder_path):
        for file in files:
            files_list.append(os.path.abspath(os.path.join(root, file)))

    return files_list


print(cached_files()[:3])

# 4. Find_password


def find_password(files_list):
    password_indication = "password"
    for file in files_list:
        with open(file) as f:
            list_of_lines = f.readlines()
            for line in list_of_lines:
                if password_indication in line.lower():
                    print(line)
                    print(f.name)

                    password = line[line.find(" ") + 1:]

                    clean_password = password.rstrip()
                    print(clean_password)

                    return clean_password


find_password(cached_files())

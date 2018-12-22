import shutil
import requests
import settings
import os
import sys

conf = settings.Settings()

if os.path.isdir(conf.save_path):
    # Aborting because the specified path already exists
    sys.exit("Aborting because the Directory '" + conf.save_path + "' already exists! Please define an other Path in the 'settings.py' file.")

os.mkdir(conf.save_path)

for row in range(conf.starting_row, conf.limit_x):
    for col in range(conf.limit_y):

        url = conf.url_trunc + str(row) + conf.separator + str(col) + conf.file_type

        response = requests.get(url, stream=True)
        if response.status_code != 200:
            print("\n" + str(response.status_code) + "\t" + url)
            print("Finished row:" + str(row), end="")
            print(" Downloaded total: " + str(conf.num_files) + " This row: " + str(col))
            print("Working on row: " + str(row+1))
            break
        else:
            with open(conf.save_path + 'imgR' + str(row) + "C" + str(col) + '.png', 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
            if conf.num_files % 10 == 0:
                print(".", end="")
            conf.num_files += 1
            del response

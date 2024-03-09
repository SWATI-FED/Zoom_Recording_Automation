import os
from datetime import datetime

today = datetime.today()

class_dict = {}

def relocate():
    if not os.path.exists('Class JSON'):
        os.makedirs('Class JSON')
    
    with open(f'Class JSON/{str(today)[:10]}.txt', 'w') as f1:
        files = os.listdir('Class Recording')
        print(files)

        for fi in files:
            with open(f'Class Recording/{fi}', 'r') as f:
                f.readline()
                f.readline()
                lines = f.readlines()
                for line in lines:
                    line = line.split('|')
                    # print("Length: ",len(line))
                    if len(line) == 2:
                        class_name = line[0].strip()
                        class_link = line[1].strip()
                        if ',' in class_link:
                            class_link = class_link.split(',')
                            class_dict[class_name] = class_link

                        if class_name not in class_dict:
                            class_dict[class_name] = [class_link]
                        else:
                            class_dict[class_name].append(class_link)
        print(class_dict, file=f1)

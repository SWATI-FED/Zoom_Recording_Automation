from datetime import datetime


def write_class(json_list: list, date: str):
    with open(f'Class Recording/{date}.txt', 'w') as f:
        # Write the Date and Time of creation
        print(f"{json_list[0]['ScheduleDate']}  {datetime.today().time()}", file=f)
        print(file=f)

        try:
            for _class in json_list:
                _class['TimeFrom'] = datetime.strptime(_class['TimeFrom'][:8], '%I:%M %p')
                curr_date = datetime.now()
                _class['TimeFrom'] = datetime(curr_date.year, curr_date.month, curr_date.day,
                                            _class['TimeFrom'].hour, _class['TimeFrom'].minute, 0)
                _class['TimeFrom'] = datetime.strftime(_class['TimeFrom'], '%Y-%m-%d %H:%M:%S')

            # Sort the Data, according to the time
            json_list.sort(key=lambda class_dict: class_dict['TimeFrom'])
            
            text_file = open("sampleData.txt", "w")
            text_file.write(str(json_list))
            text_file.close()
        except:
            print("Probably Classes are not available yet")
        try:
            for line in json_list:
                print(f"{line['SubName']} | {line['Recording']}", file=f)
                print(file=f)
        except:
            print("Probably Classes are not available yet")


def lOF(json_list: list):
    try:
        listOfIDs = [] 
        for line in json_list:
            listOfIDs.append(line['JoinUrl'][18:29])
        print(listOfIDs)
        return listOfIDs
    except:
        print("Probably Classes are not available yet")
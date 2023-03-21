import csv
import datetime
import pytz


def write_to_csv(data):
    india = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
    date = india.date()
    time = india.time()
    file_name = "data-{}.csv".format((str(date) + str(time)).replace(":", "-"))

    if data:
        field_names = list(data[0].keys())
        print(field_names)
        try:
            with open(file_name, 'w', encoding="utf-8") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=field_names)
                writer.writeheader()
                writer.writerows(data)
            return [True,file_name]
        except:
            return [False]
    else:
        return [False]
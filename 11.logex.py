### Ushtrimi 1 ###
# Parse the log file and print an overview of it:
# - how many errors, how many warnings, how many debug, how many info
# - calculate the time from the first log to the last log

from datetime import datetime

with open("django.log.txt", "r") as f:
    logs_dict = {}
    for i, line in enumerate(f.readlines()):
        if i == 0:
            first_log = line

        splitted_line = line.split(" ")
        log_level = splitted_line[2]
        if log_level not in logs_dict:
            logs_dict[log_level] = 1
        else:
            logs_dict[log_level] += 1
        last_log = line

    first_log_splitted = first_log.split(" ")
    last_log_splitted = last_log.split(" ")

    # build the datetime string
    first_log_time_str = first_log_splitted[0] + " " + first_log_splitted[1]
    last_log_time_str = last_log_splitted[0] + " " + last_log_splitted[1]

    # remove milliseconds
    first_log_time_str = first_log_time_str.split(",")[0]
    last_log_time_str = last_log_time_str.split(",")[0]

    first_log_time = datetime.strptime(first_log_time_str, "%Y-%m-%d %H:%M:%S")
    last_log_time = datetime.strptime(last_log_time_str, "%Y-%m-%d %H:%M:%S")

    difference_in_seconds = (last_log_time - first_log_time).total_seconds()

    print(f"The logs lasted {difference_in_seconds}")

    print(logs_dict)

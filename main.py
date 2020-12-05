from datetime import timedelta, datetime
import csv
from os import path

AMOUNT_PER_HOUR = 5
CSV_FILENAME = "records.csv"
CSV_FIELDNAMES = ["Date", "Start Time", "End Time", "Hours Spent", "Amount Earned"]


def convert_input_time(str_time):
    """ converts input time to timedelta """
    t = str_time.strip()
    tm = t[-2:].lower()
    tx = [int(x) for x in t[0:-2].split(":")]

    if tm == "am" and tx[0] == 12 or tm == "pm" and tx[0] != 12:
        tx[0] += 12

    if len(tx) == 1:
        return timedelta(hours=tx[0])
    return timedelta(hours=tx[0], minutes=tx[1])


def calculate_hours(start, end):
    """ returns hours between start and end """
    return (end - start) / timedelta(hours=1)


def calculate_amount(hours, rate=AMOUNT_PER_HOUR):
    """ returns amount earned given hours and hourly rate """
    return hours * rate


def init_csvfile(filename=CSV_FILENAME):
    """ creates csv record file and sets headers """
    with open(filename, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=CSV_FIELDNAMES)
        writer.writeheader()


def write_record(record, filename=CSV_FILENAME):
    """ write an entry into csv record file """
    with open("records.csv", "a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=CSV_FIELDNAMES)
        writer.writerow(record)


def main():
    print("Time tracker")
    print("Enter times in the 12-hour format eg. 6pm or 6:30pm")
    in_start_time = input("Start time: ")
    in_end_time = input("End time: ")

    start_time = convert_input_time(in_start_time)
    end_time = convert_input_time(in_end_time)

    hours = calculate_hours(start_time, end_time)
    amount_earned = calculate_amount(hours)

    if not path.exists(CSV_FILENAME):
        init_csvfile()
    record = {
        "Date": datetime.now(),
        "Start Time": in_start_time.strip(),
        "End Time": in_end_time.strip(),
        "Hours Spent": hours,
        "Amount Earned": amount_earned,
    }
    write_record(record)

    print("Amount earned: ${:,.3f}".format(amount_earned))


if __name__ == "__main__":
    main()
from datetime import timedelta

AMOUNT_PER_HOUR = 5


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


def main():
    print("Time tracker")
    print("Enter times in the format 6pm or 6:30pm")
    in_start_time = input("Start time: ")
    in_end_time = input("End time: ")

    start_time = convert_input_time(in_start_time)
    end_time = convert_input_time(in_end_time)

    hours = calculate_hours(start_time, end_time)
    amount_earned = calculate_amount(hours)

    print("Amount earned: ${}".format(amount_earned))


if __name__ == "__main__":
    main()
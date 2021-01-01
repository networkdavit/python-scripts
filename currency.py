from forex_python.converter import CurrencyRates
import time
import xlsxwriter

t = time.localtime()
current_time = time.strftime("%H:%M", t)

workbook = xlsxwriter.Workbook('Example3.xlsx')
worksheet = workbook.add_worksheet("My sheet")

c = CurrencyRates()
rate = c.get_rates("USD")
available_currency = list(rate.keys())

asking_for_input = True


def delay():
    time.sleep(2)


def write_as_txt(message):
    file = open("Currency Report.txt", "a")
    file.write(message)
    file.close()


def action1(asking_for_input):
    while asking_for_input:
        first_currency = str(input("Enter a currency: ").upper())
        second_currency = str(input("Enter another currency: ").upper())
        if first_currency and second_currency in available_currency:
            result = f"At the moment, one {first_currency} is {c.get_rate(first_currency, second_currency)} {second_currency}: Data recieved at {current_time}"
            print(result)
            asking_for_input = False
            save_as_text = int(input("Do you want to save the data as a text file?: "))
            if save_as_text == 1:
                write_as_txt(result)
                print("Saved as \"Currency Report.txt\"")
        else:
            print(
                f"One or more currencies don't exist\nPlease check the currency list here: \n{available_currency}\nTry Again")


def action2():
    current_rate = (c.get_rate("USD", "RUB"))
    usd_to_rub = [[current_time, current_rate]]
    for i in list(range(1, 4)):
        delay()
        print(i)
        usd_to_rub.append([current_time, current_rate])
        print(usd_to_rub)
    usd_to_rub = tuple(usd_to_rub)
    print(usd_to_rub)
    row = 0
    col = 0
    for date, rate in (usd_to_rub):
        worksheet.write(row, col, date)
        worksheet.write(row, col + 1, rate)
        row += 1

    workbook.close()


def main():
    mode = int(input("Do you want to convert currencies or get data sent every 10 seconds?: "))
    if mode == 1:
        action1(asking_for_input)
    if mode == 2:
        action2()


if __name__ == "__main__":
    main()

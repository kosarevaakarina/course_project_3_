from func import *

data = open_file('operations.json')
sorted_data = sorted_by_executed_and_date(data)

for i in sorted_data:
    print(f"\n{formatted_date(i)} {get_description(i)}")
    print(f"{get_sender(i)} -> {get_recipient(i)}")
    print(f"{get_transfer_amount(i)} {get_currency(i)}")


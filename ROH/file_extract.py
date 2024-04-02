from .login_info import *
from .file_dates import *
import pandas as pd
import numpy as np


def delete_all_csv_fies() -> None:
    dir_list = os.listdir(FILE_LOCATION)
    for file in dir_list:
        if file.endswith(".csv"):
            os.remove(FILE_LOCATION + "/" + file)


def is_it_a_bottle(test_str: str) -> bool:
    if test_str.find("125ml") != -1:
        return False
    if test_str.find("100ml") != -1:
        return False
    if test_str.find("175ml") != -1:
        return False
    return True


def get_list_of_orders() -> list:
    # df of csv
    df = pd.read_csv(FILE_LOCATION + "/" + file_name)

    # output list
    order_list = []

    for stings in df['Pre-order']:
        if stings is np.nan:
            continue
        list_str: list = stings.split("\n")
        wine_filter_list_str: list = list(filter(lambda x: x.find("Bin") != -1, list_str))
        glass_filter_list_str: list = list(filter(is_it_a_bottle, wine_filter_list_str))
        order_list.extend(glass_filter_list_str)

    return order_list

def format_email_order(order_list:list)->str:
    return "\n".join(order_list)

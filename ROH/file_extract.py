import pandas as pd
import numpy as np

from .login_info import *
from .file_dates import *


def delete_all_csv_fies() -> None:
    """
    deletes all csv files in the FILE_LOCATION folder
    """
    dir_list = os.listdir(FILE_LOCATION)
    for file in dir_list:
        if file.endswith(".csv"):
            os.remove(FILE_LOCATION + "/" + file)


def is_it_a_bottle(test_str: str) -> bool:
    """
    will return true if the order is bottle sized,
    else false for glass sized
    :param test_str:
    :return:
    """
    if test_str.find("125ml") != -1:
        return False
    if test_str.find("100ml") != -1:
        return False
    if test_str.find("175ml") != -1:
        return False
    return True


def get_list_of_orders() -> list:
    """
    imports the order list from the csv file
    :return: list of orders
    """
    # df of csv
    df = pd.read_csv(FILE_LOCATION + "/" + file_name)

    # if len(df.index) == 0:
    #     return []

    # output list
    order_list = []

    for stings in df['Pre-order']:
        if stings is np.nan or None:
            continue
        list_str: list = stings.split("\n")
        wine_filter_list_str: list = list(filter(lambda x: x.find("Bin") != -1, list_str))
        glass_filter_list_str: list = list(filter(is_it_a_bottle, wine_filter_list_str))
        order_list.extend(glass_filter_list_str)

    return order_list


def format_email_order(order_list: list) -> str:
    """
    format order list for email form
    :param order_list:
    :return: str of orders
    """
    return "\n".join(order_list)


def create_error_txt_file(input_str: str) -> None:
    """
    creates a txt file when an error happens in the FILE_LOCATION
    :param input_str:
    :return:
    """
    with open(f"{FILE_LOCATION}/error_file_{date_of_order.strftime(date_format_full)}.txt", "w") as f:
        f.write(f"For order date: {date_of_order.strftime(date_format_full)} \n"
                f"Error: {input_str}")

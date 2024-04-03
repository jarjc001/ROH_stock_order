from playwright.sync_api import sync_playwright

import ROH as roh


roh.delete_all_csv_fies()

with sync_playwright() as playwright:
    roh.run(playwright, roh.FILE_LOCATION )

try:
    wine_list: list = roh.get_list_of_orders()

    wine_order: str = roh.format_email_order(wine_list)

    roh.create_email(wine_order)

except FileNotFoundError:
    roh.create_error_txt_file("No csv file found")
except AttributeError:
    roh.create_error_txt_file("csv file is empty")
except:
    roh.create_error_txt_file("Error happened")






from playwright.sync_api import sync_playwright
import ROH as roh


roh.delete_all_csv_fies()

with sync_playwright() as playwright:
    roh.run(playwright, roh.FILE_LOCATION )


wine_list: list = roh.get_list_of_orders()

wine_order = roh.format_email_order(wine_list)

roh.create_email(wine_order)
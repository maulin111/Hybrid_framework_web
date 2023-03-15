from utilities import read_utils

test_add_jacket_product_data=read_utils.get_sheet_as_list("../test_data/product_test_data.xlsx","test_add_jacket_product")

test_invalid_login_data = read_utils.get_csv_as_list("../test_data/test_invalid_login_data.csv")

test_shipping_address_data = read_utils.get_sheet_as_list("../test_data/product_test_data.xlsx","test_shipping_address")
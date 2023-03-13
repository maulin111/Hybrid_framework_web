import pandas


def get_csv_as_list(file_path):
    df = pandas.read_csv(filepath_or_buffer=file_path, delimiter=";")
    return df.values.tolist()

def get_sheet_as_list(filepath, sheetname):
    df = pandas.read_excel(io = filepath,sheet_name=sheetname)
    return df.values.tolist()

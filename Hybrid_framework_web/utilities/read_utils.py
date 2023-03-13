import pandas

def get_sheet_as_list(filepath, sheetname):
    df = pandas.read_excel(io = filepath,sheet_name=sheetname)
    return df.values.tolist()
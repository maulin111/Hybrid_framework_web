""" This file will be deleted. Not part of the framework
To understand - how to read csv, excel, json """
import pandas


df=pandas.read_csv(filepath_or_buffer="../test_data/test_invalid_login_data.csv",delimiter=";")

print(df)
print(df.loc[0])

print(df.loc[0].tolist())
print(list(df.loc[0]))
print(tuple(df.loc[0]))

print(df.loc[0].tolist())
print(df.loc[1].tolist())

print(df.index)
print(60*"-")

"""rows to be converted into list of list or list of tuple"""
# print(df.values)
# print(df.values.tolist())


# print(df.loc[0].tolist())
# print(df.loc[1].tolist())
#
# list=[df.loc[0].tolist(),df.loc[1].tolist()]
# print(list)
list=[]
for i in df.index:
    print(df.loc[i].tolist())
    list.append(df.loc[i].tolist())

print(list)

list=[]
for i in df.index:
    print(tuple(df.loc[i]))
    list.append(tuple(df.loc[i]))

print(list)


print(df.values.tolist())
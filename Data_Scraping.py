try:
    import tabula as tb
    import pandas as pd
    import re
    from tabula.io import read_pdf
    from tabula.io import convert_into
except:
    print('you should install packages first using this codes in Command Prompt')
    print('pip install tabula-py and pip install pandas')
    print('It is very important to use Command Prompt if you on windows')


file = "23.pdf"
#To read table in first pageof PDF file
#table1 = read_pdf(file,pages=3)
# To read tables in secord page of PDF file
#table2 = read_pdf(file,pages=4)
#print(table1)
#print(table2)
#convert_into(file,"23.csv",pages = '4')
#data = tb.read_pdf(file, area = (300, 0, 600, 800), pages = '4')
#data= tb.read_pdf(file, pages = '1', area = (0, 0, 1000, 1000), columns = [200, 265, 300, 320], pandas_options={'header': None}, stream=True)[0]
#print(data)
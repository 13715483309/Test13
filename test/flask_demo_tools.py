import csv


def reg_write_csv(name,passwd):
    path = 'data.csv'
    with open(path,'a+',encoding='utf-8') as f:
        reg_write_csv = csv.writer(f)
        data_row = [name,passwd]
        reg_write_csv.writerow(data_row)

def login_read(name,passwd):
    path = 'data.csv'
    with open(path,encoding='utf-8') as f:
        read = csv.reader(f)
        for row in read:
            if name in row and passwd in row:
                return True
        return False
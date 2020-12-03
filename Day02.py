from xlrd import open_workbook

wb = open_workbook('Day02.xlsx')
for s in wb.sheets():
    passwords = []
    for row in range(s.nrows):
        col = 0
        data = (s.cell(row,col).value)
        passwords.append(data)

# Input data was saved to an Excel XLSX file and read using above

--- Part One ---

valid_count = 0

def check_password(password):
    colon = password.index(':')
    if colon == 5:
        min = int(password[0])
        max = int(password[2])
    elif colon == 6:
        min = int(password[0])
        max = int(password[2:4])
    elif colon == 7:
        min = int(password[0:2])
        max = int(password[3:5])
    result=password.count(password[colon-1])-1        
    valid = result in range(min,(max+1))
    return valid


for i,password in enumerate(passwords):
    if check_password(password):
        valid_count += 1
    else:
        continue
print(valid_count)

--- Part Two ---

valid_count = 0

def check_password(password):
    colon = password.index(':')
    if colon == 5:
        char1 = int(password[0])
        char2 = int(password[2])
    elif colon == 6:
        char1 = int(password[0])
        char2 = int(password[2:4])
    elif colon == 7:
        char1 = int(password[0:2])
        char2 = int(password[3:5])
    password_string = password.partition(': ')[2]
    key_char = password[colon-1]
    if (bool(password_string[char1-1] == key_char) ^ bool(password_string[char2-1] == key_char)):
        return True
    else:
        return False

for i,password in enumerate(passwords):
    if check_password(password):
        valid_count += 1
    else:
        continue
print(valid_count)

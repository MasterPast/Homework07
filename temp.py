data = ['X', 'X', 'X', 'Z', 'Z', 'X', 'X', 'Y', 'Y', 'Y', 'Z', 'Z']
     #   0    1    2    3    4
txt = ''
def encode(data):
    global txt
    ind = 0
    count = 1
    balance = None

    if not data:
        return []

    if len(data) <= 2:
        print('PPZD', len(data))
        if data[ind] == data[ind+1]:
            enc = [data[ind], count+1]
            return enc
        else:
            enc = [data[ind], 1, data [ind+1], 1]
            return enc

    while len(data) > 2:
        print(ind)
        print('dfdsf', len(data))
        print(txt)
        if data[ind] == data[ind+1]:
            enc = [data[ind], count+1]
            txt += data[ind]+str(count+1)
        else:
            print(777)
            balance = data[ind+1:]
            print(f'else len>>{len(data)} ind>>{ind} count>>{count} enc>>{enc} bal>>{balance}')
            txt+=data[ind]+str(count)
            enc = [data[ind], count]
            enc.extend(encode(balance))
            print(2345345345) 
            print(enc)
            return enc   
        ind += 1
        count += 1
        print(f'!!!len>>{len(data)} ind>>{ind} count>>{count} enc>>{enc} bal>>{balance}')

    
print(encode(data))
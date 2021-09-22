driving = input('你有沒有開過車:')
if driving != "有" and driving != '沒有':
    print('請輸入有or沒有')
    raise SystemExit
age = input('請問你年齡?')
if driving == '有':
    if int(age) >= 18:
        print('擬通過測驗了')
    else:
        print('開三小死屁孩')
elif driving == '沒有':
    if int(age) >=18:
        print('快去考照阿')
    else:
        print('很好在等等')

from random import choice

# 1:剪刀, 2:石頭, 3:布
com = choice([1, 2, 3])
hu = input('請出拳(1:剪刀, 2:石頭, 3:布)')
hu = int(hu)
if hu == com:
    print('這次平手')
elif hu - com == 1 or hu - com == -2:
    print('算你利害，你贏了')
else:
    print('哈哈，還是我強')

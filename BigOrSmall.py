import random

winTimes = 0
loseTimes = 0
# 加载游戏进度
try:
    # with ... as: 常用于打开文件操作，当代码块结束后文件会自动被关闭
    with open('record.txt', 'r') as f:
        winTimes = int(f.readline())
        loseTimes = int(f.readline())
        print('历史战绩：赢', winTimes, ",输", loseTimes)
except FileNotFoundError as e:
    pass

while True:
    guess = input("猜大还是猜小？ 2-大，1-小:")
    if guess == 'exit':
        break
    if guess != '1' and guess != '2':
        print('本轮弃权！')
        print('')
        continue
    dice = random.randint(1,6)
    print('骰子丢出了', dice)
    if dice <= 3 and guess == '1':
        print('你赢了！')
        winTimes = winTimes + 1
    elif dice >=4 and guess == '2':
        print('你赢了！')
        winTimes = winTimes + 1
    else:
        print('你输了~')
        loseTimes = loseTimes + 1
    print('当前赢', winTimes, ",输" , loseTimes)
    print('')

# 保存游戏进度
with open('record.txt', 'w') as f:
    print('保存游戏进度...')
    f.write(str(winTimes))
    f.write('\n')
    f.write(str(loseTimes))
    print('保存完成！')
import time
#https://www.youtube.com/watch?v=SqvVm3QiQVk&t=40s
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        t -= 1
    
    print('Done!')

if __name__ == '__main__':
    t = input('Enter the timer in seconds : ')
    countdown(int(t))
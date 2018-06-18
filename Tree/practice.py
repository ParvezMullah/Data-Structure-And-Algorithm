def hello():
    def h(x):
        if x == 3:
            return 'yes'
        elif x > 3:
            return h(x-1)
        else:
            return h(x + 1)
    d = h(1)
    print(d)

if __name__ =='__main__':
    hello()
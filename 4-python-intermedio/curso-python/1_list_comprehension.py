def run():
    my_list = []
    for i in range(1,101):
        if i%3 != 0:
            my_list.append(i*2)
    print(my_list)

    my_other_list = [x*2 for x in range(1,101) if x%3 != 0]
    print(my_other_list)

    my_third_list = [y for y in range(1,9999) if y%4 == 0 and y%6 == 0 and y%9 == 0] 
    print(my_third_list)   

if __name__ == '__main__':
    run()

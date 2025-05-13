while True:
    n = int(input('masukkan banyak data: '))
    data= []

    for i in range(n):
        print()
        x = float(input(f'input x ke-{i+1}: '))
        if x >= 0:
            fx = 4 * x**3 + 7 * x - 5
        else:
            fx = 3 * x**2 - 5 * x + 1
        gx = fx**2 - fx
        hx = fx * gx
        data.append((i+1,x,fx,gx,hx))

        if x >= 0:
            print('f(x) = 4 * x**3 + 7 * x - 5 ')
        else:
            print('f(x) = 3 * x**2 - 5 * x + 1 ')
        print('g(x) = f(x)**2 - f(x) ')
        print('h(x) = fx * gx ')

    print()
    print(f'{'No':<5}{'x':<10}{'f(x)':<15}{'g(x)':<20}{'h(x)':<25}')
    for d in data:
        print(f'{d[0]:<5}{d[1]:<10}{d[2]:<15}{d[3]:<20}{d[4]:<25}')

    print()
    ulang = input('input nilai x lagi Y/N? ')
    if ulang != 'Y':
        break
        



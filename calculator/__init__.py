from calculator.Model import Calculator

if __name__ == '__main__':
    calc = Calculator(int(input('1st')), int(input('2nd')))
    print('{} + {} = {}'.format(calc.first, calc.second, calc.sum()))
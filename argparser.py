import argparse  # импорт нужного модуля, который работат поверх sys.argv

# аргументы могут быть позицинными и именованными(optional)

# частый пример использования optional
parser = argparse.ArgumentParser()  # создаем обьект класса ArgumentParser
parser.add_argument("-n", "--number_conftest", help="get number of conftest", default="190")  # если ничего не переданно, использует default
parser.add_argument("-l", "--letter_task", help="get letter of task")
parser.add_argument("-p", "--programm", help="input task code")
args = parser.parse_args()
# call  python3 argparser.py -l J -p code = Namespace(letter_task='J', number_conftest='190', programm='code')
print(args)



#ACTION параметр
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--flag", help="input task code")
parser.add_argument("-f", "--flag", help="input task code", action="store_const", const='10')
#  если флаг передан подставит 10, если ничего None
# call python3 argparser.py -f  = Namespace(flag='10')
parser.add_argument("-s", "--store", help="try get True", action="store_true")
# аналогично, флаг передан подставит True
# call python3 argparser.py -s = Namespace(store=True)
parser.add_argument("-n", "--numbers", help="get values for one argumnent", nargs=2)
# можно положить в 1 аргумент несколько значений
# call python3 argparser.py -n 12 50 = Namespace(numbers=['12', '50'])
parser.add_argument("-ch", "--choices", help="choice argument only from parametrise", choices=['1', '2'])
# call python3 argparser.py -ch 12 =  invalid choice: '12' (choose from '1', '2')

args = parser.parse_args()
print(args)
#


# позиционные - должны быть переданны в строгом порядке, как вычитываются
parser = argparse.ArgumentParser()
parser.add_argument("a", type=int, help="first argument")  # по дефолту принимает type=str, но можно указать тип данных
args = parser.parse_args()
# args содержит Namespace(a=7), можно обратится к аргументу args.a для использования
# call  python3 argparser.py 7 - передали аргумент


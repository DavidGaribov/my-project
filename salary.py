print('Расчёт заработной платы оператора видеонаблюдения ООО "Бэст Прайс" \n~D. Gariboff aka b@dun007~ \nv. 1.23.2')
print()


def main():
    shift_pay = 5177.33
    days = int(input('-Введите количество отработанных смен: '))
    acts = int(input('-Введите количество отработанных актов: '))
    scales = int(input('-Введите количество докладных по весовому контролю: '))
    defective = int(input('-Введите количество докладных по браку: '))
    raw_material = int(input('-Введите количество докладных по контролю сырья: '))
    bonus = int(input('-Введите премию: '))
    fine = int(input('-Введите штраф: '))

    calculation(shift_pay, days, acts, scales, defective, raw_material, bonus, fine)


def tax(x):
    n = x - (x * (13 / 100))
    return n


def calculation(shift_pay, days, acts, scales, defective, raw_material, bonus, fine):
    salary = days * shift_pay + ((acts + scales) * 60) + ((raw_material + defective) * 100) + bonus
    prepaid = tax(13900)
    total_salary = (tax(salary) - fine) - prepaid
    accrued = total_salary + prepaid
    print()
    print(f'= Всего начислено {round(accrued, 1)}р. = \nИз них: '
          f'\n-зарплата {round(total_salary, 1)}р. \n-аванс {round(prepaid, 1)}р.')
    print()
    user_action()


def user_action():
    user_choice = int(input('Сделайте выбор:\n'
                            '0 - Завершить работу\n'
                            '1 - Повторить расчёт\n'
                            '-Ввод: '))
    print()
    choice(user_choice)


def choice(a):
    if a == 0:
        print('Денег нет, но вы держитесь!®')
    elif a == 1:
        print('Когда пересчитываешь зарплату, понимаешь, что ещё один месяц прожит зря.')
        print()
        main()
    else:
        print('Ошибка ввода.')
        print()
        user_action()


if __name__ == "__main__":
    main()

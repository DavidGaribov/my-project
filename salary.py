print('Расчёт заработной платы оператора видеонаблюдения ООО "Бэст Прайс" \n~D. Gariboff aka b@dun007~ \nv. 1.23.1')
print()


def main():
    shift_pay = 5177.33
    while True:
        days = int(input('-Введите количество отработанных смен: '))
        if check(days):
            break
        else:
            print('Ошибка ввода. Необходимо ввести целое положительное число.')
    while True:
        acts = int(input('-Введите количество отработанных актов: '))
        if check(acts):
            break
        else:
            print('Ошибка ввода. Необходимо ввести целое положительное число.')
    while True:
        scales = int(input('-Введите количество докладных по весовому контролю: '))
        if check(scales):
            break
        else:
            print('Ошибка ввода. Необходимо ввести целое положительное число.')
    while True:
        defective = int(input('-Введите количество докладных по браку: '))
        if check(defective):
            break
        else:
            print('Ошибка ввода. Необходимо ввести целое положительное число.')
    while True:
        raw_material = int(input('-Введите количество докладных по контролю сырья: '))
        if check(raw_material):
            break
        else:
            print('Ошибка ввода. Необходимо ввести целое положительное число.')
    while True:
        bonus = int(input('-Введите премию: '))
        if check(bonus):
            break
        else:
            print('Ошибка ввода. Необходимо ввести целое положительное число.')
    while True:
        fine = int(input('-Введите штраф: '))
        if check(fine):
            break
        else:
            print('Ошибка ввода. Необходимо ввести целое положительное число.')

    calculation(shift_pay, days, acts, scales, defective, raw_material, bonus, fine)


def check(c):
    return c >= 0 and isinstance(c, int)


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

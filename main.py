from classes import *

def main():
    bachelor = Bachelor('NURE', "KIU", "KI",2016,2019, 99)
    print('Бакалавр | университет: ', bachelor.get_university())
    print('Бакалавр | факультет: ', bachelor.get_faculty())
    print('Бакалавр | специальность: ', bachelor.get_specialty())
    print('Бакалавр | год начала обучения: ', bachelor.get_year_of_starting())
    print('Бакалавр | год конца обучения: ', bachelor.get_year_of_ending())
    print('Бакалавр | средний балл: ', bachelor.get_avg_mark())
    print('Бакалавр | работает?: ', bachelor.get_is_working())
    print('Пробуем оставить бакалавра на дальнейшее обучение...')
    bachelor.stay_to_study()
    print('Пробуем показать документ бакалавра...')
    bachelor.show_document()
    print('Пробуем устроиться на работу бакалавром...')
    bachelor.apply_for_a_job()
    print('Бакалавр | работает?: ', bachelor.get_is_working())
    print('Пробуем уволиться с работы бакалавром...')
    bachelor.quit_work()
    print('Бакалавр | работает?: ', bachelor.get_is_working())

    master = Master('NURE', "KIU", "KI",2016,2021, 50)
    print('Магистр | университет: ', master.get_university())
    print('Магистр | факультет: ', master.get_faculty())
    print('Магистр | специальность: ', master.get_specialty())
    print('Магистр | год начала обучения: ', master.get_year_of_starting())
    print('Магистр | год конца обучения: ', master.get_year_of_ending())
    print('Магистр | средний балл: ', master.get_avg_mark())
    print('Магистр | работает?: ', master.get_is_working())
    print('Пробуем оставить магистра на дальнейшее обучение...')
    master.stay_to_study()
    print('Пробуем показать документ магистра...')
    master.show_document()
    print('Пробуем устроиться на работу магистром...')
    master.apply_for_a_job()
    print('Магистр | работает?: ', master.get_is_working())
    print('Пробуем попросить повышение до директора магистром...')
    master.get_director_promotion()
    print('Пробуем уволиться с работы магистром...')
    master.quit_work()
    print('Магистр | работает?: ', master.get_is_working())

    engineer = Engineer('NURE', "KIU", "KI",2016,2022, 70)
    print('Инженер | университет: ', engineer.get_university())
    print('Инженер | факультет: ', engineer.get_faculty())
    print('Инженер | специальность: ', engineer.get_specialty())
    print('Инженер | год начала обучения: ', engineer.get_year_of_starting())
    print('Инженер | год конца обучения: ', engineer.get_year_of_ending())
    print('Инженер | средний балл: ', engineer.get_avg_mark())
    print('Инженер | работает?: ', engineer.get_is_working())
    print('Инженер | преподает?: ', engineer.get_is_teaching())
    print('Пробуем оставить инженера на дальнейшее обучение...')
    engineer.stay_to_study()
    print('Пробуем показать документ инженера...')
    engineer.show_document()
    print('Пробуем устроиться на работу инженером...')
    engineer.apply_for_a_job()
    print('Инженер | работает?: ', engineer.get_is_working())
    print('Пробуем попросить повышение до директора инженером...')
    engineer.get_director_promotion()
    print('Пробуем уволиться с работы инженером...')
    engineer.quit_work()
    print('Инженер | работает?: ', engineer.get_is_working())
    print('Попробуем начать преподавать инженером...')
    engineer.start_teaching()
    print('Инженер | преподает?: ', engineer.get_is_teaching())

if __name__ == '__main__':
    main()

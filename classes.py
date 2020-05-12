# Создать иерархию классов Выпускник
# вуза, Бакалавр, Магистр, Инженер. Класс Выпускник вуза должен
# содержать атрибуты и методы, общие для производных классов. Основная
# программа должна создавать массивы объектов производных классов и
# выводить их на экран.

from abc import ABC, abstractmethod
from random import randint

# По заданию не сказано, должен ли класс выпусника вуза быть абстрактным,
# Считаю, что правильнее реализовать абстрактный
class UniversityGraduate(ABC):
    @abstractmethod
    def __init__(self, university, faculty, specialty,year_of_starting, year_of_ending, avg_mark, is_working=False):
        self.set_university(university)
        self.set_faculty(faculty)
        self.set_specialty(specialty)
        self.set_year_of_starting(year_of_starting)
        self.set_year_of_ending(year_of_ending)
        self.set_avg_mark(avg_mark)
        self.set_is_working(is_working)

    def set_university(self, university):
        self.__university = university

    def get_university(self):
        return self.__university

    def set_faculty(self, faculty):
        self.__faculty = faculty

    def get_faculty(self):
        return self.__faculty

    def set_specialty(self, specialty):
        self.__specialty = specialty

    def get_specialty(self):
        return self.__specialty

    def set_year_of_starting(self, year_of_starting):
        self.__year_of_starting = year_of_starting

    def get_year_of_starting(self):
        return self.__year_of_starting

    def set_year_of_ending(self, year_of_ending):
        self.__year_of_ending = year_of_ending

    def get_year_of_ending(self):
        return self.__year_of_ending

    def set_avg_mark(self, avg_mark):
        if avg_mark > 0 and avg_mark <= 100:
            self.__avg_mark = avg_mark
        else:
            print('Балл должен быть от 0 до 100 включительно!')

    def get_avg_mark(self):
        return self.__avg_mark

    def set_is_working(self, is_working):
        self.__is_working = is_working

    def get_is_working(self):
        return self.__is_working

    @abstractmethod
    def stay_to_study(self, next_status):
        if self.__avg_mark > 60:
            print('OK! Баллы позволили идти учиться дальше на {}a!'.format(next_status))
        else:
            print('Упс. Слишком мало баллов')

    @abstractmethod
    def show_document(self):
        pass

    @abstractmethod
    def apply_for_a_job(self, percent):
        print('[ Вероятность устроиться на работу = {}% ]'.format(percent))
        r = randint(0, 100)
        if r <= percent:
            print('Поздравляю! Вы устроились на работу!')
            self.set_is_working(True)
        else:
            print('Эх. Устроиться не удалось. Попробуйте в следющий раз!')

    def quit_work(self):
        if self.__is_working:
            print('Ок, вы уволились.')
            self.set_is_working(False)
        else:
            print('Чтоб уволиться нужно сначала найти работу...')


class Bachelor(UniversityGraduate):
    def __init__(self, university, faculty, specialty, year_of_starting, year_of_ending, avg_mark, is_working=False):
        super().__init__(university, faculty, specialty, year_of_starting, year_of_ending, avg_mark, is_working)

    def show_document(self):
        print('Документ: "БАКАЛАВР!"')

    def stay_to_study(self):
        next_status = 'Магистр'
        super().stay_to_study(next_status)

    def apply_for_a_job(self):
        super().apply_for_a_job(30)


class Master(UniversityGraduate):
    def __init__(self, university, faculty, specialty, year_of_starting, year_of_ending, avg_mark, is_working=False):
        super().__init__(university, faculty, specialty, year_of_starting, year_of_ending, avg_mark, is_working)

    def show_document(self):
        print('Документ: "МАГИСТР!"')

    def stay_to_study(self):
        next_status = 'Инженер'
        super().stay_to_study(next_status)

    def get_director_promotion(self):
        if not self.get_is_working():
            print('Вы не можете стать директором, не работая.')
        else:
            print('Так как вы имеете оконченное высшее (Магистратура), Вы можете по-закону работать директором, поздравляю!')


    def apply_for_a_job(self):
        super().apply_for_a_job(60)


class Engineer(UniversityGraduate):
    def __init__(self, university, faculty, specialty, year_of_starting, year_of_ending, avg_mark, is_working=False, is_teaching = False):
        super().__init__(university, faculty, specialty, year_of_starting, year_of_ending, avg_mark, is_working)
        self.set_is_teaching(is_teaching)

    def get_is_teaching(self):
        return self.__is_teaching

    def set_is_teaching(self, is_teaching):
        self.__is_teaching = is_teaching

    def show_document(self):
        print('Документ: "ИНЖЕНЕР!"')

    def stay_to_study(self):
        print('Вы уже инженер! Но можете пройти курсы!')

    def apply_for_a_job(self):
        super().apply_for_a_job(98)

    def get_director_promotion(self):
        if not self.get_is_working():
            print('Вы не можете стать директором, не работая.')
        else:
            print('Так как вы имеете оконченное высшее (Инженерия), Вы можете по-закону работать директором, поздравляю!')

    def start_teaching(self):
        print('Вы инженер, так что, можете преподавать на здоровье!')
        if not self.get_is_working():
            self.set_is_teaching(True)

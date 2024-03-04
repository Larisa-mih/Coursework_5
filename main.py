from DBManager import DBManager
from hh_api import hh_api


def main():
    print("Добро пожаловать в программу по поиску вакансий с сайта hh.ru")
    hh_api()
    db = DBManager()
    db.create_database()
    print('База Данных "course_work" успешна создана')
    db.create_table()
    print('Таблица "head_hunter_vacancies" успешна создана')
    db.insert_into_table()
    print('Таблица "head_hunter_vacancies" заполнена данными')
    print("Для просмотра списка всех вакансий - нажмите  '1'\n"
          "Для выбора вакансии по ключевому слову - нажмите  '2'")
    choice = input()
    if choice == '1':
        print(f'Список всех вакансий: {db.get_all_vacancies()}')
    elif choice == '2':
        word = input("Введите ключевое слово для поиска ").title()
        print(db.get_vacancies_with_keyword(word))
    else:
        print("Для выхода из программы - нажмите  '1' \n"
              "Вернуться к поиску - нажмите  '2'")
        choice2 = input()
        if choice2 == '1':
            quit()
        elif choice2 == '2':
            main()

    print(f'Список компаний с их количеством вакансий: {db.get_companies_and_vacancies_count()}')
    print(f"Средняя зарплата по данным вакансиям: {db.get_avg_salary()} рублей")
    print(f"Вакансии, зарплата которых выше средней: {db.get_vacancies_with_higher_salary()}")


if __name__ == '__main__':
    main()

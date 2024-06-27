"""text for tg_bot"""

class text_1():
    """
    A class representing text for use in bot scripts

    IMPORTANT: The text is mainly before registration and during registration


    Example of using a class:
    """
    t_start_1 = "Привет! Меня зовут Белка!"
    t_start_2 = "Я помогу тебе найти попучтика для совместной поездки."
    t_agreement_1 = "Ознакомьтесь с пользовательским соглашением."
    t_agreement_2 = "Спасибо, что согласились!"
    t_agreement_3 = "Печалька"
    t_agreement_4 = "Можете ознакомиться с условиями соглашения ниже:"
    t_start_3 = "Для начала нужно зарегистрироваться!"
    t_reg_name_1 = "Отлично, давай начнем"
    t_reg_name_2 = "Введите своё имя\n(например: Иван)"
    t_reg_name_3 = "Отлично! Теперь введи фамилию\n(например: Иванов)"
    t_reg_name_4 = "Прекрасно! Теперь введи номер телефона\n(например: 89781457632)\nИли нажми на кнопку, чтобы отправить его автоматически."
    t_curse = "Не используйте мат, пожалуйста"
    t_about = "Раздел: О сервисе"
    t_time = "Cекундочку..."
    t_welcome = "Раздел: Главное меню"
    t_mistake = "Упс... Ошибочка вышла 🤷‍♂️"
    t_first_welcome = """Поздравляю! Теперь у тебя есть доступ к главному меню.
Перейдя в раздел "Создать поездку", ты сможешь найти попутчиков."""
    t_foolproof_buttons = "Используй, пожалуйста, предложенные кнопки!"
    t_foolproof_correct_data = "Вводи, пожалуйста, корректные данные!"

class text_2():
    """
    A class representing text for use in bot scripts

    IMPORTANT: The text is mainly intended for the main menu and its sections

    Example of using a class:
    """
    t_FAQ = """
1. Этот сервис только для студентов ДГТУ?\n
На данном этапе бот предназначен только для сотрудников и студентов ДГТУ, но в будущем мы планируем расширяться для  других ВУЗов, поэтому можете оставить свои контакты, чтобы узнать первым о запуске!\n
2. Как быстро придет машина?\n
Чтобы было больше шансов найти подходящего попутчика, рекомендуем вам планировать поездки заранее. Например, с вечера предыдущего дня, если утром следующего дня вам нужно совершить поездку или хотя бы за несколько часов.\n
3. Где мне встретиться с водителем?\n
Если точка А — главный кампус, универсальнее всего встретиться перед главным корпусом, где стоит памятник Юрию Гагарину. Точка А — кампус на Социалистической, то место встречи у входа в 21 корпус. На Шаповалова встреча перед КПП. Но у вас есть контакт попутчика, вы можете договориться напрямую.\n
4. Как происходит оплата?\n
Сразу после бронирования поездки у попутчика происходит списание с баланса фиксированной суммы. В случае отмены поездки не позже чем за час, средства будут возвращены, иначе они остаются в качестве компенсации водителю.)
"""
    t_rules = """
Спутник - информационный сервис.\n
Транспортные услуги оказываются партнерами сервиса\n
Сервис не отвечает за безопасность обеих сторон во время поездки, поэтому рекомендуем:\n
- не провоцировать конфликт и самим не поддаваться на провокации;\n
- следить за дорогой даже если вы - попутчик;\n
- соблюдать правила ПДД\n
"""
    t_about = """
Этот телеграмм-бот облегчает передвижение студентов и сотрудников ДГТУ между кампусами.\n
С помощью него можно создать совместную поездку водителя и пассажира(-ров), при этом водитель получает прибыль от оказанной услуги, а попутчик получает комфортную поездку по доступной цене.\n
"""
    t_support = """
Техническая поддержка работает каждый день 10:00 - 22:00.
\nВы можете написать на почту hello.sputnik@ya.ru или написать @baze1evs"""
    t_no_active_trips = "Нет активных поездок"
    t_technical_maintenance = "Проводится техническое обслуживание, попробуй повторить запрос чуть позже"


class text_3():
    """
    A class representing text for use in bot scripts

    IMPORTANT: The text is mainly intended for the section creating a trip

    Example of using a class:
    """
    t_go = "Поехали 🚀"
    t_get_dateAboutUser_typeOfMembers = "Для начало выбери свой статус для поездки: пассажир или водитель"
    t_get_dateAboutUser_carData = "Ты поедешь на машине:"
    t_get_tripNumberOfPassengers = "Какое максимально количество пассажиров ты сможешь подвезти?\n(Например: 2) "
    t_get_dateAbout_tripDates = "Отлично! Теперь выбери дату поездки"
    t_get_dateAbout_tripTimes = "Отлично! Теперь выбери время поездки"
    t_get_dateAbout_tripPointA = "Отлично! Теперь выбери откуда 'стартуем'"
    t_get_dateAbout_tripPointB = "Отлично! Теперь выбери куда 'приземляемся'"
    t_check = "Записать данные?\nДанные поездки:"
    t_get_dateAbout_tripRoute = "Отлично! Теперь нужный маршрут!"
    t_ok = "Данные записаны, ищем подходящих попутчиков ⏲"
    t_ok_1 = "Данные записаны."
    t_thePointsAreEqual = "Кажется, мы не сможем продвинуться с места.\nПостарайся, пожалуйста, выбирать разные кампусы в следующий раз."

    # dato about car
    t_noCarInTheDataBase_carBrand = "Для того чтобы попутчик смог распознать твою ракету нам необходимо уточнить некоторые данные.\nВыбери бренд своей машины"
    t_noCarInTheDataBase_carModel = "Теперь необходимо выбрать модель"
    t_carColour = "Отлично! Теперь введи цвет машины\n(например 'Белый')"
    t_carNumb = "Отлично! Теперь введи номера машины\n(например 'ЕРЕ177')"
    t_check_car = "Пожалуйста, проверь внимательно правильность введенных данных:"
    t_no_matches = "Мы обязательно уведомим тебя, когда произойдет совпадение 🕓"
    t_good_1 = "Ура! Попутчик успешно найден."
    t_good_2 = "Делюсь данными о нем и контактами для связи:\n "
    t_taxi_ride = "У меня две новости: плохая и хорошая\nПлохая: мы не нашли водителя, который сможет тебя отвезти в другой корпус\nХорошая: у тебя есть возможность объединиться с другими попутчиками и поехать  вместе на такси."

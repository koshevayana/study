class Account:
    usd_rate = 88.5
    eur_rate = 96.2

    def __init__(self, last_name, account_number, interest_rate, amount_rub):
        self.last_name = last_name
        self.account_number = account_number
        self.interest_rate = interest_rate
        self.amount_rub = amount_rub

        print(f"Банковский счет открыт!")
        self.display_info()

    def __del__(self):
        print(f"Банковский счет владельца {self.__last_name} закрыт!")

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        self.__last_name = value

    @property
    def account_number(self):
        return self.__account_number

    @account_number.setter
    def account_number(self, value):
        self.__account_number = value

    @property
    def interest_rate(self):
        return self.__interest_rate

    @interest_rate.setter
    def interest_rate(self, value):
        if value < 0:
            raise ValueError("Процент не может быть отрицательным")
        self.__interest_rate = value

    @property
    def amount_rub(self):
        return self.__amount_rub

    @amount_rub.setter
    def amount_rub(self, value):
        if value < 0:
            raise ValueError("Сумма не может быть отрицательной")
        self.__amount_rub = value

    @classmethod
    def set_usd_rate(cls, new_rate):
        if new_rate <= 0:
            raise ValueError("Курс должен быть положительным")
        cls.usd_rate = new_rate
        print(f"Курс доллара обновлен: 1 USD = {cls.usd_rate} RUB")

    @classmethod
    def set_eur_rate(cls, new_rate):
        if new_rate <= 0:
            raise ValueError("Курс должен быть положительным")
        cls.eur_rate = new_rate
        print(f"Курс евро обновлен: 1 EUR = {cls.eur_rate} RUB")

    @staticmethod
    def rub_to_usd(amount_rub, rate=None):
        if rate is None:
            rate = Account.usd_rate
        return round(amount_rub / rate, 2)

    @staticmethod
    def rub_to_eur(amount_rub, rate=None):
        if rate is None:
            rate = Account.eur_rate
        return round(amount_rub / rate, 2)

    def change_owner(self, new_last_name):
        old_name = self.__last_name
        self.__last_name = new_last_name
        print(f"Владелец счета изменен: {old_name} → {new_last_name}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма для снятия должна быть положительной")
        if amount > self.__amount_rub:
            raise ValueError(f"Недостаточно средств! Доступно: {self.__amount_rub} RUB")

        self.__amount_rub -= amount
        print(f" Снято {amount} RUB. Остаток: {self.__amount_rub} RUB")

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма для пополнения должна быть положительной")

        self.__amount_rub += amount
        print(f" Зачислено {amount} RUB. Баланс: {self.__amount_rub} RUB")

    def add_interest(self):
        interest_amount = self.__amount_rub * self.__interest_rate
        self.__amount_rub += interest_amount
        print(f" Начислены проценты ({self.__interest_rate * 100}%): +{interest_amount:.2f} RUB")
        print(f"   Новый баланс: {self.__amount_rub:.2f} RUB")

    def to_usd(self):
        return round(self.__amount_rub / Account.usd_rate, 2)

    def to_eur(self):
        return round(self.__amount_rub / Account.eur_rate, 2)

    def display_info(self):
        print("=" * 50)
        print(f"ИНФОРМАЦИЯ О СЧЕТЕ")
        print(f" Владелец: {self.__last_name}")
        print(f" Номер счета: {self.__account_number}")
        print(f" Процент начисления: {self.__interest_rate * 100}%")
        print(f" Баланс: {self.__amount_rub:.2f} RUB")
        print(f" В долларах: ${self.to_usd()}")
        print(f" В евро: €{self.to_eur()}")
        print("=" * 50)

account1 = Account("Иванов", "1234567890", 0.05, 10000)
Account.set_usd_rate(90.0)
Account.set_eur_rate(98.5)
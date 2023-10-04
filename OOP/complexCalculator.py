class Complex:

    def __init__(self, real, imag):

        self.real = real

        self.imag = imag



    def __add__(self, other):

        return Complex(self.real + other.real, self.imag + other.imag)



    def __sub__(self, other):

        return Complex(self.real - other.real, self.imag - other.imag)



    def __mul__(self, other):

        return Complex(self.real * other.real - self.imag * other.imag,

                       self.imag * other.real + self.real * other.imag)



    def __truediv__(self, other):

        denom = other.real**2 + other.imag**2

        return Complex((self.real * other.real + self.imag * other.imag) / denom,

                       (self.imag * other.real - self.real * other.imag) / denom)



class CalculatorLogger:

    _INSTANCE = None



    def __new__(cls):

        if cls._INSTANCE is None:

            cls._INSTANCE = super().__new__(cls)

        return cls._INSTANCE



    def log(self, message):

        file = open("log.txt", "a")

        file.write(message + "n")

        file.close()



def main():

    logger = CalculatorLogger()



    print("Введите два комплексных числа")

    real1 = float(input("Действительная часть первого числа: "))

    imag1 = float(input("Мнимая часть первого числа: "))

    real2 = float(input("Действительная часть второго числа: "))

    imag2 = float(input("Мнимая часть второго числа: "))



    complex1 = Complex(real1, imag1)

    complex2 = Complex(real2, imag2)



    print("nВыберите действие над числами:")

    print("1 - Сложение")

    print("2 - Вычитание")

    print("3 - Умножение")

    print("4 - Деление")

    choice = int(input("Введите номер операции: "))



    result = None



    if choice == 1:

        result = complex1 + complex2

        logger.log(f"Выполнено сложение: {complex1.real}+{complex1.imag}i + {complex2.real}+{complex2.imag}i = {result.real}+{result.imag}i")



    elif choice == 2:

        result = complex1 - complex2

        logger.log(f"Выполнено вычитание: {complex1.real}+{complex1.imag}i - {complex2.real}+{complex2.imag}i = {result.real}+{result.imag}i")



    elif choice == 3:

        result = complex1 * complex2

        logger.log(f"Выполнено умножение: {complex1.real}+{complex1.imag}i * {complex2.real}+{complex2.imag}i = {result.real}+{result.imag}i")



    elif choice == 4:

        result = complex1 / complex2

        logger.log(f"Выполнено деление: {complex1.real}+{complex1.imag}i / {complex2.real}+{complex2.imag}i = {result.real}+{result.imag}i")



    else:

        print("Ошибка ввода.")



    if result:

        print(f"nРезультат: {result.real}+{result.imag}i")



if __name__ == "__main__":

    main()

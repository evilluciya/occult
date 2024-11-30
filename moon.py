#Каббалистический / Магический квадрат Луны для усиления чакр, укрепления пораженной Луны, 
#и для помощи здоровью и общему духовному развитию, связанному с Луной
#Для духовный дел
import time
import os

def clear_screen():
    """Очищает экран в зависимости от операционной системы."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_square(square, highlighted_positions):
    """Выводит магический квадрат, с подсвеченными числами."""
    for row_idx, row in enumerate(square):
        for col_idx, number in enumerate(row):
            if (row_idx, col_idx) in highlighted_positions:
                # Число будет белым
                print(f"\033[97m{number:>3}\033[0m", end="\t") 
                
            else:
                #print(f"{number:>3}", end="\t")
                 print(f"\033[90m{number:>3}\033[0m", end="\t") 
        print()  # Переход на новую строку

def generate_positions(square):
    """Генерирует порядок позиций для мигающих чисел, начиная с правого нижнего угла, 
    двигаясь справа налево по строкам, а затем вверх по столбцам с чередованием направлений движения."""
    n = len(square)  # Размер квадратной матрицы (5x5, например)
    positions = []
    
    row = n - 1  # Начинаем с последней строки
    col = n - 1  # Начинаем с последнего столбца

    direction = -1  # Направление, по которому двигаемся: -1 (справа налево), 1 (слева направо)
    
    while len(positions) < n * n:
        # Двигаемся по строке в зависимости от направления
        while 0 <= col < n:
            positions.append((row, col))
            col += direction
        
        # После того как дошли до первого столбца в строке, переходим к следующей строке
        row -= 1
        if row < 0:
            break  # Если все строки пройдены, выходим из цикла

        # После перехода на новую строку, восстанавливаем тот же столбец
        # И меняем направление движения
        col = positions[-1][1]  # Восстанавливаем столбец текущей позиции
        direction *= -1  # Меняем направление: если было справа налево, будет слева направо, и наоборот
    
    return positions

def display_blinking_numbers(square, positions):
    """Отображает мигающие числа в соответствии с позицией и делает их красными после мигания."""
    red_numbers = set()  # Множество для отслеживания чисел, которые уже стали красными

    for position in positions:
        row, col = position
        number = square[row][col]

        # Мигание числа: количество миганий зависит от значения числа
        for _ in range(number):  # Мигание числом столько раз, сколько оно есть
            clear_screen()
            # Показываем текущее мигающее число красным
            print_square(square, red_numbers | {position})  # Подсветка красным
            time.sleep(0.5)
            clear_screen()
            print_square(square, red_numbers)  # Показываем все числа, которые стали красными
            time.sleep(0.5)
        
        # После мигания оставляем число красным
        red_numbers.add(position)  # Добавляем позицию в список красных чисел
        clear_screen()
        print_square(square, red_numbers)  # Показываем все числа, которые стали красными
        time.sleep(0.5)

def main():
    square = [
        [37, 78, 29, 70, 21, 62, 13, 54, 5],
        [6, 38, 79, 30, 71, 22, 63, 14, 46],
        [47, 7, 39, 80, 31, 72, 23, 55, 15],
        [16, 48, 8, 40, 81, 32, 64, 24, 56],
        [57, 17, 49, 9, 41, 73, 33, 65, 25],
        [26, 58, 18, 50, 10, 42, 74, 34, 66],
        [67, 27, 59, 19, 51, 11, 43, 75, 35],
        [36, 68, 28, 60, 20, 52, 12, 44, 76],
        [77, 37, 69, 29, 61, 13, 55, 5, 45],
    ]
    
    # Генерация порядка позиций
    positions = generate_positions(square)

    # Отображаем мигающие числа
    display_blinking_numbers(square, positions)
    print("Магический квадрат Луны полностью активирован.")

if __name__ == "__main__":
    clear_screen()
    main()

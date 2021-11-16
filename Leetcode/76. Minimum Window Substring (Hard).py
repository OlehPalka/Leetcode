class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result = ""

        t_length = len(t)
        s_length = len(s)

        window_left_index = 0
        window_right_index = 0
        current_smallest_window = [-float("inf"), float("inf")]

        t_dict = dict()
        # Словник для того, щоб чекати, чи всі букви зі стрінга Т є в вікні.
        s_substring_dict = dict()

        # змінна, для того, щоб знати, чи в нашому вікні знаходяться всі букви зі стрічки t
        counter_for_amount_of_let = 0

        # Вносимо всі букви стрічки t в словник, для нормального порівняння.
        for letter in t:
            t_dict[letter] = t_dict.get(letter, 0) + 1

        # рухаємо наше вікно по стрічці s, аж поки правий індекс не вийде за її межі
        while window_right_index < s_length:

            # Якщо буква зі стрічки С всловнику букв стрічки Т
            if s[window_right_index] in t_dict:
                # Добавляємо / оновлюємо значення по ключу s[window_right_index] в словнику вікна з потрібними літерами
                s_substring_dict[s[window_right_index]] = s_substring_dict.get(
                    s[window_right_index], 0) + 1

                # Якщо кількість вибраної букви в вікні <= кількість цієїї букви в стрічці Т
                if s_substring_dict[s[window_right_index]] <= t_dict[s[window_right_index]]:
                    # Добавляєм до нашого каунтера 1
                    counter_for_amount_of_let += 1

            # Якщо каунтер == довжині стрічки Т, це значить, що в нашому вікні є всі букви зі стрінга Т
            # Проходимось в циклі вайл, яж поки каунтер не стане меншим за довжину стрічки Т
            while counter_for_amount_of_let == t_length:

                # Якщо наявне вікно має менший розмір, ніж вікно, яке збережене у нас у змінній current_smallest_window
                if current_smallest_window[1] - current_smallest_window[0] > window_right_index - window_left_index:
                    # Міняємо значення current_smallest_window на нове менше вікно
                    current_smallest_window[0], current_smallest_window[1] = window_left_index, window_right_index

                # Якщо буква під лівим індексом вікна є в стрічці
                # Видаляємо її зі словника вікна
                if s[window_left_index] in t_dict:
                    s_substring_dict[s[window_left_index]] -= 1

                    # Якщо кількість цієї букви стала меншою, ніж нам потрібна в стрінгу Т
                    # Віднімаємо від каунтера 1
                    if s_substring_dict[s[window_left_index]] < t_dict[s[window_left_index]]:
                        counter_for_amount_of_let -= 1

                # робимо можливий результат - стрінгу.
                result = s[current_smallest_window[0]
                    :current_smallest_window[1] + 1]

                # посуваєм лівий індекс вікна на 1 вправо
                window_left_index += 1

            # посуваємо правий індекс вкіна на 1 вправо
            window_right_index += 1

        return result

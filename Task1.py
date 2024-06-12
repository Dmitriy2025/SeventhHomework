# Напишите функцию, которая принимает в качестве аргумента функцию, 
# вычисляющую элемент по номеру строки и столбца.

def print_operation_table(operation, num_rows = 9, num_columns = 9):
   if num_rows < 2 or num_columns < 2:
    print('ОШИБКА! Размерности таблицы должны быть больше 2!')
   else:
      for i in range(1, num_rows+1):
        for j in range(1, num_columns+1):
           if j == num_columns: 
            print(operation(i, j), end='')
           else:
            print(operation(i, j), end=' ')
        print()



print_operation_table(lambda x, y: x * y)
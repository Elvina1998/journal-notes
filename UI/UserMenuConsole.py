import UI.MenuTemplates as m

def menu_console():
      m.print_menu_title("Главное меню\nЖурнал заметок")
      print("     1 - Вывод журнала\n")
      print("     2 - Вывод заметки по ID\n")
      print("     3 - Выбор заметки по дате\n")
      print("     4 - Редактирование заметки\n")
      print("     5 - Добавление заметки\n")
      print("     6 - Удаление заметки\n")
      m.print_menu_line()
      print("\nВведите пункт из меню ")
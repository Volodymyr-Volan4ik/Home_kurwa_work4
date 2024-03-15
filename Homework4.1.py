path_on_file = "text.txt" 

def total_salary(path):

    count = 0

    total_sum = 0

    try:
        
        with open(path, "r", encoding = "utf-8") as file:

            for line in file:

                _, salaries = line.strip().split(',')

                total_sum += int(salaries)

                count += 1

        avg_salary = total_sum / count

        return total_sum, avg_salary
        
    except FileNotFoundError:

        print("Файл не найден.")

    except Exception as e:
        
        print(f"Произошла ошибка: {e}")

total_sum, avg_salary = total_salary(path_on_file)

print(f"Загальна сума заробітної плати: {total_sum}") 

print(f"Середня заробітна плата: {avg_salary}")
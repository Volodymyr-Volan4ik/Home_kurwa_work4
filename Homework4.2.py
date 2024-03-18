path_in_cats = "cats.txt"

def get_cats_info(path):

    info_or_cats = []

    try:

        with open(path, "r", encoding = "utf-8") as file:

            for line in file:

                cat_data = line.strip().split(',')

                info_or_cat = { "id": cat_data[0], "name": cat_data[1], "age": cat_data[2] }
                  
                info_or_cats.append(info_or_cat)

    except FileNotFoundError:
        
        print("Файл не знайдено")
            
    except Exception as e:

        print(f"Сталася помилка під час читання файлу: {e}")
    
    return info_or_cats
print(get_cats_info(path_in_cats))
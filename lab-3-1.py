# Yongdong Xi (2022 1 11)

def add_foods(lst):
    sixth_letter = []
    not_foods = []
    short_foods = []
    for i in lst:
        try:
            sixth_letter.append((i[5]))
        except TypeError:
            not_foods.append(i)
        except IndexError:
            short_foods.append(i)
        finally:
            print(sixth_letter)
            print(not_foods)
            print(short_foods)
    return


add_foods(["potatoes", True, "salad"])
            
        
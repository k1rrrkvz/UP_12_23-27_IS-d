# main.py
# Мини-программа: вычисляет "оценку" по списку чисел и демонстрирует изменение и коммит
# Функция calculate_score берёт список чисел и возвращает среднее и максимальное значение

def calculate_score(values):
    if not values:
        return {"count": 0, "avg": 0, "max": None}
    count = len(values)
    avg = sum(values) / count
    return {"count": count, "avg": round(avg, 2), "max": max(values)}

if __name__ == "__main__":
    sample = [10, 7, 9, 8, 10]
    result = calculate_score(sample)
    print("Input:", sample)
    print("Result:", result)
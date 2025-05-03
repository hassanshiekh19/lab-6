def running_average():
    total = 0
    count = 0

    def average(new_number):
        nonlocal total, count  
        total += new_number  
        count += 1  
        return total / count  

    return average

avg_calculator = running_average()

print(avg_calculator(10))  
print(avg_calculator(20))  
print(avg_calculator(30))  

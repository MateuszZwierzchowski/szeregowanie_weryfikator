if __name__ == "__main__":
    instance = 'in/in_141820_50.txt'
    with open(instance, 'r') as file:
        n = int(file.readline())
        speeds = list(map(float, file.readline().split()))
        p = [[0] * len(speeds) for _ in range(n)]  # czasy trwania procesu na każdej z 5 maszyn
        r = [0] * n  # czas rozpoczęcia
        d = [0] * n  # czas zakończenia
        for i in range(n):
            p[i], r[i], d[i] = map(int, file.readline().split())

    result = 'out/out.txt'
    finish_times = [0] * 5  # czasy zakończenia procesów na poszczególnych maszynach
    sum_delay = 0
    with open(result, 'r') as file:
        total_lateness = float(file.readline())
        for i in range(5):
            # kolejność zadań na maszynie i
            order = map(int, file.readline().split())
            #print(f"Maszyna {i + 1}: {list(order)}")
            for job in order:
                start_time = max(finish_times[i], r[job - 1])
                end_time = start_time + p[job - 1] * speeds[i]
                finish_times[i] = end_time
                # obliczenie opóźnienia
                delay = min(max(0, end_time - d[job - 1]), p[job-1])
                #print(f"Proces {job} na maszynie {i + 1}, czas rozpoczęcia: {start_time}, czas zakończenia: {end_time}. Opóźnienie: {delay}")
                sum_delay += delay
                #print("Maszyna ", i + 1, " proces ", job, " czas rozpoczecia ", start_time, " czas zakonczenia ", end_time, " opoznienie ", delay )
    if sum_delay > total_lateness:
        print(f"Suma opóźnień validator: {sum_delay}, suma opóźnień out: {total_lateness}")
        print("Wynik nie dopuszczalny")
    else:
        print("Wynik dopuszczalny")



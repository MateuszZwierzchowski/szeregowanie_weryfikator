import subprocess


def read_input_file(file_path):
    with open(file_path, "r") as file:
        n = int(file.readline().strip())
        tasks = []
        for _ in range(n):
            task = list(map(int, file.readline().strip().split()))
            tasks.append(task)
        setup_times = []
        for _ in range(n):
            setup_time = list(map(int, file.readline().strip().split()))
            setup_times.append(setup_time)
    return n, tasks, setup_times


def read_output_file(file_path):
    with open(file_path, "r") as file:
        expected_completion_sum = int(file.readline().strip())
        sequence = list(map(int, file.readline().strip().split()))
    return expected_completion_sum, sequence


def calculate_completion_sum(n, tasks, setup_times, sequence):
    current_time = completion_sum = 0

    for i, task_num in enumerate(sequence):
        processing_time, ready_time = tasks[task_num - 1]
        setup_time = setup_times[sequence[i - 1] - 1][task_num - 1] if i > 0 else 0
        current_time = max(current_time + setup_time, ready_time) + processing_time
        completion_sum += current_time

    return completion_sum


def main():
    input_file_path = "in_148156_500.txt"
    output_file_path = "out" + input_file_path[2:]

    subprocess.call(['java', '-jar', 'szeregowanie_zadan-1.0.jar', input_file_path])

    n, tasks, setup_times = read_input_file(input_file_path)
    expected_completion_sum, sequence = read_output_file(output_file_path)
    calculated_completion_sum = calculate_completion_sum(n, tasks, setup_times, sequence)

    if calculated_completion_sum == expected_completion_sum:
        print("Sekwencja jest poprawna.")
    else:
        print(f"Sekwencja jest niepoprawna. Oczekiwana suma: {expected_completion_sum}, obliczona suma: {calculated_completion_sum}")


if __name__ == "__main__":
    main()
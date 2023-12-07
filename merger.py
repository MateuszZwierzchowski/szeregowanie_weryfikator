import os
import glob
import re


def main():

    results = {}
    times = {}

    directory = 'out'

    # Iterate over each file in the directory that matches the pattern
    for filepath in glob.glob(os.path.join(directory, 'out_*_148120_*.txt')):
        kogo_instancja, rozmiar = parse_filename(os.path.basename(filepath))
        if kogo_instancja:
            # Initialize the dictionaries if key not present
            if kogo_instancja not in results:
                results[kogo_instancja] = []
                times[kogo_instancja] = []

            with open(filepath, 'r') as file:
                lines = file.readlines()
                # Assuming the file always has 3 lines: result, tasks, and time
                result = lines[0].strip()  # First line is the result
                time = lines[2].strip()  # Third line is the time

                # Store the results and times along with their size for sorting later
                results[kogo_instancja].append((rozmiar, result))
                times[kogo_instancja].append((rozmiar, time))

    # Sort and write the results and times to separate files
    for kogo_instancja in results:
        results[kogo_instancja].sort()
        times[kogo_instancja].sort()

        with open(f'{kogo_instancja}_wynik.txt', 'w') as file:
            for _, result in results[kogo_instancja]:
                file.write(result + '\n')

        with open(f'{kogo_instancja}_czas.txt', 'w') as file:
            for _, time in times[kogo_instancja]:
                file.write(time + '\n')

    # Print a confirmation message
    print("Files have been processed and saved.")


def parse_filename(filename):
    # This regular expression is designed to extract 'kogo_instancja' and 'rozmiar' from the filename
    match = re.search(r'out_(.*)_148120_(\d+).txt', filename)
    if match:
        return match.group(1), int(match.group(2))
    return None, None


if __name__ == "__main__":
    main()




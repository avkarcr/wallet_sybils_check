import argparse
import os

def read_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = [line.strip().lower() for line in file.readlines()]
    return lines

def find_occurrences(list1, list2):
    return [line for line in list1 if line in list2]

def main(wallets_file, sybils_file, output_file='output.txt'):
    file1_lines = read_lines(wallets_file)
    file2_lines = read_lines(sybils_file)
    occurrences = find_occurrences(file1_lines, file2_lines)
    with open(output_file, 'w', encoding='utf-8') as output_file:
        for line in occurrences:
            output_file.write(line + '\n')
    print(f'Total occurences: {len(occurrences)}. Results saved in {output_file.name}.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find occurrences of wallets in Sybil database.')
    parser.add_argument('wallets_file', type=str, help='Path to the file containing wallets.')
    parser.add_argument('sybils_file', type=str, help='Path to the Sybil database file.')
    parser.add_argument('-o', '--output', type=str, default='output.txt', help='Output file path (default: output.txt)')
    args = parser.parse_args()
    if not os.path.isfile(args.wallets_file) or not os.path.isfile(args.sybils_file):
        parser.print_help()
    else:
        main(args.wallets_file, args.sybils_file, args.output)


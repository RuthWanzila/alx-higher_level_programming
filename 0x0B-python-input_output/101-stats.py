#!/usr/bin/python3
import sys

status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
status_counts = {code: 0 for code in status_codes}
total_file_size = 0
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        split_line = line.split(' ')
        if len(split_line) >= 7:
            status_code = split_line[-2]
            file_size = int(split_line[-1])
            if status_code in status_codes:
                status_counts[status_code] += 1
            total_file_size += file_size

        if line_count % 10 == 0:
            print("File size: {}".format(total_file_size))
            for code in sorted(status_codes):
                count = status_counts[code]
                if count > 0:
                    print("{}: {}".format(code, count))

except KeyboardInterrupt:
    pass

finally:
    print("File size: {}".format(total_file_size))
    for code in sorted(status_codes):
        count = status_counts[code]
        if count > 0:
            print("{}: {}".format(code, count))

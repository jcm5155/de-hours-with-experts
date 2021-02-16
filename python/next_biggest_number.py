#!/usr/bin/python3
import sys


def main():
    next_biggest_number(sys.argv[1])


def next_biggest_number(num):
    str_num = str(num)
    # Iterate backwards through increasingly larger slices...
    for cutoff in range(len(str_num) - 2, -1, -1):
        current_slice = list(str_num[cutoff:])
        reverse_sorted_slice = sorted(current_slice, reverse=True)
        # ...until we find a slice that is NOT in sorted reverse order
        if current_slice != reverse_sorted_slice:
            # Pop off the next highest number compared to the current cutoff value
            new_cutoff_value = reverse_sorted_slice.pop(reverse_sorted_slice.index(current_slice[0])-1)
            # Re-sort the reversed slice in the opposite direction and concat everything together
            return int(f"{str_num[:cutoff]}{new_cutoff_value}{''.join(sorted(reverse_sorted_slice))}")
    return -1


if __name__ == "__main__":
    main()




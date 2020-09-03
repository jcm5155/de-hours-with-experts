#!/usr/bin/python3
import sys


def main():
    next_biggest_number(sys.argv[1])


def next_biggest_number(num):
    list_num = list(str(num))
    len_num = len(list_num)

    # If the list is already in sorted reverse order, just return -1 immediately
    if sorted(list_num)[::-1] == list_num:
        return -1

    # Iterate backwards through increasingly larger slices until we find a slice that is NOT in sorted reverse order
    for idx in range(1, len_num):
        cutoff = len_num - idx - 1
        current_list_slice = list_num[cutoff:]
        if current_list_slice != (tail_values := sorted(current_list_slice)[::-1]):
            # Pop off the next largest number in relation to our slice's value at index 0
            new_lead_tail_value = tail_values.pop(tail_values.index(current_list_slice[0])-1)
            # Re-sort the remaining tail values and concat everything together
            return int(''.join(list_num[:cutoff]) + new_lead_tail_value + ''.join(tail_values[::-1]))


if __name__ == "__main__":
    main()




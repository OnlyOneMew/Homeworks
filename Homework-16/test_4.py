def merge_sorted_lists(list1, list2):
    merged_list = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    while i < len(list1):
        merged_list.append(list1[i])
        i += 1

    while j < len(list2):
        merged_list.append(list2[j])
        j += 1

    return merged_list


def main():
    list1 = [1, 3, 5, 7]
    list2 = [2, 4, 6, 8]
    print("Merged List:", merge_sorted_lists(list1, list2))

    list3 = [1, 2, 4, 6]
    list4 = [3, 5, 7, 8]
    print("Merged List:", merge_sorted_lists(list3, list4))

    list5 = [5, 10, 15, 20]
    list6 = [3, 6, 9, 12]
    print("Merged List:", merge_sorted_lists(list5, list6))


if __name__ == "__main__":
    main()

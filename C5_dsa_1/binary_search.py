def main():
    print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 6))
    print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 100))
    print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], "6"))

    # print(sorted([1, "apple", 3]))


def binary_search(inp_array, search_element):
    if isinstance(inp_array[0], type(search_element)):
        low = 0
        high = len(inp_array)-1
        while low <= high:
            mid = (low+high)//2
            if inp_array[mid] == search_element:
                return mid
            elif inp_array[mid] > search_element:
                high = mid - 1
            else:
                low = mid + 1
        return -1
    else:
        raise TypeError("Invalid type of target element entered")


if __name__ == "__main__":
    main()

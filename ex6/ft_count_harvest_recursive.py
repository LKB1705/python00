def ft_count_harvest_recursive() -> None:
    count = int(input("Days until harvest: "))

    def helper(day: int) -> None:
        if day > count:
            print("Harvest time!")
            return
        print(f"Day {day}")
        helper(day + 1)

    helper(1)


ft_count_harvest_recursive()

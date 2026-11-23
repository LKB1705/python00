def ft_count_harvest_iterative() -> None:
    count = int(input("Days until harvest: "))
    down = range(count)
    for n in down:
        print(f"Day {n + 1}")
    print("Harvest time!")


ft_count_harvest_iterative()

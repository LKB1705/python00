def ft_plant_age() -> None:
    age = int(input("Enter plant age in days: "))
    if (age > 60):
        print("PLants is ready to harvest!")
    else:
        print("Plant needs more time to grow.")


ft_plant_age()

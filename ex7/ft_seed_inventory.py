def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    cap_seed = seed_type.capitalize()
    if (unit == "packets"):
        final_unit = unit.replace("packets", "packets available")
    elif (unit == "grams"):
        final_unit = unit.replace("grams", "grams total")
    elif (unit == "area"):
        final_unit = unit.replace("area", "square meters")
    print(f"{cap_seed} seeds: {quantity} {final_unit}")


ft_seed_inventory("tomato", 15, "packets")
ft_seed_inventory("carrot", 56, "grams")
ft_seed_inventory("lettuce", 120, "area")

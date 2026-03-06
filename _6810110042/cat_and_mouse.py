def cat_and_mouse(x, y, z):
    dist_cat_a = abs(x - z)
    dist_cat_b = abs(y - z)

    if dist_cat_a < dist_cat_b:
        return "Cat A"
    elif dist_cat_b < dist_cat_a:
        return "Cat B"
    else:
        return "Mouse C"

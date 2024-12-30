def sierpinski_triangle(size, x=0, y=0, level=5):
    """Tworzy trójkąt Sierpińskiego w konsoli."""
    if level == 0:
        return [(x, y), (x + size, y), (x + size // 2, y + size)]
    else:
        # Rekurencyjnie generujemy 3 podtrójkąty
        t1 = sierpinski_triangle(size // 2, x, y, level - 1)
        t2 = sierpinski_triangle(size // 2, x + size // 2, y, level - 1)
        t3 = sierpinski_triangle(size // 2, x + size // 4, y + size // 2, level - 1)
        return t1 + t2 + t3


def draw_fractal(points):
    """Rysuje fraktal w konsoli na podstawie punktów."""
    # Znajdź największe współrzędne dla siatki
    max_x = max(p[0] for p in points)
    max_y = max(p[1] for p in points)

    # Tworzenie siatki
    grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for x, y in points:
        if 0 <= y < len(grid) and 0 <= x < len(grid[y]):
            grid[y][x] = "*"

    # Wyświetlanie fraktalu
    for row in reversed(grid):
        print("".join(row))


if __name__ == "__main__":
    size = 128  # Rozmiar podstawowego trójkąta
    level = 10  # Poziom rekurencji
    points = sierpinski_triangle(size, level=level)
    draw_fractal(points)

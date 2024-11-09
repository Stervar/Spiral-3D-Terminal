import numpy as np

def create_3d_spiral(width=80, height=40):
    """
    Создание 3D спирали, идентичной параметрическому графику
    x(u,v) = cos(u)*(cos(v)+3)
    y(u,v) = sin(u)*(cos(v)+3)
    z(u,v) = sin(v) + u
    """
    # Параметры для создания спирали
    u = np.linspace(-2*np.pi, 2*np.pi, 300)
    v = np.linspace(-np.pi, np.pi, 300)

    # Полная сетка параметров
    U, V = np.meshgrid(u, v)

    # Точные параметрические уравнения
    X = np.cos(U) * (np.cos(V) + 3)
    Y = np.sin(U) * (np.cos(V) + 3)
    Z = np.sin(V) + U

    # Подготовка экрана терминала
    screen = np.full((height, width), ' ', dtype=str)
    z_buffer = np.full((height, width), float('-inf'))

    # Нормализация координат
    x_norm = (X - np.min(X)) / (np.max(X) - np.min(X))
    y_norm = (Y - np.min(Y)) / (np.max(Y) - np.min(Y))
    z_norm = (Z - np.min(Z)) / (np.max(Z) - np.min(Z))

    # Проекция на экран
    screen_x = (x_norm * (width-1)).astype(int)
    screen_y = (y_norm * (height-1)).astype(int)

    # Символы для отображения глубины
    depth_chars = ' .:-=+*#%@'

    # Отрисовка точек
    for x, y, z in zip(screen_x.flatten(), screen_y.flatten(), z_norm.flatten()):
        if 0 <= x < width and 0 <= y < height:
            char_index = int(z * (len(depth_chars) - 1))
            screen[y, x] = depth_chars[char_index]

    return '\n'.join(''.join(row) for row in screen)

def main():
    """
    Отрисовка спирали
    """
    spiral = create_3d_spiral()
    print(spiral)

if __name__ == "__main__":
    main()
    
    
import cv2
import numpy as np

# Leer la imagen
image = cv2.imread('C:/Users/HP/Documents/Escuela Militar Ingenieria/Inteligencia Artificial II/prueba.png')

# Convertir la imagen de BGR a HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Definir los rangos de colores en HSV
color_ranges = {
    'Rojo': [(0, 120, 70), (10, 255, 255)],  # Rango de color rojo (rojo puro)
    'Verde': [(35, 50, 50), (85, 255, 255)],  # Rango de color verde (verde puro)
    'Azul': [(100, 150, 50), (130, 255, 255)],  # Rango de color azul (azul puro)
    'Amarillo': [(20, 150, 150), (40, 255, 255)],  # Rango de color amarillo (amarillo puro)
    'Naranja': [(10, 150, 150), (20, 255, 255)],  # Rango de color naranja (naranja puro)
    'Blanco': [(0, 0, 200), (180, 30, 255)],  # Rango de color blanco (blanco puro)
    'Negro': [(0, 0, 0), (180, 255, 50)],  # Rango de color negro (negro puro
}

# Crear una imagen para el resultado
result = image.copy()

# Iterar sobre los colores definidos
for color_name, (lower, upper) in color_ranges.items():
    lower_bound = np.array(lower)
    upper_bound = np.array(upper)
    
    # Crear la máscara para el color
    mask = cv2.inRange(hsv_image, lower_bound, upper_bound)
    
    # Aplicar la máscara a la imagen original
    masked_result = cv2.bitwise_and(image, image, mask=mask)
    
    # Si hay píxeles detectados, mostrar el color en la imagen
    if np.any(mask):  # Verifica si hay píxeles dentro del rango
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(result, f'Color Detectado: {color_name}', (10, 50 + 40 * list(color_ranges.keys()).index(color_name)),
                    font, 1, (0, 255, 0), 2, cv2.LINE_AA)

# Mostrar la imagen original, la máscara y el resultado
cv2.imshow('Imagen Original', image)
cv2.imshow('Resultado con Colores Detectados', result)

# Esperar a que se presione una tecla y cerrar las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()

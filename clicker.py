import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cookie Clicker")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Fuente
font = pygame.font.Font(None, 36)

# Variables
score = 0

# Función para mostrar el puntaje en pantalla
def show_score():
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

# Función para realizar el autoguardado
def autoguardar(puntaje):
    with open("puntaje_guardado.txt", "w") as file:
        file.write(str(puntaje))

# Función para cargar el puntaje guardado desde el archivo
def cargar_puntaje_guardado():
    try:
        with open("puntaje_guardado.txt", "r") as file:
            return int(file.read())
    except FileNotFoundError:
        return 0

# Función principal del juego
def main():
    global score

    # Cargar el puntaje guardado al inicio del juego
    score = cargar_puntaje_guardado()

    running = True

    while running:
        screen.fill(WHITE)
        show_score()

        # Detección de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Verificar si se hizo clic en la galleta
                if cookie_rect.collidepoint(event.pos):
                    score += 1
                    autoguardar(score)  # Realizar autoguardado al hacer clic en la galleta

        # Dibujar galleta
        cookie_rect = pygame.draw.circle(screen, RED, (WIDTH//2, HEIGHT//2), 50)

        pygame.display.flip()
    
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()

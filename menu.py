import pygame

pygame.init()

window_width = 640
window_height = 480
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Difficulty Menu")

# Set up the font
font = pygame.font.SysFont(None, 48)

# Draw the menu options on the window
menu_text = ["Please select a difficulty by typing: ", "1 for Easy", "2 for Medium", "3 for Hard"]
text_y = window_height // 2 - len(menu_text) * 24
for text in menu_text:
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(window_width // 2, text_y))
    window.blit(text_surface, text_rect)
    text_y += 48

# Main game loop
difficulty = None  # initialize difficulty to None
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                difficulty = "easy"
            elif event.key == pygame.K_2:
                difficulty = "medium"
            elif event.key == pygame.K_3:
                difficulty = "hard"

    # Draw the selected difficulty on the window
    if difficulty:
        selected_text = f"You have selected {difficulty} difficulty."
        selected_surface = font.render(selected_text, True, (255, 255, 255))
        selected_rect = selected_surface.get_rect(center=(window_width // 2, window_height // 2 + 100))
        window.blit(selected_surface, selected_rect)
        running = False
    # Update the display
    pygame.display.update()
    if not running:
        pygame.time.wait(2000)
# Clean up
pygame.quit()

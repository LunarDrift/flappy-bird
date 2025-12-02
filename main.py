import arcade
from constants import *


class GameView(arcade.View):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class to set up the window
        super().__init__()

        self.background_color = arcade.csscolor.CORNFLOWER_BLUE
        # Player texture and sprite
        self.player_texture = arcade.load_texture("assets/astronaut.png")
        self.player_sprite = arcade.Sprite(self.player_texture)
        self.player_sprite.center_x = WINDOW_WIDTH / 2
        self.player_sprite.center_y = 128

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)

        self.left_pressed = False
        self.right_pressed = False

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        pass

    def on_draw(self):
        """Render the screen."""

        # The clear method should always be called at the start of on_draw.
        # It clears the whole screen to whatever the background color is
        # set to. This ensures that you have a clean slate for drawing each
        # frame of the game.
        self.clear()

        # Code to draw other things will go here
        self.player_list.draw()

    def on_update(self, delta_time):
        # if game_state is PLAYING:
            # update bird
            # update pipes
            # handle collisions
            # handle scoring
        
        self.player_list.update(delta_time)
    

    def update_player_speed(self):
        # Calculate speed based on keys pressed
        self.player_sprite.change_x = 0

        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""
        
        # if key is SPACE:
        #     if game_state is START:
        #         game_state = PLAYING
        #     else if game_state is PLAYING:
        #         bird.flap()
        #     else if game_state is GAME_OVER:
        #         restart_game()
        if key == arcade.key.A:
            self.left_pressed = True
            self.update_player_speed()
        elif key == arcade.key.D:
            self.right_pressed = True
            self.update_player_speed()

    def on_key_release(self, key, modifiers):
        """Called whenever a key is released."""

        if key == arcade.key.A:
            self.left_pressed = False
            self.update_player_speed()
        elif key == arcade.key.D:
            self.right_pressed = False
            self.update_player_speed()


def main():
    """Main function"""
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
    game_view = GameView()
    game_view.setup()
    window.show_view(game_view)
    arcade.run()


if __name__ == "__main__":
    main()
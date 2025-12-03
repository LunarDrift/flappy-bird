# Window
WINDOW_WIDTH = 360
WINDOW_HEIGHT = 640
FPS = 60

# Bird
BIRD_X = WINDOW_WIDTH / 8
BIRD_Y = WINDOW_HEIGHT / 2
BIRD_WIDTH = 34
BIRD_HEIGHT = 24
FLAP_STRENGTH = -6
FLAP_COOLDOWN = 120
GRAVITY = 0.4

# Pipes
PIPE_WIDTH = 64
PIPE_HEIGHT = 512
PIPE_X = WINDOW_WIDTH
PIPE_Y = 0
PIPE_VELOCITY_X = -3
PIPE_GAP = WINDOW_HEIGHT / 4

# Assets
BG_IMG = "assets/flappybirdbg.png"
BIRD_IMG = "assets/flappybird.png"
TOP_PIPE_IMG = "assets/toppipe.png"
BOTTOM_PIPE_IMG = "assets/bottompipe.png"

CRASH_SOUND = 'assets/sounds/sfx_hit.wav'
DIE_SOUND = 'assets/sounds/sfx_die.wav'
POINT_SOUND = 'assets/sounds/sfx_point.wav'
FLAP_SOUND = 'assets/sounds/sfx_swooshing.wav'
BG_MUSIC = 'assets/sounds/8-bit-arcade-138828.mp3'
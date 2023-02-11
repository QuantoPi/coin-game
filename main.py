import pyglet
from pyglet.window import key
from pyglet import shapes
import random

class Main:
    def run():
        window = pyglet.window.Window(800, 600, "UwU")

        label = pyglet.text.Label('Coins: 0', font_name='Old School Adventures', font_size=16,
                                  x=75, y=window.height-25, anchor_x='center', anchor_y='center')

        # platform = pyglet.image.load('./sprites/platform/platform.png')
        coin_gif = pyglet.image.load_animation(
            './sprites/coin/coin_animation.gif')
        coin = pyglet.sprite.Sprite(
            coin_gif, x=random.randint(10, window.width-10), y=window.height // 2 - 30)
        coin.anchor_x = 'center'
        coin.anchor_y = 'center'

        platform = shapes.Rectangle(x=window.width // 2, y=window.height // 2-184,
                                    width=window.width, height=window.height // 2, color=(170, 141, 122))
        platform.anchor_x = platform.width // 2
        platform.anchor_y = platform.height // 2
        border = shapes.Rectangle(x=window.width // 2, y=window.height // 2 - 39,
                                  width=window.width, height=10, color=(53, 44, 46))
        border.anchor_x = border.width // 2
        border.anchor_y = border.height // 2

        background = shapes.Rectangle(x=window.width // 2, y=400,
                                      width=window.width, height=window.height, color=(174, 198, 207))
        background.anchor_x = background.width // 2
        background.anchor_y = background.height // 2

        keys = key.KeyStateHandler()
        window.push_handlers(keys)

        player_frames = []

        for frame in range(1):
            image = pyglet.image.load(
                './sprites/player/{frame}.png'.format(frame=frame))
            image.anchor_x = image.width // 2
            image.anchor_y = image.height // 2

            player_frames.append(
                pyglet.image.AnimationFrame(image, duration=0.1)
            )

        player_animation = pyglet.image.Animation(frames=player_frames)

        player = pyglet.sprite.Sprite(
            img=player_animation, x=window.width // 2, y=window.height // 2)

        coin_sound = pyglet.media.load('./sounds/coin.mp3')

        def detect_collision(sprite_1, sprite_2):
            return (sprite_1.x - sprite_2.x)**2 + (sprite_1.y - sprite_2.y)**2 < (sprite_1.width/2 + sprite_2.width/2)**2

        def update(dt):
            global coins
            if not 'coins' in globals():
                coins = 0
            if keys[key.A] or keys[key.LEFT]:
                player.scale_x = -1
                player.x -= 4
            elif keys[key.D] or keys[key.RIGHT]:
                player.scale_x = 1
                player.x += 4
            if detect_collision(player, coin):
                coin_sound.play()
                coins += 1
                label.text = f"Coins: {coins}"
                coin.x = random.randint(10, window.width-10)

            @window.event
            def on_draw():
                window.clear()
                background.draw()
                label.draw()
                player.draw()
                coin.draw()
                platform.draw()
                border.draw()

        pyglet.clock.schedule_interval(update, 1/60.0)
        pyglet.app.run()


if __name__ == "__main__":
    Main.run()

import os
from math import radians
from pathlib import Path
from typing import List

import pygame as pg

from poom.entities.enemy import Enemy
from poom.graphics import (
    BackgroundRenderer,
    CrosshairRenderer,
    EntityRenderer,
    FPSRenderer,
    Pipeline,
    WallRenderer,
)
from poom.map_loader import MapLoader
from poom.viewer import Viewer

SCREEN_SIZE = WIDTH, HEIGHT = 800, 600
root = Path(os.getcwd())


def game_loop() -> None:
    pg.init()
    pg.font.init()

    screen = pg.display.set_mode(SCREEN_SIZE, vsync=1)

    player = Viewer(pg.Vector2(1.1, 1.1), radians(45), radians(90))
    map_loader = MapLoader(root / "assets" / "levels")
    map_ = map_loader.as_numpy(1)
    clock = pg.time.Clock()
    dt: float = 0

    source = pg.image.load(root / "assets" / "front_attack" / "0.png")
    soldier2 = Enemy(
        position=pg.Vector2(5.5, 5.5),
        angle=radians(45),
        fov=radians(90),
        texture=source,
        map_=map_,
        enemy=player,
    )
    renderers = [
        BackgroundRenderer(pg.image.load("assets/skybox.png"), map_.shape[0]),
        WallRenderer(map_, player),
        EntityRenderer([soldier2]),
        CrosshairRenderer(),
        FPSRenderer(clock),
    ]
    pipeline = Pipeline(player, renderers)

    run = True
    while run:
        # TODO: event handler
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            player._position += player.view_vector * dt * 5
        if keys[pg.K_s]:
            player._position -= player.view_vector * dt * 5
        if keys[pg.K_a]:
            player._angle -= dt * 5
        if keys[pg.K_d]:
            player._angle += dt * 5
        pipeline.render(screen)
        soldier2.update(dt)
        dt = clock.tick() / 1000
    pg.quit()


def main(argv: List[str]) -> int:
    game_loop()
    return 0

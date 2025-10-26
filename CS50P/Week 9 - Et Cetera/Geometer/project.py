from rendercanvas.auto import RenderCanvas, loop
import pygfx


canvas = RenderCanvas()
renderer = pygfx.WgpuRenderer(canvas)
camera = pygfx.NDCCamera()

triangle = pygfx.Mesh(
    pygfx.Geometry(
        indices=[(0, 1, 2)],
        positions=[(0.0, -0.5, 0), (0.5, 0.5, 0), (-0.5, 1, 0)],
        colors=[(1, 1, 0, 1), (1, 0, 1, 1), (0, 1, 1, 1)],
    ),
    pygfx.MeshBasicMaterial(color_mode="vertex"),
)

def main():
    # pygfx.show(triangle)
    canvas.request_draw(lambda: renderer.render(triangle, camera))
    loop.run()


def function_1():
    ...


def function_2():
    ...


def function_3():
    ...


if __name__ == "__main__":
    main()

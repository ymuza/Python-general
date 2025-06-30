import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

def bubble_sort_animate(arr):
    frames = []

    # Bubble sort with frame capture
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            frame = arr.copy()
            color = ['blue'] * len(arr)
            color[j], color[j+1] = 'red', 'red'
            frames.append((frame, color))

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                frame = arr.copy()
                color = ['blue'] * len(arr)
                color[j], color[j+1] = 'green', 'green'
                frames.append((frame, color))

    return frames

def animate_sort(frames):
    fig, ax = plt.subplots()
    bar_rects = ax.bar(range(len(frames[0][0])), frames[0][0], color=frames[0][1])
    ax.set_title("Bubble Sort Visualization")

    def update(frame):
        heights, colors = frame
        for rect, h, c in zip(bar_rects, heights, colors):
            rect.set_height(h)
            rect.set_color(c)
        return bar_rects

    ani = animation.FuncAnimation(
        fig, update, frames=frames, blit=False, interval=300, repeat=False
    )

    plt.show()

# Example usage
array = [random.randint(1, 20) for _ in range(10)]
frames = bubble_sort_animate(array.copy())
animate_sort(frames)

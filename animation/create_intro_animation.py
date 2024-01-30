"""create_intro_animation.py

This module provides functionalities to create a basic intro animation using
Pygame. It includes functions to initialize Pygame, load resources, apply text
effects, create frames, save frames, play sound, create a video from frames,
and a main function to orchestrate the creation of the intro animation.
"""

import os
import pygame
from moviepy.editor import ImageSequenceClip, AudioFileClip

NUM_FRAMES = 0


def init_pygame(window_width, window_height):
    """
    Initialize Pygame and create a display window.

    Args:
        window_width (int): The width of the window in pixels.
        window_height (int): The height of the window in pixels.

    Returns:
        tuple: A tuple containing the Pygame screen object and the clock object.
    """
    pygame.init()
    return pygame.display.set_mode([window_width, window_height]), pygame.time.Clock()


def load_resources(image_path=None, sound_path=None, image_size=None):
    """
    Load and optionally resize image and sound resources for the animation.

    Args:
        image_path (str, optional): Path to the image file. Defaults to None.
        sound_path (str, optional): Path to the sound file. Defaults to None.
        image_size (tuple, optional): New size of the image as (width, height). Defaults to None.

    Returns:
        tuple: A tuple containing the loaded and resized image and sound objects.
    """
    image, sound = None, None
    if image_path:
        image = pygame.image.load(image_path)
        if image_size:
            image = pygame.transform.scale(image, image_size)
    if sound_path:
        pygame.mixer.init()
        sound = pygame.mixer.Sound(sound_path)
    return image, sound


def apply_text_effects(font, text_content, text_color, position):
    """
    Apply effects to the text and create a text surface and rect.

    Args:
        font (pygame.font.Font): The font object to use for rendering text.
        text_content (str): The content of the text to render.
        text_color (tuple): The color of the text (RGB).
        position (tuple): The center position for the text rect.

    Returns:
        tuple: A tuple containing the text surface and rect objects.
    """
    text = font.render(text_content, True, text_color)
    text_rect = text.get_rect(center=position)
    return text, text_rect


def create_frame(screen, bg_color, text, text_rect, image=None, image_rect=None):
    """
    Create a single frame for the animation.

    Args:
        screen (pygame.Surface): The Pygame screen surface.
        bg_color (tuple): The background color (RGB).
        text (pygame.Surface): The text surface.
        text_rect (pygame.Rect): The text rectangle.
        image (pygame.Surface, optional): The image surface. Defaults to None.
        image_rect (pygame.Rect, optional): The image rectangle. Defaults to None.
    """
    screen.fill(bg_color)

    # Draw the image first
    if image:
        screen.blit(image, image_rect)

    # Then draw the text, so it's on top of the image
    screen.blit(text, text_rect)


def save_frame(screen, save_path, frame_number):
    """
    Save the current frame as an image file.

    Args:
        screen (pygame.Surface): The Pygame screen surface.
        save_path (str): The path where the frame will be saved.
        frame_number (int): The current frame number.
    """
    pygame.image.save(screen, f"{save_path}/frame_{frame_number:03d}.png")


def play_sound(sound):
    """
    Play a sound effect.

    Args:
        sound (pygame.mixer.Sound): The sound object to play.
    """
    if sound:
        sound.play()


def create_intro_animation(
    duration_in_seconds,
    fps,
    window_width,
    window_height,
    text_content,
    font_size,
    text_color,
    bg_color,
    save_path,
    image_path=None,
    sound_path=None,
    image_size=None,  # Parameter for image size
):
    """
    Create an intro animation with text, optional images, and sound.

    Args:
        duration_in_seconds (int): The duration of the intro in seconds.
        fps (int): Frames per second of the animation.
        window_width (int): The width of the animation window in pixels.
        window_height (int): The height of the animation window in pixels.
        text_content (str): The text to display in the animation.
        font_size (int): The size of the font for the text.
        text_color (tuple): The color of the text (RGB).
        bg_color (tuple): The background color (RGB).
        save_path (str): The directory path to save frame images.
        image_path (str, optional): Path to an image file for the animation. Defaults to None.
        sound_path (str, optional): Path to a sound file for the animation. Defaults to None.
        image_size (tuple, optional): New size of the image as (width, height). Defaults to None.
    """
    screen, clock = init_pygame(window_width, window_height)
    image, sound = load_resources(image_path, sound_path, image_size)
    font = pygame.font.Font(None, font_size)
    number_of_frames = duration_in_seconds * fps
    lines = text_content.split('\n')

    play_sound(sound)

    for i in range(number_of_frames):
        # Clear the screen for the new frame
        screen.fill(bg_color)


        y_offset = 0  # Initial offset for the first line
        for line in lines:
            text_surface, text_rect = apply_text_effects(
                font,
                line,
                text_color,
                (window_width / 2, window_height / 2 + y_offset)
            )
            screen.blit(text_surface, text_rect)
            y_offset += text_rect.height
        x_position = (window_width / 2) + (i % window_width) * 0.5
        opacity = 255 - (i * 255 // number_of_frames)

        # Render the text with new position and opacity
        text_surface, text_rect = apply_text_effects(
            font,
            text_content,
            text_color,
            (x_position, window_height / 2)
        )
        text_surface.set_alpha(opacity)  # Apply the opacity to the text surface

        # Position for the image
        image_rect = image.get_rect(center=(window_width / 2, window_height / 2)) if image else None

        # Create the frame
        create_frame(screen, bg_color, text_surface, text_rect, image, image_rect)
        save_frame(screen, save_path, i)
        clock.tick(fps)

    pygame.quit()


def create_video_from_frames(save_path, num_frames, fps, sound_path=None):
    """
    Create a video from a sequence of image frames and optionally add sound.

    Args:
        save_path (str): The directory path where frame images are saved.
        num_frames (int): The total number of frames to include in the video.
        fps (int): Frames per second of the video.
        sound_path (str, optional): Path to the sound file. Defaults to None.

    Returns:
        None: The function creates a video file in the specified directory.
    """
    frames = [os.path.join(save_path, f"frame_{i:03d}.png") for i in range(num_frames)]
    clip = ImageSequenceClip(frames, fps=fps)

    if sound_path:
        audio_clip = AudioFileClip(sound_path)
        audio_duration = audio_clip.duration
        video_duration = num_frames / fps
        if audio_duration > video_duration:
            audio_clip = audio_clip.subclip(0, video_duration)
        elif audio_duration < video_duration:
            # If the audio is shorter than the video, loop the audio
            audio_clip = audio_clip.loop(duration=video_duration)

        clip = clip.set_audio(audio_clip)

    clip.write_videofile(os.path.join(save_path, "intro_animation.mp4"))


def main():
    """
    Main function to create an intro animation and compile it into a video.

    Returns:
        None
    """
    # Parameters for the intro animation
    duration_in_seconds = 9
    fps = 24
    window_width = 500
    window_height = 500
    text_content = "Visionary Code Works"
    font_size = 54
    text_color = (253, 218, 13)  # White color
    bg_color = (12, 12, 12)  # Black background
    save_path = "./assets/img/frames/"
    image_path = "./assets/icons/logo.png"
    sound_path = "./assets/sounds/intro_sound.wav"
    num_frames = duration_in_seconds * fps
    image_size = (400, 400)  # desired width and height
    # image, sound = load_resources(image_path, sound_path, image_size)

    # Create intro animation frames
    create_intro_animation(
        duration_in_seconds,
        fps,
        window_width,
        window_height,
        text_content,
        font_size,
        text_color,
        bg_color,
        save_path,
        image_path,
        sound_path,
        image_size,
    )

    # Create video from frames
    create_video_from_frames(save_path, num_frames, fps, sound_path=sound_path)


if __name__ == "__main__":
    main()

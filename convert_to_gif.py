from moviepy.editor import VideoFileClip
import os

def convert_mp4_to_gif(input_path, output_path=None, fps=10):
    """
    Convert an MP4 video to a GIF
    
    Args:
        input_path (str): Path to the input MP4 file
        output_path (str, optional): Path to save the output GIF. 
                                   If None, will use the same name as input with .gif extension
        fps (int): Frames per second for the output GIF (lower = smaller file size)
    """
    if output_path is None:
        output_path = os.path.splitext(input_path)[0] + '.gif'
    
    # Load the video
    video = VideoFileClip(input_path)
    
    # Write the GIF file
    video.write_gif(
        output_path,
        fps=fps,
        program='ffmpeg',
        opt='optimizeplus',
        fuzz=3  # Slight tolerance for better compression
    )
    
    print(f"Successfully created {output_path}")
    return output_path

if __name__ == "__main__":
    input_file = "website_gif.mp4"
    output_file = "website_gif.gif"
    
    if os.path.exists(input_file):
        convert_mp4_to_gif(input_file, output_file, fps=10)
    else:
        print(f"Error: {input_file} not found in the current directory.")

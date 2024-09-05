import re
import subprocess
from config import *
from pyrogram.types import User
          
async def remove_unwanted(caption):
    try:
        # Remove .mkv and .mp4 extensions if present
        cleaned_caption = re.sub(r'\.mkv|\.mp4|\.webm', '', caption)
        return cleaned_caption
    except Exception as e:
        logger.error(e)
        return None
  
async def get_duration(file_path: str) -> str:
    try:
        # Use ffprobe to get video duration
        duration_cmd = [
            'ffprobe', '-v', 'error', '-show_entries', 'format=duration', 
            '-of', 'default=noprint_wrappers=1:nokey=1', file_path
        ]
        duration = float(subprocess.check_output(duration_cmd).strip())
        
        return duration
    except Exception as e:
        print(f"Error generating thumbnail: {e}")
        return None        
    
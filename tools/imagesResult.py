import os
from utils.images_info import ImageSearchService
from typing import List
from dotenv import load_dotenv
from langchain.tools import tool
import requests

class ImageInfoTool:
    def __init__(self):
        load_dotenv()
        self.api_key = os.environ.get("PIXABAY_API_KEY")
        self.image_service = ImageSearchService(self.api_key)
        self.image_tool_list = self._setup_tools()

    def _setup_tools(self) -> List:
        """Setup all tools for the image suggestion tool."""

        @tool
        def get_city_images(city: str) -> str:
            """Fetch top images from Pixabay based on a city name."""
            image_urls = self.image_service.get_images_for_city(city)
            if image_urls:
                return f"Top image results for '{city}':\n" + "\n".join(image_urls)
            return f"No images found for '{city}'."

        return [get_city_images]

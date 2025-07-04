import requests
from typing import List
class ImageSearchService:
    """Service to fetch images from Pixabay based on city name."""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://pixabay.com/api/"
    
    def get_images_for_city(self, city: str, count: int = 5) -> List[str]:
        try:
            params = {
                "key": self.api_key,
                "q": city,
                "image_type": "photo",
                "per_page": count
            }
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            data = response.json()
            return [hit["webformatURL"] for hit in data.get("hits", [])]
        except Exception as e:
            return [f"Error fetching images: {e}"]
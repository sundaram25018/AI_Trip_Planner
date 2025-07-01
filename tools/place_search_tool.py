import os
from utils.place_info_search import FoursquarePlaceSearchTool, TavilyPlaceSearchTool
from typing import List
from langchain.tools import tool
from dotenv import load_dotenv

class PlaceSearchTool:
    def __init__(self):
        load_dotenv()
        self.foursquare_api_key = os.environ.get("FOURSQUARE_API_KEY")
        self.foursquare_search = FoursquarePlaceSearchTool(self.foursquare_api_key)
        self.tavily_search = TavilyPlaceSearchTool()
        self.place_search_tool_list = self._setup_tools()

    def _setup_tools(self) -> List:
        """Setup all tools for the place search tool"""
        
        @tool
        def search_attractions(place: str) -> str:
            """Search attractions of a place"""
            try:
                attraction_result = self.foursquare_search.search_attractions(place)
                if attraction_result:
                    return f"Following are the attractions of {place} as suggested by Foursquare: {attraction_result}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_attractions(place)
                return f"Foursquare cannot find the details due to {e}. \nFollowing are the attractions of {place}: {tavily_result}"

        @tool
        def search_restaurants(place: str) -> str:
            """Search restaurants of a place"""
            try:
                restaurants_result = self.foursquare_search.search_restaurants(place)
                if restaurants_result:
                    return f"Following are the restaurants of {place} as suggested by Foursquare: {restaurants_result}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_restaurants(place)
                return f"Foursquare cannot find the details due to {e}. \nFollowing are the restaurants of {place}: {tavily_result}"

        @tool
        def search_activities(place: str) -> str:
            """Search activities of a place"""
            try:
                activities_result = self.foursquare_search.search_activity(place)
                if activities_result:
                    return f"Following are the activities in and around {place} as suggested by Foursquare: {activities_result}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_activity(place)
                return f"Foursquare cannot find the details due to {e}. \nFollowing are the activities of {place}: {tavily_result}"

        @tool
        def search_transportation(place: str) -> str:
            """Search transportation of a place"""
            try:
                transport_result = self.foursquare_search.search_transportation(place)
                if transport_result:
                    return f"Following are the modes of transportation available in {place} as suggested by Foursquare: {transport_result}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_transportation(place)
                return f"Foursquare cannot find the details due to {e}. \nFollowing are the modes of transportation available in {place}: {tavily_result}"

        return [search_attractions, search_restaurants, search_activities, search_transportation]

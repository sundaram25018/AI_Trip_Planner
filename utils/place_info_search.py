import os
import json
import requests
from langchain_tavily import TavilySearch

class FoursquarePlaceSearchTool:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.foursquare.com/v3/places/search"
        self.headers = {
            "Accept": "application/json",
            "Authorization": self.api_key
        }

    def search_places(self, query: str, near: str, limit=10):
        params = {
            "query": query,
            "near": near,
            "limit": limit,
            "sort": "RELEVANCE"
        }
        response = requests.get(self.base_url, headers=self.headers, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": response.text}

    def search_attractions(self, place: str) -> dict:
        """
        Searches for attractions using Foursquare API.
        """
        return self.search_places("attractions", place, limit=10)

    def search_restaurants(self, place: str) -> dict:
        """
        Searches for restaurants using Foursquare API.
        """
        return self.search_places("restaurants", place, limit=10)

    def search_activity(self, place: str) -> dict:
        """
        Searches for activities using Foursquare API.
        """
        return self.search_places("things to do", place, limit=10)

    def search_transportation(self, place: str) -> dict:
        """
        Searches for transportation options using Foursquare API.
        """
        return self.search_places("transportation", place, limit=10)


class TavilyPlaceSearchTool:
    def __init__(self):
        pass

    def tavily_search_attractions(self, place: str) -> dict:
        """
        Searches for attractions using TavilySearch.
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"top attractive places in and around {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result

    def tavily_search_restaurants(self, place: str) -> dict:
        """
        Searches for restaurants using TavilySearch.
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"what are the top 10 restaurants and eateries in and around {place}."})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result

    def tavily_search_activity(self, place: str) -> dict:
        """
        Searches for activities using TavilySearch.
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"activities in and around {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result

    def tavily_search_transportation(self, place: str) -> dict:
        """
        Searches for transportation using TavilySearch.
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"What are the different modes of transportations available in {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result

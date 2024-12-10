class WebsiteInfo:
    def __init__(self):
        self.name = "SpeedofCars.com"
        self.developer_experience = "2 weeks"
        self.purpose = "Explore a hobby while making money"
        self.target_audience = "Car enthusiasts, primarily male, interested in buying and learning about cars"

class WebsitePage:
    def __init__(self, title, content):
        self.title = title
        self.content = content

class CarDatabase:
    def __init__(self):
        self.cars = {
            "race_cars": {
                "F1": [
                    {"name": "Mercedes W14", "team": "Mercedes", "specs": "Latest F1 car"},
                    {"name": "Red Bull RB19", "team": "Red Bull Racing", "specs": "Championship-winning car"}
                ],
                "NASCAR": [
                    {"name": "Hendrick Motorsports Camaro", "team": "Hendrick", "specs": "Top-tier NASCAR vehicle"}
                ]
            },
            "dealership_types": [
                "Carvana",
                "CarMax",
                "Local Dealerships"
            ]
        }
    
    def get_race_cars(self, category=None):
        if category:
            return self.cars["race_cars"].get(category, [])
        return self.cars["race_cars"]
    
    def get_dealerships(self):
        return self.cars["dealership_types"]

class MaintenanceGuide:
    def __init__(self):
        self.tools = {
            "Basic Toolkit": {
                "items": ["Wrench Set", "Screwdriver Set", "Jack"],
                "estimated_cost": "$100-$200"
            },
            "Advanced Toolkit": {
                "items": ["Diagnostic Scanner", "Torque Wrench", "Oil Filter Wrench"],
                "estimated_cost": "$300-$500"
            }
        }
    
    def get_maintenance_tools(self, level="Basic"):
        return self.tools.get(f"{level} Toolkit", {})

class SpeedOfCarsWebsite:
    def __init__(self):
        self.info = WebsiteInfo()
        self.car_database = CarDatabase()
        self.maintenance_guide = MaintenanceGuide()
        
        # Define website pages
        self.pages = {
            "Homepage": WebsitePage(
                "Homepage", 
                "Comprehensive car information with images and specifications"
            ),
            "Dealerships": WebsitePage(
                "Car Dealerships", 
                "Listings of car dealerships, clubs, and museums"
            ),
            "Maintenance": WebsitePage(
                "Car Maintenance", 
                "Repair guides and tool recommendations"
            )
        }
    
    def display_website_info(self):
        print(f"Website Name: {self.info.name}")
        print(f"Developer Experience: {self.info.developer_experience}")
        print(f"Purpose: {self.info.purpose}")
        print(f"Target Audience: {self.info.target_audience}")
    
    def display_race_cars(self, category=None):
        print("\nRace Cars:")
        race_cars = self.car_database.get_race_cars(category)
        for car_type, cars in race_cars.items() if not category else enumerate(race_cars):
            print(f"\n{car_type}:")
            for car in cars:
                print(f"- {car['name']} (Team: {car['team']})")
                print(f"  Specs: {car['specs']}")
    
    def display_maintenance_tools(self, level="Basic"):
        tools = self.maintenance_guide.get_maintenance_tools(level)
        print(f"\n{level} Maintenance Toolkit:")
        print(f"Estimated Cost: {tools.get('estimated_cost', 'N/A')}")
        print("Tools:")
        for tool in tools.get('items', []):
            print(f"- {tool}")
    
    def display_dealerships(self):
        print("\nDealerships:")
        for dealership in self.car_database.get_dealerships():
            print(f"- {dealership}")

def main():
    website = SpeedOfCarsWebsite()
    
    print("Welcome to SpeedofCars.com!")
    
    # Display website information
    website.display_website_info()
    
    # Display race cars
    website.display_race_cars()
    
    # Display maintenance tools
    website.display_maintenance_tools()
    
    # Display dealerships
    website.display_dealerships()

if __name__ == "__main__":
    main()

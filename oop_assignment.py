class Smartphone:
    def __init__(self, brand, model, battery_life, storage):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life
        self.storage = storage
    
    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Battery Life: {self.battery_life} hours")
        print(f"Storage: {self.storage} GB")
    
    def charge(self):
        print(f"{self.model} is charging...")
    
    def use_app(self, app_name):
        print(f"Using {app_name} on {self.model}...")
        

class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, battery_life, storage, camera_resolution):
        super().__init__(brand, model, battery_life, storage)
        self.camera_resolution = camera_resolution
    
    def take_photo(self):
        print(f"Taking a photo {self.camera_resolution} Canon camera!")
        
phone = Smartphone("Apple", "iPhone 16", 50, 12)
phone.display_info()
phone.charge()
phone.use_app("Instagram")

camera_phone = SmartphoneWithCamera("Samsung", "Galaxy S30", 24, 3, 90)
camera_phone.display_info()
camera_phone.take_photo()
camera_phone.charge()

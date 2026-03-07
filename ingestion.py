import osmnx as ox

# Define the location
place_name = "Karlsruhe, Germany"

# Define what we want to look for
tags = {
    "amenity": ["restaurant", "cafe"],
    "shop": ["mall", "supermarket"],
    "tourism": ["attraction"]
}

print(f"Fetching data for {place_name} from OpenStreetMap...")

# Fetch the features
features = ox.features_from_place(place_name, tags)

# Show us a preview of what we got
print(f"Successfully retrieved {len(features)} items!")
print(features[['name', 'amenity', 'shop', 'tourism']].head())
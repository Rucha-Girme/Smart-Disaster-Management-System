// Initialize map
const map = L.map("map").setView([20.5937, 78.9629], 5);

// OpenStreetMap Tiles
L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution: "© OpenStreetMap contributors"
}).addTo(map);

// ================= ICONS =================

// User Icon (default)
const userIcon = new L.Icon.Default();

// Hospital - Red
const hospitalIcon = new L.Icon({
    iconUrl: "https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-red.png",
    shadowUrl: "https://unpkg.com/leaflet@1.9.4/dist/images/marker-shadow.png",
    iconSize: [25, 41],
    iconAnchor: [12, 41]
});

// Police - Blue
const policeIcon = new L.Icon({
    iconUrl: "https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-blue.png",
    shadowUrl: "https://unpkg.com/leaflet@1.9.4/dist/images/marker-shadow.png",
    iconSize: [25, 41],
    iconAnchor: [12, 41]
});

// Fire Station - Orange
const fireIcon = new L.Icon({
    iconUrl: "https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-orange.png",
    shadowUrl: "https://unpkg.com/leaflet@1.9.4/dist/images/marker-shadow.png",
    iconSize: [25, 41],
    iconAnchor: [12, 41]
});

// Shelter - Green
const shelterIcon = new L.Icon({
    iconUrl: "https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-green.png",
    shadowUrl: "https://unpkg.com/leaflet@1.9.4/dist/images/marker-shadow.png",
    iconSize: [25, 41],
    iconAnchor: [12, 41]
});

// ================= USER LOCATION =================

navigator.geolocation.getCurrentPosition(

    function(position){

        const lat = position.coords.latitude;
        const lon = position.coords.longitude;

        map.setView([lat, lon], 14);

        // User Marker
        L.marker([lat, lon], { icon: userIcon })
            .addTo(map)
            .bindPopup("<b>You are here</b>")
            .openPopup();

        // ================= OVERPASS QUERY =================

        const query = `
        [out:json];
        (
          node["amenity"="hospital"](around:5000,${lat},${lon});
          node["amenity"="police"](around:5000,${lat},${lon});
          node["amenity"="fire_station"](around:5000,${lat},${lon});
          node["amenity"="shelter"](around:5000,${lat},${lon});
        );
        out;
        `;

        fetch("https://overpass-api.de/api/interpreter", {
            method: "POST",
            body: query
        })
        .then(response => response.json())
        .then(data => {

            data.elements.forEach(place => {

                let icon = hospitalIcon;
                let type = "Hospital";

                switch(place.tags.amenity){

                    case "hospital":
                        icon = hospitalIcon;
                        type = "Hospital";
                        break;

                    case "police":
                        icon = policeIcon;
                        type = "Police Station";
                        break;

                    case "fire_station":
                        icon = fireIcon;
                        type = "Fire Station";
                        break;

                    case "shelter":
                        icon = shelterIcon;
                        type = "Shelter";
                        break;
                }

                L.marker([place.lat, place.lon], {
                    icon: icon
                })
                .addTo(map)
                .bindPopup(`
                    <b>${place.tags.name || type}</b><br>
                    ${type}
                `);

            });

        })
        .catch(error => {
            console.error("Overpass API Error:", error);
            alert("Unable to load nearby emergency locations.");
        });

    },

    function(error){

        alert("Please allow location access.");

        console.error(error);

    }

);
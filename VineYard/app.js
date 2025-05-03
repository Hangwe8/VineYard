// Handle distress signal button click
function sendDistressSignal() {
    const whatsappNumber = "0818179230"; // Replace with actual number
    const message = "Emergency! Please assist.";
    const whatsappUrl = `https://api.whatsapp.com/send?phone=${whatsappNumber}&text=${encodeURIComponent(message)}`;
    window.open(whatsappUrl, "_blank");
    Swal.fire({
        title: 'Distress Signal Sent!',
        text: 'Your emergency message has been sent via WhatsApp.',
        icon: 'success',
        confirmButtonText: 'OK'
    });
}

// Handle chatbot send button click
document.getElementById('sendButton').addEventListener('click', () => {
    const userInput = document.getElementById('userInput').value;
    const chatWindow = document.getElementById('chatWindow');
    chatWindow.innerHTML += `<p><strong>You:</strong> ${userInput}</p>`;
    document.getElementById('userInput').value = '';

    // Fetch AI chatbot response from backend
    fetch('/chatbot', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        chatWindow.innerHTML += `<p><strong>Bot:</strong> ${data.response}</p>`;
    });
});

// Initialize Google Maps
function initMap() {
    const mapContainer = document.getElementById("mapContainer");

    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            (position) => {
                const userLocation = {
                    lat: position.coords.latitude,
                    lng: position.coords.longitude,
                };

                const map = new google.maps.Map(mapContainer, {
                    zoom: 15,
                    center: userLocation,
                });

                new google.maps.Marker({
                    position: userLocation,
                    map: map,
                    title: "You are here",
                });

                // Example: Add a marker for nearest help (static location for now)
                const nearestHelp = { lat: userLocation.lat + 0.01, lng: userLocation.lng + 0.01 };
                new google.maps.Marker({
                    position: nearestHelp,
                    map: map,
                    title: "Nearest Help",
                    icon: "http://maps.google.com/mapfiles/ms/icons/green-dot.png",
                });
            },
            (error) => {
                console.error("Geolocation error:", error);
                mapContainer.innerHTML = "<p>Unable to retrieve your location. Please enable location services and try again.</p>";
            }
        );
    } else {
        mapContainer.innerHTML = "<p>Geolocation is not supported by your browser.</p>";
    }
}

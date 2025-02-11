<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Carpool Finder</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; padding: 20px; }
        input, button { padding: 10px; margin: 5px; }
        .driver-card { border: 1px solid #ccc; padding: 10px; margin: 10px auto; width: 300px; }
    </style>
</head>
<body>
    <h1>Find a Carpool Driver Near You</h1>
    <input type="text" id="postalCode" placeholder="Enter your postal code">
    <button onclick="findDrivers()">Find</button>
    <div id="drivers"></div>

    <script>
        async function findDrivers() {
            const postalCode = document.getElementById("postalCode").value;
            if (!postalCode.trim()) return;
            
            try {
                const response = await fetch(`http://localhost:5000/find_drivers?postal_code=${postalCode}`);
                const drivers = await response.json();
                
                const driverList = document.getElementById("drivers");
                driverList.innerHTML = "";
                
                if (drivers.length === 0) {
                    driverList.innerHTML = "<p>No drivers found.</p>";
                    return;
                }
                
                drivers.forEach(driver => {
                    const card = document.createElement("div");
                    card.className = "driver-card";
                    card.innerHTML = `<h2>${driver.name}</h2><p>Car: ${driver.car}</p><p>Contact: ${driver.contact}</p>`;
                    driverList.appendChild(card);
                });
            } catch (error) {
                console.error("Error fetching drivers:", error);
            }
        }
    </script>
</body>
</html>

var map = L.map('mapid');
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
	attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

map.setView(new L.LatLng(40.7328, -73.9560), 10);

async function asyncCall() {
	let serialized = await fetch('/static/data_test.geojson')

	data = await serialized.json()
	function displayMapLatLng (data) {
	for (i = 0; i < data['features'].length; i++) {
    	
	//var color = 'red';
	price = data['features'][i]["properties"]["prop"]
	if (price <= 150) {
 		color = 'green';
	} else if (price <= 300){
		color = 'blue';	
	} else {
		color = 'red'
	}
    	var circle = new L.circle((data['features'][i]['geometry']["coordinates"]), 25, {color: color, opacity:1})
    circle.addTo(map);
}
	
  		
	}
displayMapLatLng(data)
}

asyncCall();





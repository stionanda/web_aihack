var map = L.map('mapid');
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
	attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

map.setView(new L.LatLng(40.7128, -74.0060), 11);


L.marker().addTo(map);

async function asyncCall() {
	let serialized = await fetch('/static/output.json')

	data = await serialized.json()

	//for (i = 0; i < data.length; i++) {
  	//	name = String(i)
  	//	L.marker(data[name]).addTo(map);
	//}
	L.marker([50.5, 30.5]).addTo(map);
}

asyncCall();




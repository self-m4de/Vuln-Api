function getData() {
    fetch('http://127.0.0.1:5000/all')
    .then(response => response.json())
    .then(data => {
        data.forEach(getAll);
        });
    }

function getAll(data, index, array) {
    var element = document.getElementById("users");
    var name = document.createElement('p');
    name.innerHTML = data['name'];
    element.appendChild(name);
}
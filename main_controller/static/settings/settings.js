function saveSettings() {
    var robotIP = document.getElementById("robotIP").value;
    var port = document.getElementById("port").value;

    // Use Ajax to send a request to the server when the button is clicked
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "{% url 'savesettings' %}", true);
    xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}"); // Add CSRF token
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.send(JSON.stringify({ robotIP: robotIP, port: port }));
}
function sendmessage() {
    var message = document.getElementById("message").value;

    // Use Ajax to send a request to the server when the button is clicked
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "{% url 'sendmessage' %}", true);
    xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}"); // Add CSRF token
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.send(JSON.stringify({message: message }));

    //clear message
    document.getElementById("message").value = "";
}

var buttons = ["startBtn", "cameraBtn", "soundBtn", "shutdownBtn"];

buttons.forEach(function (btnId) {
    document.getElementById(btnId).addEventListener("click", function () {
        // Use Ajax to send a request to the server when the button is clicked
        var xhr = new XMLHttpRequest();
        xhr.open("POST", document.getElementById(btnId).parentNode.action, true);
        xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}"); // Add CSRF token
        xhr.send();
    });
});
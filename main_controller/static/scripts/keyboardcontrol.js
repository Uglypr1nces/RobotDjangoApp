document.addEventListener("keydown", function(event) {
    if (event.keyCode === "w".charCodeAt(0)) {
        window.alert("w has been pressed");
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "{% url 'forward' %}", true);
        xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}"); // Add CSRF token
        xhr.send();
    }
    if (event.keyCode === "s".charCodeAt(0)) {
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "{% url 'backward' %}", true);
        xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}"); // Add CSRF token
        xhr.send();
    }
    if (event.keyCode === "a".charCodeAt(0)) {
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "{% url 'left' %}", true);
        xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}"); // Add CSRF token
        xhr.send();
    }
    if (event.keyCode === "d".charCodeAt(0)) {
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "{% url 'right' %}", true);
        xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}"); // Add CSRF token
        xhr.send();
    }
});

document.addEventListener("DOMContentLoaded", function() {
    function putBatteryInfo(x, y) {
        var batteryArrow = document.getElementById("battery_arrow");
        var pixelRobot = document.getElementById("pixelRobot");
        let pixelRobotRect = pixelRobot.getBoundingClientRect();
        batteryArrow.style.left = pixelRobotRect.left + x + "px";
        batteryArrow.style.top = pixelRobotRect.top + y + "px";
        batteryArrow.style.display = "block"; // Make sure the arrow is visible

        console.log("Robot Position: " + pixelRobotRect.left + ", " + pixelRobotRect.top);
        console.log("Battery Arrow Position: " + batteryArrow.style.left + ", " + batteryArrow.style.top);
    }
    function showBatteryInfo(x,y) {
        var percantage = document.getElementById("percantage");
        var batteryArrow = document.getElementById("battery_arrow");
        let batteryArrowRect = batteryArrow.getBoundingClientRect();
        percantage.style.left = batteryArrowRect.left + x + "px";
        percantage.style.top = batteryArrowRect.top + y + "px";
        console.log("Battery Position: " + percantage.style.left + "," + percantage.style.top)
    }
    putBatteryInfo(420, -200);
    showBatteryInfo(0, -230);

    if (!localStorage.getItem('messageShown')) {
        alert("Hello User! If this is your first time using this website, please make sure to read the information page first. Enjoy!");
        localStorage.setItem('messageShown', true);
    }
    
    let keyboardactive = false;
    
    document.getElementById("movement").addEventListener("click", function () {
        keyboardactive = !keyboardactive;
        alert("Keyboard Control " + (keyboardactive ? "Activated" : "Deactivated"));
    });
    
    function sendmessage() {
        var message = document.getElementById("message").value;
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "{% url 'send_command' %}", true);
        xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}");
        xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
        xhr.send("message=" + encodeURIComponent(message));
        document.getElementById("message").value = "";
    }
    
    document.body.addEventListener("keydown", function (ev) {
        if (keyboardactive) {
            var xhr = new XMLHttpRequest();
            var url = "";
            if (ev.key === "w") url = "{% url 'forward' %}";
            else if (ev.key === "s") url = "{% url 'backward' %}";
            else if (ev.key === "a") url = "{% url 'left' %}";
            else if (ev.key === "d") url = "{% url 'right' %}";
            else if (ev.key === "e") url = "{% url 'camera_left' %}";
            else if (ev.key === "q") url = "{% url 'camera_right' %}";
            else if (ev.key === "r") url = "{% url 'camera_up' %}";
            else if (ev.key === "f") url = "{% url 'camera_down' %}";
    
            if (url) {
                xhr.open("POST", url, true);
                xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}");
                xhr.send();
            }
        }
    });
});
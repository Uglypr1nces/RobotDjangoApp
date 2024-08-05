document.addEventListener("DOMContentLoaded", function() {
    function positionBatteryArrow(x, y) {
        var batteryArrow = document.getElementById("battery-arrow");
        var pixelRobot = document.getElementById("pixel-robot-container");
        let pixelRobotRect = pixelRobot.getBoundingClientRect();
        
        batteryArrow.style.left = (pixelRobotRect.left + x) + "px";
        batteryArrow.style.top = (pixelRobotRect.top + y) + "px";
        batteryArrow.style.display = "block"; // Make sure the arrow is visible

        console.log("Robot Position: " + pixelRobotRect.left + ", " + pixelRobotRect.top);
        console.log("Battery Arrow Position: " + batteryArrow.style.left + ", " + batteryArrow.style.top);
    }
    
    function positionBatteryPercentage(x, y) {
        var percentage = document.getElementById("percentage");
        var batteryArrow = document.getElementById("battery-arrow");
        let batteryArrowRect = batteryArrow.getBoundingClientRect();
        
        percentage.style.left = (batteryArrowRect.left + x) + "px";
        percentage.style.top = (batteryArrowRect.top + y) + "px";
        
        console.log("Battery Position: " + percentage.style.left + ", " + percentage.style.top);
    }
    
    function displayWelcomeMessage() {
        if (!localStorage.getItem('messageShown')) {
            alert("Hello User! If this is your first time using this website, please make sure to read the information page first. Enjoy!");
            localStorage.setItem('messageShown', true);
        }
    }

    function toggleKeyboardControl() {
        keyboardActive = !keyboardActive;
        alert("Keyboard Control " + (keyboardActive ? "Activated" : "Deactivated"));
    }
    
    function sendMessage() {
        var message = document.getElementById("message-input").value;
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "{% url 'send_command' %}", true);
        xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}");
        xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
        xhr.send("message=" + encodeURIComponent(message));
        document.getElementById("message-input").value = "";
    }
    
    function handleKeyboardEvent(ev) {
        if (keyboardActive) {
            var xhr = new XMLHttpRequest();
            var url = "";
            switch(ev.key) {
                case "w": url = "{% url 'forward' %}"; break;
                case "s": url = "{% url 'backward' %}"; break;
                case "a": url = "{% url 'left' %}"; break;
                case "d": url = "{% url 'right' %}"; break;
                case "e": url = "{% url 'camera_left' %}"; break;
                case "q": url = "{% url 'camera_right' %}"; break;
                case "r": url = "{% url 'camera_up' %}"; break;
                case "f": url = "{% url 'camera_down' %}"; break;
                default: return;
            }
            
            xhr.open("POST", url, true);
            xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}");
            xhr.send();
        }
    }
    
    positionBatteryArrow(420, -200);
    positionBatteryPercentage(0, -230);
    displayWelcomeMessage();
    
    let keyboardActive = false;
    
    document.getElementById("movement-control").addEventListener("click", toggleKeyboardControl);
    document.getElementById("send-message-btn").addEventListener("click", sendMessage);
    document.body.addEventListener("keydown", handleKeyboardEvent);
});

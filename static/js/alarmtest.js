let btn_probe = document.getElementById("probealarm");
const einsatz_alarm = new Audio("./static/sounds/einsatz_alarmton.mp3");

btn_probe.addEventListener("click", function(){
    einsatz_alarm.play();
    einsatz_alarm.currentTime = 0;
});
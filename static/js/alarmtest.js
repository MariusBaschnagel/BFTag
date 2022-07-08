let btn_probe = document.getElementById("probealarm");

/* audio elements */
const einsatz_alarm = new Audio("./static/audio/einsatz_alarmton.mp3");

const f1 = new Audio("./static/audio/stichwort/feuer_eins.mp3");
const f2 = new Audio("./static/audio/stichwort/feuer_zwei.mp3");
const f3 = new Audio("./static/audio/stichwort/feuer_drei.mp3");
const h1 = new Audio("./static/audio/stichwort/hilfe_eins.mp3");
const h2 = new Audio("./static/audio/stichwort/hilfe_zwei.mp3");
const h3 = new Audio("./static/audio/stichwort/hilfe_drei.mp3");

const HLF = new Audio("./static/audio/fahrzeuge/HLF.mp3");
const TLF = new Audio("./static/audio/fahrzeuge/TLF.mp3");
const LF8 = new Audio("./static/audio/fahrzeuge/LF8.mp3");
const MTW = new Audio("./static/audio/fahrzeuge/MTW.mp3");
const GWL = new Audio("./static/audio/fahrzeuge/GWL.mp3");
const GWAS = new Audio("./static/audio/fahrzeuge/GWAS.mp3");
/******************************************************************************/

let audioArray = [einsatz_alarm]

btn_probe.addEventListener("click", function(){
    btn_probe.disabled = "true";
    generateMeldung();
    let prevSoundDurationSum = 0;
    for (let soundnr = 0; soundnr < audioArray.length; soundnr++) {
        setTimeout(playSound, prevSoundDurationSum, audioArray[soundnr]);
    
        prevSoundDurationSum += audioArray[soundnr].duration * 1250;
    }
    resetMeldung();
    setTimeout(function(){btn_probe.disabled = false;}, prevSoundDurationSum)
});

function playSound(sound) {
    sound.play();
}

function generateMeldung(){
    audioArray.push(h3, HLF, TLF, LF8);
}

function resetMeldung(){
    audioArray = [];
    audioArray.push(einsatz_alarm);
    
}
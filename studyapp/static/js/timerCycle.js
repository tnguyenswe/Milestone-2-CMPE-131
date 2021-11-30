// code from this website was referenced to write this code.
// https://dev.to/gspteck/create-a-stopwatch-in-javascript-2mak

const timer = document.getElementById('stopwatch');

var stopTime = true;

class TimerHandler {
    constructor() {
        this.h = 0;
        this.m = 0;
        this.s = 0;
    }

    runTimer() {
        if (stopTime == false) {
            this.s = this.s + 1;

            if (this.s == 60) {
                this.m = this.m + 1;
                this.s = 0;
            }
            if (this.m == 60) {
                this.h = + 1;
                this.m = 0;
                this.s = 0;
            }
            let innerHtml = ''
            let h = '' + this.h;
            let m = '' + this.m;
            let s = '' + this.s;
            if (this.h < 10 || this.h == 0) {
                h = '0' + h;
            }

            if (this.m < 10 || this.m == 0) {
                m = '0' + m;
            }
            if (this.s < 10 || this.s == 0) {
                s = '0' + s;
            }

            timer.innerHTML = h + ':' + m + ':' + s;

            setTimeout(this.runTimer.bind(this), 1000);
        }
    }
    reset() {
        this.h = 0
        this.m = 0
        this.s = 0
    }
}


var timerHandler = new TimerHandler();
function submit(e) {
    e.preventDefault();
}
function startTimer() {
    if (stopTime == true) {
        stopTime = false;
        timerHandler.runTimer();
    }
}
function stopTimer() {
    if (stopTime == false) {
        stopTime = true;
    }
}

function reset() {
    timerHandler.reset();
    timer.innerHTML = '00:00:00';
}

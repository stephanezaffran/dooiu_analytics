const inactivityDuration = 60*60*1000;
let lastActivityTime = new Date();

document.addEventListener('mousemove', () => {
    resetInterval();
});

document.addEventListener('keypress', () => {
    resetInterval();
});

window.addEventListener('load', () => {
    resetInterval();
});

let intervalId;

function autoLogout() {
        window.location.href = '/logout';
}


function resetInterval() {
    clearInterval(intervalId);
    intervalId = setInterval(autoLogout, inactivityDuration);
}

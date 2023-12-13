let startTime = 10; // 10 minutes
let currentTime = startTime * 60; // convert to seconds
const timerDisplay = document.getElementById('timer');
const endingSound = document.getElementById('ending-sound');
let timerInterval;

function updateTimerDisplay(seconds) {
  const minutes = Math.floor(seconds / 60);
  let remainderSeconds = seconds % 60;
  timerDisplay.textContent = `${minutes}:${remainderSeconds < 10 ? '0' : '' }${remainderSeconds} minutes remaining`;
  if (seconds <= 5) {
    endingSound.play();
  }
}

function startTimer() {
  clearInterval(timerInterval);
  timerInterval = setInterval(() => {
    currentTime--;
    updateTimerDisplay(currentTime);
    if (currentTime <= 0) {
      clearInterval(timerInterval);
      alert("Time's up!");
    }
  }, 1000);
}

function stopTimer() {
  clearInterval(timerInterval);
  currentTime = startTime * 60; // reset to the start time
  updateTimerDisplay(currentTime);
  endingSound.pause();
  endingSound.currentTime = 0;
}

// Initialize
updateTimerDisplay(currentTime);

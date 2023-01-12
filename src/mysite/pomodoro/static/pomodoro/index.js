// Assigning to variables stable elements
const countdownContainer = document.querySelector("#countdown-container"),
      cancelContainer = document.querySelector("#cancel-container"),
      cancelButton = document.querySelector("#cancel-button"),
      selectionContainer = document.querySelector("#selection-container"),
      instruction = document.querySelector("#instruction"),
      timeButtonsContainer = document.querySelector("#time-buttons-container")

// Add event listener to selectionContainer
selectionContainer.addEventListener("click", renderCountdown);


document.querySelector('form').addEventListener('submit', e => {
  e.preventDefault();
  const data = new FormData(e.target);
  console.log([...data.entries()]);

  hideElements(selectionContainer);
  unhideElements(countdownContainer, cancelContainer);

  const minutesChosen = parseFloat(document.querySelector('[name="time"]').value);

  startCountdown(minutesChosen);
});

// var el = selectionContainer;
// if(el){
//   el.addEventListener("click", renderCountdown);
// }

// Write the logic to display the countdown timer on the page
function renderCountdown(evt) {
  // If the element clicked inside selectionContainer is one that can set the time, then hide the unnecessary elements on the page, and start countdown timer, passing in as an integer the minute that the user chose

  if (evt.target.classList.contains("set-time")) {
    hideElements(selectionContainer);
    unhideElements(countdownContainer, cancelContainer);

    const minutesChosen = parseFloat(evt.target.id);

    startCountdown(minutesChosen);
  }
}

// Helper function to hide elements you pass in; use rest parameters to take in an unknown number of arguments
function hideElements(...elems) {
  // Set each element to hidden
  elems.forEach((elem) => (elem.hidden = true));
}

// Helper function to unhide elements you pass in
function unhideElements(...elems) {
  elems.forEach((elem) => (elem.hidden = false));
}

function startCountdown(minutesChosen) {
  // Calculate total time in seconds, the second display value, and the minute display value
  let totalTimeInSeconds = minutesChosen * 60;

  // Set the countdown to run every 1000 ms (1 second); run this function every second
  let setCountDownInterval = setInterval(function () {
    let displaySeconds = totalTimeInSeconds % 60;
    let displayMinutes = Math.floor(totalTimeInSeconds / 60);

    // Add a zero in front of displaySeconds if it is single digit
    displaySeconds =
      displaySeconds < 10 ? "0" + displaySeconds : displaySeconds;

    // Add the time to the countdown container
    countdownContainer.innerHTML = `${displayMinutes} : ${displaySeconds}`;
    
    // Decrement the totalTimeInSeconds
    totalTimeInSeconds--;

    // If the time reaches 0, then stop the countdown, and render video
    if (totalTimeInSeconds < 0) {
      clearInterval(setCountDownInterval);
      renderBackToStart();
      // renderVideo();
    }

    // If the cancel button is clicked, then render back to start
    cancelButton.addEventListener("click", (evt) => {
      clearInterval(setCountDownInterval);
      renderBackToStart();
    });
  }, 1000);
}

function renderBackToStart() {
  // Hide the countdown container, cancel button container, video container, take break span
  hideElements(countdownContainer, cancelContainer);

  // Unhide description, selection container, time buttons container
  unhideElements(selectionContainer, timeButtonsContainer);
}

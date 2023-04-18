
//breakfast
function toggleFocus() {
  var body = document.getElementsByTagName('body')[0];
  var overlay = document.createElement('div');
  var card = document.getElementById('myCard');
  if (card) {
    overlay.classList.add('overlay');
    body.appendChild(overlay);
    overlay.appendChild(card);
    overlay.classList.add('active');
    card.style.display = 'block';
    var closeButton = document.getElementById('closeButton');
if (closeButton) {
  console.log('Close button found!');
  closeButton.addEventListener('click', function() {
    overlay.classList.remove('active');
    card.style.display = 'none';
  });
} else {
  console.error('Error: Could not find close button element with ID "closeButton".');
}
}
}

//dinner

function toggleDinner() {
    // Get the <body> element
  var body = document.getElementsByTagName('body')[0];
    // Create a new <div> element for the overlay
  var Doverlay = document.createElement('div');
    // Get the <div> element with the ID "myCard"
  var Dcard = document.getElementById('Dinner-Card');
  // Check if the <div> element was found
  if(Dcard){
      // Add the "overlay" class to the new 
  Doverlay.classList.add('Doverlay');
     // Append the new <div> element to the
  body.appendChild(Doverlay);
      // Append the <div> element with the ID "myCard"
      // to the new <div> element
  Doverlay.appendChild(Dcard);
    // Add the "active" class to the new 
  Doverlay.classList.add('active');
      // Set the "display" style of the <div>
      // element with the ID "myCard" to "block"
  Dcard.style.display = 'block';
      // Get the <button> element with the ID "closeButton"
    var DcloseButton = document.getElementById('DcloseButton');
        // Check if the <button> element was found
if (DcloseButton) {
  console.log('Close button found!');
  // Add an event listener to the <button> element for the "click" event
  DcloseButton.addEventListener('click', function() {
            // Remove the "active" class from the new <div> element
    Doverlay.classList.remove('active');
            // Set the "display" style of the 
            //<div> element with the ID "myCard" to "none"
    Dcard.style.display = 'none';
  });
} else {
      // Log an error message to the console if the 
      //<div> element was not found
  console.error('Error: Could not find close button element with ID "closeButton".');
}
}
}

//lunch

function toggleLunch() {
  var body = document.getElementsByTagName('body')[0];
  var Loverlay = document.createElement('div');
  var Lcard = document.getElementById('lunch-Card');
  if (Lcard) {
    Loverlay.classList.add('Loverlay');
    body.appendChild(Loverlay);
    Loverlay.appendChild(Lcard);
    Loverlay.classList.add('active');
    Lcard.style.display = 'block';
    var LcloseButton = document.getElementById('LcloseButton');
if (LcloseButton) {
  console.log('Close button found!');
  LcloseButton.addEventListener('click', function() {
    Loverlay.classList.remove('active');
    Lcard.style.display = 'none';
  });
} else {
  console.error('Error: Could not find close button element with ID "closeButton".');
}
}
}

//pre

function togglepre(){
  var body = document.getElementsByTagName('body')[0];
  var Poverlay = document.createElement('div');
  var Pcard = document.getElementById('pre-Card');
  if (Pcard) {
    Poverlay.classList.add('Poverlay');
    body.appendChild(Poverlay);
    Poverlay.appendChild(Pcard);
    Poverlay.classList.add('active');
    Pcard.style.display = 'block';
    var PrecloseButton = document.getElementById('PrecloseButton');
if (PrecloseButton) {
  console.log('Close button found!');
  PrecloseButton.addEventListener('click', function() {
    Poverlay.classList.remove('active');
    Pcard.style.display = 'none';
  });
} else {
  console.error('Error: Could not find close button element with ID "closeButton".');
}
}
}
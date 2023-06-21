// Get the modal element
let modalDiv = document.getElementById("modal-div");
let avatarImage = document.getElementById("avatar-img"); // Get the avatar image element

// Get the image and text elements inside the modal
let modalImage = document.getElementById("modal-image");
let modalText = document.getElementById("modal-text");
let modalTitle = document.querySelector("#modal-box h2");

// Function to open the modal and display the content with fade-in effect
function openModal(imageSrc, textContent, titleContent) {
  modalDiv.style.display = "block";
  modalDiv.classList.remove("fade-in"); // Remove the fade-in class
  void modalDiv.offsetWidth; // Trigger reflow to restart the animation
  modalDiv.classList.add("fade-in"); // Add the fade-in class again
  modalImage.src = imageSrc;
  modalImage.classList.add("fade-in");
  modalText.innerText = textContent;
  modalTitle.innerText = titleContent;
  modalImage.style.display = "block";
  avatarImage.style.opacity = "1"; // Keep the avatar image visible
  document.getElementById("static-modal-content").style.display = "none";
}

// Function to close the modal
function closeModal() {
  modalDiv.style.display = "none";
  showStaticModal(); // Show the static modal
}

// Close the modal when clicking outside of it
document.addEventListener("click", function (event) {
  const targetElement = event.target;
  if (
    !modalDiv.contains(targetElement) &&
    !targetElement.classList.contains("modal-image")
  ) {
    closeModal();
  }
});

let closeButton = document.querySelector(".modal-close-button");
closeButton.addEventListener("click", function () {
  closeModal();
});

let icons = document.querySelectorAll(".modal-image");
icons.forEach(function (icon) {
  icon.addEventListener("click", function () {
    let imageSrc = icon.src;
    let textContent = icon.title;
    let titleContent = icon.alt;
    openModal(imageSrc, textContent, titleContent);
  });
});

function showStaticModal() {
  modalText.innerText = "Click any of the icons on the left!";
  modalTitle.innerText = ""; // Clear the title content
  modalText.style.textAlign = "center";
  modalImage.style.display = "none";
  document.getElementById("static-modal-content").style.display = "block";
}

// Call the showStaticModal function on page load
showStaticModal();



const introPar1 = document.getElementById("intro-par1");
const introPar2 = document.getElementById("intro-par2");

const typingSpeed = 22; // Speed of typing (in milliseconds)
const typingDelay = 1000; // Delay before starting the typing animation (in milliseconds)

const texts = [
  introPar1.textContent.trim(),
  introPar2.textContent.trim()
];

function typeText(element, text, index) {
  if (index < text.length) {
    element.textContent += text.charAt(index);
    setTimeout(() => {
      typeText(element, text, index + 1);
    }, typingSpeed);
  }
}

function startTypingAnimation() {
  texts.forEach((text, index) => {
    setTimeout(() => {
      typeText(index === 0 ? introPar1 : introPar2, text, 0);
    }, typingDelay + index * typingSpeed * text.length);
  });
}

// Show the paragraphs before starting the typing animation
introPar1.classList.remove("hidden");
introPar2.classList.remove("hidden");

// Start the typing animation after the delay
setTimeout(startTypingAnimation, typingDelay);


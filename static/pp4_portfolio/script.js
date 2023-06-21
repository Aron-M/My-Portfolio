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

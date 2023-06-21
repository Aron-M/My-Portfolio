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
  modalDiv.classList.add("fade-in"); // Add the fade-in class again
  modalImage.src = imageSrc;
  modalImage.classList.remove("fade-in"); // Remove the fade-in class
  void modalImage.offsetWidth; // Trigger reflow to restart the animation
  modalImage.classList.add("fade-in"); // Add the fade-in class again
  modalText.innerText = textContent;
  modalText.classList.remove("fade-in"); // Remove the fade-in class
  void modalText.offsetWidth; // Trigger reflow to restart the animation
  modalText.classList.add("fade-in"); // Add the fade-in class again
  modalTitle.innerText = titleContent;
  modalTitle.classList.remove("fade-in"); // Remove the fade-in class
  void modalTitle.offsetWidth; // Trigger reflow to restart the animation
  modalTitle.classList.add("fade-in"); // Add the fade-in class again
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
  modalText.innerText = "Click on the icons for more info!";
  modalTitle.innerText = ""; // Clear the title content
  modalText.style.textAlign = "center";
  modalImage.style.display = "none";
  document.getElementById("static-modal-content").style.display = "block";
}

// Call the showStaticModal function on page load
showStaticModal();

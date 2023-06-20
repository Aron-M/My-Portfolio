// Get the modal element
let modalDiv = document.getElementById("modal-div");

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
}

// Function to close the modal
function closeModal() {
  modalDiv.style.display = "none";
}

let icons = document.querySelectorAll(".modal-image");
icons.forEach(function (icon) {
  icon.addEventListener("click", function () {
    let imageSrc = icon.src;
    let textContent = icon.title;
    let titleContent = icon.alt;
    openModal(imageSrc, textContent, titleContent);
  });
});

let closeButton = document.querySelector(".modal-close-button");
closeButton.addEventListener("click", closeModal);

// Close the modal when clicking outside of it
window.addEventListener("click", function (event) {
  if (event.target === modalDiv) {
    closeModal();
  }
});

// Call the closeModal function on page load
closeModal();

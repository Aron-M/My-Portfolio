
    // Get the modal element
    var modal = document.getElementById("modal-box");

    // Get the image and text elements inside the modal
    var modalImage = document.getElementById("modal-image");
    var modalText = document.getElementById("modal-text");
    var modalTitle = document.querySelector("#modal-box h2");

    // Function to open the modal and display the content with fade-in effect
    function openModal(imageSrc, textContent, titleContent) {
  modal.style.display = "block";
  modal.classList.add("fade-in");
  modalImage.src = imageSrc;
  modalText.innerText = textContent;
  modalTitle.innerText = titleContent;

setTimeout(function () {
    modal.classList.remove("fade-in");
  }, 1000); // Adjust the delay duration as needed
}

// Function to close the modal
function closeModal() {
  modal.style.display = "none";
  modal.classList.remove("fade-in");
}

var icons = document.querySelectorAll(".modal-image");
icons.forEach(function (icon) {
  icon.addEventListener("click", function () {
    var imageSrc = icon.src;
    var textContent = "This text needs to display unique information about each individual skill displayed within this modal"; // Replace with your desired text content
    var titleContent = icon.alt;
    openModal(imageSrc, textContent, titleContent);
  });
}); 


var closeButton = document.querySelector(".modal-close-button");
closeButton.addEventListener("click", closeModal);

// Close the modal when clicking outside of it
window.addEventListener("click", function (event) {
  if (event.target === modal) {
    closeModal();
  }
});
function showErrorMessage(errorMessage) {
    const errorContainer = document.getElementById("error-box");
    errorContainer.innerHTML = "";
    const errorDiv = document.createElement("div");
    errorDiv.innerHTML = errorMessage;
    errorDiv.id = "error-msg";
    errorContainer.appendChild(errorDiv);
}
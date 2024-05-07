const handleUploadAdapter = (previewBox, noFileMessageElement) => {
    return function handleUpload() {
      if (this.files && this.files[0]) {
        const objectUrl = URL.createObjectURL(this.files[0]);
  
        const imgElement = document.createElement("img");
        imgElement.src = objectUrl;
        imgElement.style.maxWidth = "100%";
        imgElement.style.maxHeight = "100%";
  
        previewBox.innerHTML = "";
        previewBox.appendChild(imgElement);
      } else {
        previewBox.innerHTML = "";
        previewBox.appendChild(noFileMessageElement);
      }
    };
  };
  
  window.onload = function () {
    const components = document.querySelectorAll(".image-upload");
    [...components].forEach((component) => {
      const input = component.querySelector("input");
      const previewBox = component.querySelector(".image-preview");
      const noFileMessageElement = component.querySelector(".no-file-message");
  
      input.addEventListener(
        "change",
        handleUploadAdapter(previewBox, noFileMessageElement)
      );
    });
  };
  
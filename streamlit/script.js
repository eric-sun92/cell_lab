// script.js
document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("#my_form");
    const geneInput = document.querySelector("#gene_name");
    geneInput.addEventListener("keyup", function (event) {
      if (event.key === "Enter") {
        event.preventDefault();
        form.submit();
      }
    });
  });
  
const SCRIPT_URL = "https://script.google.com/macros/s/AKfycbw_JA84a_GnEr5JwRac1H4FaMqb3Qm8Dcc4DsbDk5VC2dkAuZP3KeIrKt_Z7iS3arDF/exec"; 

document.addEventListener("DOMContentLoaded", function() {
  const enquiryForm = document.getElementById("enquiryForm");
  const submitBtn = document.getElementById("submitBtn");

  if (enquiryForm) {
    enquiryForm.addEventListener("submit", function(e) {
      e.preventDefault();

      if (submitBtn) {
        submitBtn.innerText = "Submitting...";
        submitBtn.disabled = true;
      }

      // Meta Pixel Lead event
      if (typeof fbq === 'function') {
        fbq('track', 'Lead');
      }

      const formData = new FormData(enquiryForm);

      fetch(SCRIPT_URL, {
        method: "POST",
        body: formData
      })
      .then(response => {
        redirectToThankYou();
      })
      .catch(error => {
        console.error("Error submitting form:", error);
        redirectToThankYou();
      });
    });
  }
});

function redirectToThankYou() {
  setTimeout(() => {
    window.location.href = "thank-you.html";
  }, 200);
}
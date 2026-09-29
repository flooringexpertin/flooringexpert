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
    const hostname = window.location.hostname;
    
    // 1. Agar Custom Domain (flooringexpert.in) par hai
    if (hostname.includes("flooringexpert.in")) {
      window.location.href = "/thank-you.html";
    } 
    // 2. Agar GitHub Pages (username.github.io/flooringexpert) par hai
    else if (hostname.includes("github.io")) {
      window.location.href = "/flooringexpert/thank-you.html";
    } 
    // 3. Local Machine ya normal relative structure ke liye
    else {
      const pathSegments = window.location.pathname.split('/').filter(Boolean);
      // Agar kisi subfolder ke andar hain toh ../ lagakar root par bhejega
      const depth = pathSegments.length > 1 ? pathSegments.length - 1 : 0;
      const prefix = depth > 0 ? "../".repeat(depth) : "./";
      window.location.href = prefix + "thank-you.html";
    }
  }, 200);
}
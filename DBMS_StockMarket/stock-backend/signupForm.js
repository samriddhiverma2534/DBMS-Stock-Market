signupForm.addEventListener("submit", async function (e) {
  e.preventDefault();

  const name = document.getElementById("signupName").value;
  const phone = document.getElementById("signupPhone").value;
  const email = document.getElementById("signupEmail").value;
  const password = document.getElementById("signupPassword").value;
  const confirmPassword = document.getElementById("signupConfirmPassword").value;
  const enteredCaptcha = document.getElementById("enteredCaptcha").value;
  const actualCaptcha = captchaDisplay.textContent;

  if (password !== confirmPassword) {
    alert("Passwords do not match.");
    return;
  }

  if (enteredCaptcha !== actualCaptcha) {
    alert("Incorrect CAPTCHA.");
    generateCaptcha();
    return;
  }

  const response = await fetch("http://127.0.0.1:5000/api/signup", {
    method: "POST",
    credentials: "include",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ name, phone, email, password }),
  });

  const result = await response.json();
  if (response.ok) {
    alert("Signup successful!");
    localStorage.setItem("username", name);
    window.location.href = "dashboard.html";
  } else {
    alert(result.error || "Signup failed");
  }
});

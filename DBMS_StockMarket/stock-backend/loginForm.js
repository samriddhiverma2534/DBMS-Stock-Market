loginForm.addEventListener("submit", async function (e) {
  e.preventDefault();
  const email = document.getElementById("loginEmail").value;
  const password = document.getElementById("loginPassword").value;

  const response = await fetch("http://127.0.0.1:5000/api/login", {
    method: "POST",
    credentials: "include", // to support sessions
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ email, password }),
  });

  const result = await response.json();
  if (response.ok) {
    alert("Login successful!");
    localStorage.setItem("username", result.name); // save user's name
    window.location.href = "dashboard.html";
  } else {
    alert(result.error || "Login failed");
  }
});
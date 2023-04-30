// Registration form submission event
document.getElementById("registrationForm").addEventListener("submit", function(event) {
    event.preventDefault();
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    // Here you can perform AJAX requests or any other necessary actions for user registration
    console.log("Username: " + username);
    console.log("Password: " + password);
  });
  
  // Login form submission event
  document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault();
    var loginUsername = document.getElementById("loginUsername").value;
    var loginPassword = document.getElementById("loginPassword").value;
    // Here you can perform AJAX requests or any other necessary actions for user login
    console.log("Login Username: " + loginUsername);
    console.log("Login Password: " + loginPassword);
  });
  
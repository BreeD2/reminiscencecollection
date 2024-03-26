// formHandler.js
document.getElementById('myForm').addEventListener('submit', function(event) {
  event.preventDefault(); // Stop the form from submitting normally

  // Assume signInFunction is a function that handles signing in users
  signInFunction().then(() => {
    // Redirect to confirmation page upon successful sign-in
    window.location.href = 'confirm/index.html';
  }).catch((error) => {
    // Handle sign-in errors here, possibly redirect to a sign-in page
    console.error(error);
    window.location.href = 'signin/index.html';
  });
});

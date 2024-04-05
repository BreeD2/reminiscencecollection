<?php
// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Collect and sanitize input data
    $firstName = strip_tags(trim($_POST["firstName"]));
    $lastName = strip_tags(trim($_POST["lastName"]));
    $email = filter_var(trim($_POST["email"]), FILTER_SANITIZE_EMAIL);
    $message = strip_tags(trim($_POST["message"]));

    // Specify the recipient email and subject
    $toEmail = "brekd816@gmail.com";
    $emailSubject = "New Contact Form Submission";

    // Prepare the email header
    $emailHeader = "From: $firstName $lastName <$email>\r\n";
    $emailHeader .= "Reply-To: $email\r\n";
    $emailHeader .= "Content-Type: text/plain; charset=utf-8\r\n";

    // Prepare the email body
    $emailBody = "You have received a new message from your website contact form.\n\n";
    $emailBody .= "Here are the details:\n";
    $emailBody .= "First Name: $firstName\n";
    $emailBody .= "Last Name: $lastName\n";
    $emailBody .= "Email: $email\n";
    $emailBody .= "Message:\n$message\n";

    // Send the email
    if (mail($toEmail, $emailSubject, $emailBody, $emailHeader)) {
        // Redirect to a thank-you page or display a success message
        echo "<p>Thank you for your message, $firstName. We will get back to you soon.</p>";
    } else {
        // Email failed to send, handle the error
        echo "<p>Oops! Something went wrong and we couldn't send your message.</p>";
    }
} else {
    // Not a POST request, display an error or redirect
    echo "<p>Something went wrong with your submission.</p>";
}
?>

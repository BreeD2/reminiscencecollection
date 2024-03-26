const express = require('express');
const app = express();
const port = 3000;

// Middleware to parse the incoming requests with JSON payloads
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.post('/submit-form', (req, res) => {
    console.log(req.body); // Log the submitted form data
    res.json({ message: 'Form data received!' }); // Respond back to the client
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});

function greetUser(name, callback) {
  console.log("Hi " + name);
  callback(); // run after greeting
}

function sayBye() {
  console.log("Goodbye!");
}

greetUser("Nick", sayBye);

console.log("Start");

setTimeout(() => {
  console.log("Inside setTimeout (Event Loop example)");
}, 0);

console.log("End");

// ----- 3. Express App -----
const express = require("express");
const app = express();
const PORT = 3000;


// Root route
app.get("/", (req, res) => {
  res.send("Hello from Express Server!");
});

// Route with params
app.get("/user/:name", (req, res) => {
  res.send(`Welcome, ${req.params.name}!`);
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
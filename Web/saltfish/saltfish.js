for (let i = 0; i <= 127; i++) {
  fetch(`http://127.0.0.1:124?pass=${String.fromCharCode(i)}`, {
    method: "GET",
    headers: {
      "User-Agent": `${String.fromCharCode(i)}`,
    }
  })
  .then(response => response.text())
  .then(data => console.log(`Step ${i}: ${data}`))
  .catch(error => console.log("Invalid character") )
} 
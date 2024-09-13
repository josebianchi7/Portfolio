'use strict';

// Route code to enable express:
const express = require('express');
const app = express();
const PORT = 3000;

app.use(express.urlencoded({extended: true}));

app.use(express.static('public'));

// Default HTML wraps for any new webpages:
let htmlTop = `
<!DOCTYPE html>
<html>
    <head>
        <meta>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>Jose Bianchi</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" type="text/css" media="screen" href="main.css">
        <script src="main.js"></script>
        <link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png">
        <link rel="icon" type="image/png" sizes="512x512" href="android-chrome-512x512.png">
        <link rel="icon" type="image/png" sizes="192x192" href="android-chrome-192x192.png"> 
        <link rel="icon" type="image/png" sizes="32x32" href="favicon-32x32.png">
        <link rel="icon" type="image/png" sizes="16x16" href="favicon-16x16.png">
        <link rel="manifest" href="site.webmanifest">
    </head>
    
    <body>
        <header>
            <img src="android-chrome-192x192.png" alt="Jose Bianchi"/>  <h1>Jose Bianchi</h1>    
        </header>
    <nav>
        <a href="index.html">Home</a>
        <a href="gallery.html">Gallery</a>
        <a href="contact.html">Contact</a>
        <a href="order.html">Order</a>
    </nav>
    <main>
`;

let htmlBottom = `
</main>
<footer>
    <p>
        <!--Copyright statement-->
          &copy; 2024 Jose Bianchi    
    </p>
</footer>
</body>
</html>
`;


// Method to respond to user Contact form requests.
// Variables sourced from user entries that can be returned in string literals.
app.post("/review", (req, res) => {
  const person = req.body.usersName;
  const contactEmail = req.body.usersEmail;
  const purpose = req.body.purpose;
  const selectPage = req.body.internalPages;
  const radioResponse1 = req.body.muchInfo;
  const checkbox1 = req.body.futurePlan;

  res.send(`
    ${htmlTop}
    <section>
      <h2>Contact Response</h2>
      <article>
        <h3>Hi, <strong>${person}</strong>.</h3>
        <p>
          Thank you for filling out the form on my webapage. 
          I am excited to begin making improvements based on your feedback.
          I may reach out to you at the provided email, <strong>${contactEmail}</strong>. 
          I understand your purpose was the following:
        </p>
        <p>
          <strong>"${purpose}"</strong> 
        </p>
        <p>
          Some questions I may ask in my email response include why did you spend the most time on the <strong>${selectPage}</strong> page.

          Can you elaborate about why you answered <strong>${radioResponse1}</strong>
          in regards to enjoying the content of the webpages.

          Lastly, thank you for stating you would like to see more of <strong>${checkbox1}</strong>. I will get
          right on that.

          I hope you enjoyed dropping by and I look forward to following up with you in the future.
        </p>
        <p>
          All the best,
        </p>
        <p>
          Jose Bianchi
        </p>
      </article>  
    </section>  
    ${htmlBottom}

  `);
});


// Import variable 'products' object from product.js file via .products
const productList = require('./products.js').products;

// Function to accept web form input for product. 
// If choice is valid product corresponding to product in products object,
// return product with accessible properties for chosen element.
function compareProduct(choice) {
  for (const productElement of productList) {
      if (productElement.product === choice) {
          return productElement;
      }
  }
}

  // function to return total price variable from quantity requested and cost per item.
  // Amount is converted to US Currency
  function computeCost(cost, amount) {
    let costNum = cost * amount
    return costNum.toLocaleString('en-US', {     
        style: 'currency',     
        currency: 'USD',     
        minimumFractionDigits: 2 
      }
    )
  }

// Method to respond to Order form requests.
app.post("/orderReview", (req, res) => {
  const name = req.body.userName;
  const email = req.body.userEmail;
  const address = req.body.userAddress;
  const deliveryInstruct = req.body.deliveryMessage
  const productChoice = compareProduct(req.body.product)
  let quantity = req.body.productQuantity
  let totalCost = computeCost(productChoice.price, quantity)
  const price = productChoice.price.toLocaleString('en-US', {     
    style: 'currency',     
    currency: 'USD',     
    minimumFractionDigits: 2 
    }
  )


  res.send(`
    ${htmlTop}
    <section>
      <h2>Order Response</h2>
      <article>
        <p>
          Thank you for your order request, <strong>${name}</strong>. We will send email updates to <strong>${email}</strong>.
          Shipping address is recorded as <strong>${address}</strong>. Delivery note if provided is as follows:
        </p>
        <p>
          <strong>${deliveryInstruct}</strong>
        </p>
        <p>  
          Your order includes <strong>${quantity}</strong> of the <strong>${productChoice.product}</strong>, 
          from <strong>${productChoice.company}</strong>, priced at <strong>${price}</strong> per item, 
          totaling in <strong>${totalCost}</strong>. 
          If any of the above is not correct or needs to be updated at any time, please email Jose Bianchi 
          at bianchijo926@gmail.com with the necessary changes. Have a great day and thank you for your order. 
        </p>
      </article>  
    </section>  
    ${htmlBottom}

  `);
});

// Allows enrties on designated port to be recorded and prints statement to console if working.
app.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}...`);
});

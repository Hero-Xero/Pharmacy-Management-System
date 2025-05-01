// Quantity control functions
function decreaseQuantity() {
  let qty = document.getElementById('quantity');
  let value = parseInt(qty.value);
  if (value > 1) {
      qty.value = value - 1;
  }
}

function increaseQuantity() {
  let qty = document.getElementById('quantity');
  let value = parseInt(qty.value);
  if (value < 10) {
      qty.value = value + 1;
  } else {
      showAlert('Maximum quantity reached (10 items)');
  }
}

// Update stock status
function updateStockStatus(isInStock) {
  const stockElement = document.querySelector('.stock-status');
  const stockText = document.getElementById('stock-text');
  
  if (isInStock) {
      stockElement.classList.add('in-stock');
      stockElement.classList.remove('out-of-stock');
      stockText.textContent = 'In stock';
      stockElement.innerHTML = '<i class="fas fa-check-circle"></i> <span id="stock-text">In stock</span>';
  } else {
      stockElement.classList.add('out-of-stock');
      stockElement.classList.remove('in-stock');
      stockText.textContent = 'Out of stock';
      stockElement.innerHTML = '<i class="fas fa-times-circle"></i> <span id="stock-text">Out of stock</span>';
      
      document.querySelector('.cart-btn').disabled = true;
      document.querySelector('.buy-btn').disabled = true;
  }
}

// Cart and buy functions
function addToCart() {
  const quantity = parseInt(document.getElementById('quantity').value);
  const product = {
      id: window.location.pathname.split('/').pop().replace('.html', ''),
      name: document.querySelector('.product-title').textContent,
      price: parseFloat(document.querySelector('.product-price').textContent.replace('EGP ', '')),
      image: document.querySelector('.product-image').src,
      quantity: quantity
  };
  
  // Add to cart using the cart.js function
  window.addToCart(product);
}

function buyNow() {
  const quantity = document.getElementById('quantity').value;
  showAlert(`Proceeding to checkout with ${quantity} item(s)`);
}

// Add related product to cart
function addRelatedToCart(button) {
  const productItem = button.closest('.product-item');
  const product = {
      id: Date.now().toString(), // Generate unique ID
      name: productItem.querySelector('.product-name').textContent,
      price: parseFloat(productItem.querySelector('.product-price').textContent.replace('EGP ', '')),
      image: productItem.querySelector('.product-img').src,
      quantity: 1 // Default quantity for related products
  };
  
  // Add to cart using the cart.js function
  window.addToCart(product);
}

// Show alert message
function showAlert(message) {
  alert(message);
}

// Initialize product page
document.addEventListener('DOMContentLoaded', function() {
  // Set initial stock status
  updateStockStatus(true);

  // Add click event listeners to related product images
  document.querySelectorAll('.product-img').forEach(img => {
    img.addEventListener('click', function() {
      const productItem = this.closest('.product-item');
      const productName = productItem.querySelector('.product-name').textContent;
      const productPrice = productItem.querySelector('.product-price').textContent;
      const productImage = this.src;
      
      // Create a temporary product object
      const product = {
        id: Date.now().toString(),
        name: productName,
        price: parseFloat(productPrice.replace('EGP ', '')),
        image: productImage,
        quantity: 1
      };
      
      // Add to cart
      window.addToCart(product);
    });
  });
});

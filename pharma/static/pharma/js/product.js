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
  const quantity = document.getElementById('quantity').value;
  showAlert(`Added ${quantity} item(s) to your cart`);
}

function buyNow() {
  const quantity = document.getElementById('quantity').value;
  showAlert(`Proceeding to checkout with ${quantity} item(s)`);
}

// Show alert message
function showAlert(message) {
  alert(message);
}

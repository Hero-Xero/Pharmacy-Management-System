// Cart functionality
let cart = JSON.parse(localStorage.getItem('cart')) || [];

// Initialize cart page
document.addEventListener('DOMContentLoaded', function() {
    displayCart();
    updateCartSummary();
});

// Display cart items
function displayCart() {
    const cartItemsContainer = document.getElementById('cart-items');
    const emptyCartMessage = document.getElementById('empty-cart-message');
    
    if (cart.length === 0) {
        cartItemsContainer.style.display = 'none';
        emptyCartMessage.style.display = 'block';
        return;
    }

    cartItemsContainer.style.display = 'block';
    emptyCartMessage.style.display = 'none';

    cartItemsContainer.innerHTML = cart.map((item, index) => `
        <div class="cart-item" data-index="${index}">
            <img src="${item.image}" alt="${item.name}" class="cart-item-image">
            <div class="cart-item-details">
                <h3 class="cart-item-title">${item.name}</h3>
                <p class="cart-item-price">EGP ${item.price.toFixed(2)}</p>
                <div class="cart-item-quantity">
                    <label>Quantity:</label>
                    <div class="quantity-control">
                        <button onclick="updateQuantity(${index}, -1)"><i class="fas fa-minus"></i></button>
                        <input type="text" value="${item.quantity}" readonly>
                        <button onclick="updateQuantity(${index}, 1)"><i class="fas fa-plus"></i></button>
                    </div>
                </div>
            </div>
            <div class="remove-item" onclick="removeItem(${index})">
                <i class="fas fa-trash"></i>
            </div>
        </div>
    `).join('');
}

// Update item quantity
function updateQuantity(index, change) {
    const newQuantity = cart[index].quantity + change;
    
    if (newQuantity < 1) {
        removeItem(index);
    } else if (newQuantity <= 10) {
        cart[index].quantity = newQuantity;
        localStorage.setItem('cart', JSON.stringify(cart));
        displayCart();
        updateCartSummary();
    } else {
        showAlert('Maximum quantity reached (10 items)');
    }
}

// Remove item from cart
function removeItem(index) {
    cart.splice(index, 1);
    localStorage.setItem('cart', JSON.stringify(cart));
    displayCart();
    updateCartSummary();
}

// Update cart summary
function updateCartSummary() {
    const subtotal = cart.reduce((sum, item) => sum + (item.price * item.quantity), 0);
    const shipping = subtotal > 500 ? 0 : 50;
    const total = subtotal + shipping;

    document.getElementById('subtotal').textContent = `EGP ${subtotal.toFixed(2)}`;
    document.getElementById('shipping').textContent = `EGP ${shipping.toFixed(2)}`;
    document.getElementById('total').textContent = `EGP ${total.toFixed(2)}`;
}

// Proceed to checkout
function proceedToCheckout() {
    if (cart.length === 0) {
        showAlert('Your cart is empty');
        return;
    }
    // Add your checkout logic here
    showAlert('Proceeding to checkout...');
}

// Show alert message
function showAlert(message) {
    alert(message);
}

// Add to cart function (to be called from product and category pages)
window.addToCart = function(product) {
    const existingItem = cart.find(item => item.id === product.id);
    
    if (existingItem) {
        const newQuantity = existingItem.quantity + product.quantity;
        if (newQuantity <= 10) {
            existingItem.quantity = newQuantity;
        } else {
            showAlert('Maximum quantity reached (10 items)');
            return;
        }
    } else {
        cart.push({
            id: product.id,
            name: product.name,
            price: product.price,
            image: product.image,
            quantity: product.quantity || 1
        });
    }
    
    localStorage.setItem('cart', JSON.stringify(cart));
    showAlert('Item added to cart');
}; 
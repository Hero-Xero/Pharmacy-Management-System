
document.addEventListener("DOMContentLoaded", function () {
    let minPriceInput = document.getElementById("minPriceRange");
    let maxPriceInput = document.getElementById("maxPriceRange");
    let priceValue = document.getElementById("priceValue");

    function updatePrice() {
        let minPrice = parseInt(minPriceInput.value);
        let maxPrice = parseInt(maxPriceInput.value);

        // Ensure min doesn't exceed max
        if (minPrice > maxPrice) {
            [minPrice, maxPrice] = [maxPrice, minPrice]; // Swap values
        }

        priceValue.innerText = `${minPrice}-${maxPrice}`;

        // Product Filtering Logic
        let products = document.querySelectorAll(".card");
        products.forEach(product => {
            let productPrice = parseFloat(
                product.querySelector(".price").innerText.replace(/EGP|,/g, "").trim()
            );

            product.style.display = (productPrice >= minPrice && productPrice <= maxPrice) ? "block" : "none";
        });
    }

    // Event Listeners
    minPriceInput.addEventListener("input", updatePrice);
    maxPriceInput.addEventListener("input", updatePrice);
});


document.addEventListener("DOMContentLoaded", function () {
    let sortBy = document.getElementById("sort-by");

    function sortProducts() {
        let productsContainer = document.querySelector(".products-container"); // Make sure this is the correct container
        let products = Array.from(document.querySelectorAll(".card"));
        let sortValue = sortBy.value;

        products.sort((a, b) => {
            let titleA = a.querySelector(".card-title").innerText.trim().toLowerCase();
            let titleB = b.querySelector(".card-title").innerText.trim().toLowerCase();
            let priceA = parseFloat(a.querySelector(".price").innerText.replace(/EGP|,/g, "").trim());
            let priceB = parseFloat(b.querySelector(".price").innerText.replace(/EGP|,/g, "").trim());

            switch (sortValue) {
                case "Alphabetically, A-Z":
                    return titleA.localeCompare(titleB);
                case "Alphabetically, Z-A":
                    return titleB.localeCompare(titleA);
                case "Price, low to high":
                    return priceA - priceB;
                case "Price, high to low":
                    return priceB - priceA;
                default:
                    return 0; // Default for "Featured" and "Best selling"
            }
        });

        // Clear the container and append sorted products
        productsContainer.innerHTML = "";
        products.forEach(product => productsContainer.appendChild(product));
    }

    // Event Listener for Sorting
    sortBy.addEventListener("change", sortProducts);
});



    
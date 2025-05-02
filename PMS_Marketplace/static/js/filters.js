<script>
document.addEventListener("DOMContentLoaded", function () {
    const minPriceInput = document.getElementById("minPriceRange");
    const maxPriceInput = document.getElementById("maxPriceRange");
    const priceValue = document.getElementById("priceValue");

    function updatePrice() {
        let minPrice = parseInt(minPriceInput.value);
        let maxPrice = parseInt(maxPriceInput.value);

        // Ensure min doesn't exceed max
        if (minPrice > maxPrice) {
            [minPrice, maxPrice] = [maxPrice, minPrice]; // Swap values
        }

        priceValue.innerText = `${minPrice} - ${maxPrice}`;

        // Product Filtering Logic
        const products = document.querySelectorAll(".card");
        products.forEach(product => {
            const productPrice = parseFloat(
                product.querySelector(".price").innerText.replace(/EGP|,/g, "").trim()
            );
            product.style.display = (productPrice >= minPrice && productPrice <= maxPrice) ? "block" : "none";
        });
    }

    minPriceInput.addEventListener("input", updatePrice);
    maxPriceInput.addEventListener("input", updatePrice);
});

document.addEventListener("DOMContentLoaded", function () {
    const sortBy = document.getElementById("sort-by");

    function sortProducts() {
        const productsContainer = document.querySelector(".products-container");
        const products = Array.from(document.querySelectorAll(".card"));
        const sortValue = sortBy.value;

        products.sort((a, b) => {
            const titleA = a.querySelector(".card-title").innerText.trim().toLowerCase();
            const titleB = b.querySelector(".card-title").innerText.trim().toLowerCase();
            const priceA = parseFloat(a.querySelector(".price").innerText.replace(/EGP|,/g, "").trim());
            const priceB = parseFloat(b.querySelector(".price").innerText.replace(/EGP|,/g, "").trim());

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
                    return 0; // No sort
            }
        });

        // Clear and re-append sorted products
        productsContainer.innerHTML = "";
        products.forEach(product => productsContainer.appendChild(product));
    }

    sortBy.addEventListener("change", sortProducts);
});
</script>

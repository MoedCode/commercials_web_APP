function openPopup(Idx) {
    const product = productsList[Idx - 1]; // Adjust for 0-based index in array
    console.log(product.brand, "\n", Idx);

    // Update the popup content with product details
    document.getElementById('myPopup').innerHTML = `
        <div class="product-card-0">
        <button id="close0" onclick="closePopup()"> X</button>
        <h3>${product.name}</h3>
        <img src="${product.image}" alt="Product Image" class="popup-image">
        <p><strong>ID:</strong> ${product.id}</p>
        <p><strong>Barcode:</strong> ${product.barcode}</p>
        <p><strong>Category:</strong> ${product.category}</p>
        <p><strong>Description:</strong> ${product.description}</p>
        <p><strong>Price:</strong> ${product.price}</p>
        <p><strong>Discount:</strong> ${product.discount}</p>
        <p><strong>Stock Quantity:</strong> ${product.stock_quantity}</p>
        <p><strong>Brand:</strong> ${product.brand}</p>
        <p><strong>Rating:</strong> ${product.rating}</p>
        <p><strong>In Stock:</strong> ${product.in_stock}</p>
    </div>

    `;

    // Display the popup
    document.getElementById('myPopup').style.display = 'block';
}

function closePopup() {
    document.getElementById('myPopup').style.display = 'none';
}

window.document.body.style.backgroundColor="#212121"
window.document.body.style.color="#fdfddfdf"
// Close the popup if the user clicks outside of it
window.onclick = function(event) {
    var popup = document.getElementById('myPopup');
    if (event.target === popup) {
        popup.style.display = 'none';
    }
}
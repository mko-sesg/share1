// js/index.js

document.addEventListener('DOMContentLoaded', function() {
  // Code here runs when the DOM is fully loaded
  console.log('DOM is fully loaded');
  const textarea = document.getElementById('data');
  console.log('Textarea:', textarea);

  // Get data from the server and display it as plain text in the textarea.
  async function loadProducts() {
    try {
      const response = await fetch('/api/products');
      if (!response.ok) {
        throw new Error(`HTTP ${response.status}`);
      }

      const products = await response.json();
      if (!Array.isArray(products) || products.length === 0) {
        textarea.value = 'No products found.';
        return;
      }

      textarea.value = products
        .map((product) => `${product.product_name} - $${product.price}`)
        .join('\n');
    } catch (error) {
      console.error('Failed to load products:', error);
      textarea.value = 'Failed to load products from server.';
    }
  }

  loadProducts();
});

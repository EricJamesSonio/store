let total = 0;

function addToCart(itemName, price) {
  // Add item to list
  const cartList = document.getElementById("cart-list");
  const li = document.createElement("li");
  li.textContent = `${itemName} - ₱${price}`;
  cartList.appendChild(li);

  // Update total
  total += price;
  document.getElementById("total").textContent = total;
}

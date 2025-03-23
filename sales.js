document.getElementById('productForm').addEventListener('submit', function(event) {
    event.preventDefault(); // impede o envio padrão do formulário

    const productName = document.getElementById('productName').value;
    const productQuantity = document.getElementById('productQuantity').value;
    const productPrice = document.getElementById('productPrice').value;

    addProductToTable(productName, productQuantity, productPrice);

    // Limpar o formulário
    this.reset();
});

function addProductToTable(name, quantity, price) {
    const tableBody = document.querySelector('#productTable tbody');
    const row = document.createElement('tr');

    row.innerHTML = `
        <td>${name}</td>
        <td>${quantity}</td>
        <td>R$ ${parseFloat(price).toFixed(2)}</td>
        <td><button onclick="removeProduct(this)">Remover</button></td>
    `;

    tableBody.appendChild(row);
}

function removeProduct(button) {
    const row = button.parentElement.parentElement;
    row.remove();
}
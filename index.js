document.getElementById("product-form").addEventListener("submit", function(event){
    event.preventDefault();

    let productName = document.getElementById("product-name").value;
    let productQuantity = document.getElementById("product-quantity").value;
    let productPrice = document.getElementById("product-price").value;

    addProductToList(productName, productQuantity, productPrice);

    // Limpar os campos
    document.getElementById("product-form").reset();
});

function addProductToList(name, quantity, price) {
    let table = document.getElementById("product-list").getElementsByTagName('tbody')[0];
    
    let newRow = table.insertRow();

    let cellName = newRow.insertCell(0);
    let cellQuantity = newRow.insertCell(1);
    let cellPrice = newRow.insertCell(2);
    let cellActions = newRow.insertCell(3);

    cellName.textContent = name;
    cellQuantity.textContent = quantity;
    cellPrice.textContent = price;

    // Ação de deletar o produto
    let deleteButton = document.createElement("button");
    deleteButton.textContent = "Remover";
    deleteButton.onclick = function() {
        table.deleteRow(newRow.rowIndex - 1);
    };
    cellActions.appendChild(deleteButton);
}
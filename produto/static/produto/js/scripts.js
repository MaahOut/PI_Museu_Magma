function abrirModalVenda(nome) {
    document.getElementById('produtoNomeVenda').value = nome;
    var myModal = new bootstrap.Modal(document.getElementById('modalVenda'));
    myModal.show();
}

function registrarVenda() {
    const nome = document.getElementById('produtoNomeVenda').value;
    const quantidade = document.getElementById('quantidadeVenda').value;
    const nomeCliente = document.getElementById('nomeCliente').value;
    const cpfCliente = document.getElementById('cpfCliente').value;
    const cnpjCliente = document.getElementById('cnpjCliente').value;
    const registroVenda = document.getElementById('registroVenda').value;

    fetch(`/registrar-venda/${nome}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': '{{ csrf_token }}'
        },
        body: `quantidade=${quantidade}&nomeCliente=${nomeCliente}&cpfCliente=${cpfCliente}&cnpjCliente=${cnpjCliente}&registroVenda=${registroVenda}`
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            alert(data.message);
            location.reload();
        } else {
            alert(data.message);
        }
    });
}

function abrirModalEntrada(nome) {
    document.getElementById('produtoNomeEntrada').value = nome;
    var myModal = new bootstrap.Modal(document.getElementById('modalEntrada'));
    myModal.show();
}

function registrarEntrada() {
    const nome = document.getElementById('produtoNomeEntrada').value;
    const quantidade = document.getElementById('quantidadeEntrada').value;

    fetch(`/adicionar-estoque/${nome}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': '{{ csrf_token }}'
        },
        body: `quantidade=${quantidade}`
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            alert(data.message);
            location.reload();
        } else {
            alert(data.message);
        }
    });
}

function abrirModalAjuste(nome) {
    document.getElementById('produtoNomeAjuste').value = nome;
    var myModal = new bootstrap.Modal(document.getElementById('modalAjuste'));
    myModal.show();
}

function registrarAjuste() {
    const nome = document.getElementById('produtoNomeAjuste').value;
    const quantidade = document.getElementById('quantidadeAjuste').value;

    fetch(`/ajustar-estoque/${nome}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': '{{ csrf_token }}'
        },
        body: `quantidade=${quantidade}`
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            alert(data.message);
            location.reload();
        } else {
            alert(data.message);
        }
    });
}

function abrirModalAlterarPreco(nome) {
    document.getElementById('produtoNomePreco').value = nome;
    var myModal = new bootstrap.Modal(document.getElementById('modalAlterarPreco'));
    myModal.show();
}

function alterarPreco() {
    const nome = document.getElementById('produtoNomePreco').value;
    const novoPreco = document.getElementById('novoPreco').value;

    fetch(`/alterar-preco/${nome}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': '{{ csrf_token }}'
        },
        body: `novo_preco=${novoPreco}`
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            alert(data.message);
            location.reload();
        } else {
            alert(data.message);
        }
    });
}

// Funções do código original
function destacarCard(card) {
    card.classList.add('destaque');
    setTimeout(function() {
        card.classList.remove('destaque');
    }, 2000);
}

function abrirModal(imagemUrl) {
    var modalImg = document.getElementById("imagemModal");
    modalImg.src = imagemUrl;
    var myModal = new bootstrap.Modal(document.getElementById("modalImagem"));
    myModal.show();
}
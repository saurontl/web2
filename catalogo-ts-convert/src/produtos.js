"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Categoria = exports.produtos = void 0;
exports.adicionarProduto = adicionarProduto;
exports.listarProdutos = listarProdutos;
exports.calcularTotal = calcularTotal;
exports.filtrarPorCategoria = filtrarPorCategoria;
// Criando Enum para Categorias
var Categoria;
(function (Categoria) {
    Categoria["Eletronicos"] = "Eletr\u00F4nicos";
    Categoria["Vestuario"] = "Vestu\u00E1rio";
    Categoria["Alimentos"] = "Alimentos";
    Categoria["Outros"] = "Outros";
})(Categoria || (exports.Categoria = Categoria = {}));
// Tipando o array de produtos
var produtos = [];
exports.produtos = produtos;
//Agora a função recebe um objeto do tipo Produto
function adicionarProduto(produto) {
    produtos.push(produto);
}
//Aqui também recebe um array do tipo Produto
function listarProdutos() {
    return produtos;
}
function calcularTotal() {
    return produtos.reduce(function (acc, p) { return acc + p.preco * p.quantidade; }, 0);
}
//O filtro agora recebe uma categoria do tipo Categoria
function filtrarPorCategoria(categoria) {
    return produtos.filter(function (p) { return p.categoria === categoria; });
}

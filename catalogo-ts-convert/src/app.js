"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var produtos_js_1 = require("./produtos.js");
//Agora usando o Enum Categoria
(0, produtos_js_1.adicionarProduto)({ nome: 'Notebook', preco: 3000, quantidade: 2, categoria: produtos_js_1.Categoria.Eletronicos });
(0, produtos_js_1.adicionarProduto)({ nome: 'Camiseta', preco: 50, quantidade: 5, categoria: produtos_js_1.Categoria.Vestuario });
(0, produtos_js_1.adicionarProduto)({ nome: 'Fone de Ouvido', preco: 200, quantidade: 3, categoria: produtos_js_1.Categoria.Eletronicos });
console.log('Todos os produtos:');
console.log((0, produtos_js_1.listarProdutos)());
console.log('\nTotal em estoque:');
console.log((0, produtos_js_1.calcularTotal)());
//Aqui também usando o Enum Categoria
console.log('\nFiltrar por Eletrônicos:');
console.log((0, produtos_js_1.filtrarPorCategoria)(produtos_js_1.Categoria.Eletronicos));

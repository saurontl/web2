import {
  adicionarProduto,
  listarProdutos,
  calcularTotal,
  filtrarPorCategoria,
  Categoria
} from './produtos.js'

//Agora usando o Enum Categoria
adicionarProduto({ nome: 'Notebook', preco: 3000, quantidade: 2, categoria: Categoria.Eletronicos })
adicionarProduto({ nome: 'Camiseta', preco: 50, quantidade: 5, categoria: Categoria.Vestuario })
adicionarProduto({ nome: 'Fone de Ouvido', preco: 200, quantidade: 3, categoria: Categoria.Eletronicos })

console.log('Todos os produtos:')
console.log(listarProdutos())

console.log('\nTotal em estoque:')
console.log(calcularTotal())

//Aqui também usando o Enum Categoria
console.log('\nFiltrar por Eletrônicos:')
console.log(filtrarPorCategoria(Categoria.Eletronicos))

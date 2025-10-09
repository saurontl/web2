// Criando a interface de Produto
interface Produto {
  nome: string
  preco: number
  quantidade: number
  categoria: Categoria
}

// Criando Enum para Categorias
enum Categoria {
  Eletronicos = 'Eletrônicos',
  Vestuario = 'Vestuário',
  Alimentos = 'Alimentos',
  Outros = 'Outros'
}

// Tipando o array de produtos
const produtos: Produto[] = []

//Agora a função recebe um objeto do tipo Produto
function adicionarProduto(produto: Produto) {
  produtos.push(produto)
}

//Aqui também recebe um array do tipo Produto
function listarProdutos(): Produto[] {
  return produtos
}

function calcularTotal(): number {
  return produtos.reduce((acc: number, p: Produto) => acc + p.preco * p.quantidade, 0)
}

//O filtro agora recebe uma categoria do tipo Categoria
function filtrarPorCategoria(categoria: Categoria): Produto[] {
  return produtos.filter((p: Produto) => p.categoria === categoria)
}

export {
  produtos,
  Categoria,
  adicionarProduto,
  listarProdutos,
  calcularTotal,
  filtrarPorCategoria
}
Implementação de um Simulador de Caches

Implementação do Simulador

Deverá ser implementado um simulador funcional de caches com múltiplos níveis de cache sendo que todas
as caches deverão ser unificadas (não haverá separação entre caches de dados e instruções), em uma
linguagem de programação qualquer e o simulador deverá ser parametrizável (configurações da cache). A
cache é endereçada a bytes e endereço possui 32 bits. O simulador deverá suportar no mínimo 3 níveis de
cache.

A configuração de cache deverá ser repassada por linha de comando é formatada com os seguintes
parâmetros (o arquivo de entrada poderá ter extensão), como por exemplo:
cache_simulator <nsets_L1>: <bsize_L1>: <assoc_L1> arquivo_de_entrada
cache_simulator <nsets_L1>: <bsize_L1>: <assoc_L1> <nsets_L2>:<bsize_L2>:<assoc_L2> arquivo_de_entrada

Onde cada um destes campos possui o seguinte significado:
• <nsets> número de conjuntos na cache;
• <bsize> tamanho do bloco em bytes;
• <assoc> associatividade;

A política de substituição será sempre randômica. A configuração default será de uma cache com
mapeamento direto com tamanho de bloco de 8 bytes e com 2048 conjuntos. O tamanho da cache é dado
pelo produto do número de conjuntos na cache (<nsets>), tamanho do bloco em bytes (<bsize>) e
associatividade (<assoc>).

A saída do simulador será um relatório de estatísticas com o número total de acessos, número total hits (e
hit ratio) e misses (e miss ratio) por nível de cache (os misses deverão ser classificados em compulsórios,
capacidade + conflito).

O arquivo de entrada indica a leitura de um arquivo que será utilizado como entrada para o simulador
(armazenado em formato binário) que conterá os endereços requisitados a cache (endereços em 32 bits).

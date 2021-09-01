from venvinstaladorMaster import  connection

class Search():

    def select(self):
        con = connection.BdConnections()

        conn = con.firebird_connection(host='192.168.56.1', database='C:\SistemasEquiplano\\492\EQUIPLANO.GDB', user='sysdba', password='masterkey', port=3050)

        cur = conn.cursor()
        cur.execute(
        """ select 
          origem, total, total/5.0 as paginas 
        from 
        (
          select 'unidade de medida' as origem, count(*) as total from unidademedida
          union all
          select 'grupo', count(*) from grupo  
          union all
          select 'subgrupo', count(*) from subgrupo  
          union all
          select 'classe', count(*) from classe
          union all
          select 'objetos da despesa', count(*) from scp55_tcepr_tpcategtpobjeto
          union all
          select 'derivações', count(*) from sal_derivacaoproduto
          union all
          select 'componentes', count(*) from sal_derivacaocomponenteproduto
          union all
          select 'tipo movimentação', count(*) from sal_tipomovimento
          union all
          select 'ocorrência de produtos', count(*) from scp55_tipoocorrenciaproduto
          union all
          select 'produtos', count(*) from produto
          union all
          select 'pessoas', count(*) from pessoa
          union all
          select 'fornecedores', count(*) from fornecedor
          union all
          select 'centros de custo', count(*) from scp55_localexercicio where codentidade=492
          union all
          select 'depósitos', count(*) from sal_deposito where codentidade=492
          union all
          select 'entradas', count(*) from sal_movimento m join sal_tipomovimento tm on (m.idtipomovimento=tm.idtipomovimento) where m.codentidade=492 and m.quantidade > 0.00 and tm.tipomovimento='E'
          union all
          select 'saídas', count(*) from sal_movimento m join sal_tipomovimento tm on (m.idtipomovimento=tm.idtipomovimento) where m.codentidade=492 and m.quantidade > 0.00 and tm.tipomovimento='S'
        )
        order by 1 """)
        lista = cur.fetchall()
        cur.close()
        conn.close()
        
        return lista
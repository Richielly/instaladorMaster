from venvinstaladorMaster import  connection

hostdborigin = 'localhost'
dborigin = 'C:\\Users\\richielly.carvalho\Desktop\SCP_ALMOX\\007\\EQUIPLANO.FDB'
userdborigin = 'sysdba'
senhadborigin = 'masterkey'
portdborigin = 3050

hostdest = 'localhost'
portdest = '5432'
bddest = 'almoxarifado'
userdest = 'postgres'
passworddest = 'es74079'

class Search():
    
    def select(self):
        con = connection.BdConnections()

        conn = con.firebird_connection(host=hostdborigin, database=dborigin, user=userdborigin, password=senhadborigin, port=portdborigin)
   
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
          select 'centros de custo', count(*) from scp55_localexercicio where codentidade=007
          union all
          select 'depósitos', count(*) from sal_deposito where codentidade=007
          union all
          select 'entradas', count(*) from sal_movimento m join sal_tipomovimento tm on (m.idtipomovimento=tm.idtipomovimento) where m.codentidade=007 and m.quantidade > 0.00 and tm.tipomovimento='E'
          union all
          select 'saídas', count(*) from sal_movimento m join sal_tipomovimento tm on (m.idtipomovimento=tm.idtipomovimento) where m.codentidade=007 and m.quantidade > 0.00 and tm.tipomovimento='S'
        )
        order by 1 """)
        lista = cur.fetchall()
        cur.close()
        conn.close()
        
        return lista

    def select_tables_firebird(self):
        con = connection.BdConnections()
        conn = con.firebird_connection(host=hostdborigin, database=dborigin, user=userdborigin, password=senhadborigin, port=portdborigin)
        cur = conn.cursor()
        cur.execute(
            """ select 
                rdb$relation_name from rdb$relations
                where rdb$system_flag = 0; """)
        lista = cur.fetchall()
        cur.close()
        conn.close()

        return lista

    def select_columns_firebird(self, table_name):
        con = connection.BdConnections()

        conn = con.firebird_connection(host=hostdborigin, database=dborigin, user=userdborigin, password=senhadborigin, port=portdborigin)
        cur = conn.cursor()
        cur.execute(
            """ select rdb$field_name from rdb$relation_fields
             where rdb$relation_name=""" + "'" + table_name + "'" +';')
        lista = cur.fetchall()
        cur.close()
        conn.close()

        return lista

    def select_filter_firebird(self, table, column='*'):
        con = connection.BdConnections()
        conn = con.firebird_connection(host=hostdborigin, database=dborigin, user=userdborigin, password=senhadborigin, port=portdborigin)
        cur = conn.cursor()
        cur.execute(
        """ SELECT """
        + column +
        """ FROM """ + table + ";")
        lista = cur.fetchall()
        cur.close()
        conn.close()

        return lista

    def select_postgre(self):
        con = connection.BdConnections()
        conn = con.postgre_connection(host=hostdest, port=portdest,bd=bddest, user=userdest, password=passworddest)
        cur = conn.cursor()
        cur.execute(
            """ SELECT idconfiguracao, idcliente, estado, idusuariocriador, datacriacao, idusuarioatualizador, dataatualizacao, chaveacesso, quantidadelinhastabelas, diferencaordemretirada, tamanhomaximoanexo, conferenciacega, localbkp, dataultimobkp, diabackup
	FROM public.configuracao; """)
        lista = cur.fetchall()
        cur.close()
        conn.close()

        return lista
    
    def select_tables_postgre(self):
        con = connection.BdConnections()
        conn = con.postgre_connection(host=hostdest, port=portdest,bd=bddest, user=userdest, password=passworddest)
        cur = conn.cursor()
        cur.execute(
        """SELECT table_name 
           FROM information_schema.tables
           WHERE table_schema='public'
           AND table_type='BASE TABLE';""")

        list = cur.fetchall()
        cur.close()
        conn.close()

        return list

    def select_columns_tables(self, table_name):
        con = connection.BdConnections()
        conn = con.postgre_connection(host=hostdest, port=portdest,bd=bddest, user=userdest, password=passworddest)
        cur = conn.cursor()
        cur.execute(
        """SELECT column_name, data_type, character_maximum_length
           FROM INFORMATION_SCHEMA.COLUMNS 
           WHERE table_name = """ + "'" +  table_name + "'" +';')

        list = cur.fetchall()
        cur.close()
        conn.close()

        return list

    def select_filter(self, table, column='*'):
        con = connection.BdConnections()
        conn = con.postgre_connection(host=hostdest, port=portdest,bd=bddest, user=userdest, password=passworddest)
        cur = conn.cursor()
        cur.execute(
        """ SELECT """
        + column +
        """ FROM public. """ + table + ";")
        lista = cur.fetchall()
        cur.close()
        conn.close()

        return lista
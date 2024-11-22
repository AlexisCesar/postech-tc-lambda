import psycopg2
import os
from datetime import datetime

def lambda_handler(event, context):
    # Configurações do banco de dados (substitua pelos valores reais)
    host = os.environ['DB_HOST']
    database = os.environ['DB_NAME']
    user = os.environ['DB_USER']
    password = os.environ['DB_PASSWORD']

    # Conectar ao banco de dados
    try:
        conn = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        print("Conexão bem-sucedida!")
        cur = conn.cursor()

        # Primeira query: Excluir registros relacionados na tabela ItemPedido
        query_itempedido = """
            DELETE FROM public."ItemPedido"
            WHERE "PedidoAggregateId" IN (
                SELECT p."Id"
                FROM public."Pedido" p
                JOIN public."Acompanhamento" a ON p."AcompanhamentoId" = a."Id"
                WHERE a."Status" = 1
                AND p."HorarioRecebimento" < NOW() - INTERVAL '0 minutes'
            );
        """

        # Executar a query para remover da tabela ItemPedido
        cur.execute(query_itempedido)

        # Segunda query: Excluir os registros da tabela Acompanhamento e, consequentemente, da tabela Pedido
        query_pedido = """
        DELETE FROM public."Acompanhamento"
            WHERE "Status" = 1
            AND "Id" IN (
                SELECT a."Id"
                FROM public."Acompanhamento" a
                JOIN public."Pedido" p ON a."Id" = p."AcompanhamentoId"
                WHERE p."HorarioRecebimento" < NOW() - INTERVAL '0 minutes'
                AND a."Status" = 1
            );
        """

        # Executar a query para remover da tabela Pedido
        cur.execute(query_pedido)

        # Aplicar as mudanças no banco de dados
        conn.commit()

        # Fechar cursor e conexão
        cur.close()
        print(f"Pedidos com status 'recebido' (1) e HorarioRecebimento superior a 2 horas removidos em {datetime.now()}.")
    except Exception as e:
        print(f"Erro ao conectar: {e}")
        return {"statusCode": 500, "body": "Erro ao conectar ao banco de dados"}
    finally:
        if conn:
            conn.close()
            print("Conexão fechada.")

    return {"statusCode": 200, "body": "Conexão bem-sucedida!"}
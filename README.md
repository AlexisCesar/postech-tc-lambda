<div align="center">
<img src="https://github.com/user-attachments/assets/208a0ebb-ca7c-4b0b-9f68-0b35050a9880" width="30%" />
</div>

# Lanchonete do Bairro - AWS LAMBDA (POS TECH: TECH CHALLENGE - 3a FASE)🚀

Este é o repositório responsável pelas funções lambda do sistema.

Integrantes do grupo:<br>
Alexis Cesar (RM 356558)<br>
Bruna Gonçalves (RM 356557)

Para mais informações, consulte o projeto principal: [Pos Tech: Tech Challenges](https://github.com/AlexisCesar/postech-tech-challenges)

## Subindo a função Lambda com Terraform Manualmente
Passos necessários para subir a Lambda na nuvem da AWS de forma manual.

Requisitos:
- Infraestrutura base (VPC, subnets...) já rodando. Repositório: [postech-tc-eks](https://github.com/AlexisCesar/postech-tc-eks);
- Banco de dados RDS já rodando. Repositório: [postech-tc-rds](https://github.com/AlexisCesar/postech-tc-rds);
- AWS CLI instalada;
- Terraform instalado;
- Credenciais AWS configuradas;
- Subir a infraestrutura com Terraform: ```terraform apply```
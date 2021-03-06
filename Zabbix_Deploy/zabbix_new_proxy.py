#!/usr/bin/python3.6
# coding: utf-8
import sys
from pyzabbix import ZabbixAPI

#Variaveis de acesso
zbx_srv_url=sys.argv[1]
zbx_srv_username=sys.argv[2]
zbx_srv_password=sys.argv[3]
zbx_proxy_name = sys.argv[4]
zbx_proxy_key = sys.argv[5]


# Acesso Zabbix
zapi = ZabbixAPI(zbx_srv_url)
zapi.login(zbx_srv_username,zbx_srv_password)

# Cadastrando novo Proxy no zabbix Server 
zapi.proxy.create(
    host=zbx_proxy_name,
    status=5,
    description='Proxy criado via deploy automatico do Zabbix Proxy \n\nby Andre Antunes - andreantunes@gmail.com',
    tls_accept=2, 
    tls_psk_identity=zbx_proxy_name.lower(),
    tls_psk=zbx_proxy_key
)

# Criando Grupo de host 
zapi.hostgroup.create(name=zbx_proxy_name)
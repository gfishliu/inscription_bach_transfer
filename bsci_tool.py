# -*- coding: UTF-8 -*-
from web3 import Web3
import time

def send_(hash):
    from_address = w3.to_checksum_address(address)
    transaction = {
        'from': from_address,
        'to': w3.to_checksum_address(to_address),
        'data': hash,
        'value': 0,
        'chainId': 56,
        'nonce': w3.eth.get_transaction_count(from_address),
        'gasPrice': int(w3.eth.gas_price),
        'gas':23000
    }

    try:
        signed = w3.eth.account.sign_transaction(transaction, password)
        new_raw = signed.rawTransaction.hex()
        tx_hash = w3.eth.send_raw_transaction(new_raw)
        print(f"发送成功 > {transaction} , 交易Hash > {w3.to_hex(tx_hash)}")
    except Exception as e:
        print(f'发送失败 > {transaction}', e)
        return
    try:
        res = w3.eth.wait_for_transaction_receipt(tx_hash, timeout=120, poll_latency=0.5)  #等待2分钟查结果
        if res['status'] == 1:
            print(f'交易成功 > {w3.to_hex(tx_hash)}')
    except:
        print(f'查询交易结果超时，请自行手动检查交易结果 > {w3.to_hex(tx_hash)}')

def go():
    isfun=input('请选择输入Hash方式：读取本地 [hash_list.txt] 请按1，在线输入请按2   >>> ')

    if isfun=='1':
        with open('./hash_list.txt') as f:
            hash_list=f.read().split('\n')
    elif isfun=='2':
        txt=input("请输入要发送的资产Hash，多个资产请用空格隔开，按下回车结束输入   >>> ")
        hash_list = [i for i in txt.split(' ') if i!='']
    else:
        print('输入错误，3秒后退出...')
        time.sleep(3)
        return

    for i in hash_list:
        # print(i)
        send_(i)


if __name__ == '__main__':
    print('对脚本有疑问或者建议，请推特联系：@buyuelongmen')
    print('需要进场外交易群的(加的时候注明进什么群)，联系V: bjqs1122')
    print('本软件不保存任何数据，有能力的朋友优先使用源码，打包好的软件流传过程中有被替换/破解的风险，请自行承担该风险....')

    print('\n\n\n.\n.\n.\n\n\n')

    rpc = 'https://bsc-dataseed.binance.org/'  # bsc有条件的可以自行更换更好的
    w3 = Web3(Web3.HTTPProvider(rpc))

    address = input('请输入您的地址(回车确认)：')  # 自己的地址
    password = input('请输入上面地址私钥(回车确认)：')  # 自己址的私钥
    to_address = input('请输入接收方地址(回车确认)：')  # 转账接收地址

    go()



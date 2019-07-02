from handle_data.save_to_mysql import Save_to_sql
def to_save(data):
    '''消费数据'''
    # 将解析完的数据进行存库
    save_to_analysis = Save_to_sql('yctformdata')
    if data:
        is_del = data.pop('delete_set')
        if is_del:  # 判断是否删除记录
            save_to_analysis.del_set(data)
        else:
            save_to_analysis.insert_new(data)
    return data

data={'product_id': '0.8592270774201917', 'customer_id': '', 'methods': 'POST', 'web_name': 'yct.sh.gov.cn', 'to_server': 'http://yct.sh.gov.cn/bizhallnz_yctnew/apply/save_info', 'time_circle': '2019-07-02 03:24:15', 'parameters': '{"sjjydz": "\u4e0a\u6d77\u5e02\u9ec4\u6d66\u533a\u5357\u4eac\u897f\u8def", "zcdz": "\u4e0a\u6d77\u5e02\u9ec4\u6d66\u533a\u5357\u4eac\u897f\u8def", "qylx": "\u6709\u9650\u8d23\u4efb\u516c\u53f8(\u81ea\u7136\u4eba\u6295\u8d44\u6216\u63a7\u80a1)", "zczbje": "100", "jyfw": "", "sshy": "", "cwryxm": "\u770b", "cwrydh": "15845236599", "frxm": "\u6211", "frsj": "15845236599", "frsfz": "411522199403080011", "frdz": "\u5409\u6797\u7701\u5409\u6797\u5e02", "llyxm": "\u5427", "llysj": "15845236599", "llysfz": "411522199403080011"}', 'pageName': 'apply_form', 'anync': '', 'isSynchronous': '0', 'delete_set': False, 'registerAppNo': '0000000120190701A002', 'yctAppNo': 'f702415f56284bb6a927115c66418be5', 'etpsName': '上海要闻让软件有限责任公司'}
to_save(data)

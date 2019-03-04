import yaml
with open("./data.yml",'r') as f:
    data =yaml.load(f)
    # test: login_data01
    # test_name: lili
    # test_pwd: 3434
    da = data.get('Test')
    print(da)
    for i in da:
        print("test: "+i)
        print("test_name: "+da[i]['name'])

